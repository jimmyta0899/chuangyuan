"""Cut out the CHUANG YUAN wordmark for use on the dark site header.

The supplied artwork is RGB, pure-white background, with:
  * a saturated red/blue emblem (clean, easy to keep)
  * very faint grey wordmark strokes (values 233-254 on 255 white)

A plain white-key would erase the lettering, so the two regions are handled
separately: emblem keeps its original colour; faint grey strokes are
thresholded into solid white, thickened slightly, then upscaled for HD.
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

SRC = Path("C:/Users/Administrator/Desktop/logo-nubb-1200.webp")
DST = Path("app/public/images/logo-nubb-cutout.webp")

src = Image.open(SRC).convert("RGB")
a = np.asarray(src).astype(np.int16)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
lo = np.minimum(np.minimum(r, g), b)
hi = np.maximum(np.maximum(r, g), b)
darkness = 255 - lo
chroma = hi - lo

# Emblem = saturated colour or clearly dark pixels -> keep source colour.
is_emblem = (chroma > 12) | (darkness > 30)
# Wordmark = any remaining pixel that is even slightly off-white -> solid white.
is_letters = (~is_emblem) & (darkness >= 1)

out = np.zeros((*lo.shape, 4), dtype=np.uint8)
out[..., :3][is_emblem] = a[is_emblem]
out[..., 3][is_emblem] = np.clip(darkness[is_emblem] * 10 + chroma[is_emblem] * 10, 0, 255)
out[..., :3][is_letters] = (255, 255, 255)
out[..., 3][is_letters] = 255

cut = Image.fromarray(out, "RGBA")
alpha = cut.getchannel("A")
# Close the gaps in the thin antialiased strokes, but keep shapes sharp.
alpha = alpha.filter(ImageFilter.MaxFilter(3))
cut.putalpha(alpha)
bbox = alpha.getbbox()
cut = cut.crop(bbox)
cut = cut.resize((cut.width * 2, cut.height * 2), Image.Resampling.LANCZOS)
DST.parent.mkdir(parents=True, exist_ok=True)
cut.save(DST, "WEBP", quality=95, method=6)
print("source", src.size, "ink bbox", bbox, "output", cut.size,
      "bytes", DST.stat().st_size)
