"""把新版 CHUANG YUAN 徽标（红蓝圆形 + 银色金属字）从白底抠成透明。

新素材是 RGB/JPEG，纯白背景，主体是：
  * 饱和的红蓝圆形（高 chroma）
  * 银色金属质感的"创远机电 / CHUANGYUAN M&E"字（有深色描边 + 金属纹理，
    明暗跨度大，不能简单按阈值二值化，否则会毁掉金属质感）。

策略：按"离白色的距离"计算 alpha —— 纯白背景透明，任何偏色/变暗的像素
按比例保留。银字内部的高光接近白会偏透明，但其描边和纹理足够深，能保住
字形。最后轻微膨胀 alpha 连起抗锯齿缝隙，再放大到高清。
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

SRC = Path("C:/Users/Administrator/.workbuddy/clipboard-images/clipboard-2026-11-23T19-58-43-531Z-0ab63ae0.jpg")
DST_CUT = Path("app/public/images/logo-nubb-cutout.webp")
DST_FLAT = Path("app/public/images/logo-nubb-1200.webp")

src = Image.open(SRC).convert("RGB")
a = np.asarray(src).astype(np.int16)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
lo = np.minimum(np.minimum(r, g), b)
hi = np.maximum(np.maximum(r, g), b)
darkness = 255 - lo          # 离纯白的距离（暗度）
chroma = hi - lo             # 彩色度

# alpha：以最暗通道为准，纯白=0，越暗/越彩越不透明
# 银字高光可达 250+，用较陡的曲线让接近白的像素快速透明，同时保住纹理
raw_alpha = np.maximum(darkness * 3, chroma * 4)
alpha = np.clip(raw_alpha, 0, 255).astype(np.uint8)

rgba = np.dstack([a.clip(0, 255).astype(np.uint8), alpha])
cut = Image.fromarray(rgba, "RGBA")

# 轻微膨胀，连起银字描边的抗锯齿缝隙；不放大字形本身
alpha_img = cut.getchannel("A").filter(ImageFilter.MaxFilter(3))
cut.putalpha(alpha_img)

bbox = alpha_img.getbbox()
cut = cut.crop(bbox)
# 输出宽度 2000px 级别，保证高清
scale = 2000 / cut.width
cut = cut.resize((round(cut.width * scale), round(cut.height * scale)), Image.Resampling.LANCZOS)
cut.save(DST_CUT, "WEBP", quality=95, method=6)

# 页脚用的白底版：直接缩放原图（页脚后续也会改成用透明版，这里保留兼容）
flat = src.crop((int(bbox[0]*0), int(bbox[1]*0), src.width, src.height))
flat.save(DST_FLAT, "WEBP", quality=92, method=6)

print("source", src.size, "ink bbox", bbox, "cutout", cut.size,
      "bytes", DST_CUT.stat().st_size)
