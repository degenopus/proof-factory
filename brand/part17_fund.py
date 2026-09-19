# -*- coding: utf-8 -*-
"""Part 17: power-up fund, human vs agent duel, governance vote GIFs."""
from brandkit import *
from part1_logo import OUT
import os, random, math
os.makedirs(OUT, exist_ok=True)

W = H = 480


# ============ G17: THE POWER-UP FUND ============
GOAL = 50000
UNLOCKS = [("REAL MODELS", 0.25), ("2x ROUNDS/HOUR", 0.5), ("BIG PRIZES", 1.0)]
DONORS = ["0xF1A7\u2026 1,200", "PR #2049 +800", "0xD00D\u2026 2,500",
          "0x5A1E\u2026 640", "anon +100", "0xBE11\u2026 3,000"]


def g17_frame(f, end=False):
    img = dither(W, H, seed=211)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE POWER-UP FUND", font=silk(14, bold=True), fill=INK)
    d.text((260, 16), "buy the brain", font=vt(22), fill=GREY)

    k = min(1.0, f / 70.0)
    fund = int(GOAL * k)

    # thermometer
    tx, ty0, ty1 = 70, 70, 330
    d.rectangle([tx - 26, ty0 - 22, tx + 26, ty1 + 22], fill=WHITE, outline=INK, width=5)
    fh = int((ty1 - ty0) * k)
    d.rectangle([tx - 16, ty1 - fh, tx + 16, ty1], fill=ACCENT)
    d.ellipse([tx - 34, ty1 + 14, tx + 34, ty1 + 82], fill=WHITE, outline=INK, width=5)
    dk = min(1.0, fh / (ty1 - ty0) * (ty1 - ty0) / (ty1 - ty0))
    fillh = int(54 * k)
    d.ellipse([tx - 24, ty1 + 66 - fillh, tx + 24, ty1 + 66], fill=ACCENT)
    # markers
    for label, th in [("25%", 0.25), ("50%", 0.5), ("100%", 1.0)]:
        my = ty1 - int((ty1 - ty0) * th)
        d.line([tx + 28, my, tx + 40, my], fill=INK, width=3)
        hit = k >= th
        d.text((tx + 46, my - 12), label, font=vt(22), fill=GREEN if hit else GREY)

    # unlock rows
    rx = 190
    d.text((rx, 70), "UNLOCKS", font=silk(11, bold=True), fill=INK)
    y = 96
    for name, th in UNLOCKS:
        hit = k >= th
        d.rectangle([rx + 5, y + 5, rx + 252, y + 58], fill=INK)
        d.rectangle([rx, y, rx + 252, y + 53], fill=WHITE if hit else PAPER2, outline=INK, width=4)
        d.text((rx + 12, y + 8), name, font=silk(12, bold=True), fill=GREEN if hit else GREY)
        pb = min(1.0, k / th) if th else 0
        d.rectangle([rx + 12, y + 34, rx + 236, y + 44], outline=INK, width=2)
        d.rectangle([rx + 14, y + 36, rx + 14 + int(218 * pb), y + 42], fill=GREEN if hit else GREY)
        if hit:
            d.text((rx + 184, y + 6), "OPEN", font=silk(10, bold=True), fill=GREEN)
        y += 74

    # fund counter
    d.rectangle([150, 330, 446, 376], fill=BOARD, outline=INK, width=4)
    d.text((162, 338), f"FUND: {fund:,} / {GOAL:,}", font=vt(28), fill=YELLOW)
    d.text((162, 358), "$PROOFACTORY", font=vt(20), fill=GREY)

    # coins flying into thermometer
    for j in range(18):
        launch = 2 + j * 4
        t = (f - launch) / 22.0
        if 0 <= t <= 1:
            x = 430 - (430 - tx) * t
            y = 420 - (420 - (ty0 - 10)) * t
            d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=YELLOW, outline=INK, width=2)
    d.text((380, 400), "contributions", font=vt(20), fill=GREY)

    # donor ticker
    d.rectangle([24, 396, 370, 424], fill=BOARD, outline=(70, 62, 105), width=2)
    d.text((34, 401), f"> {DONORS[(f // 14) % len(DONORS)]} $PROOFACTORY", font=vt(20), fill=CHALK)

    if end:
        stamp(img, (428, 448), "FUNDING", ORANGE, 16, -6)
        d = ImageDraw.Draw(img)
        d.text((24, 428), "the fund buys compute. 3% flows back.", font=vt(20), fill=INK)
        d.text((24, 452), "-> prooffactory.icu", font=vt(20), fill=ACCENT)
    return img


def g17(path):
    frames = [g17_frame(f) for f in range(84)]
    for _ in range(14):
        frames.append(g17_frame(83, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=120, loop=0, optimize=True)
    print("g17 frames:", len(frames))


# ============ G18: THE DUEL ============
DUEL_LINES = [
    "TASK: x\u00b2 - 9x + 20 = 0",
    "D = 81 - 80 = 1",
    "x1 = (9 + 1) / 2 = 6",
    "x2 = (9 - 1) / 2 = 4",
]


def g18_frame(f, end=False):
    img = board_bg(W, H, seed=221)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE DUEL", font=silk(14, bold=True), fill=YELLOW)
    d.text((250, 16), "you vs G\u00d6DEL-9000", font=vt(22), fill=(159, 208, 255))

    # headers + reading bars
    d.text((40, 52), "YOU", font=silk(13, bold=True), fill=(169, 229, 161))
    d.text((300, 52), "G\u00d6DEL-9000", font=silk(13, bold=True), fill=(196, 224, 255))
    you_k = min(1.0, max(0.0, (f - 8) / 46.0))
    god_k = min(1.0, max(0.0, (f - 8) / 8.0))
    d.rectangle([40, 72, 210, 82], outline=CHALK, width=2)
    d.rectangle([42, 74, 42 + int(164 * you_k), 80], fill=GREEN)
    d.rectangle([300, 72, 440, 82], outline=CHALK, width=2)
    d.rectangle([302, 74, 302 + int(134 * god_k), 80], fill=BLUE)

    # proof
    px0, py0 = 60, 110
    d.rectangle([px0 + 6, py0 + 6, 420, py0 + 190], fill=INK)
    d.rectangle([px0, py0, 414, py0 + 184], fill=(52, 46, 82), outline=CHALK, width=3)
    shown = min(sum(len(l) for l in DUEL_LINES) + 8, f * 2)
    y = py0 + 16
    budget = shown
    lie_reveal = f >= 56
    for i, ln in enumerate(DUEL_LINES):
        if budget <= 0:
            break
        t = ln[:budget]
        col = CHALK
        if lie_reveal and i == 2:
            col = ORANGE
        d.text((px0 + 20, y), t, font=vt(30), fill=col)
        budget -= len(ln) + 2
        y += 42

    # GÖDEL approves early (below the proof)
    if f >= 18:
        stamp(img, (350, 312), "APPROVED", (159, 208, 255), 16, 8)
        d = ImageDraw.Draw(img)

    # your magnifier scan
    if 30 <= f < 56:
        t = (f - 30) / 25.0
        mx = 80 + t * 300
        my = 110 + 42 * 2 + 15
        d.ellipse([mx - 20, my - 20, mx + 20, my + 20], outline=YELLOW, width=4)
        d.line([mx + 14, my + 14, mx + 30, my + 30], fill=YELLOW, width=4)
    if f >= 56:
        stamp(img, (130, 312), "CAUGHT", ORANGE, 20, -8)
        d = ImageDraw.Draw(img)
        d.text((40, 344), "line 3 is wrong. x1 = 5, not 6. +50 rep", font=vt(24), fill=(169, 229, 161))
        d.text((40, 372), "it wrote the proof. conflict of interest.", font=vt(20), fill=GREY)
    if end:
        d.text((24, 404), "it computes. you verify.", font=vt(26), fill=CHALK)
        d.text((24, 436), "that is the deal. -> prooffactory.icu", font=vt(24), fill=YELLOW)
    return img


def g18(path):
    frames = [g18_frame(f) for f in range(84)]
    for _ in range(14):
        frames.append(g18_frame(83, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g18 frames:", len(frames))


# ============ G19: THE VOTE ============
def g19_frame(f, end=False):
    img = board_bg(W, H, seed=231)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE VOTE", font=silk(14, bold=True), fill=YELLOW)
    d.text((286, 16), "holders steer", font=vt(22), fill=(159, 208, 255))

    # proposal
    d.rectangle([30, 56, 450, 146], fill=(52, 46, 82), outline=CHALK, width=3)
    witch = pixel_face(64, (207, 179, 255), mood="error")
    img.paste(witch, (44, 68))
    d.rectangle([44, 68, 107, 131], outline=INK, width=3)
    d.text((124, 66), "PROPOSAL #7", font=silk(12, bold=True), fill=YELLOW)
    d.text((124, 92), "add agent #6: WITCH-\u222b", font=vt(26), fill=CHALK)
    d.text((124, 120), "chaos mode. 55% error rate. we want it.", font=vt(22), fill=GREY)

    # votes
    yes_k = min(1.0, f / 58.0) * 0.74
    no_k = min(1.0, f / 64.0) * 0.26
    d.text((40, 172), "YES", font=silk(13, bold=True), fill=GREEN)
    d.rectangle([120, 168, 420, 194], outline=CHALK, width=3)
    d.rectangle([123, 171, 123 + int(294 * yes_k), 191], fill=GREEN)
    d.text((424, 170), f"{int(yes_k * 100)}%", font=vt(24), fill=GREEN)
    d.text((40, 216), "NO", font=silk(13, bold=True), fill=PINK)
    d.rectangle([120, 212, 420, 238], outline=CHALK, width=3)
    d.rectangle([123, 215, 123 + int(294 * no_k), 235], fill=PINK)
    d.text((424, 214), f"{int(no_k * 100)}%", font=vt(24), fill=PINK)

    # quorum
    d.text((40, 262), "quorum", font=vt(22), fill=GREY)
    d.rectangle([120, 264, 420, 276], outline=CHALK, width=2)
    qk = min(1.0, f / 50.0) * 0.36
    d.rectangle([122, 266, 122 + int(296 * qk), 274], fill=YELLOW)
    d.text((424, 258), "36%", font=vt(22), fill=YELLOW)

    # voter ticker
    voters = ["0xV073\u2026 YES", "PR #3117 YES", "0xD1E7\u2026 NO", "0xC4A0\u2026 YES", "anon YES"]
    d.rectangle([24, 296, 456, 324], fill=BOARD, outline=(70, 62, 105), width=2)
    d.text((34, 301), f"> {voters[(f // 12) % len(voters)]}", font=vt(22), fill=CHALK)

    if f >= 72 or end:
        stamp(img, (240, 360), "PASSED", ORANGE, 24, -7)
        d = ImageDraw.Draw(img)
        d.rectangle([40, 388, 440, 424], fill=(52, 46, 82), outline=(207, 179, 255), width=3)
        d.text((56, 396), "WITCH-\u222b clocks in next epoch.", font=vt(24), fill=(207, 179, 255))
    if end:
        d.text((24, 440), "one $PROOFACTORY = one vote. -> prooffactory.icu", font=vt(20), fill=YELLOW)
    return img


def g19(path):
    frames = [g19_frame(f) for f in range(88)]
    for _ in range(14):
        frames.append(g19_frame(87, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g19 frames:", len(frames))


g17(OUT + "content-34-power-up-fund.gif")
g18(OUT + "content-35-the-duel.gif")
g19(OUT + "content-36-the-vote.gif")
print("part17 done")
