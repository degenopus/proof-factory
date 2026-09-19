# -*- coding: utf-8 -*-
"""Part 14: three lore GIFs - betting window, the hold, rank ladder. Same tokens."""
from brandkit import *
from part1_logo import OUT
import os, random
os.makedirs(OUT, exist_ok=True)

W = H = 480


# ============ G8: BETTING WINDOW ============
BETS = [
    "0xDE6E\u2026 50 on SYLPH-\u03c0", "0xC0FF\u2026 25 on GRUNT-7",
    "0xBA5E\u2026 10 on XOR-13 (brave)", "PR #1337 50 on G\u00d6DEL-9000",
    "0xF00D\u2026 25 on BRUTE-666", "0x5EED\u2026 25 on SYLPH-\u03c0",
    "0xDE6E\u2026 +25 on SYLPH-\u03c0", "anon 10 on XOR-13",
    "0xBEEF\u2026 50 on GRUNT-7", "0xC0DE\u2026 25 on G\u00d6DEL-9000",
]


def g8_frame(f, end=False):
    img = board_bg(W, H, seed=111)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE BETTING WINDOW", font=silk(14, bold=True), fill=YELLOW)

    # countdown number (5 -> 0), 11 frames each
    if not end:
        n = 5 - min(5, f // 11)
        scale = 1.0 + 0.35 * ((f % 11) / 11.0)
        fsz = int(120 * scale)
        fnt = ps2p(fsz)
        t = str(n)
        w, h, b = ts(d, t, fnt)
        d.text((240 - w // 2 - b[0], 150 - h // 2 - b[1]), t, font=fnt, fill=YELLOW if n > 1 else RED)
        d.text((240 - 120, 236), "bets close at zero", font=vt(28), fill=GREY)
    else:
        for txt, yy, fs in [("BETS CLOSED.", 120, 40), ("round starts.", 196, 28)]:
            fnt = ps2p(fs)
            w, h, b = ts(d, txt, fnt)
            d.text((240 - w // 2 - b[0], yy), txt, font=fnt, fill=RED if fs == 40 else CHALK)

    # incoming bets log (left)
    d.text((20, 280), "INCOMING:", font=silk(10, bold=True), fill=(159, 208, 255))
    nb = min(len(BETS), f // 4 + 1)
    y = 300
    for line in BETS[max(0, nb - 4):nb]:
        d.text((20, y), line, font=vt(24), fill=CHALK)
        y += 26

    # pot
    pot = sum(int(tok) for b in BETS[:nb] for tok in b.split() if tok.isdigit())
    d.rectangle([300, 286, 456, 336], fill=BOARD, outline=YELLOW, width=3)
    d.text((312, 292), "POT", font=silk(10, bold=True), fill=GREY)
    d.text((312, 308), f"{pot} $PF", font=vt(28), fill=YELLOW)

    # odds flicker
    rng = random.Random(f // 3)
    d.text((300, 352), "ODDS", font=silk(10, bold=True), fill=GREY)
    for i, a in enumerate(["SYLPH-\u03c0", "GRUNT-7", "G\u00d6DEL-9000"]):
        odd = 1.5 + rng.random() * 2.5
        d.text((300, 370 + i * 24), f"{a} x{odd:.1f}", font=vt(22), fill=CHALK)

    if end:
        d.text((24, 440), "the window is short. -> prooffactory.icu", font=vt(24), fill=YELLOW)
    return img


def g8(path):
    frames = [g8_frame(f) for f in range(66)]
    for _ in range(14):
        frames.append(g8_frame(66, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=120, loop=0, optimize=True)
    print("g8 frames:", len(frames))


# ============ G9: THE HOLD OPENS ============
KONAMI = ["\u2191", "\u2191", "\u2193", "\u2193", "\u2190", "\u2192", "\u2190", "\u2192", "B", "A"]


def g9_frame(f, end=False):
    img = board_bg(W, H, seed=121)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "BASEMENT CAM 03", font=silk(14, bold=True), fill=(159, 208, 255))

    door_open = max(0, min(1.0, (f - 34) / 20.0))
    dx0, dy0, dx1, dy1 = 110, 60, 370, 380
    # red glow behind the door
    if door_open > 0:
        gw = int((dx1 - dx0) * door_open * 0.6)
        d.rectangle([240 - gw, dy0 + 14, 240 + gw, dy1 - 14], fill=(120, 20, 20))
    # door leaves
    lw = int((240 - dx0) * (1 - door_open))
    for x0, x1 in [(dx0, dx0 + lw), (dx1 - lw, dx1)]:
        d.rectangle([x0, dy0, x1, dy1], fill=(70, 62, 105), outline=INK, width=5)
    # hazard stripes on top of door
    for i in range(8):
        x = dx0 + i * 33
        col = YELLOW if i % 2 == 0 else INK
        d.rectangle([x, dy0 - 14, x + 33, dy0], fill=col)
    # sign
    d.rectangle([140, 96, 340, 132], fill=YELLOW, outline=INK, width=3)
    d.text((150, 104), "DO NOT OPEN", font=silk(13, bold=True), fill=INK)
    d.text((128, 140), "G\u00d6DEL-9000's orders", font=vt(24), fill=GREY)

    # BRUTE-666 face appears in the gap
    if door_open > 0.35:
        face = pixel_face(96, (217, 43, 43), brute=True)
        img.paste(face, (192, 190))
        d.rectangle([192, 190, 287, 285], outline=RED, width=4)

    # konami code typing (bottom)
    if not end:
        d.text((24, 398), "someone typed:", font=vt(24), fill=GREY)
        shown = min(len(KONAMI), max(0, (f - 6) // 3))
        kx = 24
        for k in range(shown):
            ch = KONAMI[k]
            d.rectangle([kx, 424, kx + 34, 458], fill=BOARD, outline=CHALK, width=2)
            d.text((kx + 9, 430), ch, font=silk(14, bold=True), fill=YELLOW)
            kx += 42
        if 0 < shown < len(KONAMI) and f % 3 == 0:
            d.rectangle([kx, 424, kx + 34, 458], outline=GREY, width=2)

    # status / enumeration
    if f < 34:
        st, c = "STATUS: QUIET. TOO QUIET.", GREY
    else:
        st, c = "STATUS: THE HOLD IS OPEN.", RED
    d.text((24, 372), st, font=silk(11, bold=True), fill=c)
    if door_open > 0:
        prog = min(1.0, (f - 34) / 22.0)
        enum = int(1048576 * prog ** 3)
        d.text((276, 372), f"enum: {enum:,}", font=vt(24), fill=ORANGE)
    if end:
        d.text((24, 432), "BRUTE-666 clocks in. err 2% -> prooffactory.icu", font=vt(20), fill=YELLOW)
    return img


def g9(path):
    frames = [g9_frame(f) for f in range(64)]
    for _ in range(14):
        frames.append(g9_frame(64, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g9 frames:", len(frames))


# ============ G10: RANK LADDER ============
LADDER = [  # name, color, base rep
    ("GRUNT-7", (217, 138, 0), 120),
    ("SYLPH-\u03c0", (224, 82, 153), 98),
    ("G\u00d0DEL-9000".replace("\u00d0", "\u00d6"), (43, 111, 217), 96),
    ("XOR-13", (124, 252, 0), 40),
    ("BRUTE-666", (217, 43, 43), 10),
]
EVENTS = [  # frame, agent index, delta, note, color
    (14, 0, +18, "GRUNT-7 solved in 4 steps", GREEN),
    (28, 3, +45, "XOR-13 caught a lie!", GREEN),
    (42, 2, +12, "G\u00d6DEL-9000: flawless proof", GREEN),
    (56, 3, -70, "XOR-13 lied. caught. -70", RED),
    (70, 1, +22, "SYLPH-\u03c0: elegant as always", GREEN),
    (84, 4, +8, "BRUTE-666 brute-forced it", ORANGE),
]


def g10_frame(f, end=False):
    img = board_bg(W, H, seed=131)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "RANK LADDER", font=silk(14, bold=True), fill=YELLOW)
    d.text((250, 16), "reputation is earned", font=vt(22), fill=(159, 208, 255))

    scores = [LADDER[i][2] for i in range(len(LADDER))]
    note = "round in progress\u2026"
    notec = GREY
    flash = -1
    for ef, ai, delta, n, c in EVENTS:
        if f >= ef:
            scores[ai] += delta
            if f - ef < 12:
                note, notec = n, c
                flash = ai
    order = sorted(range(len(LADDER)), key=lambda i: -scores[i])

    # displayed ranks lerp toward target
    if not hasattr(g10_frame, "rank"):
        g10_frame.rank = {i: float(i) for i in range(len(LADDER))}
    tgt = {agent: r for r, agent in enumerate(order)}
    if f == 0:
        g10_frame.rank = {i: float(i) for i in range(len(LADDER))}
    for i in range(len(LADDER)):
        cur = g10_frame.rank[i]
        g10_frame.rank[i] = cur + (tgt[i] - cur) * 0.18

    y0, rh = 64, 62
    for r, agent in enumerate(order):
        name, col, _ = LADDER[agent]
        y = int(round(y0 + g10_frame.rank[agent] * rh))
        x = 30
        bc = GREEN if agent == flash else CHALK
        d.rectangle([x + 5, y + 5, x + 420, y + 54], fill=INK)
        d.rectangle([x, y, x + 420, y + 49], fill=(52, 46, 82), outline=bc, width=3)
        face = pixel_face(38, col)
        img.paste(face, (x + 5, y + 5))
        d.text((x + 52, y + 6), name, font=silk(13, bold=True), fill=CHALK)
        d.text((x + 52, y + 28), f"rep {scores[agent]}", font=vt(24),
               fill=notec if agent == flash and not end else (169, 229, 161))
        d.text((x + 330, y + 8), f"#{r + 1}", font=ps2p(20), fill=YELLOW)

    d.rectangle([24, 400, 456, 430], fill=BOARD, outline=(70, 62, 105), width=2)
    if end:
        d.text((36, 404), "> prooffactory.icu", font=vt(24), fill=YELLOW)
    else:
        d.text((36, 404), f"> {note}", font=vt(24), fill=notec)
    if end:
        stamp(img, (390, 340), "EARNED", RED, 20, -8)
        d = ImageDraw.Draw(img)
        d.text((24, 440), "no airdrops. no boosts. per proof.", font=vt(24), fill=CHALK)
    return img


def g10(path):
    frames = [g10_frame(f) for f in range(98)]
    for _ in range(14):
        frames.append(g10_frame(97, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g10 frames:", len(frames))


g8(OUT + "content-25-betting-window.gif")
g9(OUT + "content-26-the-hold.gif")
g10(OUT + "content-27-rank-ladder.gif")
print("part14 done")
