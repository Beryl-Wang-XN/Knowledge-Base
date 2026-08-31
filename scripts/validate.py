#!/usr/bin/env python3
"""校验知识库内容与结构。

检查：
    - kb.config.yaml 能否正常加载
    - 每条 entry 的分类是否在配置声明的 categories 内

用法：
    python scripts/validate.py ai
    python scripts/validate.py --all
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.core.config import list_kbs, load_kb  # noqa: E402


def validate_kb(name: str) -> list[str]:
    """返回问题列表，空列表表示通过。"""
    problems: list[str] = []
    kb = load_kb(name)

    valid = set(kb.categories)
    if kb.entries_dir.exists():
        for md in kb.entries_dir.rglob("*.md"):
            rel = md.relative_to(kb.entries_dir)
            category = rel.parts[0] if len(rel.parts) > 1 else ""
            if valid and category and category not in valid:
                problems.append(f"{rel}: 未知分类 '{category}'")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="校验知识库")
    ap.add_argument("name", nargs="?", help="知识库名称")
    ap.add_argument("--all", action="store_true", help="校验全部")
    args = ap.parse_args()

    targets = list_kbs() if args.all else ([args.name] if args.name else [])
    if not targets:
        ap.error("请提供知识库名称，或使用 --all")

    failed = False
    for name in targets:
        problems = validate_kb(name)
        if problems:
            failed = True
            print(f"[{name}] 发现 {len(problems)} 个问题：")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"[{name}] 校验通过")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
