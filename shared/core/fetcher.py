"""数据抓取器。

按来源的 `type` 分派到不同抓取实现，返回原始素材（raw records）。
这里提供分派框架与占位实现，具体网络抓取按需补充。

安全提示（SSRF）：任何基于配置 URL 的网络请求，都应在真正实现网络访问前
校验目标地址，拒绝访问内网/元数据地址（如 10.*、172.16-31.*、192.168.*、
127.*、169.254.*）。如确需访问内部域名，请显式在配置中开启白名单。
"""

from __future__ import annotations

from .models import KnowledgeBase, Source

# 已注册的抓取器：type -> callable(source) -> list[dict]
_FETCHERS: dict[str, callable] = {}


def register(source_type: str):
    """注册一个抓取器实现的装饰器。"""

    def deco(fn):
        _FETCHERS[source_type] = fn
        return fn

    return deco


def fetch_source(source: Source) -> list[dict]:
    """抓取单个来源，返回原始记录列表。"""
    if not source.enabled:
        return []
    fetcher = _FETCHERS.get(source.type)
    if fetcher is None:
        raise NotImplementedError(f"未注册的来源类型：{source.type}")
    return fetcher(source)


def fetch_all(kb: KnowledgeBase) -> list[dict]:
    """抓取一个知识库配置中所有启用的来源。"""
    records: list[dict] = []
    for source in kb.sources:
        records.extend(fetch_source(source))
    return records


# --- 占位实现：按需替换为真实逻辑 ---

@register("rss")
def _fetch_rss(source: Source) -> list[dict]:  # pragma: no cover - 骨架占位
    raise NotImplementedError(
        "RSS 抓取尚未实现。实现时请先做 SSRF 校验再发起请求。"
    )


@register("file")
def _fetch_file(source: Source) -> list[dict]:  # pragma: no cover - 骨架占位
    raise NotImplementedError("本地文件导入尚未实现。")
