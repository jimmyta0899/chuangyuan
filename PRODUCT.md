# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

B2B 采购方与工程项目的设备选型人员：中国境内大型工程总包、央企及其采购/技术部门，以及需要高端机电设备、阀门、仪表、通讯终端设备、电子自动化产品进口与国内采购的海外买家。他们的实际任务是：确认供应商资质、确认代理品牌范围、发起询价或索取资料。站点同时提供简体中文与美式英语两套内容。

## Product Purpose

广州创远机电设备有限公司的对外介绍与询盘入口。让访客在几秒内看懂「这家公司卖什么、有什么资质、代理哪些品牌、怎么联系」，并可直接发起询问。成功 = 合格采购方发起有效询盘，而非流量本身。

## Positioning

创远是「专业高品质机电设备供应商」，同时是中交集团、中能建、中铁国际等央企的合格供应商（已核实事实，见 source/FACTS.md）。这一资质组合是同行无法照抄的具体凭据。业务口径为高端机电设备、阀门、仪表、通讯终端设备、电子自动化产品的国内采购及进出口贸易。

## Operating Context

- 2015 年成立；参与多个国内外大型工程项目。
- 代理品牌 7 个：Schneider、Orbinox、Vertiv、Emerson、Samson、Rosemount、Greenwood Crosby。
- 资质：质量服务诚信单位、AAA 级企业资信等级证书、重质量守信用单位。
- 创业理念：品质改变一切，服务成就未来。
- 联系：广州市海珠区赤岗北路8号瑞福大厦304、305室（510000）；020-62718818；14749327080；Lucy@chuangyuancorp.com。
- 站点需支持日后从现有服务器迁至 GitHub Pages，域名保持 `www.chuangyuancorp.com`。

## Capabilities and Constraints

- 静态站点（Astro 4，构建产物 `app/dist/`），8 个双语页面：`/en/` `/zh/` 各 home/about/brands/contact，加根跳转页。
- 已有 SEO/GEO 骨架：逐页 canonical、hreflang en/zh/x-default、Organization JSON-LD、sitemap、robots.txt。GA4 / GSC / GTM 目前只有占位符，真实 ID 待提供（未确认，不得编造）。
- **内容红线**：所有事实、数字、品牌名、资质、联系方式只能取自 `source/FACTS.md`；未记载的一律不写，不用中性造词填充。禁止 jingsourcing 的一切数字与业务叙事；英文一律美式拼写。
- **图片红线**：只用 `source/images/` 内来自原站的现有素材；不得为没有图片的品牌配不存在的产品图；不得宣称自有拍摄。
- **视觉约束（用户 2026-11-23 明确钉死）**：保持原网站风格；工业感；纯黑白灰；禁止上一版的橙黄色；主视觉为高清大图居中满屏；像素不够时修图提升，不另换图。
- **发布锁**：未建仓、未 push、未部署、未改 DNS；上线必须等用户明说。

## Brand Commitments

- 名称：广州创远机电设备有限公司 / Guangzhou Chuangyuan Mechanical and Electrical Equipment Co., Ltd.；品牌 CHUANG YUAN / 创远机电。
- 视觉身份依据原站 `www.chuangyuancorp.com`：纯黑白灰（实测主色 #2f2f2f / #333333 / #666666 / #919191 / #fbfbfb / #ffffff），全屏深色工业摄影，文字居中；原站使用 jQuery fullPage 单屏滚动。
- 原站标语（可作 Hero 文案依据）：创远机电为您量身订做；WIN-WIN / INNOVATION / COOPERATION；创新 / 合作 / 共赢。
- Logo 素材：`source/images/logo-nubb.png`（3309×1117）。

## Evidence on Hand

- `source/FACTS.md` —— 唯一权威事实源（2026-11-23 从原站 page86 / page87 / page89 抓取）。
- `source/IMAGES.md` / `source/images/SOURCES.csv` —— 图片来源登记。
- `source/images/hero-p30x.jpg` —— 原站首页全屏背景（1920×1080，深色工业配电柜/开关柜厂房照片，无水印无烧字）。
- `_orig/home.html` / `_orig/site.css` —— 原站首页 HTML 与样式，配色与文案证据。
- `app/` —— 当前可运行的 Astro 实现（橙黄版，为本次替换的 anti-reference）。
- 缺失：其余 6 个代理品牌的图片素材、真实 GA4/GSC/GTM ID、公司自有产品照片。禁止编造。

## Product Principles

1. 事实先行：任何数字、资质、品牌、联系方式必须可回溯到 FACTS.md 或原站抓取证据。
2. 原站风格是身份，不是可替换的皮肤：黑白灰工业风、满屏摄影、居中排布保持不变。
3. 双语等权：同一事实在 /en/ 与 /zh/ 表述一致，英文美式拼写。
4. 迁移友好：静态产物、相对内链、逐页 canonical/hreflang，随时可迁至 GitHub Pages。
5. 发布需授权：设计与构建可以自主完成，上线动作必须等用户明说。

## Accessibility & Inclusion

WCAG 2.1 AA 基线：正文对比度 ≥4.5:1、大字号 ≥3:1；每页恰好一个 h1；图片 alt；键盘可聚焦；双语 `lang` 属性与 hreflang 双向互指。

---

> 记录方式说明：本文件由 `source/FACTS.md`、`_orig/home.html` 抓取证据与用户 2026-11-23 的明确 brief 直接提取，未再发起一轮访谈确认（用户的长期偏好是不重复索要已授权的输入）。除上文 `## Capabilities and Constraints` 中标注「未确认」的项目外，均已由仓库证据支撑；如与事实有出入，以 `source/FACTS.md` 为准并回改本文件。
