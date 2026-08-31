"""配置加载与校验。

从 knowledge/<name>/kb.config.yaml 读取某个知识库的配置，
并可选地叠加 config/global.yaml 中的全局默认值。
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .models import KnowledgeBase, Source

# 仓库根目录：shared/core/config.py -> 上溯三层
REPO_ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE_DIR = REPO_ROOT / "knowledge"
GLOBAL_CONFIG = REPO_ROOT / "config" / "global.yaml"


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_global() -> dict:
    """加载全局配置（可为空）。"""
    return _read_yaml(GLOBAL_CONFIG)


def load_kb(name: str) -> KnowledgeBase:
    """按名称加载一个知识库配置。

    Args:
        name: 知识库目录名，如 "ai" 或 "finance"。

    Raises:
        FileNotFoundError: 对应知识库或其配置文件不存在。
    """
    root = KNOWLEDGE_DIR / name
    config_path = root / "kb.config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"未找到知识库配置：{config_path}")

    data = _read_yaml(config_path)
    sources = [Source(**s) for s in data.get("sources", [])]

    return KnowledgeBase(
        name=data.get("name", name),
        title=data.get("title", name),
        root=root,
        description=data.get("description", ""),
        categories=data.get("categories", []),
        sources=sources,
        schedule=data.get("schedule", {}),
        index=data.get("index", {}),
    )


def list_kbs() -> list[str]:
    """列出 knowledge/ 下所有知识库名称。"""
    if not KNOWLEDGE_DIR.exists():
        return []
    return sorted(
        p.name
        for p in KNOWLEDGE_DIR.iterdir()
        if p.is_dir() and (p / "kb.config.yaml").exists()
    )
