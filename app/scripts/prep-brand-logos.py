"""Normalize brand logo artwork into uniform transparent WebP assets.

Sources (all recorded in source/images/PROVENANCE.md):
  - ABB/Emerson/Orbinox/SIEMENS/Schneider/Vertiv: the client's own existing
    site (www.chuangyuancorp.com, page86 brand wall).
  - Samson: Wikimedia Commons "Samson logo wiki.png".
  - Rosemount: Emerson media server, official Rosemount brand logo.
  - Greenwood Crosby: typographic wordmark drawn locally (Emerson sub-brand,
    no standalone public logo) - flagged as such in PROVENANCE.md.

Nothing here is presented as own photography.
"""

from pathlib import Path

from PIL import Image

SRC = Path(__file__).resolve().parents[2] / "source" / "images" / "brands-raw"
OUT = Path(__file__).resolve().parents[1] / "public" / "images"

# source file -> output slug, optional white-threshold tweak
JOBS = [
    ("Schneider.jpg", "schneider", 244),
    ("Orbinox.png", "orbinox", 244),
    ("Vertiv.jpg", "vertiv", 244),
    ("Emerson.jpg", "emerson", 244),
    ("Samson.png", "samson", 244),
    ("Rosemount.png", "rosemount", 244),
    ("GreenwoodCrosby.png", "greenwood", 244),
]

# Orbinox ships a tagline line ("VALVE SOLUTIONS IN MORE THAN 70 COUNTRIES")
# that is unreadable at wall size; keep only the mark itself.
CROP_BOTTOM = {"orbinox": 50}

MAX_EDGE = 640
PAD_RATIO = 0.02


def white_to_alpha(im: Image.Image, threshold: int) -> Image.Image:
    """Drop a flat white studio background, keep anti-aliased edges."""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            if r >= threshold and g >= threshold and b >= threshold:
                px[x, y] = (r, g, b, 0)
            else:
                # Feather: near-white pixels keep partial alpha so edges stay soft.
                near = min(r, g, b)
                if near >= threshold - 14:
                    ratio = (threshold - near) / 14.0
                    px[x, y] = (r, g, b, int(a * max(0.0, min(1.0, ratio))))
    return im


def drop_edge_frame(im: Image.Image) -> Image.Image:
    """The Wikimedia Samson PNG carries a 1-2px black frame around the canvas.
    Flood-fill it from the corner so only the round mark survives."""
    from PIL import ImageDraw

    im = im.convert("RGBA")
    for corner in [(0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)]:
        px = im.getpixel(corner)
        if px[3] > 0 and sum(px[:3]) < 60:
            ImageDraw.floodfill(im, corner, (0, 0, 0, 0), thresh=8)
    return im


def trim(im: Image.Image) -> Image.Image:
    box = im.getchannel("A").getbbox()
    return im.crop(box) if box else im


def fit(im: Image.Image) -> Image.Image:
    w, h = im.size
    scale = MAX_EDGE / max(w, h)
    if scale < 1:
        im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    pad = round(max(im.size) * PAD_RATIO)
    canvas = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    canvas.alpha_composite(im, (pad, pad))
    return canvas


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, slug, thr in JOBS:
        src = SRC / name
        if not src.exists():
            print(f"MISSING {src}")
            continue
        im = Image.open(src)
        if slug == "samson":
            im = drop_edge_frame(im)
        if slug in CROP_BOTTOM:
            im = im.crop((0, 0, im.width, min(im.height, CROP_BOTTOM[slug])))
        has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
        im = im.convert("RGBA")
        if has_alpha:
            # Already transparent art: just trim any stray matte.
            im = trim(im)
        else:
            im = trim(white_to_alpha(im, thr))
        im = fit(im)
        dst = OUT / f"brand-{slug}-logo.webp"
        im.save(dst, "WEBP", quality=94, method=6)
        print(f"{dst.name:28s} {im.size[0]}x{im.size[1]}  {dst.stat().st_size // 1024}KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
