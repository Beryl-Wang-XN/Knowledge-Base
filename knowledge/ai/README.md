# AI 知识库

给 MaaS TokenHub 用的技术侧知识库。条目按 `framework.md` 的 A–G 模块组织。每日学习和情报回顾走 skill `ai-kb-daily`，不走仓库里的通用 RSS 更新脚本。

## 目录

- `entries/`：知识条目，按 `A-model` 到 `F-landscape` 分目录。
- `registry/`：模型档案和横向对比表。G 模块在这里，不在 `entries/`。
- `daily/`：每日学习页。`_sample.md` 只是版式样例，正式学习写成 `YYYY-MM-DD.md`。
- `inbox/`：还没归进条目的情报和追问。
- `publish/`：小红书文案和播客口播稿、音频。
- `_templates/`：条目、每日页、inbox 的模板。
- `framework.md`：模块地图。`sources.md`：来源分级。`learning-plan.md`：学习计划。`progress.md`：打卡。
- `kb.config.yaml`：本库配置。播客音色和每天 08:00 的说明在这里。
- `site/`：`python3 scripts/build_site.py ai` 生成的静态站，不手改。

## 使用

在仓库根目录执行：

```bash
python3 scripts/build_site.py ai
python3 scripts/synthesize_podcast.py knowledge/ai/publish/podcast/某日.md
python3 scripts/validate.py ai
```

`python scripts/update_kb.py ai` 是全仓库共用的更新入口。它只抓本库 `kb.config.yaml` 里启用的来源。当前没有启用的来源，所以它不会写出 A–G 条目、每日页或 inbox。每天 08:00 的定时任务单独把情报写入 `inbox/`。
