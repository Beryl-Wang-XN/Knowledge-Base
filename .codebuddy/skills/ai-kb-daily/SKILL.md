---
name: ai-kb-daily
description: "Drives the daily co-building of the user's AI knowledge base at knowledge/ai/ (a MaaS TokenHub PM learning system). This skill should be used when the user says things like 开始今天的学习, 今天学什么, 拉一下最新AI资讯, 更新知识库, 做今天的学习材料/小红书/播客, or when running the one-time full backfill of module tabs. It orchestrates reporting last progress, pulling the last 24h of industry updates online, advancing one 20-30 min learning unit, writing entries and model registry, generating the static HTML site with quiz plus Xiaohongshu draft and podcast script, and updating the check-in log."
---

# AI 知识库每日共建 (ai-kb-daily)

## 目的

驱动用户（MaaS TokenHub 产品经理）的 AI 知识库 `knowledge/ai/` 的**每日共建**与**首次全量填充**。
把「联网拉取最新信息 → 学习一个知识点 → 沉淀入库 → 生成多端呈现物 → 打卡」这一整套动作固化为可复用流程，
使「会话主动触发」与「未来的定时自动化」复用同一套规范。

## 何时使用

当用户表达以下意图时使用：
- 每日学习触发：「开始今天的学习」「今天学什么」「继续」。
- 情报拉取：「拉一下最新 AI 资讯」「更新知识库」。
- 呈现物生成：「做今天的学习材料 / 小红书 / 播客 / quiz」。
- 一次性首建：「全量填充模块 tab 页」「backfill」。

## 关键背景（必读）

- 知识库根目录：`knowledge/ai/`。骨架文档：`framework.md`（A–G 框架）、`sources.md`（分级来源）、
  `learning-plan.md`（四阶段计划+每日机制）、`progress.md`（打卡表）。
- 用户画像与深度锚点见 `framework.md`：不做算法工程师，目标是「理解技术选择背后的成本与商业含义」的 PM 深度。
- 用户节奏：**每天 20-30 分钟**；偶尔会跳过某天；**每次必须确认当天是否学习并如实打卡**。

## 能力边界（必须对用户诚实声明，不得假装能做）

1. **无后台自动运行**：仅在对话时可联网。默认采用「方式一·会话触发」——用户主动发起才执行。
2. **无法生成音频**：播客只能产出**文字口播稿**（`.md`），需用户用第三方 TTS 转语音。
3. **无法自动发布**：小红书只能产出**文案 + AI 生成配图**，由用户手动复制发布。
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
- **daily（每日增量，常态）**：执行下方「每日流程」，推进一个学习单元 + 拉当日情报 + 生成呈现物。

## 每日流程（daily 模式，按顺序执行）

1. **报告进度**：读 `knowledge/ai/progress.md`，向用户报告上次学到哪、当前阶段/模块。
2. **确认状态**：询问用户今天是「学习」还是「跳过」。若跳过 → 只在打卡表记一笔，结束。
3. **副轨·情报（5-10 min）**：联网拉取过去 24h AI 行业更新（依 `sources.md` 的一手源优先）。
   每条尝试**挂回框架某模块**（降价→E/G，新模型→G 建档，技术突破→B/C…）；挂不上的存入 `inbox/`。
   与用户业务强相关（对标友商/供应商动态）**特别标记**。
4. **主轨·学习（15-20 min）**：按 `learning-plan.md` 当前阶段推进**一个知识点**（控制在 20 分钟内）。
   用一手源（英文原版优先）→ 翻译提炼 → 按 `_templates/entry.md` 写入对应 `entries/<模块>/`。
   条目必须含「对我的意义 ★」；模型相关顺手更新 `registry/`（按 `_schema.md`）。
5. **生成呈现物**（daily，明天起与用户共建后启用）：详见 `references/presentation.md`。
   - 每日 HTML 学习页（可累计、可翻历史）+ quiz；刷新受影响的模块 Tab 页。
   - 小红书文案（含 AI 生成配图）→ 待用户手动发布。
   - 播客口播稿（`.md`）→ 待用户 TTS 转音频。
6. **收尾打卡**：更新 `progress.md`（日期/是否学习/主轨学了什么/副轨情报要点）。如实记录，不虚记。

## 数据写入规范

- 普通条目：模板 `knowledge/ai/_templates/entry.md`，存入 `entries/<A-model|B-inference|C-compute|D-serving|E-economics|F-landscape>/`。
- 模型档案：规范 `knowledge/ai/registry/_schema.md`，一模型一文件存 `registry/models/<name>.md`，并更新 `registry/index.md` 对比总表。
- 情报暂存：未归类更新存 `knowledge/ai/inbox/`。
- 所有来源须可追溯（front matter 的 `sources` 字段，对应 `sources.md` 分级）。

## 呈现层与站点构建

静态站点结构、构建脚本约定、小红书与播客的产出格式，详见 `references/presentation.md`。
站点为纯静态（HTML+CSS+少量 JS），数据源唯一（`knowledge/ai/*.md`），一次写作多端产出。

## 迭代

每次实跑后如发现流程卡点，更新本 SKILL.md 或 `references/` 下文档，并在 `framework.md`/`learning-plan.md` 记录机制变更。
