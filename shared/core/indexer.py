"""索引生成。

扫描一个知识库的 entries/ 目录，生成 index/index.json，
供检索或站点构建使用。索引结构与领域无关，两库通用。
"""

from __future__ import annotations

import json
from pathlib import Path

from .models import KnowledgeBase


def build_index(kb: KnowledgeBase) -> dict:
    """遍历 entries/ 下的 Markdown 文件，构建索引数据。"""
    items = []
    entries_dir = kb.entries_dir
    if entries_dir.exists():
        for md in sorted(entries_dir.rglob("*.md")):
            rel = md.relative_to(kb.root)
            items.append(
                {
                    "path": str(rel),
                    "title": _extract_title(md),
                    "category": rel.parts[1] if len(rel.parts) > 2 else "",
                }
            )

    index = {"kb": kb.name, "count": len(items), "items": items}
    return index


def write_index(kb: KnowledgeBase) -> Path:
    """构建并写入 index/index.json。"""
    index = build_index(kb)
    out_dir = kb.index_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    return out_path


def _extract_title(md_path: Path) -> str:
    """从 Markdown 首个一级标题提取标题，退化为文件名。"""
    with md_path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return md_path.stem
