# -*- coding: utf-8 -*-
"""Part 7: wave-3 social cards 1080x1080. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os, random
os.makedirs(OUT, exist_ok=True)

S = 1080


def ctitle(img, text, y, size=52):
    glitch_text(img, (S // 2, y), text, ps2p(size), k=2)
    return ImageDraw.Draw(img)


# ============ C12: KNOW YOUR LIES ============
def c12(path):
    img = dither(S, S, seed=73)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, S, 46], "\u2736 SPECIMEN BOARD \u2736 HANDLE WITH DOUBT \u2736")
    d = ctitle(img, "KNOW YOUR", 84, 58)
    d = ctitle(img, "LIES.", 196, 58)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 360, 300), "\u2736 the flawed-proof engine's greatest hits \u2736", 38, GREY)
    specimens = [
        ("TYPE 01 \u00b7 OFF-BY-ONE", "x = 4", "(should be 5)"),
        ("TYPE 02 \u00b7 SIGN FLIP", "D = -1", "(should be 1)"),
        ("TYPE 03 \u00b7 PLUS TWO", "x2 = 5", "(should be 3)"),
        ("TYPE 04 \u00b7 TIMES TEN", "120", "(should be 12)"),
    ]
    pos = [(90, 360), (550, 360), (90, 580), (550, 580)]
    for (label, wrong, note), (x, y) in zip(specimens, pos):
        sticker(img, [x, y, x + 440, y + 196], fill=WHITE, shadow=6, border=5)
        d = ImageDraw.Draw(img)
        d.text((x + 24, y + 20), label, font=silk(17, bold=True), fill=INK)
        d.text((x + 24, y + 62), wrong, font=vt(52), fill=RED)
        d.text((x + 200, y + 86), note, font=vt(32), fill=GREY)
        d.rectangle([x + 24, y + 140, x + 416, y + 146], fill=PAPER2)
        d.text((x + 24, y + 152), "frequency: every round. unavoidably.", font=vt(26), fill=GREY)
    d = ImageDraw.Draw(img)
    d.text((110, 830), "one of them hides in every proof.", font=vt(44), fill=INK)
    d.text((110, 884), "learning the catalog is the whole meta.", font=vt(44), fill=ACCENT)
    vtext(d, (S // 2 - 260, 990), "\u2736 study the lies \u2736", 38, RED)
    img.save(path)


# ============ C13: THE SABOTAGE DECK ============
def c13(path):
    img = dither(S, S, seed=79)
    d = ctitle(img, "THE SABOTAGE DECK", 80, 40)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 330, 160), "\u2736 every tool costs credits \u2736", 38, GREY)
    cards = [
        ("COFFEE", ORANGE, "mug",
         ["speeds up your", "agent. ethically", "sourced. probably."]),
        ("SABOTAGE", RED, "bolt",
         ["stalls the leader.", "the factory is not", "fair. it is fun."]),
        ("HINT", YELLOW, "bulb",
         ["circles the lie's", "neighborhood. zero", "refunds. ever."]),
    ]
    for i, (name, col, icon, desc) in enumerate(cards):
        x = 90 + i * 305
        y0, y1 = 240, 900
        sticker(img, [x, y0, x + 290, y1], fill=WHITE, shadow=7, border=5)
        d = ImageDraw.Draw(img)
        d.rectangle([x, y0, x + 290, y0 + 74], fill=col, outline=INK, width=5)
        tw, _, tb = ts(d, name, ps2p(22))
        d.text((x + 145 - tw // 2 - tb[0], y0 + 37 - 11), name, font=ps2p(22), fill=INK)
        # icon canvas
        cx, cy = x + 145, y0 + 210
        if icon == "mug":
            d.rectangle([cx - 34, cy - 24, cx + 30, cy + 44], fill=(133, 87, 44), outline=INK, width=5)
            d.rectangle([cx + 30, cy - 8, cx + 56, cy + 28], outline=INK, width=5)
            d.rectangle([cx - 22, cy - 60, cx - 12, cy - 36], fill=GREY)
            d.rectangle([cx + 2, cy - 70, cx + 12, cy - 36], fill=GREY)
        elif icon == "bolt":
            d.polygon([(cx + 14, cy - 70), (cx - 34, cy + 6), (cx - 8, cy + 6),
                       (cx - 22, cy + 66), (cx + 34, cy - 12), (cx + 6, cy - 12)],
                      fill=YELLOW, outline=INK)
            d.line([(cx + 14, cy - 70), (cx - 34, cy + 6)], fill=INK, width=5)
            d.line([(cx - 8, cy + 6), (cx - 22, cy + 66)], fill=INK, width=5)
            d.line([(cx - 22, cy + 66), (cx + 34, cy - 12)], fill=INK, width=5)
            d.line([(cx + 34, cy - 12), (cx + 6, cy - 12)], fill=INK, width=5)
            d.line([(cx + 6, cy - 12), (cx + 14, cy - 70)], fill=INK, width=5)
        else:
            d.ellipse([cx - 34, cy - 66, cx + 34, cy + 2], fill=CHALK, outline=INK, width=5)
            d.rectangle([cx - 14, cy + 2, cx + 14, cy + 26], fill=GREY, outline=INK, width=4)
            d.rectangle([cx - 22, cy + 26, cx + 22, cy + 40], fill=GREY, outline=INK, width=4)
            tw, _, tb = ts(d, "?", vt(52))
            d.text((cx - tw // 2 - tb[0], cy - 46), "?", font=vt(52), fill=INK)
        yy = y0 + 330
        for ln in desc:
            d.text((x + 28, yy), ln, font=vt(32), fill=INK)
            yy += 42
        d.text((x + 28, y1 - 60), "cost: credits.", font=vt(26), fill=GREY)
        d.text((x + 28, y1 - 32), "worth it: yes.", font=vt(26), fill=ACCENT)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 280, 990), "\u2736 the house is a quadratic equation \u2736", 34, GREY)
    img.save(path)


# ============ C14: FILE 666 ============
def c14(path):
    img = dither(S, S, seed=83)
    d = ctitle(img, "FILE 666", 80, 56)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 220, 180), "\u2736 classified \u2736", 38, RED)
    # dossier panel (the one dark element)
    px0, py0, px1, py1 = 90, 250, S - 90, 860
    d.rectangle([px0 + 9, py0 + 9, px1 + 9, py1 + 9], fill=INK)
    d.rectangle([px0, py0, px1, py1], fill=BOARD, outline=INK, width=6)
    rows = [
        ("SUBJECT: BRUTE-666", None),
        ("ROLE: brute force", None),
        ("ERROR RATE: 2% (verified twice)", None),
        ("STATUS:", "locked"),
        ("LAST SEEN: the basement. it never left.", None),
        ("THREAT LEVEL:", "maximum"),
        ("NOTE: do not ask about the hold.", None),
    ]
    y = py0 + 44
    for text, redact in rows:
        d.text((px0 + 44, y), text, font=vt(40), fill=CHALK)
        if redact:
            tw = d.textlength(text, font=vt(40))
            bw = d.textlength(redact, font=vt(40))
            d.rectangle([px0 + 44 + tw + 10, y + 4, px0 + 44 + tw + 10 + bw + 30, y + 42], fill=CHALK)
            d.rectangle([px0 + 44 + tw + 10, y + 4, px0 + 44 + tw + 10 + bw + 30, y + 42], outline=(36, 31, 61), width=2)
        y += 82
    stamp(img, (S // 2 + 260, py0 + 120), "TOP SECRET", RED, 28, -9)
    stamp(img, (S // 2 + 300, py0 + 230), "DO NOT ASK", RED, 26, 7)
    d = ImageDraw.Draw(img)
    d.text((110, 900), "the door stays locked. the error rate stays 2%.", font=vt(42), fill=INK)
    d.text((110, 952), "G\u00d6DEL-9000 denies writing this file.", font=vt(42), fill=GREY)
    vtext(d, (S // 2 - 240, 1020), "\u2736 prooffactory.icu \u2736", 34, GREY)
    img.save(path)


# ============ C15: LAB PASS ============
def c15(path):
    img = dither(S, S, seed=89)
    d = ImageDraw.Draw(img)
    # lanyard
    d.line([S // 2 - 90, 0, S // 2 - 34, 150], fill=INK, width=10)
    d.line([S // 2 + 90, 0, S // 2 + 34, 150], fill=INK, width=10)
    d.rectangle([S // 2 - 44, 140, S // 2 + 44, 176], fill=GREY, outline=INK, width=4)
    # badge
    bx0, by0, bx1, by1 = 190, 170, S - 190, 930
    sticker(img, [bx0, by0, bx1, by1], fill=WHITE, shadow=9, border=6)
    d = ctitle(img, "LAB PASS", 210, 44)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 190, 292), "\u2736 phase 02 \u2736", 32, GREY)
    # photo
    fimg = pixel_face(180, (43, 111, 217), mood="idle")
    img.paste(fimg, (250, 350))
    d.rectangle([250, 350, 250 + 179, 350 + 179], outline=INK, width=5)
    d.text((250, 540), "photo: G\u00d6DEL-9000", font=vt(26), fill=GREY)
    # fields
    fx = 470
    d.text((fx, 360), "HOLDER: ____________", font=vt(38), fill=INK)
    d.text((fx, 412), "REP: PORTABLE", font=vt(38), fill=ACCENT)
    d.text((fx, 464), "CHAIN: YOURS", font=vt(38), fill=INK)
    d.text((fx, 516), "ISSUED BY: the basement", font=vt(34), fill=GREY)
    # barcode
    d.rectangle([250, 600, 830, 730], fill=WHITE, outline=INK, width=4)
    rng = random.Random(11)
    bx = 266
    while bx < 810:
        w = rng.choice([3, 3, 6, 9, 12])
        if rng.random() < 0.6:
            d.rectangle([bx, 612, bx + w, 718], fill=INK)
        bx += w + rng.choice([3, 5, 8])
    d.text((250, 748), "scan at the factory door. it knows you now.", font=vt(28), fill=GREY)
    stamp(img, (826, 344), "COMING", ORANGE, 26, -7)
    stamp(img, (852, 424), "SOON", ORANGE, 26, 6)
    d = ImageDraw.Draw(img)
    d.text((S // 2 - 270, 960), "wallet in. reputation out.", font=vt(40), fill=INK)
    d.text((S // 2 - 330, 1012), "the fund feeds phase 2. \u2192 prooffactory.icu", font=vt(40), fill=ACCENT)
    img.save(path)


# ============ C16: BETTING SLIP ============
def c16(path):
    img = dither(S, S, seed=97)
    d = ImageDraw.Draw(img)
    # receipt
    rx0, ry0, rx1, ry1 = 150, 90, S - 150, 900
    sticker(img, [rx0, ry0, rx1, ry1], fill=WHITE, shadow=8, border=5)
    # zigzag tear edges
    for x in range(rx0, rx1, 24):
        d.polygon([(x, ry0), (x + 12, ry0 - 14), (x + 24, ry0)], fill=WHITE)
        d.polygon([(x, ry1), (x + 12, ry1 + 14), (x + 24, ry1)], fill=WHITE)
    d.rectangle([rx0 + 40, ry0 + 36, rx1 - 40, ry0 + 44], fill=INK)
    tw, _, tb = ts(d, "FACTORY BETTING SLIP", ps2p(26))
    d.text((S // 2 - tw // 2 - tb[0], ry0 + 70), "FACTORY BETTING SLIP", font=ps2p(26), fill=INK)
    d.text((S // 2 - 90, ry0 + 122), "No. 0042 \u00b7 guest pass", font=vt(30), fill=GREY)
    d.rectangle([rx0 + 40, ry0 + 172, rx1 - 40, ry0 + 176], fill=PAPER2)
    # agent rows
    y = ry0 + 205
    for name, tag, color, bg, err in AGENTS:
        d.rectangle([rx0 + 60, y + 6, rx0 + 84, y + 30], outline=INK, width=4)
        d.text((rx0 + 104, y), name, font=vt(38), fill=INK)
        d.text((rx0 + 420, y), f"err {int(err*100)}%", font=vt(32), fill=GREY)
        d.line([rx0 + 640, y + 22, rx1 - 80, y + 22], fill=PAPER2, width=3)
        y += 66
    # stake + difficulty
    y += 18
    d.text((rx0 + 60, y), "STAKE:", font=silk(18, bold=True), fill=INK)
    for i, s in enumerate(["10", "25", "50"]):
        x = rx0 + 200 + i * 150
        d.rectangle([x, y + 4, x + 24, y + 28], outline=INK, width=4)
        d.text((x + 40, y), s, font=vt(34), fill=INK)
    y += 66
    d.text((rx0 + 60, y), "DIFFICULTY:", font=silk(18, bold=True), fill=INK)
    for i, s in enumerate(["x1", "x2", "x3"]):
        x = rx0 + 290 + i * 130
        d.rectangle([x, y + 4, x + 24, y + 28], outline=INK, width=4)
        d.text((x + 40, y), s, font=vt(34), fill=INK)
    d.rectangle([rx0 + 40, y + 66, rx1 - 40, y + 70], fill=PAPER2)
    d.text((rx0 + 60, y + 92), "bets close at start.", font=vt(36), fill=INK)
    d.text((rx0 + 60, y + 140), "no refunds. no mercy.", font=vt(36), fill=RED)
    stamp(img, (rx1 - 160, ry0 + 250), "PENDING", BLUE, 26, -8)
    d = ImageDraw.Draw(img)
    d.text((S // 2 - 350, 950), "the factory pays the suspicious,", font=vt(40), fill=INK)
    d.text((S // 2 - 380, 1002), "not the lucky. \u2192 prooffactory.icu", font=vt(40), fill=ACCENT)
    img.save(path)


c12(OUT + "content-12-lie-catalog.png")
c13(OUT + "content-13-sabotage-deck.png")
c14(OUT + "content-14-file-666.png")
c15(OUT + "content-15-lab-pass.png")
c16(OUT + "content-16-betting-slip.png")
print("part7 done")
