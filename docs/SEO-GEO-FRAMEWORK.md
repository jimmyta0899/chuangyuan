# SEO / GEO 框架规范（双语站）

> 按 SITE-QA-PLAYBOOK 阶段 0/1 与新站开工一页清单。builder 产出后逐条核对，不符合的修。

## 1. 域名与 URL 口径（阶段 0，先定死）

- 主机：全站统一 `www.chuangyuancorp.com`（裸域 301 → www，见 MIGRATION-PLAN.md）。
- 双语 URL：英文 `/en/...`，中文 `/zh/...`。`/` 重定向到 `/en/`（默认英文商业版，**待用户确认默认语言**）。
- trailingSlash：统一带尾斜杠（如 `/en/about/`），全站一致。
- hreflang：每页 `<link rel="alternate" hreflang="en" href=".../en/...">` 与 `hreflang="zh-CN"` 对应；加 `x-default` 指 `/en/`。
- canonical：每页显式指向自己的 www 绝对 URL（中英各自独立，不互相指）。

## 2. metadata 三层（阶段 1）

- 根 template：标题模板 `页面标题 | CHUANG YUAN`（品牌后缀只在这里加）。
- 页面级：标题不带 `| CHUANG YUAN`（否则重复）；description 每条唯一、不截断成半句（QA-REPORT：four-point 曾被手工截断）。
- og:url：每页显式绝对 URL，不用相对路径。
- 美式英语：所有英文 meta 与正文用美式拼写。

## 3. Schema（结构化数据）

- Organization：`@id` 统一（如 `https://www.chuangyuancorp.com/#organization`），字段 = FACTS.md 的公司名/成立年/地址/电话/邮箱/logo。
- 每个内页按类型加 WebPage / AboutPage / ContactPage / ItemList（品牌列表）。
- 站内 URL 走工具函数补斜杠与 www 前缀，不手写字符串。
- 不编造：schema 里的 aggregateRating、review、employee 等字段没有真实数据就不写。

## 4. 图片管线（GEO 关键）

- 真实尺寸表：`image-dims.json` 记录每张图真实像素，渲染 width/height 与之匹配（防 CLS）。
- 格式：现有 jpg/png 可直接用；保持 1:1 或原比例，容器固定高度。
- alt 两层：内容图有描述性 alt（基于 IMAGES.md 的真实内容），装饰图 `alt=""` 且若可交互需 aria-label 兜底。
- caption：每张内容图配 figure/figcaption（是什么 + 来源 + 关键属性），**禁写 in-house photography**（IMAGES.md 红线）。
- 一图一篇原则：不同页面不重复用同一张图（尤其 hero 与 brand-gy3i 高度相似，别同页用）。

## 5. 内链与结构

- 内链全部相对路径（`/en/about/` 而非绝对 URL），绝对地址会被某些渲染器当外链新窗口打开。
- 每页正文内链 ≥3（nofollow 导航不算）；无孤儿页（按 sitemap 口径算入链）。
- sitemap 收录所有 indexable 页面（中英各 4 页 + 首页 + 桩页），不含 404/noindex。

## 6. a11y

- 每页 1 个 h1；深色底上的文字对比度实测 ≥4.5:1。
- 小控件（轮播圆点、语言切换）点击区 ≥24×24。
- logo-nubb.png 是白字 logo，必须放深色底（否则看不清）。

## 7. GEO（让 AI 抓取器能读）

- 正文服务端渲染可见（不靠 JS hydration 才出内容）——静态站天然满足。
- 5 个 AI UA（GPTBot / OAI-SearchBot / ChatGPT-User / PerplexityBot / ClaudeBot）与普通 UA 返回**完全一致**的 HTML（无 cloaking）。
- RSC payload 若内联过大，参考 silk 做外置（首页 176KB → 57KB）；本栈若非 Next 则不适用。
- 事实密度：FAQ 页把 FACTS.md 的真实问答（成立年、代理品牌、资质、联系方式）写成明确句子，便于 AI 引用。

## 8. 门禁（builder 产出后跑）

- 类型检查 0 错；build 成功。
- SEO preflight：FAIL 0 / WARN 0。
- 双门禁脚本：用坏样本自测过（知道它会 FAIL）。
- 内容闸：若写了正文，跑闸 1（编辑红线）+ 闸 2（五维 ≥94）。
- Lighthouse 四项 ≥94（干净本地环境，独立 headless 实例 + 单斜杠 URL）。
- 产物对外：canonical 全 www、sitemap URL 数、AI UA 字节一致、图片尺寸对账。

## 9. 待用户确认项

- 默认语言：`/` → `/en/` 还是保留 `/` 为中文？当前按 `/en/` 规划。
- 联系表单：静态站无后端，用 mailto 还是占位表单（不接真后端）？当前按 mailto 规划。
