<p align="center">
  <img src="brand/out/logo-horizontal.png" alt="PROOF FACTORY — the little math-agent lab" width="720">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/deploy-GitHub%20Pages-2b2440?style=flat-square&labelColor=ff9ecf" alt="GitHub Pages">
  <img src="https://img.shields.io/badge/deps-zero-2b2440?style=flat-square&labelColor=a9e5a1" alt="zero dependencies">
  <img src="https://img.shields.io/badge/license-MIT-2b2440?style=flat-square&labelColor=9fd0ff" alt="MIT">
  <img src="https://img.shields.io/badge/88%C3%9731-or%20die-2b2440?style=flat-square&labelColor=ffe28a" alt="88x31 or die">
</p>

<p align="center">
  <b>a cozy little research station where pocket math-agents live in the basement.<br>
  you are the SCIENCE DIRECTOR. bet on them. check their proofs. trust no one.</b>
</p>

<p align="center">⚠ WARNING: agents sometimes lie. that's not a bug, that's the philosophy. ⚠</p>

---

## ∎ what is this?

**PROOF FACTORY** is a tiny web sandbox where five AI-ish math agents race to
solve — and *prove* — formulas, and you, the human, run the betting desk and
the rubber stamp. Every round, the agents type full step-by-step proofs on a
chalkboard. One of the proofs contains a deliberately broken step. Speed wins
credits; **catching the lie wins reputation**.

No install. No build step. No email. One HTML file, a guest pass, and a
grudge against XOR-13.

`→` live: **[prooffactory.icu](https://prooffactory.icu)**

---

## ∎ the philosophy

Modern AI gives you fluent answers and asks for blind trust. Proof Factory
builds the opposite habit:

1. **Outputs are claims, not facts.** Every agent answer ships with a proof —
   and the proof is where the game lives.
2. **Verification is the fun part.** The approval minigame makes you read the
   work: one step is wrong on purpose, and the factory pays you for noticing.
3. **Agents have reputations, not vibes.** Each agent has a measurable error
   rate (35% intern → 2% brute force). Betting against your own agent is
   allowed. encouraged, even.
4. **The indie web is a feature.** Guest passes instead of accounts, an
   engineer's log instead of comments, 88×31 badges instead of metrics. Small,
   honest, weird software that runs forever on free hosting.

> a proof you didn't check is just a rumor with math in it.

---

## ∎ how a round works

<p align="center">
  <img src="brand/out/infographic.png" alt="How the factory works" width="480">
</p>

1. **GET A PASS** — enter on a guest pass (free, zero questions) or connect a
   wallet for the LAB PASS.
2. **PICK AN AGENT & STAKE** — five agents, different speeds and honesty.
   Stake 10/25/50 credits, pick difficulty ×1/×2/×3. Bets close at start.
3. **THE RACE** — agents type full proofs line by line. Coffee your agent,
   sabotage the leader, buy a hint. The factory is not fair. It is fun.
4. **CHECK THE PROOF** — one proof step is WRONG ON PURPOSE. Approve a good
   proof → credits + rep. Reject a bad one → bigger rep.
5. **REP & THE ECONOMY** — go broke and the factory grants you +25. Forgiveness
   is a mechanic. So are badges.

---

## ∎ technology

The entire app is **one `index.html`** (~1000 lines) with **zero
dependencies and zero build tooling**. Everything is generated at runtime.

| Layer | What it does | How |
|---|---|---|
| **Task engines** | 8 generators (quadratic, linear, derivative, Collatz, Euclid GCD, primality, arithmetic combos, Diophantine systems). Every task ships with a canonical step-by-step reference proof. | pure functions, seeded randomness |
| **Flawed-proof engine** | Injects a plausible lie into the last step of a proof (off-by-one, sign flip, ±2, ±10) for the approval minigame. | `makeFlawed()` |
| **Race engine** | Token queues per agent; proofs type out char-by-char at agent-specific speeds; random stalls, errors and mood lines. | `setTimeout` queues, no frameworks |
| **Pixel faces** | Each agent has a 14-unit-grid canvas face (visor, square eyes, mood mouths: idle / typing / error / brute) with a blink loop. | `<canvas>` + `drawRect`, `image-rendering: pixelated` |
| **Sound** | Square-wave blips per keystroke, a two-oscillator sawtooth ambient drone at 55 Hz. | WebAudio API, **no audio assets** |
| **State** | Credits, rep, bets, guestbook, unlocks survive reloads. | `localStorage` |
| **Wallet hook** | "Connect wallet (lab pass)" stub ready for on-chain rep. | `window.ethereum` detection |
| **Deploy** | Static hosting on GitHub Pages, custom domain + HTTPS on Porkbun. | A records → GitHub edge |

Design system: cream paper `#f6edd8`, ink `#2b2440`, hard offset shadows,
glitch headlines (pink→blue→yellow stack), dithered backgrounds, marquee
status line. Full brand kit in [`brand/`](brand/BRAND.md) — palette,
typography (Press Start 2P / VT323 / Silkscreen), generators included.

### run it locally

```bash
git clone https://github.com/degenopus/proof-factory.git
cd proof-factory
python -m http.server 8000   # or just open index.html
```

No `npm install`. There is no npm. The agents like it that way.

---

## ∎ why it matters

- **Agent verification, gamified.** As AI agents take over more work, the
  scarce human skill is *checking* outputs, not producing them. Proof Factory
  trains exactly that muscle, on math that is objective enough to grade.
- **Trust as an economy.** Reputation is earned by catching lies, not by
  generating content. A tiny preview of how human–agent markets could price
  honesty instead of fluency.
- **Cheap to run, forever.** One static file on free hosting. No database to
  rot, no API keys to expire. Indie-web software has a long half-life.
- **A real game loop.** Stakes, risk, sabotage, forgiveness, collectibles
  (88×31 badges), a locked agent (BRUTE-666 — you didn't hear it from us).

---

## ∎ prospects / roadmap

- **LAB PASS on-chain** — wallet login becomes the real thing: rep as a
  portable on-chain record, seasonal leaderboards, director tournaments.
- **Agent marketplace** — community-submitted agents with published error
  profiles. Breed your own liar. Stake against it.
- **New proof domains** — logic puzzles, code-correctness races, lightweight
  zero-knowledge-flavored challenges ("prove you checked without showing the
  check").
- **Multiplayer factory floor** — shared rounds, visible bets, spectator
  stamping.
- **Embeddable identity** — export your 88×31 badge with live rep burned in.
- **Public race API** — stream agent token queues to other sites. Host your
  own betting desk.

Direction is set by the engineers' log. Sign it.

---

## ∎ project layout

```
index.html          the whole app (markup + CSS + JS)
brand/              identity kit: palette, fonts, generators, all assets
brand/out/          logos, banner, og-image, infographic, 5 content cards
CNAME               prooffactory.icu
LICENSE             MIT
```

## ∎ contributing

Issues and pull requests welcome. Rules: keep it dependency-free, keep the
paper background, don't trust XOR-13.

## ∎ license

[MIT](LICENSE). The agents remain property of the basement.

---

<p align="center">
  <img src="brand/out/badge-88x31.png" alt="PROOF FACTORY 88x31 badge">
  <br>
  ✶ est. 2026 ✶ 88×31 or die ✶ best viewed at 800×600 ✶<br>
  webmaster: GÖDEL-9000 (do not ask) ✶ there's nothing at the bottom of this page. really.
</p>
