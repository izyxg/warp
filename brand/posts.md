# Posts

Five text-only posts, then the four that carry an image. Written to the same rule
as the site: no APY, no rate, nothing promised that the mechanism could not keep.

---

## Text only

### 01 · Meet Warp

Meet Warp.

Every trade pays a 3% fee. Two thirds of it buys RTX 5090 capacity. Once an hour that capacity is split among holders as compute credits — GPU hours you spend through an OpenAI-compatible API, or a pod you SSH into.

Trading fees, turned into compute.

### 02 · Why compute and not cash

Why compute and not cash?

Paying holders cash in proportion to what they hold is the shape of a security almost everywhere. Compute is a good — you get access to a machine, at what the machine costs.

That distinction isn't a wrapper around the same thing. It's the whole design.

### 03 · What it isn't

No staking. No lock-up. No mint.

There's no contract to deposit into and nothing to approve. Balances are read at a block and left alone.

Sell whenever you want. It costs you the next snapshot, and nothing already in your ledger.

### 04 · What we don't control

Three things decide what you get, and we set none of them:

— how much is traded
— how much eligible supply there is
— what an RTX 5090 hour costs

No APY appears anywhere on our site. A rate is a promise about the future, and nothing here could keep one.

### 05 · For the people who'll use it

If your code already calls an OpenAI-compatible API, the integration is two environment variables.

If you'd rather have the whole card: same credits, a 5090 pod, root over SSH.

Hold the token, spend the compute. Nothing else to sign.

---

## With an image

### 06 · Fees in. Hours out. — `warp-card-01.png`

Fees in. Hours out.

Every WARP buy and sell pays 3%. Two thirds of it — the creator tax — buys RTX 5090 capacity at spot. Once an hour that capacity is split among holders as compute credits.

Nothing is minted to pay anyone. The fee is the only inflow.

### 07 · The arithmetic — `warp-card-02.png`

$100 traded buys about 2 hours 14 minutes on an RTX 5090.

$100 → $3.00 fee → $2.00 of compute → 2.25 hours at $0.89.

Volume and GPU prices both move. Quiet market, fewer hours. Cheaper cards, more hours. We publish the arithmetic instead of a rate.

### 08 · Settlement — `warp-card-03.png`

Every hour, on the hour.

Wallets holding 1,000 WARP or more are recorded, and the capacity bought in that window is split by share of eligible supply — not total supply. Under the threshold you neither receive nor dilute.

No staking. Balances are read at a block and left alone.

### 09 · The gateway — `warp-card-04.png`

Change the base URL. That's the integration.

The Warp gateway speaks the OpenAI chat protocol, so anything already pointed at that shape of API just works. Credits pay for the GPU seconds.

Want the whole card instead? The same credits launch a 5090 pod you SSH into.
