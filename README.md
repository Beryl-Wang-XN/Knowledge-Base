# Knowledge-Base

个人知识库仓库（monorepo）。包含多个内容彼此独立的领域知识库，共享同一套构建方法、更新机制与工具。

## 目录结构

```
Knowledge-Base/
├── knowledge/                  # 内容区（各领域知识库内容彼此独立）
│   ├── ai/                     # AI 知识库（已构建）
│   │   ├── framework.md        #   认知框架（A–G 骨架地图）
│   │   ├── sources.md          #   分级来源地图
│   │   ├── learning-plan.md    #   学习计划 + 每日双轨机制
│   │   ├── progress.md         #   学习打卡表
│   │   ├── entries/<模块>/     #   知识条目（按框架模块分目录）
│   │   ├── registry/           #   模型档案库（核心结构化实体）
│   │   ├── inbox/              #   情报暂存区
│   │   ├── _templates/         #   本库模板
│   │   └── kb.config.yaml      #   本库配置
│   └── finance/                # 金融知识库（待构建，用 kb-builder 开始）
├── shared/                     # 复用层：核心工具 + 更新机制 + 模板
│   ├── core/                   #   models / config / fetcher / parser / indexer
│   ├── pipelines/              #   update：标准更新流程
│   └── templates/              #   默认条目模板
├── scripts/                    # 命令行入口（update_kb.py / validate.py）
├── config/                     # 全局配置（global.yaml）
├── .codebuddy/skills/          # 项目级 skills
│   ├── kb-builder/             #   知识库构建方法论（复用于任意新领域）
│   └── ai-kb-daily/            #   AI 库每日共建流程
└── requirements.txt
```

## 设计理念

- **内容隔离**：`knowledge/<domain>/` 每个子目录是一个独立知识库，内容互不干扰。
- **工具复用**：更新机制与工具沉淀在 `shared/`，与领域无关；各库差异由自身 `kb.config.yaml` 与 `framework.md` 表达。
- **方法复用**：`kb-builder` skill 固化了从零建库的六步方法论，可复用于任意新领域。
- **标准结构**：所有领域库遵循统一目录结构（见 `.codebuddy/skills/kb-builder/references/kb-structure.md`），以 `knowledge/ai/` 为样板。

## Skills

- **kb-builder**：构建新领域知识库。对我说「用 kb-builder 构建金融知识库」即可启动六步引导，并自动生成该领域的每日 skill。
- **ai-kb-daily**：AI 库每日共建。对我说「开始今天的学习」即可推进学习 + 拉取当日情报 + 生成呈现物 + 打卡。

## 快速开始

```bash
pip install -r requirements.txt

python scripts/update_kb.py --all       # 更新全部库
python scripts/validate.py --all        # 校验全部库
```

## 分支命名规范

所有修改通过功能分支 + MR 合入 `main`，禁止直接推送 `main`。

分支命名格式：`<type>/<scope>-<description>`

- **type**：`feature`（新功能）、`fix`（修复）、`docs`（文档）、`refactor`（重构）、`chore`（工具/构建）
- **scope**：模块域
- **description**：短横线连接的英文描述
