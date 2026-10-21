#!/usr/bin/env python3
"""把播客口播稿合成同名 m4a。

只朗读 `## 【…】` 分段里的正文：去掉分段标题、第一个分段之前的说明、
文末 `---` 之后的流程说明。音色读该知识库 `kb.config.yaml` 的 `publish.podcast`。

用法：
    python3 scripts/synthesize_podcast.py knowledge/ai/publish/podcast/_sample.md
    python3 scripts/synthesize_podcast.py knowledge/ai/publish/podcast/2026-10-21.md
    python3 scripts/synthesize_podcast.py <稿子路径> --print   # 只打印将要朗读的文本

依赖：python3 -m pip install --user edge-tts。合成时联网，不需要语音账号。
输出与稿子同目录、同名的 .m4a。再运行 scripts/build_site.py 才会出现在每日页。
"""

from __future__ import annotations

import argparse
import asyncio
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"


def kb_root_for(md_path: Path) -> Path:
    for parent in [md_path.parent, *md_path.parents]:
        if (parent / "kb.config.yaml").is_file() and parent.parent.name == "knowledge":
            return parent
    raise SystemExit(f"找不到这篇稿子所属的知识库：{md_path}")


def load_voice(root: Path) -> str:
    data = yaml.safe_load((root / "kb.config.yaml").read_text(encoding="utf-8")) or {}
    podcast = (data.get("publish") or {}).get("podcast") or {}
    voice = str(podcast.get("voice") or DEFAULT_VOICE).strip()
    return voice or DEFAULT_VOICE


def spoken_text(markdown: str) -> str:
    """取出应朗读的正文。没有分段标记时，朗读去掉文末流程说明后的全文。"""
    text = markdown
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    sections: list[str] = []
    current: list[str] | None = None
    for line in text.splitlines():
        if current is not None and line.strip() == "---":
            break
        if line.startswith("## 【"):
            if current is not None:
                sections.append("\n".join(current).strip())
            current = []
            continue
        if current is not None:
            current.append(line)
    if current is not None:
        sections.append("\n".join(current).strip())
    parts = [part for part in sections if part]
    if parts:
        return "\n\n".join(parts)
    body = []
    for line in text.splitlines():
        if line.strip() == "---":
            break
        if line.startswith("#"):
            continue
        body.append(line)
    return "\n".join(body).strip()


def to_m4a(mp3: Path, dest: Path) -> Path:
    """转成 m4a。转码不可用时保留 mp3，并去掉同名旧 m4a，避免每日页继续播旧音频。"""
    afconvert = shutil.which("afconvert")
    if afconvert:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "speech.m4a"
            try:
                subprocess.run(
                    [afconvert, str(mp3), str(out), "-f", "m4af", "-d", "aac"],
                    check=True,
                )
            except subprocess.CalledProcessError:
                pass
            else:
                shutil.copyfile(out, dest)
                return dest
    fallback = dest.with_suffix(".mp3")
    shutil.copyfile(mp3, fallback)
    if dest.is_file():
        dest.unlink()
    return fallback


async def synthesize(text: str, voice: str, dest: Path) -> Path:
    import edge_tts

    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        mp3 = Path(tmp) / "speech.mp3"
        await edge_tts.Communicate(text, voice).save(str(mp3))
        return to_m4a(mp3, dest)


def main() -> None:
    parser = argparse.ArgumentParser(description="把播客口播稿合成同名 m4a")
    parser.add_argument("markdown", help="口播稿路径")
    parser.add_argument("--print", dest="print_only", action="store_true", help="只打印朗读文本")
    args = parser.parse_args()

    md_path = Path(args.markdown)
    if not md_path.is_absolute():
        md_path = REPO_ROOT / md_path
    if not md_path.is_file():
        raise SystemExit(f"找不到口播稿：{md_path}")

    text = spoken_text(md_path.read_text(encoding="utf-8"))
    if not text:
        raise SystemExit(f"没有可朗读的正文：{md_path}")
    if args.print_only:
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
        return

    voice = load_voice(kb_root_for(md_path))
    dest = md_path.with_suffix(".m4a")
    try:
        written = asyncio.run(synthesize(text, voice, dest))
    except ModuleNotFoundError:
        raise SystemExit("缺少 edge-tts。先运行：python3 -m pip install --user edge-tts")
    print(f"voice={voice} chars={len(text)} -> {written}")


if __name__ == "__main__":
    main()
