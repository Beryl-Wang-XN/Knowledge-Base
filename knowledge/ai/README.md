# AI 知识库

AI 相关知识条目。内容独立于其他知识库，更新与索引由仓库根目录的共享工具（`shared/`）驱动。

## 目录说明

- `entries/`：知识条目（Markdown），按主题子目录组织。
- `sources/`：原始素材与来源资料（抓取或手动导入）。
- `index/`：由工具生成的索引与元数据（一般不手工编辑）。
- `kb.config.yaml`：本知识库的配置（更新源、分类、调度等）。

## 使用

在仓库根目录执行：

```bash
python scripts/update_kb.py ai       # 按配置更新本库
python scripts/validate.py ai        # 校验本库内容与结构
```
