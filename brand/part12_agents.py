# -*- coding: utf-8 -*-
"""Part 12: inside the agent GIF - how a math agent computes. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os, random
os.makedirs(OUT, exist_ok=True)

W = H = 480
HEX = "0123456789ABCDEF"

STEPS = [
    "TASK: x\u00b2 - 7x + 12 = 0",
    "D = 49 - 48 = 1",
    "x1 = (7 + 1) / 2 = 4",
    "x2 = (7 - 1) / 2 = 3",
]
LIE_STEP = "x1 = (7 + 1) / 2 = 5"   # the wrong version XOR-13 is tempted by


def noise_line(rng, n=26):
    return " ".join("".join(rng.choice(HEX) for _ in range(4)) for _ in range(n // 5))


def frame(f):
    img = board_bg(W, H, seed=41)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "INSIDE THE AGENT", font=silk(14, bold=True), fill=(159, 208, 255))
    d.text((286, 16), "episode 07", font=vt(22), fill=GREY)

    # ---------- agent face (left) ----------
    mood = "idle"
    if 9 <= f < 31:
        mood = "typing"
    elif f >= 52:
        mood = "error"
    fx, fy = 24, 60
    face = pixel_face(128, (124, 252, 0), mood=mood)
    if f % 14 == 13 and f < 50:   # blink
        face = face.copy()
        fd = ImageDraw.Draw(face)
        fd.rectangle([40, 70, 88, 78], fill=(124, 252, 0))
    img.paste(face, (fx, fy))
    d.rectangle([fx, fy, fx + 127, fy + 127], outline=INK, width=4)
    d.text((fx + 4, fy + 134), "XOR-13", font=silk(13, bold=True), fill=(169, 229, 161))
    d.text((fx + 4, fy + 156), "intern \u00b7 35%", font=vt(24), fill=GREY)

    # ---------- agent log (right): the solution types out ----------
    lx0, ly0, lx1, ly1 = 180, 56, 456, 250
    d.rectangle([lx0 + 6, ly0 + 6, lx1 + 6, ly1 + 6], fill=INK)
    d.rectangle([lx0, ly0, lx1, ly1], fill=(52, 46, 82), outline=CHALK, width=3)
    d.rectangle([lx0, ly0, lx1, ly0 + 26], fill=INK)
    d.text((lx0 + 10, ly0 + 6), "AGENT.LOG", font=silk(11, bold=True), fill=YELLOW)
    # typing phases
    if f < 8:
        t = "awaiting task\u2026" if f < 4 else "task received."
        d.text((lx0 + 16, ly0 + 44), t, font=vt(28), fill=CHALK)
    else:
        shown = min(4, (f - 8) // 5 + (1 if f >= 8 else 0))
        y = ly0 + 42
        for i, s in enumerate(STEPS):
            col = CHALK
            txt = s
            if i < shown:
                # check-sweep after step 34; line 2 becomes the lie at 52
                if f >= 52 and i == 2:
                    txt, col = LIE_STEP, ORANGE
                if 34 <= f < 52 and i == min(3, (f - 34) // 4):
                    col = GREEN
                d.text((lx0 + 16, y), txt, font=vt(28), fill=col)
                if 34 <= f < 52 and i == min(3, (f - 34) // 4):
                    d.text((lx1 - 66, y), "OK", font=silk(12, bold=True), fill=GREEN)
            y += 40
        if 30 <= f < 34:
            d.text((lx0 + 16, ly0 + 42 + 4 * 40 + 2), "proof assembled.", font=vt(26), fill=(159, 208, 255))
        if f >= 52:
            stamp(img, (lx1 - 90, ly0 + 152), "LIE", ORANGE, 20, -8)
            d = ImageDraw.Draw(img)

    # ---------- working memory (bottom): hex noise + progress ----------
    mx0, my0, mx1, my1 = 24, 288, 456, 386
    d.rectangle([mx0 + 6, my0 + 6, mx1 + 6, my1 + 6], fill=INK)
    d.rectangle([mx0, my0, mx1, my1], fill=BOARD, outline=(70, 62, 105), width=3)
    d.text((mx0 + 12, my0 + 8), "WORKING MEMORY", font=silk(10, bold=True), fill=(159, 208, 255))
    rng = random.Random(f)
    if 9 <= f < 31:
        for r in range(3):
            d.text((mx0 + 12, my0 + 30 + r * 22), noise_line(rng), font=vt(20), fill=(70, 62, 105))
        pct = (f - 9) / 21.0
        d.rectangle([mx0 + 12, my1 - 30, mx1 - 12, my1 - 12], outline=CHALK, width=2)
        d.rectangle([mx0 + 14, my1 - 28, mx0 + 14 + int((mx1 - mx0 - 28) * pct), my1 - 14], fill=ACCENT)
        d.text((mx0 + 12, my1 - 56), "computing\u2026", font=vt(24), fill=YELLOW)
    elif f < 9:
        d.text((mx0 + 12, my0 + 34), "idle. staring at the chalk. waiting.", font=vt(24), fill=GREY)
    else:
        d.text((mx0 + 12, my0 + 34), "output buffer flushed.", font=vt(24), fill=GREY)
        d.text((mx0 + 12, my0 + 62), "confidence: 100% (unjustified)", font=vt(24), fill=(255, 158, 207))

    # ---------- status line ----------
    if f < 8:
        st, c = "STATUS: IDLE", GREY
    elif f < 31:
        st, c = "STATUS: SOLVING", YELLOW
    elif f < 52:
        st, c = "STATUS: PRESENTING PROOF", (159, 208, 255)
    else:
        st, c = "STATUS: LIE INJECTED (err 35%)", ORANGE
    d.text((24, 398), st, font=silk(12, bold=True), fill=c)
    if f >= 52:
        d.text((24, 420), "they compute fast. honesty is optional.", font=vt(28), fill=CHALK)
        d.text((24, 450), "catching it: YOUR job. -> prooffactory.icu", font=vt(24), fill=(255, 226, 138))
    return img


def g6(path):
    frames = [frame(f) for f in range(66)]
    for _ in range(14):
        frames.append(frame(65))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("frames:", len(frames))


g6(OUT + "content-23-inside-the-agent.gif")
print("part12 done")
