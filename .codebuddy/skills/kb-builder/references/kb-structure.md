# 知识库标准结构 (kb-structure)

> 被 kb-builder 的 SKILL.md 引用。定义所有领域知识库遵循的统一目录结构与骨架文件模板。
> 参考实现样板：`knowledge/ai/`。

## 目录结构

```
knowledge/<domain>/
├── kb.config.yaml      # 配置：name / title / categories / sources / schedule
├── README.md           # 本库简介与使用方式
├── framework.md        # 认知框架（骨架地图，所有条目挂靠于此）
├── sources.md          # 分级来源地图 + 信息处理原则
├── learning-plan.md    # 学习计划（分阶段）+ 每日双轨机制 + 打卡原则
├── progress.md         # 学习打卡表
├── entries/            # 知识条目，按框架模块分子目录
│   └── <模块代号>/      #   如 A-xxx / B-xxx（与 framework 模块一致）
├── registry/           # 核心结构化实体库（若该领域有可对比核心实体）
│   ├── _schema.md      #   实体字段规范（分维度组，null=待核实）
│   ├── <实体>/          #   一实体一文件
│   └── index.md        #   横向对比总表
├── inbox/              # 情报暂存区（未归类的每日更新）
├── _templates/         # 本库模板（entry.md 等）
├── site/               # 静态站点构建产物（HTML，gitignore，勿手改）
└── publish/            # 呈现物产出
    ├── xhs/            #   小红书文案 + AI 配图
    └── podcast/        #   播客口播稿
```

## 命名约定

- `<domain>`：小写英文，如 `ai` / `finance` / `legal`。
- 模块子目录：`<代号>-<英文名>`，代号与 framework 模块表一致（如 `A-model`）。
- 每日页/呈现物：`YYYY-MM-DD.<ext>`。

## 骨架文件模板要点

### kb.config.yaml
含 `name` / `title` / `description` / `categories`（对应 framework 模块）/ `sources`（更新源，默认 `enabled: false`）/ `schedule`（cron，供未来自动化参考）。

### framework.md
段落顺序：定位与深度锚点 → 脊柱主线 → 模块表（模块/名称/主题/优先级）→ 各模块深度标准 → 核心实体设计 → 版本记录。

### sources.md
段落顺序：信息处理原则（一手优先/鲜度/二手仅补充/多媒体处理/内部源）→ 分级图例（🥇🥈🛠）→ 按模块来源表 → 重点组合建议 → 待补充内部源 → 版本记录。

### learning-plan.md
段落顺序：分阶段计划表 → 每日双轨机制（🅰主轨/🅱副轨 + 联动规则 + 每日流程）→ 更新拉取能力边界（会话触发/定时自动化）→ 打卡确认原则 → 固化为 skill 的待办。

### progress.md
含「当前进度」（所处阶段/当前模块/下一步）+「打卡记录」表（日期/状态✅⏭️🔜/主轨学了什么/副轨情报要点）。

### _templates/entry.md
front matter：title / module / tags / level / sources[name,url,tier] / created / updated / status。
正文：一句话总结 / 关键点 / **对我的意义★** / 原文与参考（含英文术语对照）。

### registry/_schema.md
按维度组组织字段（AI 例：身份/技术规格/能力评估/商业属性/运营属性）。
数值默认 `null`（待联网核实）。正文含：概述 / **选型建议★** / 变更记录表。

## 与 shared/ 工具层的关系

- `shared/` 提供跨库通用工具（配置加载、索引、更新流程编排）与默认模板。
- 各库差异由自身 `kb.config.yaml` 与 `framework.md` 表达，工具与领域无关。
- 呈现层构建脚本建议复用 `shared/`，读取 `knowledge/<domain>/**/*.md` 渲染为 `site/`。
