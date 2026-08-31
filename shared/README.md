# shared —— 复用层

所有知识库共享的工具、更新机制与模板。**不包含任何具体知识内容**，只提供能力；
各知识库通过自己的 `kb.config.yaml` 驱动这里的通用逻辑。

## 结构

- `core/`：可复用的核心组件。
  - `models.py`：数据模型（知识库配置、条目、来源等）。
  - `config.py`：加载与校验 `kb.config.yaml` / 全局配置。
  - `fetcher.py`：从来源抓取原始素材（按 `source.type` 分派）。
  - `parser.py`：清洗与规整为统一的条目结构。
  - `indexer.py`：为条目生成索引/元数据。
- `pipelines/`：知识更新机制（把 core 的组件编排成完整流程）。
  - `update.py`：`fetch -> parse -> write entries -> index` 的标准流程。
- `templates/`：统一的知识条目模板。
  - `entry.md`：新知识条目模板（含 front matter）。

## 复用方式

工具不关心是 AI 还是金融库，一切差异由传入的知识库配置决定：

```python
from shared.core.config import load_kb
from shared.pipelines.update import run_update

kb = load_kb("ai")        # 或 "finance"
run_update(kb)
```
