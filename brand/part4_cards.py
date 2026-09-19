# -*- coding: utf-8 -*-
"""Part 4: five content cards 1080x1080."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

S = 1080

def card_bg(seed):
    return dither(S, S, seed=seed)

def ctitle(img, text, y, size=52):
    glitch_text(img, (S // 2, y), text, ps2p(size), k=2)
    return ImageDraw.Draw(img)

# ============ C1: MEET THE AGENTS ============
def c1(path):
    img = card_bg(31)
    d = ctitle(img, "MEET THE", 70)
    d = ctitle(img, "AGENTS", 150)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 250, 240), "\u2736 five liars on payroll \u2736", 40, GREY)
    cw, ch, gap = 188, 400, 16
    x0 = (S - (5 * cw + 4 * gap)) // 2
    y0 = 360
    for i, (name, tag, color, bg, err) in enumerate(AGENTS):
        x = x0 + i * (cw + gap)
        sticker(img, [x, y0, x + cw, y0 + ch], fill=bg, shadow=6, border=4)
        d = ImageDraw.Draw(img)
        fimg = pixel_face(120, color, brute=(name == "BRUTE-666"), mood="typing" if i == 0 else "idle")
        img.paste(fimg, (x + 34, y0 + 22))
        d.rectangle([x + 34, y0 + 22, x + 34 + 119, y0 + 22 + 119], outline=INK, width=4)
        tw, _, tb = ts(d, name, silk(16, bold=True))
        d.text((x + cw // 2 - tw // 2 - tb[0], y0 + 158), name, font=silk(16, bold=True), fill=INK)
        tw, _, tb = ts(d, tag, silk(12))
        d.text((x + cw // 2 - tw // 2 - tb[0], y0 + 186), tag, font=silk(12), fill=(58, 51, 84))
        # err bar
        d.text((x + 16, y0 + 222), "ERROR RATE", font=silk(10), fill=INK)
        bx, by, bw, bh = x + 16, y0 + 246, cw - 32, 22
        d.rectangle([bx + 3, by + 3, bx + bw + 3, by + bh + 3], fill=INK)
        d.rectangle([bx, by, bx + bw, by + bh], fill=WHITE, outline=INK, width=3)
        fillw = max(6, int(bw * err))
        d.rectangle([bx + 3, by + 3, bx + 3 + fillw - 3, by + bh - 3], fill=RED if err > .3 else (ORANGE if err > .1 else GREEN))
        d.text((x + 16, y0 + 278), f"{int(err*100)}%", font=vt(34), fill=INK)
        d.text((x + 16, y0 + 330), ["fast + sloppy", "steady", "elegant", "rarely wrong", "always right?"][i], font=vt(24), fill=GREY)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 330, 800), "\u2736 same task. same chalk. different honesty. \u2736", 40, ACCENT)
    marquee(img, [0, S - 56, S, S], "\u2736 PICK YOUR FAVORITE \u2736 BET BEFORE THE ROUND \u2736 NO REFUNDS \u2736")
    img.save(path)

# ============ C2: TRUST NO ONE ============
def c2(path):
    img = card_bg(37)
    d = ctitle(img, "TRUST NO ONE.", 70, 46)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 320, 140), "\u2736 the approval minigame \u2736", 40, GREY)
    # chalkboard
    bx0, by0, bx1, by1 = 90, 220, S - 90, 740
    d.rectangle([bx0 + 9, by0 + 9, bx1 + 9, by1 + 9], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=BOARD, outline=INK, width=6)
    d.text((bx0 + 36, by0 + 26), "TASK: x\u00b2 - 7x + 12 = 0", font=ps2p(24), fill=YELLOW)
    d.text((bx0 + 36, by0 + 84), "D = b\u00b2 - 4ac = 49 - 48 = 1", font=vt(44), fill=CHALK)
    d.text((bx0 + 36, by0 + 138), "\u221aD = 1", font=vt(44), fill=CHALK)
    d.text((bx0 + 36, by0 + 192), "x1 = (7 + 1) / 2 = 4", font=vt(44), fill=CHALK)
    d.text((bx0 + 36, by0 + 246), "x2 = (7 - 1) / 2 = 5", font=vt(44), fill=RED)
    d.text((bx0 + 36, by0 + 300), "check: 4+5=9 \u2260 7. hmm.", font=vt(36), fill=(159, 208, 255))
    d.text((bx0 + 36, by0 + 352), "answer: x = 4 ; x = 5", font=vt(44), fill=CHALK)
    d.text((bx0 + 36, by0 + 412), "final line typed by: XOR-13 (intern, err 35%)", font=vt(32), fill=GREY)
    stamp(img, (S // 2 + 180, by0 + 190), "WRONG ON", RED, 30, -7)
    stamp(img, (S // 2 + 210, by0 + 300), "PURPOSE?", RED, 30, 5)
    d = ImageDraw.Draw(img)
    d.text((110, 790), "one step is a lie. find it. reject the proof.", font=vt(42), fill=INK)
    d.text((110, 842), "catching lies pays better than being fast.", font=vt(42), fill=ACCENT)
    vtext(d, (S // 2 - 250, 960), "\u2736 prooffactory.icu \u2736", 36, GREY)
    img.save(path)

# ============ C3: THE ECONOMY ============
def c3(path):
    img = card_bg(41)
    d = ctitle(img, "THE ECONOMY", 80)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 300, 165), "\u2736 credits, rep & tiny pride \u2736", 40, GREY)
    # HUD chips
    chips = [("CREDITS: 100", GREEN), ("REP: 0", PINK), ("PASS: GUEST", YELLOW)]
    cx = (S - (3 * 290 + 2 * 24)) // 2
    for label, col in chips:
        sticker(img, [cx, 240, cx + 290, 320], fill=WHITE, shadow=5, border=4)
        d = ImageDraw.Draw(img)
        tw, _, tb = ts(d, label, ps2p(22))
        d.text((cx + 145 - tw // 2 - tb[0], 280 - 12), label, font=ps2p(22), fill=INK)
        cx += 314
    d = ImageDraw.Draw(img)
    d.text((110, 370), "win a round  ->  +credits, +rep", font=vt(44), fill=INK)
    d.text((110, 426), "catch a lie  ->  bigger rep", font=vt(44), fill=INK)
    d.text((110, 482), "go broke      ->  request a grant (+25)", font=vt(44), fill=INK)
    d.text((110, 538), "the factory forgives. once. twice. always.", font=vt(40), fill=GREY)
    # badges
    d.text((110, 620), "// YOUR 88\u00d731 BADGE SHEET", font=ps2p(20), fill=ACCENT)
    badges = [
        (["PROOF", "FACTORY"], PINK),
        (["best viewed", "at 800\u00d7600"], YELLOW),
        (["powered", "by coffee"], GREEN),
        (["under", "construction"], LILAC),
        (["dirtier", "than 99%"], WHITE),
    ]
    bx = (S - (5 * 88 + 4 * 22)) // 2
    for lines, bg in badges:
        b = badge88(lines, bg=bg)
        img.paste(b, (bx, 680))
        d.rectangle([bx, 680, bx + 87, 680 + 30], outline=INK, width=2)
        bx += 110
    d = ImageDraw.Draw(img)
    d.text((110, 760), "display them on your site. that's the whole point.", font=vt(42), fill=INK)
    d.text((110, 814), "88 pixels wide. 31 tall. zero compromise.", font=vt(42), fill=ACCENT)
    # giant 88x31 proof
    big = badge88(["PROOF", "FACTORY"], bg=PINK).resize((88 * 4, 31 * 4), Image.NEAREST)
    img.paste(big, (S // 2 - 176, 900))
    d.rectangle([S // 2 - 176, 900, S // 2 - 176 + 351, 900 + 123], outline=INK, width=6)
    img.save(path)

# ============ C4: THE PHILOSOPHY ============
def c4(path):
    img = card_bg(43)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, S, 46], "LAB DIRECTIVE 003 \u2736 DO NOT ASK ABOUT THE HOLD \u2736")
    d = ctitle(img, "THE", 130, 60)
    d = ctitle(img, "PHILOSOPHY", 230, 60)
    # big yellow warning poster
    dashed_sticker(img, [90, 380, S - 90, 700], fill=YELLOW, border=6, shadow=8)
    d = ImageDraw.Draw(img)
    d.text((130, 420), "\u2605 AGENTS SOMETIMES LIE. \u2605", font=ps2p(34), fill=INK)
    d.text((130, 500), "that's not a bug,", font=vt(64), fill=INK)
    d.text((130, 580), "that's the philosophy.", font=vt(64), fill=INK)
    d.text((110, 760), "a proof you didn't check is a rumor with math in it.", font=vt(44), fill=INK)
    d.text((110, 820), "the factory sells doubt. the fun is in the checking.", font=vt(44), fill=ACCENT)
    d.text((110, 890), "not optimized for a single machine.", font=vt(40), fill=GREY)
    d.text((110, 940), "optimized for a suspicious one.", font=vt(40), fill=GREY)
    vtext(d, (S // 2 - 210, 1000), "\u2736 trust no one \u2736", 38, RED)
    img.save(path)

# ============ C5: NIGHT SHIFT ============
def c5(path):
    img = card_bg(47)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, S, 46], "\u2736 THE BASEMENT IS OPEN \u2736 AGENTS PROVE THE UNPROVABLE \u2736")
    d = ctitle(img, "WORK THE", 110, 58)
    d = ctitle(img, "NIGHT SHIFT", 210, 58)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 330, 310), "\u2736 prooffactory.icu \u2736", 44, ACCENT)
    # big CTA button
    bx0, by0, bx1, by1 = 150, 410, S - 150, 516
    d.rectangle([bx0 + 8, by0 + 8, bx1 + 8, by1 + 8], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=GREEN, outline=INK, width=5)
    tw, _, tb = ts(d, "\u25b8 ENTER ON A GUEST PASS", ps2p(27))
    d.text((S // 2 - tw // 2 - tb[0], (by0 + by1) // 2 - 16), "\u25b8 ENTER ON A GUEST PASS", font=ps2p(27), fill=INK)
    # wallet button
    gx0, gy0, gx1, gy1 = 240, 556, S - 240, 636
    d.rectangle([gx0 + 6, gy0 + 6, gx1 + 6, gy1 + 6], fill=INK)
    d.rectangle([gx0, gy0, gx1, gy1], fill=WHITE, outline=INK, width=4)
    # hexagon glyph
    hx, hy, r = gx0 + 52, (gy0 + gy1) // 2, 16
    d.polygon([(hx + r, hy), (hx + r // 2, hy + int(r * 0.87)), (hx - r // 2, hy + int(r * 0.87)),
               (hx - r, hy), (hx - r // 2, hy - int(r * 0.87)), (hx + r // 2, hy - int(r * 0.87))], outline=INK, width=4)
    d.text((gx0 + 92, gy0 + 22), "connect wallet (lab pass)", font=vt(38), fill=INK)
    # agents peeking from bottom
    fx = 140
    for i, (name, tag, color, bg, err) in enumerate(AGENTS):
        fimg = pixel_face(130, color, brute=(name == "BRUTE-666"), mood="typing" if i == 2 else "idle")
        img.paste(fimg, (fx, 740))
        d.rectangle([fx, 740, fx + 129, 740 + 129], outline=INK, width=5)
        fx += 170
    d = ImageDraw.Draw(img)
    d.text((S // 2 - 350, 960), "no email. no signup. five agents. one liar per round.", font=vt(40), fill=GREY)
    vtext(d, (S // 2 - 220, 1010), "\u2736 est. 2026 \u2736 88\u00d731 or die \u2736", 36, GREY)
    img.save(path)

c1(OUT + "content-1-meet-the-agents.png")
c2(OUT + "content-2-trust-no-one.png")
c3(OUT + "content-3-the-economy.png")
c4(OUT + "content-4-the-philosophy.png")
c5(OUT + "content-5-night-shift.png")
print("part4 done")
