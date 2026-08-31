---
name: kb-builder
description: "Guides building a brand-new domain knowledge base from scratch inside this monorepo, reusing the proven methodology used to build the AI knowledge base. This skill should be used when the user wants to start a new knowledge base for any domain (e.g. 建一个金融知识库, 用 kb-builder 构建金融知识库, 我想建一个新的知识库, start a new knowledge base, build a finance/legal knowledge base). It runs a six-step conversational method (anchor goals, build cognitive framework, curate tiered sources, design learning plan and daily mechanism, design data structure and presentation, generate a per-domain daily skill), producing the knowledge base skeleton under knowledge/ following the standard structure, plus a per-domain kb-daily skill."
---

# 知识库构建方法论 (kb-builder)

## 目的

指导从零构建一个**新领域**的知识库，复用构建 AI 知识库时验证过的方法论。
产出：`knowledge/<domain>/` 下符合「知识库标准结构」的骨架 + 一个 `<domain>-kb-daily` 每日共建 skill。
本仓库为 monorepo：各领域知识库内容隔离于 `knowledge/<domain>/`，通用工具沉淀在 `shared/`。

## 何时使用

当用户想为某个领域开建知识库时，例如：
- 「建一个金融知识库」「用 kb-builder 构建金融知识库」
- 「我想建一个新的知识库」「帮我搭一个 XX 领域的学习体系」

## 核心理念（从 AI 库实践提炼，务必贯彻）

1. **服务决策，而非博学**：知识框架必须锚定用户的真实工作决策，先定「知识深度锚点」（学到多深就够）。
2. **框架优先**：先搭全局认知骨架，再按实用性排序填充，避免碎片堆积。
3. **稳态层 + 动态层**：区分慢变的体系知识与快变的最新情报；动态情报须能「挂回框架」，否则进 inbox。
4. **一手源 + 鲜度**：优先一手源（常为英文原版）翻译入库；关键事实联网核实，`null` 表待核实，绝不凭记忆瞎填。
5. **知识回流决策**：每条知识都要有「对我的意义」，强制关联实际工作。
6. **核心结构化实体**：多数领域有一类核心可对比实体（AI=模型；金融可能是公司/资产/指标），单列为结构化 registry。
7. **诚实的能力边界**：无后台自动运行、无法生成音频、无法自动发布、无法看视频/听音频——必须向用户声明。
8. **因地制宜，勿照搬**：AI 库的模块结构（A–G）、核心实体（模型档案）、呈现形态（HTML/小红书/播客）只是**一个样板**。每个新领域的知识结构与呈现方式都可能不同（如金融也许用数据表格、时间线，未必做小红书/播客）。步骤 1（框架）与步骤 4（数据结构+呈现）必须**为该领域重新设计**，只复用方法论，不复制具体形态。呈现方式在步骤 4 与用户逐项确认后再定。

## 六步引导法（对话式，逐步与用户确认）

按顺序推进，每步产出一份骨架文档并请用户确认后再进入下一步。**每步的引导问题清单与产出模板见 `references/methodology.md`**。

- **步骤 0 · 锚定目标**：明确知识服务的核心决策、深度锚点、时间优先级。产出：目标锚定段落。
- **步骤 1 · 认知框架**：搭主线脊柱 + 模块树 + 各模块深度标准。产出：`framework.md`。
- **步骤 2 · 分级来源**：为每模块找一手/二手/工具站来源并确认。产出：`sources.md`。
- **步骤 3 · 学习计划 + 每日机制**：分阶段计划 + 双轨（主轨学习/副轨情报）每日机制 + 打卡。产出：`learning-plan.md`、`progress.md`。
- **步骤 4 · 数据结构 + 呈现层**：目录组织、条目模板、核心 registry schema、静态站点/quiz/小红书/播客。产出：目录骨架 + `_templates/`。
- **步骤 5 · 生成每日 skill**：把上面固化为 `<domain>-kb-daily` skill。做法见 `references/daily-skill-template.md`。

> 引导原则：一次不问太多问题；用选择题辅助用户决策；每步先给方案草案再请确认；允许用户随时调整框架。

## 知识库标准结构

所有领域库遵循统一结构，保证仓库一致、工具可复用。**完整结构与各骨架文件模板见 `references/kb-structure.md`**。概览：

```
knowledge/<domain>/
├── kb.config.yaml      # 配置（名称/分类/来源/调度）
├── README.md
├── framework.md        # 认知框架（骨架地图）
├── sources.md          # 分级来源地图
├── learning-plan.md    # 学习计划 + 每日机制
├── progress.md         # 学习打卡表
├── entries/<模块>/     # 知识条目（按框架模块分子目录）
├── registry/           # 核心结构化实体库（_schema.md + 实体文件 + index.md）
├── inbox/              # 情报暂存区
├── _templates/         # 本库条目/档案模板
├── site/               # 静态站点构建产物（gitignore）
└── publish/            # 小红书/播客产出
```

## 生成每日 skill

六步走完后，为该领域生成 `<domain>-kb-daily` skill（参照本仓库既有 `ai-kb-daily`）。
模板、必需的每日流程与能力边界声明见 `references/daily-skill-template.md`。
用官方 `init_skill.py` 初始化，用 `package_skill.py` 校验（注意 description 不得含尖括号 `<` `>`）。

## 完成后

- 提醒用户后续可用 `<domain>-kb-daily` skill 开始该库的 backfill 与每日学习。
- 若构建中发现方法论可改进，更新本 skill 的 SKILL.md 或 `references/`。
