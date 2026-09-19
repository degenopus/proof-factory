# -*- coding: utf-8 -*-
"""Part 9: the dev's 7% transparency card 1080x1080. Same tokens as the site."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

S = 1080


def ctitle(img, text, y, size=52):
    glitch_text(img, (S // 2, y), text, ps2p(size), k=2)
    return ImageDraw.Draw(img)


def c20(path):
    img = dither(S, S, seed=101)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, S, 46], "\u2736 FULL DISCLOSURE \u2736 TOKENOMICS WITHOUT THE FINE PRINT \u2736")
    d = ctitle(img, "THE DEV'S", 84, 58)
    d = ctitle(img, "7%", 196, 58)
    d = ImageDraw.Draw(img)
    vtext(d, (S // 2 - 330, 296), "\u2736 where it goes, line by line \u2736", 38, GREY)

    # big 7% sticker, rotated slightly
    big = Image.new("RGBA", (300, 240), (0, 0, 0, 0))
    bd = ImageDraw.Draw(big)
    bd.rectangle([10, 10, 289, 229], fill=WHITE, outline=INK, width=8)
    bd.rectangle([24, 24, 275, 215], outline=ACCENT, width=4)
    bd.text((62, 60), "7%", font=ps2p(96), fill=INK)
    bd.text((40, 176), "OF SUPPLY", font=silk(20, bold=True), fill=ACCENT)
    big = big.rotate(-5, expand=True, resample=Image.NEAREST)
    img.paste(big, (110, 380), big)

    rows = [
        ("COMPUTE & SERVERS", "agents must keep proving", 0.42, GREEN),
        ("LIQUIDITY", "so you can always exit", 0.24, BLUE),
        ("TOURNAMENT PRIZES", "paid in tokens, not promises", 0.16, YELLOW),
        ("3% PAYOUT BUFFER", "distributions never miss", 0.11, PINK),
        ("RESERVE", "thermostat repairs (G\u00d6DEL insists)", 0.07, LILAC),
    ]
    x0, y = 470, 370
    d = ImageDraw.Draw(img)
    for name, why, frac, col in rows:
        d.rectangle([x0 + 6, y + 6, x0 + 520, y + 96], fill=INK)
        d.rectangle([x0, y, x0 + 520, y + 90], fill=WHITE, outline=INK, width=4)
        d.rectangle([x0, y, x0 + 14, y + 90], fill=col)
        d.text((x0 + 28, y + 10), name, font=silk(22, bold=True), fill=INK)
        d.text((x0 + 28, y + 46), why, font=vt(28), fill=GREY)
        d.text((x0 + 540, y + 8), f"{int(frac * 100)}%", font=vt(52), fill=INK)
        d.rectangle([x0 + 540, y + 62, x0 + 540 + int(frac * 200), y + 82], fill=col)
        y += 106

    # the dark board: why not 0%
    bx0, by0, bx1, by1 = 90, 920, S - 90, 1040
    d.rectangle([bx0 + 8, by0 + 8, bx1 + 8, by1 + 8], fill=INK)
    d.rectangle([bx0, by0, bx1, by1], fill=BOARD, outline=INK, width=6)
    d.text((bx0 + 34, by0 + 18), "WHY NOT 0%? a dev with no stake has no reason to stay.",
           font=vt(32), fill=CHALK)
    d.text((bx0 + 34, by0 + 62), "no VC. no presale. the 7% IS the budget - on the label.",
           font=vt(32), fill=(159, 208, 255))

    stamp(img, (250, 810), "SKIN IN THE GAME", ACCENT, 24, -7)
    stamp(img, (840, 330), "NOT A VC", RED, 24, 6)
    img.save(path)


c20(OUT + "content-20-devs-seven.png")
print("part9 done")
