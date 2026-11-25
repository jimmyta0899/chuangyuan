# 迁移准备：websiteonline.cn 自助站 → GitHub Pages

> 目标域名不变：`www.chuangyuancorp.com`。旧站在 websiteonline.cn（自助建站），新静态站将托管在 GitHub Pages。
> 本文件是迁移执行清单，**不是已执行记录**。所有操作等用户明说「迁移/上线」才做。

## 0. 迁移原则（从 QA-REPORT 经验来的）

1. **域名口径唯一化**：全站统一 `www.chuangyuancorp.com`，裸域 `chuangyuancorp.com` 做 301 → www（GitHub Pages 对 apex 的 301 需在 DNS 层用 A 记录指向 GitHub 的 apex IP，或用重定向服务；实测后定）。
2. **先并行验证，再切 DNS**：新站先在 GitHub Pages 的 `*.github.io` 域名跑通全部门禁，再改 DNS，避免中途下线。
3. **迁移当天的风险**：websiteonline 的旧 URL（`/page86`、`/page87?product_id=51` 等）与新站 URL 结构不同，必须有 301 映射，否则旧链接全断。
4. **绝不自动切 DNS**：DNS 变更是发布动作，须用户当场明说。

## 1. 迁移前（在旧站仍在线时做）

- [ ] 完整备份旧站：图片已下载到 `source/images/`（8 张，见 SOURCES.csv）；页面文字已归档到 `source/FACTS.md`。确认无遗漏（page88 新闻、page93 招聘未抓，需补）。
- [ ] 导出旧站全部 URL 清单（首页 + page86/87/88/89/93 + 所有 `?product_id=` 详情页），作为 301 映射的输入。
- [ ] 记录旧站当前 GSC 状态：是否已验证、是否有索引、点击/展示基线（用户需提供 GSC 访问权限或让我用其环境查）。
- [ ] 确认 GitHub 仓库 `jimmyta0899/chuangyuan` 是否可建（用户明说「建仓」才建）。

## 2. GitHub Pages 侧准备（新域名跑通后再切）

- [ ] 建仓 `jimmyta0899/chuangyuan`（PUBLIC 还是 PRIVATE 待定；Pages 两种都支持）。
- [ ] push main 源码；`gh-pages` 分支放产物（沿用 silk 的两步部署模式）。
- [ ] 配 `CNAME` 文件 = `www.chuangyuancorp.com`（放产物根）。
- [ ] GitHub 仓库 Settings → Pages → 指向 gh-pages 分支根目录。
- [ ] 先访问 `<user>.github.io/chuangyuan/` 验证 200，再配自定义域。

## 3. DNS 切换（须用户当场授权）

- [ ] `www` CNAME → `<user>.github.io`（GitHub Pages 自定义域标准做法）。
- [ ] apex（裸域）A 记录 → GitHub Pages IP：`185.199.108.153` / `.109.153` / `.110.153` / `.111.153`（4 条），实现裸域 301 到 www。
- [ ] 在 GitHub 仓库 Settings → Pages 勾选 "Enforce HTTPS"，等证书签发（最长数小时）。
- [ ] 切换前把 TTL 调到最低（如 300s），减少切换当天的缓存滞留。

## 4. 301 映射（旧 URL → 新 URL）

旧站 URL 结构（`chuangyuancorp.com/pageXX?product_id=N`）与新站（`/en/...` `/zh/...`）完全不同。GitHub Pages 静态托管**无法在服务端写 301 规则**（无 `.htaccess`/Nginx）。可选方案：

| 方案 | 做法 | 代价 |
|---|---|---|
| A 客户端 meta refresh 桩页（推荐） | 为每个旧 URL 建一个静态页，写 `<meta http-equiv="refresh">` + canonical 指新址 | 需为 N 个旧 URL 生成桩页；Google 认 canonical，Bing 稍慢 |
| B 保留旧路径别名 | 新站生成 `/page86/` 等别名页直接 200（内容同新页） | 旧链接不跳转但可用；SEO 信号分散 |
| C 不处理 | 旧链接 404 | 丢失外部入链权重，最差 |

**默认选 A**：生成桩页，与 silk 项目旧 slug 处理一致（旧 URL 200 + noindex + meta refresh + canonical 指新址）。

**已执行（2026-11-25）**：旧站已下线，完整 URL 清单抓不到；按本节已记录的 5 个路径建桩页（`app/src/pages/page86.astro` … `page93.astro`），统一 200 + noindex + `meta refresh` + canonical：
- `/page86/` → `/zh/about/`（关于我们）
- `/page87/` → `/zh/brands/`（产品中心；`?product_id=N` 由同一桩页接住）
- `/page88/` → `/zh/`（新闻，新站无对应栏目）
- `/page89/` → `/zh/contact/`（联系我们）
- `/page93/` → `/zh/`（招聘，新站无对应栏目）

`astro.config.mjs` 的 sitemap filter 排除这 5 条，sitemap 仍只有 8 条正式 URL。旧站为中文站，故统一跳中文页。

## 5. 切换后验证（当天）

- [ ] `curl -sI https://www.chuangyuancorp.com/` → HTTP 200，`Location`/canonical 正确。
- [ ] 裸域 `curl -sI https://chuangyuancorp.com/` → 301 到 www。
- [ ] 抽查 4 个旧 URL 桩页 → meta refresh + canonical 正确。
- [ ] sitemap 提交到 GSC + IndexNow（86 条换成新站实际 URL 数）。
- [ ] GA4/GSC/GTM 真实 ID 填入（见 ANALYTICS-FRAMEWORK.md），验证数据采集。
- [ ] Lighthouse 四项 ≥94（干净环境）。
- [ ] 72 小时巡检：GSC 收录、索引状态、404、GA4 流量（与旧站基线对比）。

## 6. 回滚预案

- DNS TTL 已提前调低，出问题可在数分钟内把 CNAME 指回 websiteonline。
- 旧站不要立刻关闭，保留至少 2 周作为回滚兜底。
