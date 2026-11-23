# Design — CHUANG YUAN B2B site

<!-- impeccable:design-schema 1 -->

Rebuilt 2026-11-23 with impeccable. This is a **replacement visual world**:
product truth, copy, pages and routes are preserved; the prior look is the
anti-reference. The user pinned the direction, so no concept-seed roll was run.

## Direction

Industrial equipment documentation. The site reads like a clean engineering
catalog photographed on a plant floor: one full-bleed monochrome photograph
opens the page, neutral paper carries the facts, and thin rules do the work
that decoration would do elsewhere. No accent hue, no pill buttons, no
rounded cards. The older orange-and-white version was derived from a
JingSourcing capture and is explicitly retired.

Surface mode: **Persuade** for the home page (the visitor decides whether to
enquire) and **Read** for about / brands / contact. The same world carries all
four surfaces; the inner pages simply reduce expression.

## Evidence

- Original site `www.chuangyuancorp.com`, captured 2026-11-23 to
  `_orig/home.html` and `_orig/site.css`.
- Measured original palette: `#2f2f2f`, `#333333`, `#666666`, `#919191`,
  `#fbfbfb`, `#ffffff`, `rgb(224,224,224)`, `rgba(0,0,0,0.18)`. No chromatic
  color in the original stylesheet.
- Original homepage uses jQuery fullPage with a single full-screen dark
  industrial photograph, centered copy, and the words
  “WIN-WIN / INNOVATION / COOPERATION / 创新·合作·共赢”.
- Full source register: `source/FACTS.md`, `source/IMAGES.md`,
  `source/images/SOURCES.csv`.

## Tokens

| Purpose | Value |
|---|---|
| Paper | `#ffffff` / `#f5f5f5` |
| Ink | `#111111` / `#2f2f2f` / `#333333` |
| Secondary ink | `#666666` / `#919191` |
| Rule | `#e0e0e0` on paper, `rgba(255,255,255,.14)` on night |
| Night | `#0d0d0d` / `#161616` |
| Radius | `0` everywhere |
| Body measure | `72ch` |
| Display | `clamp(2.25rem, 4.8vw, 4.5rem)` |
| Section rhythm | `clamp(76px, 8vw, 128px)` |
| Typeface | system sans stack (`Helvetica Neue`, Arial, `Noto Sans SC`, `PingFang SC`, `Microsoft YaHei`) |

**Detector decision.** `impeccable detect src --json` reports one warning:
`overused-font` for the system sans stack. Sustained deliberately — the
original site is a system sans-serif black-face design, and the brief pins
“keep the original site style”. A distinctive display face would break the
brand commitment. No other findings.

## Composition

- **Home:** 100svh photograph with centered headline, subhead, the three
  original-site words, one primary action and one secondary link. A header
  wordmark floats over it; no card grid in the first viewport. Below:
  trust facts → represented brands → full-bleed second photograph →
  differentiators → contact form.
- **Inner pages:** short dark page lead (no eyebrow), then unique content —
  company dossier, brand coverage table, or contact details plus form.
  One main heading per page; no repeated hero across routes.
- **Photography:** `hero-p30x` opens the home page; `brand-gy3i` is the
  mid-page full-width band. Both are the original site's own images,
  upscaled and sharpened (see `source/images/PROVENANCE.md`).

## Motion and states

One authored moment only: a slow scale settle on the hero photograph with
exponential ease-out from an already-visible state. All other motion is
short hover transitions. `prefers-reduced-motion` collapses all of it.
Focus rings use `currentColor`, selection is inverted, scrollbars and
underline offsets are themed, tables use tabular numerals.

## Refusals observed

No kicker/eyebrow above headings, no hero-metric template, no icon-heading-
paragraph card wall as the page structure, no gradient text, no glass
decoration, no colored side borders, no hard offset shadows, no emoji icons,
no rounded pill CTAs, no chromatic accent.

## Verification (2026-11-23)

- `npm run build` passes, 9 HTML files (8 real pages + root redirect).
- 0 broken internal refs, including `srcset` candidates.
- 8/8 pages: exactly one h1; canonical and hreflang en/zh/x-default correct
  and reciprocal; sitemap 8 URLs.
- 0 contamination by JingSourcing numbers, business narrative, or the retired
  orange; 0 British spellings.
- Rendered and inspected at 1440px desktop and 500px mobile. The 390px
  headless capture clipped text because Chrome enforces a 500px minimum
  window width; at a true 500px viewport there is no overflow.
