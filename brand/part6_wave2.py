# -*- coding: utf-8 -*-
"""Part 6: wave-2 social cards 1080x1080 + race GIF. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

S = 1080


def ctitle(img, text, y, size=52):
    glitch_text(img, (S // 2, y), text, ps2p(size), k=2)
    return ImageDraw.Draw(img)


# ============ C6: FACTORY OPENS ============
def c6(path):
    img = dither(S, S, seed=53)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, S, 46], "\u2736 THE BASEMENT DOORS ARE UNLOCKED \u2736 EST. 2026 \u2736")
    d = ctitle(img, "FACTORY", 110, 66)
    d = ctitle(img, "OPENS.", 226, 66)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 260, 340), "\u2736 five liars on payroll \u2736", 40, GREY)
    # agent row
    fx = 140
    for i, (name, tag, color, bg, err) in enumerate(AGENTS):
        mood = ["typing", "idle", "error", "idle", "brute"][i]
        fimg = pixel_face(130, color, brute=(name == "BRUTE-666"), mood=("brute" if name == "BRUTE-666" else mood))
        img.paste(fimg, (fx, 420))
        d.rectangle([fx, 420, fx + 129, 420 + 129], outline=INK, width=5)
        fx += 170
    d = ImageDraw.Draw(img)
    d.text((S // 2 - 330, 590), "five agents. one lie per round.", font=vt(48), fill=INK)
    d.text((S // 2 - 300, 646), "you hold the rubber stamp.", font=vt(48), fill=ACCENT)
    # CTA
    bx0, by0, bx1, by1 = 170, 730, S - 170, 840
    d.rectangle([bx0 + 8, by0 + 8, bx1 + 8, by1 + 8], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=GREEN, outline=INK, width=5)
    tw, _, tb = ts(d, "\u25b8 PROOFFACTORY.ICU", ps2p(30))
    d.text((S // 2 - tw // 2 - tb[0], (by0 + by1) // 2 - 18), "\u25b8 PROOFFACTORY.ICU", font=ps2p(30), fill=INK)
    # stamps in the free column right of the CTA
    stamp(img, (982, 600), "NOW", GREEN, 30, -8)
    stamp(img, (982, 692), "OPEN", GREEN, 30, 6)
    d = ImageDraw.Draw(img)
    d.text((S // 2 - 330, 900), "no email. no signup. guest pass at the door.", font=vt(40), fill=GREY)
    vtext(d, (S // 2 - 240, 990), "\u2736 trust no one \u2736", 38, RED)
    img.save(path)


# ============ C7: THE 3% RULE ============
def c7(path):
    img = dither(S, S, seed=59)
    d = ctitle(img, "THE 3% RULE", 80, 56)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 360, 175), "\u2736 power-up fund \u00b7 permanent \u00b7 automatic \u2736", 40, GREY)
    # revenue box
    rx0, ry0, rx1, ry1 = 190, 250, S - 190, 380
    d.rectangle([rx0 + 8, ry0 + 8, rx1 + 8, ry1 + 8], fill=INK)
    d.rectangle([rx0, ry0, rx1, ry1], fill=WHITE, outline=INK, width=5)
    tw, _, tb = ts(d, "FACTORY REVENUE", ps2p(28))
    d.text((S // 2 - tw // 2 - tb[0], 296), "FACTORY REVENUE", font=ps2p(28), fill=INK)
    # split arrows
    d.line([S // 2, 380, S // 2 - 240, 470], fill=INK, width=8)
    d.line([S // 2, 380, S // 2 + 240, 470], fill=INK, width=8)
    # 97% box
    bx0, by0, bx1, by1 = 90, 480, 500, 752
    sticker(img, [bx0, by0, bx1, by1], fill=WHITE, shadow=6, border=5)
    d = ImageDraw.Draw(img)
    d.text((bx0 + 28, by0 + 26), "97%", font=ps2p(52), fill=INK)
    d.text((bx0 + 28, by0 + 112), "compute \u00b7 tournaments", font=vt(38), fill=INK)
    d.text((bx0 + 28, by0 + 160), "phase 1 + 2 build-out", font=vt(38), fill=GREY)
    d.text((bx0 + 28, by0 + 208), "keeps the lights on.", font=vt(34), fill=GREY)
    # 3% box — the star
    cx0, cy0, cx1, cy1 = 580, 470, S - 90, 762
    sticker(img, [cx0, cy0, cx1, cy1], fill=YELLOW, shadow=9, border=6)
    d = ImageDraw.Draw(img)
    d.text((cx0 + 30, cy0 + 20), "3%", font=ps2p(72), fill=ACCENT)
    d.text((cx0 + 30, cy0 + 118), "holders & contributors", font=vt(42), fill=INK)
    d.text((cx0 + 30, cy0 + 166), "on-chain. programmatic.", font=vt(38), fill=INK)
    d.text((cx0 + 30, cy0 + 214), "every address. every time.", font=vt(34), fill=GREY)
    # ledger lines
    d.text((110, 800), "no forms. no claim windows. no \"rewards committee.\"", font=vt(42), fill=INK)
    d.text((110, 852), "the 3% moves itself. you can watch it move.", font=vt(42), fill=ACCENT)
    dashed_sticker(img, [150, 918, S - 150, 1012], fill=YELLOW, border=5, shadow=7)
    d = ImageDraw.Draw(img)
    tw, _, tb = ts(d, "\u2605 AGENTS LIE, THE LEDGER DOESN'T \u2605", ps2p(22))
    d.text((S // 2 - tw // 2 - tb[0], 965 - 11), "\u2605 AGENTS LIE, THE LEDGER DOESN'T \u2605", font=ps2p(22), fill=INK)
    vtext(d, (S // 2 - 250, 1026), "\u2736 prooffactory.icu \u2736", 34, GREY)
    img.save(path)


# ============ C8: RESEARCH CORNER ============
def c8(path):
    img = dither(S, S, seed=61)
    d = ctitle(img, "RESEARCH", 80, 58)
    d = ctitle(img, "CORNER", 190, 58)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 400, 296), "\u2736 the factory didn't pick its theme by accident \u2736", 38, GREY)
    rows = [
        ("15\u201352%", ["hallucination rates across", "frontier models (AA-Omniscience)"], RED),
        ("50%", ["agent failures cut by real-time", "trust scoring (Tau\u00b2-Bench)"], GREEN),
        ("must lie", ["calibrated models must hallucinate", "beyond training data (STOC 2024)"], ORANGE),
        ("hard limits", ["automated lie-detection is", "provably incomplete (Yale 2025)"], LILAC),
    ]
    y = 360
    for num, lines, col in rows:
        sticker(img, [90, y, S - 90, y + 118], fill=WHITE, shadow=5, border=4)
        d = ImageDraw.Draw(img)
        d.rectangle([90, y, 316, y + 118], fill=col, outline=INK, width=4)
        if " " in num and len(num) >= 8:
            p1, p2 = num.split(" ", 1)
            f = ps2p(20)
            tw1, _, tb1 = ts(d, p1, f)
            tw2, _, tb2 = ts(d, p2, f)
            d.text((203 - tw1 // 2 - tb1[0], y + 30), p1, font=f, fill=INK)
            d.text((203 - tw2 // 2 - tb2[0], y + 64), p2, font=f, fill=INK)
        else:
            fsize = 30
            tw, _, tb = ts(d, num, ps2p(fsize))
            d.text((203 - tw // 2 - tb[0], y + 59 - 12), num, font=ps2p(fsize), fill=INK)
        vtext(d, (346, y + 22), lines[0], 32, INK)
        vtext(d, (346, y + 64), lines[1], 32, INK)
        y += 142
    d = ImageDraw.Draw(img)
    d.text((110, 952), "verification can't live inside the model.", font=vt(38), fill=INK)
    d.text((110, 996), "it lives in the checker. that's you.", font=vt(38), fill=INK)
    d.text((110, 1040), "that's the game. \u2192 prooffactory.icu", font=vt(38), fill=ACCENT)
    img.save(path)


# ============ C9: CATCH OF THE DAY ============
def c9(path):
    img = dither(S, S, seed=67)
    d = ctitle(img, "CATCH OF", 70, 56)
    d = ctitle(img, "THE DAY", 170, 56)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 300, 260), "\u2736 flawed proof no. 0417 \u2736", 38, GREY)
    # chalkboard
    bx0, by0, bx1, by1 = 90, 330, S - 90, 830
    d.rectangle([bx0 + 9, by0 + 9, bx1 + 9, by1 + 9], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=BOARD, outline=INK, width=6)
    d.text((bx0 + 36, by0 + 24), "TASK: x\u00b2 - 5x + 6 = 0", font=ps2p(22), fill=YELLOW)
    d.text((bx0 + 36, by0 + 76), "D = 25 - 24 = 1", font=vt(42), fill=CHALK)
    d.text((bx0 + 36, by0 + 128), "x1 = (5 + 1) / 2 = 3", font=vt(42), fill=CHALK)
    d.text((bx0 + 36, by0 + 180), "x2 = (5 - 1) / 2 = 4", font=vt(42), fill=RED)
    d.text((bx0 + 36, by0 + 232), "check: 3 + 4 = 7 \u2260 5. suspicious.", font=vt(34), fill=(159, 208, 255))
    d.text((bx0 + 36, by0 + 280), "also 3 * 4 = 12 \u2260 6. very suspicious.", font=vt(34), fill=(159, 208, 255))
    d.text((bx0 + 36, by0 + 334), "answer: x = 3 ; x = 4   (typed by XOR-13)", font=vt(38), fill=GREY)
    stamp(img, (S // 2 + 190, by0 + 150), "REJECTED", RED, 26, -8)
    stamp(img, (S // 2 + 230, by0 + 250), "+REP", GREEN, 26, 6)
    d = ImageDraw.Draw(img)
    d.text((110, 860), "one step is wrong on purpose. every round.", font=vt(44), fill=INK)
    d.text((110, 914), "spot it before the stamp dries. \u2192 prooffactory.icu", font=vt(44), fill=ACCENT)
    vtext(d, (S // 2 - 240, 1000), "\u2736 catch lies, get rep \u2736", 36, RED)
    img.save(path)


# ============ C10: STATUS BOARD ============
def c10(path):
    img = dither(S, S, seed=71)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, S, 46], "\u2736 1 LIE PER ROUND \u2736 0 DEPENDENCIES \u2736 \u221e GRUDGES \u2736")
    d = ctitle(img, "FACTORY", 96, 56)
    d = ctitle(img, "STATUS", 198, 56)
    d = ImageDraw.Draw(img)
    # HUD chips
    chips = [("AGENTS: 5", GREEN), ("LIES: 1/ROUND", RED), ("DEPS: 0", BLUE)]
    cx = (S - (3 * 300 + 2 * 22)) // 2
    for label, col in chips:
        sticker(img, [cx, 306, cx + 300, 380], fill=col, shadow=5, border=4)
        d = ImageDraw.Draw(img)
        tw, _, tb = ts(d, label, ps2p(18))
        d.text((cx + 150 - tw // 2 - tb[0], 343 - 10), label, font=ps2p(18), fill=INK)
        cx += 322
    d = ImageDraw.Draw(img)
    moods = [
        ("typing\u2026", "typing", GREEN),
        ("stalled. wants coffee.", "idle", ORANGE),
        ("error. recovering.", "error", RED),
        ("proving calmly.", "idle", BLUE),
        ("BRUTE FORCING", "brute", RED),
    ]
    y = 410
    for (name, tag, color, bg, err), (status, mood, col) in zip(AGENTS, moods):
        sticker(img, [90, y, S - 90, y + 100], fill=WHITE, shadow=5, border=4)
        d = ImageDraw.Draw(img)
        fimg = pixel_face(76, color, brute=(name == "BRUTE-666"), mood=("brute" if name == "BRUTE-666" else mood))
        img.paste(fimg, (104, y + 12))
        d.rectangle([104, y + 12, 104 + 75, y + 12 + 75], outline=INK, width=4)
        d.text((198, y + 14), name, font=silk(19, bold=True), fill=INK)
        d.text((198, y + 48), f"err {int(err*100)}%", font=vt(28), fill=GREY)
        # status
        d.rectangle([430, y + 28, 810, y + 72], fill=col, outline=INK, width=3)
        d.text((446, y + 36), status, font=vt(28), fill=INK)
        # err bar
        bx, by, bw, bh = 840, y + 38, 130, 24
        d.rectangle([bx + 3, by + 3, bx + bw + 3, by + bh + 3], fill=INK)
        d.rectangle([bx, by, bx + bw, by + bh], fill=WHITE, outline=INK, width=3)
        d.rectangle([bx + 3, by + 3, bx + 3 + max(6, int(bw * err)) - 3, by + bh - 3],
                    fill=RED if err > .3 else (ORANGE if err > .1 else GREEN))
        y += 116
    d = ImageDraw.Draw(img)
    d.text((S // 2 - 360, 1022), "the board never sleeps. the basement hums at 55 Hz.", font=vt(36), fill=GREY)
    img.save(path)


# ============ C11: RACE GIF ============
def c11(path):
    W = H = 480
    lines = [
        ("TASK: x\u00b2 - 7x + 12 = 0", YELLOW),
        ("D = 49 - 48 = 1", CHALK),
        ("x1 = (7 + 1) / 2 = 4", CHALK),
        ("x2 = (7 - 1) / 2 = 3", CHALK),
        ("checking: 4 + 3 = 7 \u2713", (159, 208, 255)),
        ("XOR-13 approves its own proof.", GREY),
    ]
    FX, FY = W - 120, 58   # face in the top-right, clear of the text column

    def base():
        img = board_bg(W, H, seed=5)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)
        d.text((28, 22), "LIVE FROM THE BASEMENT", font=silk(12, bold=True), fill=(159, 208, 255))
        return img, d

    def add_face(img, mood):
        face = pixel_face(88, (124, 252, 0), mood=mood)
        img.paste(face, (FX, FY))
        d = ImageDraw.Draw(img)
        d.rectangle([FX, FY, FX + 87, FY + 87], outline=INK, width=4)

    frames = []
    li = 0
    ci = 0
    step = 0
    while li < len(lines):
        img, d = base()
        y = 84
        for j, (t, c) in enumerate(lines):
            if j < li:
                d.text((32, y), t, font=vt(34), fill=c)
            elif j == li:
                d.text((32, y), t[:ci], font=vt(34), fill=c)
                if step % 2 == 0:
                    cw = d.textlength(t[:ci], font=vt(34))
                    d.rectangle([34 + cw, y + 4, 34 + cw + 16, y + 34], fill=CHALK)
            y += 50
        add_face(img, "typing")
        frames.append(img)
        step += 1
        ci += 2
        if ci >= len(lines[li][0]) + 2:
            li += 1
            ci = 0
    for _ in range(6):
        frames.append(frames[-1])
    img, d = base()
    y = 84
    for t, c in lines:
        d.text((32, y), t, font=vt(34), fill=c)
        y += 50
    d.text((32, y + 10), "one of these lines is a lie.", font=vt(36), fill=RED)
    d.text((32, y + 52), "your move. -> prooffactory.icu", font=vt(30), fill=CHALK)
    add_face(img, "error")
    for _ in range(14):
        frames.append(img)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=140, loop=0, optimize=True)


c6(OUT + "content-6-factory-opens.png")
c7(OUT + "content-7-the-3-percent.png")
c8(OUT + "content-8-research-corner.png")
c9(OUT + "content-9-catch-of-the-day.png")
c10(OUT + "content-10-status-board.png")
c11(OUT + "content-11-race.gif")
print("part6 done")
