"""标准知识更新流程。

把 core 中的组件编排为完整的更新机制，两个知识库复用同一套流程：

    fetch(来源) -> parse(规整) -> write(写入条目) -> index(建索引)

领域差异全部来自传入的 KnowledgeBase 配置。
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from shared.core import fetcher, indexer, parser
from shared.core.models import Entry, KnowledgeBase


def run_update(kb: KnowledgeBase, *, dry_run: bool = False) -> dict:
    """执行一次完整更新，返回统计信息。

    Args:
        kb: 目标知识库配置。
        dry_run: 为 True 时只抓取与解析，不落盘。
    """
    raw = fetcher.fetch_all(kb)
    entries = parser.parse_all(raw, kb)

    written = 0
    if not dry_run:
        for entry in entries:
            _write_entry(kb, entry)
            written += 1
        indexer.write_index(kb)

    return {
        "kb": kb.name,
        "fetched": len(raw),
        "parsed": len(entries),
        "written": written,
        "dry_run": dry_run,
    }


def _write_entry(kb: KnowledgeBase, entry: Entry) -> Path:
    """把一条 Entry 写为 entries/<category>/<slug>.md。"""
    category_dir = kb.entries_dir / (entry.category or "uncategorized")
    category_dir.mkdir(parents=True, exist_ok=True)
    path = category_dir / f"{_slugify(entry.title)}.md"

    front_matter = (
        "---\n"
        f"title: {entry.title}\n"
        f"category: {entry.category}\n"
        f"tags: [{', '.join(entry.tags)}]\n"
        f"source: {entry.source}\n"
        f"url: {entry.url}\n"
        f"updated_at: {datetime.now(timezone.utc).isoformat()}\n"
        "---\n\n"
    )
    with path.open("w", encoding="utf-8") as f:
        f.write(front_matter + entry.body + "\n")
    return path


def _slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text)
    return text.strip("-") or "untitled"
