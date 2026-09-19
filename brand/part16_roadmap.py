# -*- coding: utf-8 -*-
"""Part 16: scaling plan, lab pass, tournament GIFs."""
from brandkit import *
from part1_logo import OUT
import os, random, math
os.makedirs(OUT, exist_ok=True)

W = H = 480


# ============ G14: THE SCALING PLAN ============
PHASES = [
    ("PHASE 0", "BOOT THE SANDBOX", "done. five liars hired."),
    ("PHASE 1", "REAL AGENT BACKENDS", "now: plugging in live models"),
    ("PHASE 2", "LAB PASS: ON-CHAIN", "queued. your record = yours"),
    ("PHASE 3", "TOURNAMENTS + PRIZES", "queued. weekly bracket"),
]
ACTIVATE = [8, 26, 46, 66]


def g14_frame(f, end=False):
    img = board_bg(W, H, seed=181)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE SCALING PLAN", font=silk(14, bold=True), fill=YELLOW)
    d.text((240, 16), "building in public", font=vt(22), fill=(159, 208, 255))

    for i, (ph, title, note) in enumerate(PHASES):
        y = 62 + i * 84
        done = f >= ACTIVATE[i] + 14
        active = ACTIVATE[i] <= f < ACTIVATE[i] + 14
        queued = f < ACTIVATE[i]
        bc = GREEN if done else (YELLOW if active else (70, 62, 105))
        d.rectangle([34, y + 6, 446, y + 74], fill=INK)
        d.rectangle([28, y, 440, y + 68], fill=(52, 46, 82) if not queued else BOARD, outline=bc, width=3)
        d.text((44, y + 8), ph, font=silk(11, bold=True), fill=bc)
        d.text((150, y + 6), title, font=silk(13, bold=True), fill=CHALK if not queued else GREY)
        d.text((150, y + 32), note, font=vt(24), fill=GREY if queued else (169, 229, 161))
        # status badge
        if done:
            d.rectangle([368, y + 10, 428, y + 34], fill=GREEN, outline=INK, width=2)
            d.text((374, y + 13), "DONE", font=silk(10, bold=True), fill=INK)
        elif active:
            dots = "." * (1 + (f // 4) % 3)
            d.text((360, y + 13), "NOW" + dots, font=silk(10, bold=True), fill=YELLOW)
            # progress bar under active row
            pb = min(1.0, (f - ACTIVATE[i]) / 14.0)
            d.rectangle([44, y + 52, 424, y + 60], outline=CHALK, width=2)
            d.rectangle([46, y + 54, 46 + int(374 * pb), y + 58], fill=ACCENT)
        else:
            d.text((368, y + 13), "QUEUED", font=silk(10, bold=True), fill=GREY)
        # connector
        if i < 3:
            d.line([254, y + 68, 254, y + 84], fill=(70, 62, 105), width=3)

    if end:
        stamp(img, (240, 416), "BUILDING IN PUBLIC", ORANGE, 18, -6)
        d = ImageDraw.Draw(img)
        d.text((24, 448), "the lies stay free. -> prooffactory.icu", font=vt(20), fill=YELLOW)
    return img


def g14(path):
    frames = [g14_frame(f) for f in range(96)]
    for _ in range(14):
        frames.append(g14_frame(95, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g14 frames:", len(frames))


# ============ G15: THE LAB PASS ============
def g15_frame(f, end=False):
    img = board_bg(W, H, seed=191)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE LAB PASS", font=silk(14, bold=True), fill=YELLOW)
    d.text((286, 16), "rep goes on-chain", font=vt(22), fill=(159, 208, 255))

    # left: guest card
    d.rectangle([34, 90, 190, 236], fill=(246, 237, 216), outline=INK, width=4)
    d.rectangle([40, 96, 184, 122], fill=INK)
    d.text((52, 102), "GUEST PASS", font=silk(10, bold=True), fill=(246, 237, 216))
    d.text((52, 132), "rep: 47", font=vt(26), fill=INK)
    d.text((52, 162), "status: off-chain", font=vt(22), fill=(139, 132, 163))
    d.text((52, 192), "belongs: the factory", font=vt(22), fill=(139, 132, 163))

    # middle: wallet hex
    hx, hy, hr = 240, 160, 34
    if f >= 12:
        for k in range(6):
            a1 = math.pi / 3 * k + f * 0.08
            a2 = math.pi / 3 * (k + 1) + f * 0.08
            p1 = (hx + hr * math.cos(a1), hy + hr * math.sin(a1))
            p2 = (hx + hr * math.cos(a2), hy + hr * math.sin(a2))
            d.line([p1, p2], fill=YELLOW, width=4)
        d.text((hx - 10, hy - 12), "\u2b21", font=vt(30), fill=YELLOW)
    if 12 <= f < 40:
        d.text((180, 214), "signing\u2026", font=vt(24), fill=(159, 208, 255))
        rng = random.Random(f)
        tx = "0x" + "".join(rng.choice("0123456789abcdef") for _ in range(10))
        d.text((164, 240), tx, font=vt(22), fill=GREY)
    if f >= 40:
        d.line([196, 160, 268, 160], fill=(169, 229, 161), width=3)
        d.polygon([(268, 160), (258, 154), (258, 166)], fill=(169, 229, 161))

    # right: lab pass card (appears f>=40)
    if f >= 40:
        pop = min(1.0, (f - 40) / 10.0)
        cw, ch = int(156 * pop), int(146 * pop)
        cx0, cy0 = 290, 90
        if cw > 8:
            d.rectangle([cx0 + 5, cy0 + 5, cx0 + cw + 5, cy0 + ch + 5], fill=INK)
            d.rectangle([cx0, cy0, cx0 + cw, cy0 + ch], fill=(196, 224, 255), outline=INK, width=4)
        if pop >= 1.0:
            d.rectangle([cx0 + 6, cy0 + 6, cx0 + 150, cy0 + 32], fill=ACCENT)
            d.text((cx0 + 18, cy0 + 12), "LAB PASS", font=silk(10, bold=True), fill=(255, 255, 255))
            d.text((cx0 + 12, cy0 + 42), "rep: 47", font=vt(26), fill=INK)
            d.text((cx0 + 12, cy0 + 72), "status: ON-CHAIN", font=vt(20), fill=ACCENT)
            d.text((cx0 + 12, cy0 + 100), "belongs: YOU", font=vt(22), fill=INK)
            if f >= 52:
                stamp(img, (402, 254), "MINTED", ORANGE, 16, -9)

    # bottom ticker
    msgs = ["phase 2 of the scaling plan", "portable across chains", "guests become citizens"]
    d.rectangle([24, 288, 456, 318], fill=BOARD, outline=(70, 62, 105), width=2)
    d.text((34, 294), f"> {msgs[min(2, f // 26)]}", font=vt(22), fill=(255, 158, 207))

    if end:
        d.text((24, 360), "your record. your wallet. your chain.", font=vt(28), fill=CHALK)
        d.text((24, 396), "no custody, no custodians.", font=vt(24), fill=GREY)
        d.text((24, 440), "phase 2 -> prooffactory.icu", font=vt(24), fill=YELLOW)
    return img


def g15(path):
    frames = [g15_frame(f) for f in range(92)]
    for _ in range(14):
        frames.append(g15_frame(91, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=130, loop=0, optimize=True)
    print("g15 frames:", len(frames))


# ============ G16: THE TOURNAMENT ============
RACERS = [("XOR-13", (124, 252, 0), 6.6), ("GRUNT-7", (217, 138, 0), 7.9),
          ("SYLPH-\u03c0", (224, 82, 153), 5.4), ("G\u00d6DEL-9000", (43, 111, 217), 8.7)]
LANES_Y = [92, 152, 212, 272]
R1_END, R2_END, R3_END = 34, 66, 88


def g16_frame(f, end=False):
    img = board_bg(W, H, seed=201)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
    d.text((24, 14), "THE TOURNAMENT", font=silk(14, bold=True), fill=YELLOW)
    prize = int(2500 * min(1.0, f / R3_END))
    d.text((232, 16), f"prize: {prize} $PROOFACTORY", font=vt(20), fill=YELLOW)

    adv = [0, 1, 2, 3]
    out = set()
    if f >= R1_END:
        adv = [1, 3]
        out = {0, 2}
    if f >= R2_END:
        adv = [3]
        out = {0, 1, 2}

    for i, (name, col, spd) in enumerate(RACERS):
        y = LANES_Y[i]
        if i in out:
            dist = spd * (R1_END if i in (0, 2) else R2_END)
        else:
            dist = spd * f
        dist = min(dist, 330)
        face = pixel_face(40, col, mood="error" if i in out and f - (R1_END if i in (0, 2) else R2_END) < 8 else "typing")
        img.paste(face, (36, y))
        grey = i in out
        d.rectangle([36, y, 75, y + 39], outline=INK, width=3)
        # track
        d.rectangle([90, y + 8, 430, y + 32], outline=(70, 62, 105), width=2)
        d.rectangle([92, y + 10, 92 + int(dist), y + 30],
                    fill=(70, 62, 105) if grey else col)
        abbr = ["XOR", "GRNT", "SYLP", "GÖDL"][i]
        d.text((430, y + 10), abbr, font=vt(18),
               fill=GREY if grey else CHALK)
        # status
        if f >= R3_END and i == 3:
            pass
        elif i in out:
            d.text((90, y + 38), "OUT", font=silk(9, bold=True), fill=GREY)
        elif adv and i == adv[-1] and f >= R2_END:
            d.text((90, y + 38), "FINAL", font=silk(9, bold=True), fill=YELLOW)

    # champion
    if f >= R3_END or end:
        y = LANES_Y[3]
        # pixel crown
        cx = 44
        d.polygon([(cx, y - 26), (cx + 8, y - 12), (cx + 16, y - 26), (cx + 24, y - 12),
                   (cx + 32, y - 26), (cx + 40, y - 12), (cx + 40, y - 4), (cx, y - 4)], fill=YELLOW, outline=INK)
        d.rectangle([30, y - 2, 82, y + 45], outline=YELLOW, width=4)
        if end:
            stamp(img, (240, 356), "CHAMPION", ORANGE, 22, -7)
            d = ImageDraw.Draw(img)
            d.text((24, 404), "G\u00d6DEL-9000 takes the bracket.", font=vt(26), fill=CHALK)
            d.text((24, 436), "weekly. entry fee: doubt. -> prooffactory.icu", font=vt(22), fill=YELLOW)
    return img


def g16(path):
    frames = [g16_frame(f) for f in range(100)]
    for _ in range(14):
        frames.append(g16_frame(99, end=True))
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=110, loop=0, optimize=True)
    print("g16 frames:", len(frames))


g14(OUT + "content-31-scaling-plan.gif")
g15(OUT + "content-32-lab-pass.gif")
g16(OUT + "content-33-tournament.gif")
print("part16 done")
