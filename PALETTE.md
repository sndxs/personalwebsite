# Turquoise Oasis Palette

Source: https://colordrop.io/palette/29291

## Swatches (lightest → darkest)

| Hex       | RGB               | Notes |
|-----------|--------------------|-------|
| `#d1f1e8` | 209, 241, 232      | page background (site + CV) |
| `#a8e2d1` | 168, 226, 209      | hover / lift tint |
| `#7fd5c1` | 127, 213, 193      | |
| `#52c9b0` | 82, 201, 176       | |
| `#3ab4a1` | 58, 180, 161       | |
| `#28a18d` | 40, 161, 141       | hero-credential text / button hover |
| `#189a7b` | 24, 154, 123       | |
| `#0f7f68` | 15, 127, 104       | CV heading/link accent |
| `#0b6f58` | 11, 111, 88        | primary accent (buttons, links, eyebrows) |
| `#0a5944` | 10, 89, 68         | CV rule accents |

## Where it's used

**Website (`index.html`)** — CSS custom properties in `:root`. Note the
variable *names* still say `--navy`/`--white` for historical reasons, but
their *values* were flipped to a light theme:

- `--navy` (`#D1F1E8`) — page/hero background
- `--navy-mid`, `--navy-card` (`#FFFFFF`) — nav bar, cards, modals
- `--navy-lift` (`#A8E2D1`) — hover/input fill
- `--gold` (`#0B6F58`) — primary accent (buttons, links, eyebrow labels)
- `--wood-light` (`#28A18D`) — hero credential text, button hover
- `--white` (`#08281F`) — main text (dark ink, despite the name)
- `--muted` (`#3E6D60`) — secondary text
- The two decorative wood-grain background images (`.wood-a`, `.wood-b`)
  are the *original* brown wood photos, shifted to teal at render time via
  `filter: hue-rotate(140deg) saturate(...) brightness(...)` — not
  regenerated images.
- Two intentional exceptions stay dark regardless of theme: the CTA band's
  photo scrim (`.cta-band-overlay`) and the contact modal's backdrop
  (`.modal-overlay`) — both are dark scrims text sits on top of, not page
  backgrounds.

**LaTeX CV (`cv-latex/gen.py`)** — `xcolor` definitions near the top of
`PREAMBLE`:

- `cvbg` (`#D1F1E8`) — page background, via `\pagecolor{cvbg}`
- `cvgray` (`#FFFFFF`) — table row background (white, popping off the tinted page)
- `cvteal` (`#0F7F68`) — section headings, links
- `cvtealdark` (`#0A5944`) — rule lines under headings, subsection headings

## Changing it later

Both the website and the CV pull every color from a small number of
central definitions (`:root` in `index.html`; the `\definecolor` block in
`cv-latex/gen.py`), so swapping to a different palette is mostly a matter
of editing those two spots and regenerating the CV PDF (`python gen.py &&
xelatex main.tex`, run twice for the table of contents / links to settle).
