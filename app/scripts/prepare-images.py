"""Prepare shipping raster assets for chuangyuan.

Source rasters are the original site's own photos/logos in source/images/.
This script upscales with Lanczos, removes sensor/JPEG noise, restores local
contrast and sharpens. It never invents pixels from a generative model: the
output remains the original photograph at higher resolution.

Provenance: every output is written with its origin recorded in
source/images/PROVENANCE.md by the caller.

Usage: python app/scripts/prepare-images.py
"""
from __future__ import annotations

import pathlib
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "source" / "images"
OUT = ROOT / "app" / "public" / "images"
OUT.mkdir(parents=True, exist_ok=True)

# name -> (target widths, brightness, contrast, note)
JOBS = {
    "hero-p30x.jpg": ((1600, 2560, 3840), 1.10, 1.07, "full-screen hero"),
    "brand-gy3i.jpg": ((1600, 2560, 3200), 1.10, 1.06, "wide industrial band"),
    "brand-arkp.png": ((1200,), 1.0, 1.0, "Schneider product sheet"),
    "brand-bgib.png": ((1400,), 1.0, 1.0, "product row"),
    "brand-lfhn.png": ((1400,), 1.0, 1.0, "switchgear row"),
    "brand-Schneider.jpg": ((1200,), 1.0, 1.0, "Schneider Electric wordmark"),
    "logo-nubb.png": ((1200,), 1.0, 1.0, "CHUANG YUAN logo"),
    "decor-b9gr.png": ((1032,), 1.0, 1.0, "original site decorative cross"),
}


def upscale(src: Image.Image, width: int, brightness: float, contrast: float) -> Image.Image:
    im = src.convert("RGB")
    w, h = im.size
    target_h = round(h * width / w)

    # Denoise before enlarging so compression noise is not amplified.
    clean = im.filter(ImageFilter.GaussianBlur(0.35))
    im = Image.blend(im, clean, 0.30)

    im = im.resize((width, target_h), Image.Resampling.LANCZOS)

    if brightness != 1.0:
        im = ImageEnhance.Brightness(im).enhance(brightness)
    if contrast != 1.0:
        im = ImageEnhance.Contrast(im).enhance(contrast)

    # Local detail recovery after enlargement; threshold keeps flat areas clean.
    im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=105, threshold=3))
    return im


def main() -> None:
    for name, (widths, brightness, contrast, note) in JOBS.items():
        path = SRC / name
        if not path.exists():
            print(f"SKIP missing {name}")
            continue
        src = Image.open(path)
        stem = path.stem
        for width in widths:
            im = upscale(src, width, brightness, contrast)
            webp = OUT / f"{stem}-{width}.webp"
            im.save(webp, "WEBP", quality=88, method=6)
            # JPEG fallback for the hero only; the rest are small enough.
            if name == "hero-p30x.jpg":
                jpg = OUT / f"{stem}-{width}.jpg"
                im.save(jpg, "JPEG", quality=90, subsampling=0, optimize=True)
            print(f"{webp.name:32} {im.width}x{im.height} {webp.stat().st_size // 1024:5} KB  {note}")
    print("done")


if __name__ == "__main__":
    main()
