# -*- coding: utf-8 -*-
"""Part 3: explanatory infographic 1200x1900."""
from brandkit import *
from part1_logo import OUT
import os
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 2400

def step_panel(img, y, num, title, lines, note=None, accent=BLUE):
    d = ImageDraw.Draw(img)
    x0, x1 = 70, W - 70
    h = 108 + len(lines) * 46 + (56 if note else 0)
    sticker(img, [x0, y, x1, y + h], fill=WHITE, shadow=7, border=5)
    d = ImageDraw.Draw(img)
    # number chip
    d.rectangle([x0 + 26 + 6, y + 26 + 6, x0 + 106 + 6, y + 106 + 6], fill=INK)
    d.rectangle([x0 + 26, y + 26, x0 + 106, y + 106], fill=accent, outline=INK, width=5)
    nw, nh, nb = ts(d, num, ps2p(34))
    d.text((x0 + 66 - nw // 2 - nb[0], y + 66 - nh // 2 - nb[1]), num, font=ps2p(34), fill=INK)
    d.text((x0 + 136, y + 34), title, font=ps2p(26), fill=INK)
    ty = y + 118
    for ln, col in lines:
        d.text((x0 + 60, ty), ln, font=vt(36), fill=col)
        ty += 46
    if note:
        d.text((x0 + 60, ty + 6), note, font=vt(30), fill=GREY)
    return y + h + 34

def infographic(path):
    img = dither(W, H, seed=21)
    d = ImageDraw.Draw(img)
    marquee(img, [0, 0, W, 46], "\u2736 HOW THE FACTORY WORKS \u2736 READ THIS BEFORE TOUCHING ANYTHING \u2736")
    # title
    glitch_text(img, (W // 2, 84), "HOW THE", ps2p(56), k=2)
    glitch_text(img, (W // 2, 180), "FACTORY WORKS", ps2p(56), k=2)
    d = ImageDraw.Draw(img)
    st = stars()
    tmp = Image.new("RGB", (10, 10)); tdr = ImageDraw.Draw(tmp)
    sw = vtext(tdr, (0, 0), st, 40, GREY)
    vtext(d, (W // 2 - sw // 2, 268), st, 40, GREY)
    y = 330
    # WHAT IS THIS
    sticker(img, [70, y, W - 70, y + 190], fill=LILAC, shadow=7, border=5)
    d = ImageDraw.Draw(img)
    d.text((100, y + 24), "// WHAT IS THIS?", font=ps2p(24), fill=INK)
    d.text((100, y + 74), "a sandbox where 5 pocket math-agents race to prove", font=vt(34), fill=INK)
    d.text((100, y + 112), "formulas. you are the SCIENCE DIRECTOR. they work", font=vt(34), fill=INK)
    d.text((100, y + 150), "for you. they also lie to you. that is the product.", font=vt(34), fill=INK)
    y += 224
    y = step_panel(img, y, "1", "GET A PASS", [
        ("enter on a GUEST PASS \u2014 free, zero questions asked.", INK),
        ("or connect a wallet for the LAB PASS (on-chain rep later).", INK)], note="no email. no signup. very 1999.", accent=GREEN)
    y = step_panel(img, y, "2", "PICK AN AGENT & STAKE", [
        ("5 agents. intern to professor. error rate 35% -> 2%.", INK),
        ("stake 10 / 25 / 50 credits. difficulty \u00d71 / \u00d72 / \u00d73.", INK)], note="bets close when the round starts.", accent=YELLOW)
    y = step_panel(img, y, "3", "THE RACE", [
        ("agents type full proofs line by line on the task board.", INK),
        ("cheer yours: coffee (+focus). hurt the leader: sabotage.", INK),
        ("stuck? buy a hint. the factory is not fair. it is fun.", INK)], note="GRUNT-7's kettle is an official sabotage target.", accent=PINK)
    y = step_panel(img, y, "4", "CHECK THE PROOF", [
        ("one proof step is WRONG ON PURPOSE. read carefully.", RED),
        ("approve a good proof -> credits + rep.", INK),
        ("reject a bad one -> bigger rep. rubber stamps are free.", INK)], note="the fastest agent is not the most honest one.", accent=BLUE)
    y = step_panel(img, y, "5", "REP & THE ECONOMY", [
        ("win rounds -> CREDITS. catch lies -> REP.", INK),
        ("broke? request a grant (+25). the factory forgives.", INK),
        ("collect 88\u00d731 badges. display them with pride.", INK)], note="rep is memory. agents remember a sharp director.", accent=ORANGE)
    # warning
    wh = 118
    dashed_sticker(img, [70, y, W - 70, y + wh], fill=YELLOW, border=5, shadow=6)
    d = ImageDraw.Draw(img)
    vtext(d, (100, y + 20), "\u2605 WARNING: agents sometimes lie.", 38, INK)
    vtext(d, (100, y + 64), "that's not a bug, that's the philosophy. \u2605", 38, INK)
    y += wh + 30
    vtext(d, (W // 2 - 300, y), "\u2736 prooffactory.icu \u2736 est. 2026 \u2736", 36, GREY)
    img.save(path)

infographic(OUT + "infographic.png")
print("part3 done")
