# BUILD BRIEF — 给 craft anything builder 的硬约束

> 这是本次重建的最高约束。任何一条冲突时，以本文件为准，不得自作主张。

## 任务

把 jingsourcing.com 的**信息架构、版式、信任元素、CTA 样式**作为**结构参考**，为「广州创远机电设备有限公司」重建一个**中英双语 B2B 网站**。不是复制 jingsourcing 的内容，是借它的骨架、填创远的真实血肉。

## 绝对禁止（违反即失败）

1. **禁止搬运 jingsourcing 的任何业务与数字**：不得出现 sourcing agent、Amazon sellers、dropshipping、retailers、government procurement 这些业务叙事；不得出现 6,000+ clients、4,000+ clients、100+ million-dollar sellers、200+ staff、1M+ followers、save 30%、1-by-1 inspection、free inspection 等任何数字或承诺。这些是 jingsourcing 的，不是创远的。
2. **禁止编造任何事实**：公司名、成立年份、产品、品牌、客户、认证、地址、电话、邮箱，只能来自 `source/FACTS.md`。FACTS.md 没有的，不写。
3. **禁止给未配图的品牌编造产品图**：`source/IMAGES.md` 写明只有 Schneider 有图；Orbinox/Vertiv/Emerson/Samson/Rosemount/格林伍德克罗斯比没有图，只能用文字品牌卡，不许找图、不许生成图冒充。
4. **禁止英文英式拼写**：全部美式（meter/color/center/organize/analyze/behavior/while/license/utilize 等）。
5. **禁止在图片 alt/caption/正文写 in-house photography / photographed by 等**：现有图来源见 `source/IMAGES.md`，不确定是否创远自拍，只能写中性表述（如 "Schneider switchgear in a project installation"）。
6. **禁止发布/建仓/push/改 DNS/git remote**：本阶段只在本地 `app/` 写代码，不做任何发布动作。
7. **禁止 AI 生成图片**：只用 `source/images/` 里的现有素材。若某个版式位置缺图，用 CSS 色块/文字卡占位，不要生成。

## 必须做到

1. **中英双语**：URL 结构 `/en/` 与 `/zh/`（英文为默认商业版本，中文为对照）。两种语言内容对应，不是只有英文。所有 `<html lang>`、hreflang、导航语言切换正确。
2. **站点内容完全基于 `source/FACTS.md` 与 `source/IMAGES.md`**：公司身份、7 个代理品牌、资质、联系方式，一字不改地用真实值。
3. **参照 jingsourcing 的结构**，但换成创远语义的板块：
   - Hero：一句价值主张（基于创远真实业务，如"High-end electromechanical equipment, valves and instrumentation, sourced and supplied from China"）+ CTA（联系我们）
   - 业务线/产品：7 个代理品牌（Schneider 等），只用真实名称
   - "Why work with us" 差异化卡片：基于 FACTS.md 的真实资质（2015 成立、央企合格供应商、进出口贸易能力、品质理念）
   - 信任条：只能用真实数字——2015（成立年）、7（代理品牌数）、3（央企客户类别：中交/中能建/中铁国际）；**不得编造客户总数/员工数**
   - 品牌墙：Schneider 等 7 个品牌名
   - 联系区：FACTS.md 的地址/电话/邮箱
4. **SEO/GEO 友好**（框架级）：
   - 每页一个 h1、语义化 HTML、canonical 显式指向 www 主机
   - metadata 三层：根 template + 页面标题不带品牌后缀（layout 自动追加）+ og:url 显式
   - JSON-LD：Organization 统一 @id，必填字段齐全
   - sitemap.xml 与 robots.txt 预留（真实域名 www.chuangyuancorp.com）
   - 图片 alt 两层：装饰图 alt=""、内容图有描述性 alt
   - 内链全部相对路径
5. **美式英语**、中英内容一致。

## 图片使用

- 只用 `source/images/` 下 8 张图，来源见 `source/IMAGES.md`。
- `brand-arkp.png` / `brand-bgib.png` / `brand-lfhn.png` 上有中文产品标注——英文站用它们时要加英文说明或处理，不能声称是原生英文图。
- `logo-nubb.png` 是白字 logo，必须放深色底。
- 不要给无图的 6 个品牌配图。

## 完成标准（done when）

- `/en/` 与 `/zh/` 两种语言首页 + 至少：关于我们、产品/品牌、联系我们 三个内页，各自双语。
- 全站无任何 jingsourcing 业务/数字、无编造事实、无英式拼写、无假摄影署名。
- `app/` 下代码可本地构建（`npm run build` 或等价），无 TS 错误。
- 不做任何发布动作。
