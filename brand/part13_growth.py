# -*- coding: utf-8 -*-
"""Part 13: exponential dividend growth GIF 480x480. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os, math
os.makedirs(OUT, exist_ok=True)

W = H = 480
R = 1.32                 # growth factor per round
D0 = 30.0                # $PROOF distributed in round 1
NBARS = 8

PX0, PY0, PX1, PY1 = 50, 60, 460, 318   # plot area (bottom axis at PY1)
BARW = 30
STEP = (PX1 - PX0 - 30) / NBARS


def dval(i):
    return D0 * R ** i


def cum(n):
    return D0 * (R ** n - 1) / (R - 1)


VMAX = dval(NBARS - 1)


def bar_geom(i):
    x = PX0 + 24 + i * STEP
    v = dval(i)
    h = (PY1 - PY0 - 30) * v / VMAX
    return x, h, v


def curve_pts():
    pts = []
    for k in range(70):
        t = k / 69 * (NBARS - 0.6)
        v = D0 * R ** t
        x = PX0 + 24 + t * STEP + BARW / 2
        y = PY1 - (PY1 - PY0 - 30) * v / VMAX
        pts.append((x, y))
    return pts


def frame(f, end=False):
    img = board_bg(W, H, seed=91)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "EXPONENTIAL LEDGER", font=silk(14, bold=True), fill=YELLOW)
    d.text((268, 16), "growth math, no hopium", font=vt(22), fill=(159, 208, 255))

    # ---------- plot ----------
    # grid
    for gy in range(PY0 + 40, PY1, 50):
        for gx in range(PX0, PX1, 12):
            d.point((gx, gy), fill=(70, 62, 105))
    # axes
    d.line([PX0, PY0 - 10, PX0, PY1], fill=CHALK, width=3)
    d.line([PX0, PY1, PX1, PY1], fill=CHALK, width=3)
    d.text((8, PY0 - 6), "$PROOFACTORY", font=vt(20), fill=GREY)

    # bars (appear from f=8, one per 4 frames, grow over 3)
    for i in range(NBARS):
        a = 8 + i * 4
        if f < a:
            continue
        g = min(1.0, (f - a) / 3.0)
        x, h, v = bar_geom(i)
        hh = h * g
        d.rectangle([x, PY1 - hh, x + BARW, PY1], fill=ACCENT, outline=CHALK, width=2)
        if g >= 1.0:
            d.text((x - 2, PY1 - hh - 24), f"{int(round(v))}", font=vt(20), fill=YELLOW)
        d.text((x + 2, PY1 + 8), f"R{i + 1}", font=vt(20), fill=GREY)

    # exponential curve (draws progressively from f=10 over ~30 frames)
    prog = min(1.0, max(0.0, (f - 10) / 30.0))
    pts = curve_pts()
    n = max(1, int(len(pts) * prog))
    if n > 1:
        d.line(pts[:n], fill=(255, 226, 138), width=3)

    # ---------- formula box ----------
    bx0, by0, bx1, by1 = 24, 348, 456, 416
    d.rectangle([bx0 + 6, by0 + 6, bx1 + 6, by1 + 6], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=BOARD, outline=CHALK, width=3)
    if f < 40:
        msg = "plotting the 3% stream\u2026" if f >= 8 else "collecting round data\u2026"
        d.text((bx0 + 16, by0 + 28), msg, font=vt(28), fill=GREY)
    else:
        d.text((bx0 + 16, by0 + 8), f"D(n) = 30 \u00b7 {R}^n  per round", font=vt(28), fill=CHALK)
        d.text((bx0 + 16, by0 + 40), f"n=16: {int(round(dval(15))):,} \u00b7 n=30: {int(round(dval(29))):,} $PROOFACTORY",
               font=vt(22), fill=YELLOW)

    # ---------- cumulative line ----------
    if 8 <= f < 40:
        d.text((24, 428), "STATUS: GROWING", font=silk(12, bold=True), fill=(255, 158, 207))
    elif f >= 40:
        k = min(NBARS, 1 + (f - 40) // 4)
        if end:
            k = NBARS
        d.text((24, 426), f"total after {k} rounds: {int(round(cum(k))):,} $PROOFACTORY",
               font=vt(22), fill=GREEN)
    if end:
        stamp(img, (360, 240), "COMPOUNDED", ORANGE, 20, -8)
        d = ImageDraw.Draw(img)
        d.text((24, 452), "small rounds, big exponent. -> prooffactory.icu", font=vt(20), fill=(255, 226, 138))
    return img


def g7(path):
    frames = [frame(f) for f in range(72)]
    for _ in range(14):
        frames.append(frame(71, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=140, loop=0, optimize=True)
    print("frames:", len(frames))


g7(OUT + "content-24-exponential-ledger.gif")
print("part13 done")
