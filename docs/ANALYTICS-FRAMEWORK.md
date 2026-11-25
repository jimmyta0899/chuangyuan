# GA4 / GSC / GTM 框架与接入步骤（占位符阶段）

> 2026-11-25 已接入真实 ID：GA4 measurement `G-127ZKMZS0X`，Google tag / GTM container `GTM-WRMKGVGB`；GSC URL 前缀属性 `https://www.chuangyuancorp.com/` 已建，HTML 文件验证中。GA4 配置标签由 Google tag 容器下发，页面不另装独立 gtag，避免重复 page_view。

## 1. GA4（Google Analytics 4）

**状态**：已接入。`G-127ZKMZS0X`（property `565773757`，web stream `16408544898`），通过 Google tag 容器下发，ID 存于 `app/src/config/analytics.ts`。

框架要求（builder/实现者照此留位）：
- GA4 脚本通过环境变量注入，如 `NEXT_PUBLIC_GA_ID`，放在 `.env.local`（**不进 git**）。
- 组件 `Analytics.tsx` 挂载在根 layout，仅在 ID 存在时加载 `gtag`。
- **事件埋点已接入（2026-11-25）**：`app/src/layouts/Layout.astro` 有一个事件委托脚本，读取元素上的 `data-cy-event` + `data-cy-location` / `data-cy-locale` / `data-cy-brand`，把 `{event, ...detail}` push 进 `window.dataLayer`，由 Google tag 容器转给 GA4。四类事件：
  - `language_switch`（`data-cy-locale`）：页头 `中文` / `EN`。
  - `contact_cta_click`（`data-cy-location`）：header-nav、header-cta、mobile-nav、hero-cta、footer-nav、footer-email。
  - `brand_card_click`（`data-cy-brand`）：品牌墙 8 张卡片，key 见 `BrandGrid.astro`。
  - `form_submit`（`data-cy-location`）：联系表单 submit，用 submit 事件而非 click，避免重复计数。
  - 表单本身仍是 `action="#"` 的静态占位，没有后端收件；事件上报与收件是两回事。
- **判据提醒**（来自 QA-REPORT）：Next 16 `next/script` 会把脚本塞进 RSC payload，HTML 里 grep 不到 GA 不代表断了；判断是否采集只看 GA4 API 按日数据，不看 HTML grep。

接入步骤（用户给 ID 后）：
1. 写 `.env.local`：`NEXT_PUBLIC_GA_ID=G-用户提供`（无 BOM，格式合法）。
2. 本地 build，确认产物 `.rsc.js` / `__next._full.txt` 含测量 ID。
3. 切换当天用 GA4 Realtime 报告确认有 session；次日看按日数据连续。

## 2. GSC（Google Search Console）

**状态**：URL 前缀属性已建，HTML 文件验证阶段。验证文件 `googlebff6e25a7117fd4b.html` 放产物根。

框架要求：
- 站点地图路径固定 `/sitemap.xml`，robots.txt 声明之。
- 预留 GSC 验证文件占位：Google 提供的 `googleXXXXXXXX.html` 放产物根（内容待用户提供）。
- 双语 hreflang 在 sitemap 与页面 `<link rel="alternate">` 两处一致（见 SEO-GEO-FRAMEWORK.md）。

接入步骤（切换 DNS 前后）：
1. GSC 添加属性 `https://www.chuangyuancorp.com/`，用 HTML 文件验证（文件放产物根）。
2. 提交 sitemap：`https://www.chuangyuancorp.com/sitemap.xml`。
3. 存档基线读数：收录数、点击、展示、平均排名（GSC Overview 卡片实数，不用 API 猜）。
4. 判据：page 维度结论要求 impressions ≥5；`query` 维度常返 0 行属展示量分散，不是故障。

## 3. GTM（Google Tag Manager）

**状态**：已接入。`GTM-WRMKGVGB`（GA4 建流时 Google 自动生成的 Google tag 容器），页面注入官方 snippet，GA4 tag 在容器内配置。

框架要求：
- GTM 容器骨架：`<head>` 与 `<body>` 两段标准 snippet 的挂载位，通过环境变量 `NEXT_PUBLIC_GTM_ID` 控制。
- 容器内部结构建议（在 GTM 后台配，不写代码）：
  - Tags：GA4 Configuration（引用上面 measurement ID）
  - Triggers：All Pages、Click - Contact CTA、Click - Language Switch
  - Variables：Page Path、Language（从 URL `/en/` `/zh/` 提取）
- GA4 与 GTM 并存时避免重复发送 page_view（二选一：要么 GA4 脚本独立、GTM 只管其他标签；要么 GA4 由 GTM 下发）。

接入步骤：
1. 用户建好 GTM container，给 ID。
2. 填 `NEXT_PUBLIC_GTM_ID`，本地验证 snippet 出现。
3. 在 GTM 预览模式确认触发器命中。

## 4. 三者关系图（文字版）

```
用户访问 → GTM snippet（容器）→ 触发 GA4 tag → GA4 收数据 → GA4 API 查询验证
                            └→ 其他标签（预留）
GSC ← sitemap + hreflang + 验证文件 ← 站点产物
```

## 5. 已知判据（写进项目记忆）

- GA 死活只看 GA4 API 按日数据，不看 HTML grep（QA-REPORT 教训）。
- 线上验证只用 curl + 核对 `Last-Modified`（python urllib 会拿到旧副本）。
- GSC 收录只认 URL Inspection / Sitemap 页，不认 `site:` 操作符。
