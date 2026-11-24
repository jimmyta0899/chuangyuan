#!/usr/bin/env python3
"""
Turn the new white-background JPG logo into a clean transparent WebP.

Two variants are produced:
  - logo-nubb-cutout.webp : white wordmark variant for dark headers/footers
  - logo-color.webp       : original-color variant for light backgrounds

The source artwork is a dark-gray wordmark plus a red/blue emblem on pure white.
On the site the header and footer are near-black (#0d0d0d / #111111), so the
dark-gray wordmark would be invisible; the white variant recolors neutral
(desaturated) pixels to pure white while keeping the emblem's red/blue intact.
"""
from pathlib import Path
import numpy as np
from PIL import Image

SRC = Path(r"C:/Users/Administrator/.workbuddy/clipboard-images/clipboard-2026-11-24T03-22-56-152Z-bdd19722.jpg")
OUT_DIR = Path(__file__).resolve().parent.parent / "public" / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_WIDTH = 2064  # matches previous high-res logo width
SAT_THRESHOLD = 42   # above this the pixel is treated as colored emblem


def build_alpha(arr: np.ndarray) -> np.ndarray:
    """Alpha from whiteness: pure white -> 0, dark/colored -> high."""
    mn = arr.min(axis=2)
    alpha = 255.0 - mn
    # Push anti-aliased edges toward solid so small sizes stay crisp.
    alpha = np.clip(alpha * 1.35, 0, 255)
    # The JPEG background is not a perfect 255, so kill the near-white grain
    # that would otherwise keep the full square canvas inside the bbox.
    alpha = np.where(alpha < 12, 0.0, alpha)
    return alpha


def unpremultiply_white(arr: np.ndarray, alpha: np.ndarray) -> np.ndarray:
    """Recover true color from a white-composited pixel."""
    a = np.clip(alpha / 255.0, 1e-6, 1.0)[..., None]
    rgb = (arr - 255.0 * (1.0 - a)) / a
    return np.clip(rgb, 0, 255)


def make_variant(src_arr: np.ndarray, alpha: np.ndarray, sat: np.ndarray, white_text: bool) -> Image.Image:
    h, w = src_arr.shape[:2]
    rgb = unpremultiply_white(src_arr, alpha)

    color_mask = sat > SAT_THRESHOLD
    if white_text:
        for c in range(3):
            rgb[..., c] = np.where(color_mask, rgb[..., c], 255.0)
        # Neutral glyphs should be fully opaque where they are clearly ink,
        # and fully transparent on the near-white background.
        neutral_alpha = np.clip((255.0 - src_arr.min(axis=2)) * 1.6, 0, 255)
        neutral_alpha = np.where(src_arr.min(axis=2) > 243, 0.0, neutral_alpha)
        alpha = np.where(color_mask, alpha, neutral_alpha)

    out = np.zeros((h, w, 4), dtype=np.uint8)
    out[..., :3] = rgb.astype(np.uint8)
    out[..., 3] = alpha.astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def trim_and_resize(img: Image.Image, target_w: int) -> Image.Image:
    bbox = img.getchannel("A").getbbox()
    if bbox:
        img = img.crop(bbox)
    h = round(img.height * target_w / img.width)
    return img.resize((target_w, h), Image.Resampling.LANCZOS)


def main() -> None:
    im = Image.open(SRC).convert("RGB")
    arr = np.asarray(im).astype(np.float32)
    mx = arr.max(axis=2)
    mn = arr.min(axis=2)
    sat = mx - mn
    alpha = build_alpha(arr)

    for name, white in (("logo-nubb-cutout.webp", True), ("logo-color.webp", False)):
        variant = make_variant(arr, alpha.copy(), sat, white)
        final = trim_and_resize(variant, TARGET_WIDTH)
        path = OUT_DIR / name
        final.save(path, "WEBP", quality=95, method=6)
        print(f"{name}: {final.size[0]}x{final.size[1]}  {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
