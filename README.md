# WARP

**Fees in. Hours out.**

A token on Robinhood Chain, paired against tokenised NVDA. Every buy and sell pays a
3% fee — a 2% creator tax and a 1% Pons fee. The creator tax is priced in dollars
against the Chainlink NVDA feed and spent on RTX 5090 capacity. Once an hour that
capacity is divided among holders as compute credits, measured in 5090 hours and
fixed at the price of the hour they were credited.

Credits are spent through an OpenAI-compatible gateway, or on a dedicated pod you
SSH into. They are compute access — not cash, not a yield, and no amount is
guaranteed.

## The loop

| Step | What happens |
|---|---|
| **Trade** | Every buy and sell on the Pons curve pays 3% of its value in NVDA. Per side, not per round trip. |
| **Buy capacity** | The 2% creator tax is priced via Chainlink NVDA and spent on RTX 5090 hours at the current rate. |
| **Settle** | Once an hour, wallets holding ≥ 1,000 WARP are recorded and capacity is split by share of *eligible* supply. |
| **Claim** | Credits sit in your ledger until you attach them to an API key. Nothing expires, nothing is pushed. |

## Parameters

| Parameter | Value |
|---|---|
| Trading fee | 3% per side — 2% creator tax, 1% Pons |
| Holder allocation | The creator tax, two thirds of collected fees |
| Minimum balance | 1,000 WARP |
| Settlement | Hourly |
| Pricing feed | Chainlink NVDA |
| GPU price | Updated weekly; hours fixed when credited |
| Credit expiry | None |
| Credit transfer | Not transferable |
| Key capacity | 40 RTX 5090 hours |
| Network | Robinhood Chain · 4663 |
| Minted for rewards | 0 — compute is funded by fees, not issuance |

## Running it

No build step, no dependencies to install. It is one HTML file.

```bash
python -m http.server 5173 --directory .
```

Then open <http://localhost:5173>.

## Deploying

Any static host works — the page pulls only Three.js from cdnjs and two families
from Google Fonts.

```bash
npx vercel deploy --prod .
```

## What is in here

```
index.html    the whole site — markup, styles, the WebGL cluster and the estimator
README.md     this file
LICENSE       MIT
```

### The cluster

A WebGL scene built on Three.js r128: 120 instanced RTX cards across two rack rows
either side of a cold aisle, 240 individually rotating fans, hourly settlement
pulses travelling the overhead spine, and six labelled landmarks that open the rule
they stand for. Lighting and materials read the page's CSS custom properties, so the
scene follows the light/dark toggle.

### The estimator

Arithmetic on values you type — balance, 30-day volume, GPU price, eligible supply.
Nothing is fetched and nothing is stored. It exists so the answer is yours rather
than a marketing figure, including when the answer is close to nothing.

## Notes

- No APY appears anywhere in this project, by design. A rate implies a promise about
  the future and there is no mechanism here that could keep one.
- No contract address is published in this repository.
- Nothing here is an offer of securities or investment advice.
