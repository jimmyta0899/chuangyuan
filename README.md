# 创远 Chuang Yuan — 项目卡

> 切换项目/开新会话前必读 `E:\projects\_SWITCH-PROTOCOL.md`，并用 `python E:\projects\whereami.py` 核对当前身份。
> 建卡：2026-11-23。项目 ID = GitHub 仓库名 = Pages 项目名 = 本地目录名。

## 1. 身份

- 项目 ID：`chuangyuan`
- 一句话定位：把现有中文站 www.chuangyuancorp.com（广州创远机电设备有限公司）重做成**中英双语 B2B 站**，面向海外买家，参照 jingsourcing 的信息架构与体验，但**业务与事实全部用创远真实信息**。
- 本地根：`E:\projects\chuangyuan`（git 根即此目录；craft anything 产出后实测回填 app 还是根目录）
- GitHub：`https://github.com/jimmyta0899/chuangyuan`（**未创建**，等用户明说再建仓/发布）
- 线上：`https://www.chuangyuancorp.com/`（现有 websiteonline.cn 自助站，将来迁到 GitHub Pages；**未迁移**）

## 2. 技术栈与部署（规划，待 craft anything 产出后实测回填）

- 框架：由 craft anything 依 jingsourcing 参照重建，具体栈待产出后核对（优先静态可导出）
- 构建命令：待定
- 输出目录：待定
- 部署平台：**GitHub Pages（用户 2026-11-23 拍板）**，两步：push main → 推产物到 gh-pages
- 是否有后端：无（静态 B2B 站，联系表单走 mailto 或占位，不接真后端）

## 3. 当前状态

- 最近一次发版：无（未创建仓库、未部署）
- 已上线内容：无（现有 websiteonline.cn 站不在本项目管理范围，仅作素材来源与迁移对象）
- 未完成遗留项：
  1. 待 craft anything 产出双语站并复核；
  2. GA4/GSC/GTM 真实 ID 未提供，仅搭框架+占位符；
  3. GSC 域名验证需域名控制权，未做；
  4. 图片为现有站自有素材，需逐张登记来源 URL；
  5. websiteonline.cn → GitHub Pages 的 DNS/301/验证迁移清单待写。
- 下次会话第一件事：跑 craft anything rebuild，拿到首版产出。

## 4. 红线（不可违反）

- **业务定位**：创远是机电设备/阀门/仪表供应商 + 品牌代理（Schneider/Emerson/Vertiv/Rosemount 等）+ 央企合格供应商；**不得套用 jingsourcing 的采购代理业务模式**（Amazon sellers / dropshipping / 6,000+ clients 等数字一律不许出现）。参照 jingsourcing 只限于**信息架构、版式、信任元素、CTA 样式**。
- **出处红线**：任何事实、数字、规格、客户名、认证必须有可核查出处；查不到就不写。不得编造。
- **图片**：只用现有 www.chuangyuancorp.com 自有素材（pending 归档登记来源）；不得写 `in-house photography` 除非确为创远自拍。craft anything 若生成新图，须明确标注为 AI 生成占位，不可冒充实拍。
- **美式英语**：所有英文输出一律美式（meter/color/center/organize/analyze/behavior/while/license/utilize 等），禁止英式拼写。
- **发布锁**：**绝不自动发布/建仓/push/改 DNS**。建仓、上线、迁移必须用户当场明说「上线」或「建仓」。
- **参照边界**：craft anything 的 publish / delete_outside / system 审批一律锁 `refuse`，只允许读网页、写项目内文件、跑常规构建。
- **品牌**：创远品牌 CHUANG YUAN / 创远机电 可正常出现在前端（与 WokMaster 的"品牌名不上前端"红线无关，勿混用）。

## 5. 记忆与资料（去哪找，不复制）

- 项目记忆：`E:\projects\chuangyuan\.workbuddy\memory\MEMORY.md`
- 工作日志：同目录 `YYYY-MM-DD.md`（只追加）
- 建站方法论总纲：`E:\data\2026-10-30-08-37-32\SITE-QA-PLAYBOOK.md`（六阶段 + 新站开工一页清单）
- 全链路纪实：`E:\data\2026-10-30-08-37-32\PROJECT-FULL-CHAIN-2026-11-23.md`（建站工程/UI/技能栈/博客产线）
- 自检与经验：`E:\data\2026-10-30-08-37-32\_qa-2026-11-23\QA-REPORT.md`（18 项读数 + 第 11 章经验总结）
- 现有站事实源：www.chuangyuancorp.com（page86 关于我们 / page87 产品中心 / page89 联系我们）

## 6. 更新记录

- 2026-11-23 17:58：建卡。用户拍板三件事：保留创远真实定位、原域名迁 GitHub Pages、分析框架只搭占位符。
