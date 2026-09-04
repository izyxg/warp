# Brand

The mark is a graphics card seen head-on — board, two fans, bracket tabs, PCIe
fingers. It is the thing the protocol buys, drawn small enough to be a favicon.

| File | Use |
|---|---|
| `mark.svg` | Full colour, on dark |
| `mark-mono.svg` | `currentColor` — takes the colour of its parent |
| `favicon.svg` | Boxed, for tabs and app icons |
| `card.html` | Renders one social card. `?i=0..3` |
| `out/*.png` | The four cards, 3200 × 1800 (2× of 1600 × 900) |

The living version of this page is the **Brand** tab on the site, which shows the
lockups, palette, type scale and the cards together.

## Re-rendering the cards

Edit the `CARDS` array in `card.html`, then, with the site served locally:

```bash
for i in 0 1 2 3; do
  n=$(printf "%02d" $((i+1)))
  chrome --headless=new --disable-gpu --hide-scrollbars \
    --window-size=1600,900 --force-device-scale-factor=2 --virtual-time-budget=8000 \
    --screenshot="out/warp-card-$n.png" "http://localhost:5173/brand/card.html?i=$i"
done
```

On Windows the `--screenshot` path must be absolute and backslashed.

## Rules

- Violet `#8A6BFF` is the only accent. Cyan, gold and green are semantic — data,
  caution, pass — and none of them ever stands in for the brand.
- If it is a figure, it is monospaced. No exceptions.
- Every card carries a real number and a real panel. No stock imagery, nothing
  rendered for decoration.

## Twitter / X assets

| File | Size | Where |
|---|---|---|
| `out/warp-avatar.png` | 1000 × 1000 | Profile picture — X renders it at 400 |
| `out/warp-banner.png` | 3000 × 1000 | Header — a 1500 × 500 at 2× |
| `out/warp-card-0*.png` | 3200 × 1800 | Post images — 1600 × 900 at 2× |

The banner keeps its bottom-left corner empty on purpose: that is where X
overlays the profile picture, and anything placed there is lost.

```bash
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
OUT="C:\path\to\warp\brand\out"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1000,1000 --virtual-time-budget=7000 \
  --screenshot="$OUT\warp-avatar.png" "http://localhost:5173/brand/avatar.html"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1500,500 --force-device-scale-factor=2 --virtual-time-budget=8000 \
  --screenshot="$OUT\warp-banner.png" "http://localhost:5173/brand/banner.html"
```
