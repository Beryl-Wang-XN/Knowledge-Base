"""解析与规整。

把 fetcher 返回的原始记录（dict）清洗为统一的 Entry 结构。
两个知识库共用同一套解析逻辑，领域差异通过分类映射等配置表达。
"""

from __future__ import annotations

from .models import Entry, KnowledgeBase


def parse_record(record: dict, kb: KnowledgeBase) -> Entry:
    """把单条原始记录转换为标准 Entry。"""
    category = record.get("category", "")
    if kb.categories and category not in kb.categories:
        category = kb.categories[0]  # 落入默认分类

    return Entry(
        title=record.get("title", "未命名"),
        category=category,
        body=record.get("body", ""),
        tags=record.get("tags", []),
        source=record.get("source", ""),
        url=record.get("url", ""),
    )


def parse_all(records: list[dict], kb: KnowledgeBase) -> list[Entry]:
    """批量解析。"""
    return [parse_record(r, kb) for r in records]
