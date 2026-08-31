"""统一的数据模型。

用 dataclass 表达知识库配置、来源与条目，保证两个知识库共用同一套结构，
从而让 fetcher / parser / indexer 等组件与具体领域无关。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class Source:
    """一个更新来源。"""

    name: str
    type: str                      # 抓取器类型，如 rss / api / file
    url: str = ""
    enabled: bool = True
    options: dict = field(default_factory=dict)


@dataclass
class KnowledgeBase:
    """一个知识库的配置与路径信息。"""

    name: str                      # ai / finance ...
    title: str
    root: Path                     # knowledge/<name> 目录
    description: str = ""
    categories: list[str] = field(default_factory=list)
    sources: list[Source] = field(default_factory=list)
    schedule: dict = field(default_factory=dict)
    index: dict = field(default_factory=dict)

    @property
    def entries_dir(self) -> Path:
        return self.root / "entries"

    @property
    def sources_dir(self) -> Path:
        return self.root / "sources"

    @property
    def index_dir(self) -> Path:
        return self.root / "index"


@dataclass
class Entry:
    """一条标准化后的知识条目。"""

    title: str
    category: str
    body: str = ""
    tags: list[str] = field(default_factory=list)
    source: str = ""               # 来源名称
    url: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
