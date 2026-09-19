# -*- coding: utf-8 -*-
"""Part 10: Mandelbrot zoom GIF - basement math visualization. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

import numpy as np

W = H = 480
FR = 44          # zoom frames
ITERS = 90       # escape iterations
SIZE = 380       # fractal canvas

# brand-gradient bands (dark -> bright), interior = board color
BANDS = [
    (52, 46, 82), (74, 58, 255), (159, 208, 255), (169, 229, 161),
    (255, 226, 138), (255, 179, 107), (255, 158, 207), (255, 107, 107),
    (242, 236, 255),
]

# zoom path: from full set into the seahorse valley
C0 = np.array([-0.50, 0.00])
C1 = np.array([-0.745428, 0.186919])
W0, W1 = 3.4, 0.0035


def mandel(cx, cy, w):
    h = w * SIZE / SIZE
    x = np.linspace(cx - w / 2, cx + w / 2, SIZE)
    y = np.linspace(cy - h / 2, cy + h / 2, SIZE)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    N = np.zeros(C.shape, dtype=np.float64)
    M = np.ones(C.shape, dtype=bool)
    for i in range(ITERS):
        Z[M] = Z[M] * Z[M] + C[M]
        escaped = M & (np.abs(Z) > 2)
        N[escaped] = i + 1 - np.log2(np.log2(np.abs(Z[escaped])))
        M = M & ~escaped
        if not M.any():
            break
    return N, M  # smooth iter count + still-inside mask


def fractal_img(N, inside):
    img = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
    img[:] = BANDS[0]
    idx = (N * 0.7).astype(int) % len(BANDS)
    for i in range(len(BANDS)):
        m = idx == i
        img[m] = BANDS[i]
    img[inside] = BOARD  # the set itself: deep board purple
    # chalk dust on the border region
    border = (~inside) & (N < 2)
    img[border] = (96, 88, 140)
    return Image.fromarray(img, "RGB")


def frame(t, hold=False):
    # ease: exponential zoom, slight drift along the path
    k = t / (FR - 1)
    ease = k * k * (3 - 2 * k)           # smoothstep
    c = C0 + (C1 - C0) * ease
    w = W0 * (W1 / W0) ** ease
    N, ins = mandel(c[0], c[1], w)
    frac = fractal_img(N, ins)

    img = board_bg(W, H, seed=77)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 16), "BASEMENT MATH \u2116 5", font=silk(12, bold=True), fill=(159, 208, 255))
    d.text((300, 16), f"Z\u2192Z\u00b2+C", font=vt(26), fill=(255, 226, 138))
    # paste fractal with hard pixel border
    px, py = (W - SIZE) // 2, 56
    d.rectangle([px - 4, py - 4, px + SIZE + 3, py + SIZE + 3], fill=INK)
    d.rectangle([px - 4, py - 4, px + SIZE + 3, py + SIZE + 3], outline=(159, 208, 255), width=2)
    img.paste(frac, (px, py))
    d = ImageDraw.Draw(img)
    zoom = int(np.log2(W0 / w))
    d.text((24, H - 40), f"zoom: 2^{zoom}", font=vt(26), fill=(169, 229, 161))
    d.text((150, H - 40), f"iterations: {ITERS}", font=vt(26), fill=(139, 132, 163))
    if not hold:
        d.text((300, H - 40), "checking\u2026", font=vt(26), fill=(255, 158, 207))
    return img


def g4(path):
    frames = []
    for t in range(FR):
        frames.append(frame(t))
    end = frame(FR - 1, hold=True)
    d = ImageDraw.Draw(end)
    d.rectangle([60, 200, 420, 290], fill=BOARD, outline=(255, 107, 107), width=3)
    d.text((84, 214), "the border is infinite.", font=vt(34), fill=CHALK)
    d.text((84, 252), "the agents are still checking.", font=vt(30), fill=(255, 158, 207))
    for _ in range(12):
        frames.append(end)
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=150, loop=0, optimize=True)
    print("frames:", len(frames))


g4(OUT + "content-21-mandelbrot-zoom.gif")
print("part10 done")
