# -*- coding: utf-8 -*-
"""Part 15: treasury vault, bot swarm math, pro-rata distribution GIFs."""
from brandkit import *
from part1_logo import OUT
import os, math, random
os.makedirs(OUT, exist_ok=True)

W = H = 480


# ============ G11: THE TREASURY ============
VCX, VCY, VR = 225, 245, 95          # vault center / radius
ALLOCS = [("COMPUTE", 40, ACCENT), ("LIQUIDITY", 25, BLUE),
          ("DIV BUFFER", 20, PINK), ("RESERVE", 15, LILAC)]
SPIGOTS = [("fees", 24, 100), ("rounds", 24, 220), ("tourney", 24, 330)]
COIN_PER = 520
TOTAL_COINS = 24
TREASURY_MAX = COIN_PER * TOTAL_COINS   # 12,480


def spigot_paths():
    out = []
    for name, sx, sy in SPIGOTS:
        out.append([(sx + 78, sy + 10), (VCX - VR - 6, VCY + (sy - VCY) // 2)])
    return out


def g11_frame(f, end=False):
    img = board_bg(W, H, seed=151)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE TREASURY", font=silk(14, bold=True), fill=YELLOW)
    d.text((286, 16), "watch it live", font=vt(22), fill=(159, 208, 255))

    # --- spigots ---
    paths = spigot_paths()
    for (name, sx, sy), pts in zip(SPIGOTS, paths):
        d.rectangle([sx, sy, sx + 76, sy + 22], fill=BOARD, outline=CHALK, width=2)
        d.text((sx + 8, sy + 2), name, font=vt(20), fill=CHALK)
        d.line(pts, fill=(70, 62, 105), width=6)

    # --- interior (behind door) ---
    arrived = min(TOTAL_COINS, max(0, (f - 40) // 2))
    if f > 26:
        d.ellipse([VCX - VR, VCY - VR, VCX + VR, VCY + VR], fill=(52, 46, 82), outline=CHALK, width=3)
        # coin stacks inside
        stacks = [arrived // 3, arrived // 3, arrived - 2 * (arrived // 3)]
        for si, cnt in enumerate(stacks):
            bx = VCX - 52 + si * 38
            for c in range(min(cnt, 8)):
                yy = VCY + 58 - c * 12
                d.ellipse([bx, yy, bx + 30, yy + 9], fill=YELLOW, outline=INK, width=2)

    # --- vault door ---
    unlock = min(90.0, max(0.0, (f - 10) * 6.0))
    open_k = max(0.0, min(1.0, (f - 26) / 14.0))
    r_door = int(VR * 0.92 * (1 - open_k))
    if r_door > 4:
        d.ellipse([VCX - r_door, VCY - r_door, VCX + r_door, VCY + r_door],
                  fill=(70, 62, 105), outline=CHALK, width=4)
        a = math.radians(unlock)
        for k in range(4):
            ang = a + k * math.pi / 2
            x2 = VCX + int(math.cos(ang) * (r_door - 10))
            y2 = VCY + int(math.sin(ang) * (r_door - 10))
            d.line([VCX, VCY, x2, y2], fill=CHALK, width=4)
        d.ellipse([VCX - 14, VCY - 14, VCX + 14, VCY + 14], fill=BOARD, outline=YELLOW, width=3)
    else:
        d.ellipse([VCX - 8, VCY - 8, VCX + 8, VCY + 8], fill=YELLOW, outline=INK, width=2)
    d.ellipse([VCX - VR - 8, VCY - VR - 8, VCX + VR + 8, VCY + VR + 8], outline=(70, 62, 105), width=6)

    # --- coins in flight ---
    for pi, pts in enumerate(paths):
        length = ((pts[1][0] - pts[0][0]) ** 2 + (pts[1][1] - pts[0][1]) ** 2) ** .5
        for j in range(3):
            launch = 4 + (pi * 3 + j) * 3
            dist = (f - launch) * 5.0
            if 0 <= dist <= length:
                t = dist / length
                x = pts[0][0] + (pts[1][0] - pts[0][0]) * t
                y = pts[0][1] + (pts[1][1] - pts[0][1]) * t
                d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=YELLOW, outline=INK, width=2)

    # --- treasury counter ---
    treasury = TREASURY_MAX * min(1.0, max(0.0, (f - 40) / 26.0)) if f > 26 else 0
    d.rectangle([60, 392, 392, 424], fill=BOARD, outline=YELLOW, width=3)
    d.text((72, 398), f"TREASURY: {int(treasury):,} $PROOFACTORY", font=vt(26), fill=YELLOW)

    # --- allocation panel ---
    px = 344
    d.text((px, 66), "ALLOCATION", font=silk(10, bold=True), fill=GREY)
    y = 88
    for name, pct, col in ALLOCS:
        d.text((px, y), name, font=vt(20), fill=CHALK)
        d.text((px + 96, y), f"{pct}%", font=vt(20), fill=col)
        d.rectangle([px, y + 22, px + 112, y + 32], outline=CHALK, width=2)
        fillw = int(108 * pct / 40)
        d.rectangle([px + 2, y + 24, px + 2 + fillw, y + 30], fill=col)
        y += 58
    if end:
        stamp(img, (225, 150), "ON-CHAIN", ORANGE, 20, -8)
        d = ImageDraw.Draw(img)
        d.text((24, 434), "agents lie, the ledger doesn't.", font=vt(20), fill=CHALK)
        d.text((24, 456), "-> prooffactory.icu", font=vt(20), fill=YELLOW)
    return img


def g11(path):
    frames = [g11_frame(f) for f in range(74)]
    for _ in range(14):
        frames.append(g11_frame(73, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g11 frames:", len(frames))


# ============ G12: BOT MATH ============
SWARM_COLORS = [(124, 252, 0), (217, 138, 0), (224, 82, 153), (43, 111, 217), (217, 43, 43)]
EVENTS12 = ["lie detected in lane 2 - human paid +5 rep",
            "BRUTE-666 solved by enumeration. again.",
            "XOR-13 apologized. we accepted. we regret.",
            "hint bought. the house profits.",
            "a proof was 100% honest. suspicious."]


def g12_frame(f, end=False):
    img = board_bg(W, H, seed=161)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "BOT MATH", font=silk(14, bold=True), fill=YELLOW)

    # throughput
    pph = int(min(300, max(0, (f - 6) * 5)))
    d.text((286, 16), f"proofs/hour: {pph}", font=vt(24), fill=(169, 229, 161))

    # swarm 5 x 3
    for r in range(3):
        for c in range(5):
            idx = r * 5 + c
            rng = random.Random(idx * 1000 + f // 5)
            roll = rng.random()
            mood = "error" if roll < 0.07 else ("typing" if roll < 0.6 else "idle")
            fx = 40 + c * 88
            fy = 62 + r * 66
            face = pixel_face(48, SWARM_COLORS[c], mood=mood)
            img.paste(face, (fx, fy))
            bc = ORANGE if mood == "error" else INK
            d.rectangle([fx, fy, fx + 47, fy + 47], outline=bc, width=3)

    # equation (types out)
    eq = "5 bots x 60 rounds/h = 300 proofs/h"
    shown = min(len(eq), max(0, (f - 12) // 1))
    if f >= 12:
        d.text((60, 272), eq[:shown], font=vt(26), fill=CHALK)
        if shown < len(eq) and f % 2 == 0:
            cw = d.textlength(eq[:shown], font=vt(26))
            d.rectangle([62 + cw, 276, 72 + cw, 296], fill=CHALK)

    # event ticker
    d.rectangle([24, 316, 456, 346], fill=BOARD, outline=(70, 62, 105), width=2)
    ev = EVENTS12[(f // 18) % len(EVENTS12)]
    d.text((34, 322), f"> {ev}", font=vt(22), fill=(255, 158, 207))

    # the catch stat
    d.text((24, 358), "1 in 5 proofs hides a lie. find it, get paid.",
           font=vt(20), fill=(159, 208, 255))
    if end:
        d.text((24, 420), "bots do the math. humans do the doubt.", font=vt(26), fill=CHALK)
        d.text((24, 450), "-> prooffactory.icu", font=vt(24), fill=YELLOW)
    return img


def g12(path):
    frames = [g12_frame(f) for f in range(92)]
    for _ in range(14):
        frames.append(g12_frame(91, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=120, loop=0, optimize=True)
    print("g12 frames:", len(frames))


# ============ G13: PRO-RATA ============
HOLDERS = [("0xDE6E\u2026", 250000, 7.5), ("0xC0FF\u2026", 100000, 3.0), ("PR #1337", 50000, 1.5)]
SUPPLY = 1000000


def g13_frame(f, end=False):
    img = board_bg(W, H, seed=171)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "PRO-RATA", font=silk(14, bold=True), fill=YELLOW)
    d.text((286, 16), "the 3%, fairly split", font=vt(22), fill=(159, 208, 255))

    # formula box
    d.rectangle([24, 54, 456, 148], fill=BOARD, outline=CHALK, width=3)
    d.text((40, 62), "POOL THIS ROUND: 30 $PROOFACTORY", font=silk(11, bold=True), fill=YELLOW)
    eq = "cut = 3% x balance / supply"
    shown = min(len(eq), max(0, (f - 8)))
    if f >= 8:
        d.text((40, 92), eq[:shown], font=vt(34), fill=CHALK)
    if f >= 34:
        d.text((40, 122), "supply: 1,000,000", font=vt(24), fill=GREY)

    # holder rows
    for i, (name, bal, payout) in enumerate(HOLDERS):
        a = 40 + i * 12
        p = min(1.0, max(0.0, (f - a) / 16.0))
        y = 168 + i * 78
        d.rectangle([30, y, 330, y + 66], fill=(52, 46, 82), outline=CHALK, width=3)
        d.text((44, y + 6), name, font=silk(13, bold=True), fill=CHALK)
        d.text((44, y + 30), f"balance {bal:,}", font=vt(24), fill=GREY)
        share = bal / SUPPLY * 100
        d.text((212, y + 8), f"{share:.0f}%", font=vt(30), fill=YELLOW)
        d.text((212, y + 40), f"+{payout * p:.2f}", font=vt(26), fill=(169, 229, 161))
        # payout bar right
        bh = int(60 * p * payout / 7.5)
        d.rectangle([346, y + 66 - bh, 400, y + 66], fill=ACCENT, outline=CHALK, width=2)

    if f >= 78 or end:
        d.text((30, 406), "checked: 7.50 + 3.00 + 1.50 = 12.00 / 30", font=vt(24), fill=GREEN)
        d.text((30, 432), "rest goes to the other holders. same formula.", font=vt(22), fill=GREY)
    if end:
        stamp(img, (366, 314), "NO COMMITTEE", ORANGE, 16, -8)
        d = ImageDraw.Draw(img)
        d.text((24, 456), "verify on-chain. -> prooffactory.icu", font=vt(22), fill=YELLOW)
    return img


def g13(path):
    frames = [g13_frame(f) for f in range(96)]
    for _ in range(14):
        frames.append(g13_frame(95, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g13 frames:", len(frames))


g11(OUT + "content-28-treasury.gif")
g12(OUT + "content-29-bot-math.gif")
g13(OUT + "content-30-pro-rata.gif")
print("part15 done")
