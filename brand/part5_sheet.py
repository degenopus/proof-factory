# -*- coding: utf-8 -*-
"""Part 5: standalone 88x31 badge + contact sheet."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

badge88(["PROOF", "FACTORY"], bg=PINK).save(OUT + "badge-88x31.png")

# contact sheet for final review
files = ["logo-mark.png", "logo-horizontal.png", "favicon.png", "banner.png", "og-image.png",
         "infographic.png", "content-1-meet-the-agents.png", "content-2-trust-no-one.png",
         "content-3-the-economy.png", "content-4-the-philosophy.png", "content-5-night-shift.png",
         "badge-88x31.png"]
cols, tw_, th_ = 4, 420, 300
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw_, rows * th_), (250, 250, 250))
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(OUT + f).convert("RGB")
    im.thumbnail((tw_ - 16, th_ - 40))
    x = (i % cols) * tw_ + 8; y = (i // cols) * th_ + 8
    sheet.paste(im, (x, y))
    d.text((x + 2, y + th_ - 34), f, font=silk(10), fill=(60, 60, 60))
sheet.save(OUT + "_contact-sheet.png")
print("part5 done")
