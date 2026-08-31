#!/usr/bin/env python3
"""更新指定知识库的命令行入口。

用法：
    python scripts/update_kb.py ai            # 更新 AI 库
    python scripts/update_kb.py finance       # 更新金融库
    python scripts/update_kb.py --all         # 更新全部
    python scripts/update_kb.py ai --dry-run  # 只跑流程不落盘
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# 保证可从仓库根目录导入 shared 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.core.config import list_kbs, load_kb  # noqa: E402
from shared.pipelines.update import run_update  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="更新知识库")
    ap.add_argument("name", nargs="?", help="知识库名称，如 ai / finance")
    ap.add_argument("--all", action="store_true", help="更新全部知识库")
    ap.add_argument("--dry-run", action="store_true", help="只跑流程不落盘")
    args = ap.parse_args()

    if args.all:
        targets = list_kbs()
    elif args.name:
        targets = [args.name]
    else:
        ap.error("请提供知识库名称，或使用 --all")

    for name in targets:
        kb = load_kb(name)
        stats = run_update(kb, dry_run=args.dry_run)
        print(f"[{name}] {stats}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
