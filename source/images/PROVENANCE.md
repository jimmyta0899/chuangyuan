# 图片出处与修图记录（2026-11-23）

所有站点图片均来自创远现有站 `www.chuangyuancorp.com` 自身的图片服务器，逐张来源 URL 与 MD5 登记见 `SOURCES.csv`。**除客户 2026-11-24 提供的 Anderson Greenwood Crosby 标志外，没有任何一张是自有拍摄或外部下载图**，版权状态仍是“待人工确认”，不得在 alt / caption / 正文声称 in-house、自有拍摄或photographed by。

## 放大修图

放大脚本：`app/scripts/prepare-images.py`（Pillow 13）。处理链：原图 → 高斯 0.35 半径轻度降噪（30% 混合，避免放大 JPEG 噪点）→ Lanczos 放大 → 亮度/对比微调 → UnsharpMask 局部锐化 → WebP q88。不生成新像素、不 AI 补全，输出仍是原照片的高分辨率版本。

| 输出 | 原图尺寸 | 输出尺寸 | 用途 |
|---|---|---|---|
| hero-p30x-1600.webp / -2560.webp / -3840.webp | 1920×1080 | 1600×900 / 2560×1440 / 3840×2160 | 首页 100svh 满屏主图，三档响应式，object-position: center |
| brand-gy3i-1600.webp / -2560.webp / -3200.webp | 1920×511 | 1600×426 / 2560×681 / 3200×852 | 首页中部满宽图带，三档响应式 |
| brand-Schneider-1200.webp | 600×177 | 1200×354 | 品牌页 Schneider 标识 |
| brand-greenwood-logo.webp | 496×273（客户提供 agcsl-logo.png） | 484×246 | Anderson Greenwood Crosby 官方标志，白底去除，原始文件存 `source/images/brands-raw/agcsl-logo.png` |
| brand-arkp-1200.webp | 947×595 | 1200×754 | 品牌资料图（备用） |
| brand-bgib-1400.webp | 916×307 | 1400×469 | 品牌资料图（备用） |
| brand-lfhn-1400.webp | 843×282 | 1400×468 | 品牌资料图（备用） |
| logo-nubb-1200.webp | 3309×1117 | 1200×405 | 备用；当前页头用原站文字标识 CHUANG YUAN，不嵌白底图 |
| decor-b9gr-1032.webp | 516×254 | 1032×508 | 原站装饰元素（备用） |

## 使用说明

- 主图与中部图带用 `<picture>` + `srcset`，`sizes="100vw"`，无头截图需 `--virtual-time-budget` 才会等到 async 解码完成；线上浏览器正常。
- 品牌区七个品牌各配一张可核查的标志图：Schneider / Orbinox / Vertiv / Emerson 取自客户现有站品牌墙，Samson 取自 Wikimedia Commons，Rosemount 取自 Emerson 媒体库，Anderson Greenwood Crosby 由客户于 2026-11-24 提供（agcsl-logo.png）。不许用产品图冒充标志。
- 2026-11-24 起按客户要求删除通栏图的 caption “Image: original Chuang Yuan website” / “图片：创远原网站”，图带只保留行业描述行。
