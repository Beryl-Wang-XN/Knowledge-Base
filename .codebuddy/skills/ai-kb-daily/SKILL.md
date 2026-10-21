---
name: ai-kb-daily
description: "Drives the daily co-building of the user's AI knowledge base at knowledge/ai/ (a MaaS TokenHub PM learning system). This skill should be used when the user says things like 开始今天的学习, 今天学什么, 拉一下最新AI资讯, 更新知识库, 做今天的学习材料/小红书/播客, 回顾 inbox, 这页没看懂, or when running the one-time full backfill of module tabs. It orchestrates reporting last progress, pulling the last 24h of industry updates online, advancing one 20-30 min learning unit, writing entries and model registry, generating the static HTML site with quiz plus Xiaohongshu draft and podcast script, answering follow-up questions on the daily page, reviewing the inbox, and updating the check-in log."
---

# AI 知识库每日共建 (ai-kb-daily)

## 目的

驱动用户（MaaS TokenHub 产品经理）的 AI 知识库 `knowledge/ai/` 的**每日共建**与**首次全量填充**。
把「联网拉取最新信息 → 学习一个知识点 → 沉淀入库 → 生成多端呈现物 → 打卡」这一整套动作固化为可复用流程。
会话里说「开始今天的学习」跑完整流程。每天 8:00 的定时任务只把过去 24 小时的情报放进 `inbox/`。学习从回顾这个队列开始：用户点名今天要学的回顾项，再加上计划里的下一课，一起核实后生成每日页、小红书草稿和播客。

## 何时使用

当用户表达以下意图时使用：
- 每日学习触发：「开始今天的学习」「今天学什么」「继续」。
- 情报拉取：「拉一下最新 AI 资讯」「更新知识库」。
- 呈现物生成：「做今天的学习材料 / 小红书 / 播客 / quiz」。
- 看完每日页后的追问：「这页没看懂」「再讲一下」「为什么」。
- inbox 回顾：「回顾 inbox」。
- 一次性首建：「全量填充模块 tab 页」「backfill」。

## 关键背景（必读）

- 知识库根目录：`knowledge/ai/`。骨架文档：`framework.md`（A–G 框架）、`sources.md`（分级来源）、
  `learning-plan.md`（四阶段计划+每日机制）、`progress.md`（打卡表）。
- 用户画像与深度锚点见 `framework.md`：不做算法工程师，目标是「理解技术选择背后的成本与商业含义」的 PM 深度。
- 用户节奏：**每天 20-30 分钟**；偶尔会跳过某天；**每次必须确认当天是否学习并如实打卡**。

## 能力边界（必须对用户诚实声明，不得假装能做）

1. **会话内不自己定时**：在对话里只有用户发起才跑完整学习。情报拉取另有一条已启用的定时任务，每天 8:00 只写入 `inbox/`。
2. **播客不自动出声、不代发小宇宙**：口播稿写入 `publish/podcast/` 后，用 `scripts/synthesize_podcast.py` 按 `kb.config.yaml` 的晓晓音色合成同名 m4a，构建进每日页播放器，由用户点播放。再把同一条音频预填进小宇宙主播后台草稿，不点发布。账号未完成主体认证时停下来，让用户自己认证，不代填证件。步骤见 `references/presentation.md`。
3. **不代点发布**：小红书文案写入 `publish/xhs/` 后，在用户已登录的 Chrome 创作服务平台预填草稿。可见范围设为**仅自己可见**，只点「暂存离开」。草稿在该浏览器本地，不进 App。用户自己打开这篇草稿再发布。步骤见 `references/presentation.md`。
4. **无法看视频/听音频**：视频/课程源优先抓取配套文字（讲义/字幕/博客/GitHub）；
   优质但无文字载体的，直接返回链接让用户自学。
5. **信息鲜度 + 一手核实**：所有入库事实（规格/价格/榜单分数/原理数字）必须用 **web_fetch 打开一手源核实**，`null` 或"待核实"表示未证实，**绝不凭记忆瞎填**。注意：`code-explorer` subagent 无联网能力，核实须在主线程用 web_fetch。
6. **条目 vs 推送的粒度（关键，勿搞反）**：
   - **知识库条目（entries/、registry/）= 完整、丰富、详尽**，是系统查阅的参考资料，按 `_templates/entry.md` 的完整结构写深写透。
   - **每日推送（HTML每日页/小红书/播客）= 精简**，从条目中提炼一小份供 20-30 分钟消化。
   - 即：条目求全，推送求精。

## 两种运行模式

- **backfill（全量首建，仅一次）**：全网跑一遍，按当天可核实的最新信息，为 A–F 每模块填基础骨架条目、
  为 `registry/models/` 建主流模型档案，然后搭好模块 Tab 页。**广度优先，结构先立起来**，不求极致。
- **daily（每日增量，常态）**：从 inbox 回顾开场，把用户点名的回顾项和计划里的下一课一起核实，再生成呈现物。

## 每日流程（daily 模式，按顺序执行）

1. **报告进度**：读 `knowledge/ai/progress.md`，向用户报告上次学到哪、当前阶段/模块。列出 `inbox/` 里待回顾的标题（`status` 为 `open`，或 `later` 且 `review_after` 已到；忽略 `README.md` 和已写入学习计划的 `promote`）。队列为空就直接说今天没有新的回顾项。同时说出计划里的下一课：`learning-plan.md`「从回顾排入的课」的第一条；没有则按四阶段里还没学过的下一单元。
2. **确认状态**：先问今天是「学习」还是「跳过」。若跳过 → 只在打卡表记一笔，结束。若学习，请用户从待回顾列表里点名今天要一起学的条目，可以一条、多条或一条都不点。没点名的每条等用户给一个处置，当天不展开：
   - **不管了**：`status: dropped`，处置记录里写原因。
   - **写到学习计划里**：把标题和一句话追加到 `learning-plan.md` 的「从回顾排入的课」，`status: promote`。之后不再出现在每日待回顾列表，轮到它时作为计划里的下一课。
   - **留在回顾里下次处理**：保持 `status: open`。用户指定了日期才改 `later` 并填写 `review_after`。
3. **联网整理今天这一课**：不再另拉一轮 24 小时情报进 inbox。8:00 的任务已经放过。本步只为一件事检索一手源：计划里的下一课，加上用户点名的回顾项。用户明确说「再拉一次」，或确认 8:00 任务没有写入时，才补拉，新条目先放进待回顾，不自动并进今天。
4. **写入**：下一课按 `_templates/entry.md` 写入对应 `entries/<模块>/`，必须含「对我的意义 ★」。点名的回顾项核实后写入它挂靠的条目或模型档案，`status: merged`，`entry` 填路径。模型相关顺手更新 `registry/`。某一条点名项核实后发现撑不起今天这一页，停下来改问：改写入学习计划，还是留到下次。不把它写成第二课。
5. **生成呈现物**：详见 `references/presentation.md`。
   - 写 `knowledge/ai/daily/YYYY-MM-DD.md`（模板 `_templates/daily.md`）：计划下一课的学习卡片、当天点名的回顾、3–5 题 quiz。运行 `python3 scripts/build_site.py ai`，生成 `site/daily/YYYY-MM-DD.html`（含可作答 quiz），并刷新首页归档和受影响的模块 Tab 页。
   - 小红书：文案与配图写入 `publish/xhs/YYYY-MM-DD.md`（图片同目录）后，按 `references/presentation.md` 预填进创作服务平台草稿。可见范围为仅自己可见，暂存离开，不点发布。
   - 播客：口播稿写入 `publish/podcast/YYYY-MM-DD.md` 后，运行 `python3 scripts/synthesize_podcast.py` 合成同名 m4a，再构建进每日页播放器。小宇宙按 `references/presentation.md` 预填草稿；未认证或节目标题超过 20 字时停下来问用户，不点发布。
   - `kind: sample` 只验证版式，不写入 `progress.md`。
6. **收尾打卡**：更新 `progress.md`（日期 / 是否学习 / 主轨写计划下一课 / 副轨写当天点名的回顾标题）。如实记录，不虚记。把每日页地址给用户，并停下来等追问。不要把会话收成已经结束。
7. **追问（看完每日页之后，同一次对话）**：用户可以接着问。先回答，再决定要不要落盘。
   - **这页或这条目没讲清**：先按当天条目回答。条目不够，就打开一手源核实，把补充写回该条目。若补充改变了当天卡片的结论，同步改 `daily/当天.md` 并重建站点，在 `progress.md` 当天那一行补一句。这种追问不进 inbox。
   - **值得以后单独一课**：按 `_templates/inbox.md` 记一条，`from: followup`，并写入「从回顾排入的课」，`status: promote`。当天不展开成第二课。
   - **暂时挂不上框架**：同样记一条，`status: open`。

## 回顾怎么并进当天

每天的学习都从回顾开始，不另开一场只回顾、不写每日页的流程。用户说「回顾 inbox」时，走同一套：先列出待回顾，等用户点名和处置，再和计划里的下一课一起做成当天的每日页、小红书草稿和播客。

点名项和下一课都写进 `progress.md` 当天那一行。没点名的只记处置（不管了 / 已写入学习计划 / 留到下次），不写成学过的知识点。队列不用清空。

## 数据写入规范

- 普通条目：模板 `knowledge/ai/_templates/entry.md`，存入 `entries/<A-model|B-inference|C-compute|D-serving|E-economics|F-landscape>/`。
- 模型档案：规范 `knowledge/ai/registry/_schema.md`，一模型一文件存 `registry/models/<name>.md`，并更新 `registry/index.md` 对比总表。
- 情报暂存：未归类更新或「以后再学」的追问，按 `_templates/inbox.md` 存 `knowledge/ai/inbox/`。目录说明见 `inbox/README.md`。
- 所有来源须可追溯（front matter 的 `sources` 字段，对应 `sources.md` 分级）。

## 呈现层与站点构建

静态站点结构、构建脚本约定、小红书与播客的产出格式，详见 `references/presentation.md`。
站点为纯静态（HTML+CSS+少量 JS），数据源唯一（`knowledge/ai/*.md`），一次写作多端产出。

## 迭代

每次实跑后如发现流程卡点，更新本 SKILL.md 或 `references/` 下文档，并在 `framework.md`/`learning-plan.md` 记录机制变更。
