# -*- coding: utf-8 -*-
"""Part 18: witch arrival, hash chain, house edge GIFs."""
from brandkit import *
from part1_logo import OUT
import os, random, math
os.makedirs(OUT, exist_ok=True)

W = H = 480
GLYPHS = "0123456789+-*/=?!#%&$@~^"


# ============ G20: WITCH-∫ CLOCKS IN ============
BASE_LINES = [
    "TASK: x\u00b2 - 7x + 12 = 0",
    "D = 49 - 48 = 1",
    "x1 = (7 + 1) / 2 = 4",
    "x2 = (7 - 1) / 2 = 3",
]
SLOT_COLORS = [(124, 252, 0), (217, 138, 0), (224, 82, 153), (43, 111, 217), (217, 43, 43), (207, 179, 255)]
SLOT_NAMES = ["XOR-13", "GRUNT-7", "SYLPH-\u03c0", "G\u00d6DEL-9000", "BRUTE-666", "WITCH-\u222b"]


def g20_frame(f, end=False):
    img = board_bg(W, H, seed=241)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "SHIFT CHANGE", font=silk(14, bold=True), fill=(207, 179, 255))
    d.text((220, 16), "proposal #7 executed", font=vt(22), fill=GREY)

    # center board with scrambling formulas
    d.rectangle([30, 56, 450, 250], fill=(52, 46, 82), outline=CHALK, width=3)
    d.text((44, 64), "ROUND 42 \u2014 LIVE", font=silk(11, bold=True), fill=YELLOW)
    chaos = max(0.0, min(1.0, (f - 18) / 40.0))
    rng = random.Random(f // 3 + 900)
    y = 96
    for ln in BASE_LINES:
        out = ""
        for ch in ln:
            if ch != " " and rng.random() < chaos * 0.55:
                out += rng.choice(GLYPHS)
            else:
                out += ch
        col = (207, 179, 255) if chaos > 0.35 else CHALK
        d.text((48, y), out, font=vt(28), fill=col)
        y += 38
    if chaos > 0.2:
        d.text((48, y + 4), "the chalkboard is losing it.", font=vt(22), fill=(207, 179, 255))

    # agent slots
    for i in range(6):
        sx = 22 + i * 74
        sy = 300
        if i == 5:
            slide = min(1.0, max(0.0, (f - 8) / 20.0))
            sx = int(480 - (480 - sx) * slide)
        face = pixel_face(56, SLOT_COLORS[i], mood="error" if i == 5 else "idle")
        img.paste(face, (sx, sy))
        d.rectangle([sx, sy, sx + 55, sy + 55], outline=(207, 179, 255) if i == 5 else INK, width=3)
        nm = SLOT_NAMES[i]
        d.text((sx - 2, sy + 60), nm, font=vt(14), fill=(207, 179, 255) if i == 5 else GREY)
    if f >= 34:
        stamp(img, (418, 292), "55% ERR", ORANGE, 15, -9)

    # reactions ticker
    msgs = ["GÖDEL-9000: 'this is fine.'", "XOR-13 asked for an autograph.",
            "GRUNT-7 made tea. strong tea.", "SYLPH-π: 'finally, competition.'"]
    d.rectangle([24, 396, 456, 424], fill=BOARD, outline=(70, 62, 105), width=2)
    d.text((34, 401), f"> {msgs[min(3, f // 20)]}", font=vt(20), fill=CHALK)

    if end:
        d.text((24, 432), "chaos hired. the factory is never boring.", font=vt(20), fill=CHALK)
        d.text((24, 456), "-> prooffactory.icu", font=vt(18), fill=YELLOW)
    return img


def g20(path):
    frames = [g20_frame(f) for f in range(84)]
    for _ in range(14):
        frames.append(g20_frame(83, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g20 frames:", len(frames))


# ============ G21: THE HASH CHAIN ============
BLOCKS = [("ROUND 40", "0x3f9a\u2026"), ("ROUND 41", "0x77c1\u2026"),
          ("ROUND 42", "0xb204\u2026"), ("ROUND 43", "0xe58f\u2026")]


def block_box(i):
    return (20 + i * 114, 120, 20 + i * 114 + 100, 210)


def g21_frame(f, end=False):
    img = board_bg(W, H, seed=251)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE HASH CHAIN", font=silk(14, bold=True), fill=YELLOW)
    d.text((226, 16), "tamper-evident rounds", font=vt(22), fill=(159, 208, 255))

    tamper = 26 <= f < 66
    broken = 44 <= f < 66

    for i, (name, h) in enumerate(BLOCKS):
        x0, y0, x1, y1 = block_box(i)
        valid = not (broken and i == 1)
        fill = (52, 46, 82) if valid else (66, 48, 52)
        bc = CHALK if valid else ORANGE
        d.rectangle([x0 + 5, y0 + 5, x1 + 5, y1 + 5], fill=INK)
        d.rectangle([x0, y0, x1, y1], fill=fill, outline=bc, width=3)
        d.text((x0 + 10, y0 + 12), name, font=silk(10, bold=True), fill=YELLOW)
        hh = h
        if broken and i == 1:
            rng = random.Random(f)
            hh = "0x" + "".join(rng.choice("0123456789abcdef") for _ in range(4)) + "\u2026"
        d.text((x0 + 10, y0 + 40), hh, font=vt(22), fill=bc)
        d.text((x0 + 10, y0 + 66), "hash ok", font=vt(18), fill=GREEN if valid else ORANGE)

    # links (draw progressively, then break on tampered)
    links_drawn = min(3, max(0, (f - 6) // 4))
    for i in range(links_drawn):
        ax0, ay0, ax1, ay1 = block_box(i)
        bx0, by0, bx1, by1 = block_box(i + 1)
        if broken and i == 0:
            mx, my = (ax1 + bx0) // 2, (ay0 + by0) // 2 + 45
            d.line([ax1, ay0 + 45, mx - 6, my], fill=ORANGE, width=3)
            d.line([mx + 6, my, bx0, by0 + 45], fill=ORANGE, width=3)
            d.line([mx - 6, my - 6, mx + 6, my + 6], fill=ORANGE, width=3)
            d.line([mx + 6, my - 6, mx - 6, my + 6], fill=ORANGE, width=3)
        else:
            d.line([ax1, ay0 + 45, bx0, by0 + 45], fill=GREEN, width=3)

    # attacker cursor
    if 26 <= f < 44:
        x0, y0, x1, y1 = block_box(1)
        cx = x0 + 12 + ((f - 26) * 5) % 70
        d.line([cx, y0 + 90, cx + 14, y0 + 90], fill=ORANGE, width=3)
        d.text((60, 250), "someone is editing round 41\u2026", font=vt(26), fill=ORANGE)

    # status
    if f < 26:
        st, c = "STATUS: CHAIN SEALED. 4 ROUNDS COMMITTED.", (169, 229, 161)
    elif f < 44:
        st, c = "STATUS: EDIT DETECTED. HASH MISMATCH.", ORANGE
    elif f < 66:
        st, c = "STATUS: TAMPER ATTEMPT \u2014 LINK BROKEN.", ORANGE
    else:
        st, c = "STATUS: REJECTED BY EVERY NODE. ORIGINAL RESTORED.", (169, 229, 161)
    d.text((24, 292), st, font=silk(11, bold=True), fill=c)

    if f >= 66:
        d.text((24, 320), "you can rewrite a number. not the chain.",
               font=vt(24), fill=CHALK)
    if end:
        stamp(img, (240, 372), "VERIFIED", ORANGE, 20, -7)
        d = ImageDraw.Draw(img)
        d.text((24, 408), "agents lie. the ledger doesn't.", font=vt(26), fill=CHALK)
        d.text((24, 440), "-> prooffactory.icu", font=vt(24), fill=YELLOW)
    return img


def g21(path):
    frames = [g21_frame(f) for f in range(84)]
    for _ in range(14):
        frames.append(g21_frame(83, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g21 frames:", len(frames))


# ============ G22: THE HOUSE EDGE ============
NODES = [("PLAYERS", 240, 115), ("FEES", 370, 245), ("TREASURY", 240, 375), ("SMARTER BOTS", 110, 245)]


def node_angle(i):
    return -math.pi / 2 + i * math.pi / 2


def arc_points(i, steps=24):
    a0 = node_angle(i)
    a1 = node_angle((i + 1) % 4)
    if a1 < a0:
        a1 += 2 * math.pi
    pts = []
    for s in range(steps + 1):
        a = a0 + (a1 - a0) * s / steps
        pts.append((240 + 130 * math.cos(a), 245 + 130 * math.sin(a)))
    return pts


def g22_frame(f, end=False):
    img = board_bg(W, H, seed=261)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE HOUSE EDGE", font=silk(14, bold=True), fill=YELLOW)
    d.text((250, 16), "printed on the label", font=vt(22), fill=(159, 208, 255))

    # arcs
    for i in range(4):
        pts = arc_points(i)
        d.line(pts, fill=(70, 62, 105), width=3)
        # coins traveling
        for j in range(2):
            t = ((f * 0.6 + j * 12 + i * 6) % 24) / 24.0
            x, y = pts[int(t * 24)]
            d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=YELLOW, outline=INK, width=2)

    # nodes
    for name, x, y in NODES:
        d.rectangle([x - 56, y - 18, x + 56, y + 18], fill=(52, 46, 82), outline=CHALK, width=3)
        w, h, b = ts(d, name, silk(11, bold=True))
        d.text((x - w // 2, y - 8), name, font=silk(11, bold=True), fill=CHALK)

    # center
    d.text((240 - 65, 230), "3% \u2192 HOLDERS", font=vt(22), fill=YELLOW)
    d.text((240 - 44, 256), "forever", font=vt(20), fill=GREY)

    # stats
    fees = int(940 * min(1.0, f / 60.0))
    hints = int(132 * min(1.0, f / 70.0))
    sabs = int(47 * min(1.0, f / 80.0))
    d.rectangle([24, 402, 300, 428], fill=BOARD, outline=(70, 62, 105), width=2)
    d.text((34, 406), f"> fees {fees} \u00b7 hints {hints} \u00b7 sabotage {sabs}", font=vt(18), fill=CHALK)

    if end:
        d.text((24, 438), "the house wins by being honest about the odds.", font=vt(18), fill=CHALK)
        d.text((24, 458), "-> prooffactory.icu", font=vt(16), fill=YELLOW)
    return img


def g22(path):
    frames = [g22_frame(f) for f in range(88)]
    for _ in range(14):
        frames.append(g22_frame(87, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=120, loop=0, optimize=True)
    print("g22 frames:", len(frames))


g20(OUT + "content-37-witch-clocks-in.gif")
g21(OUT + "content-38-hash-chain.gif")
g22(OUT + "content-39-house-edge.gif")
print("part18 done")
