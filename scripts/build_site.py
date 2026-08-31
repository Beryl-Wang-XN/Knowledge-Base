#!/usr/bin/env python3
"""知识库静态站点生成器。

读取 knowledge/<domain>/ 下的 Markdown（entries/ 各模块条目、registry/ 模型档案、
framework.md 等），生成纯静态 HTML 站点到 knowledge/<domain>/site/。

用法：
    python3 scripts/build_site.py            # 默认构建 ai
    python3 scripts/build_site.py ai
    python3 scripts/build_site.py finance

特性：
- 每个条目生成独立详情页（modules/<模块>/<slug>.html），模块页为条目列表，避免长页面。
- 支持 mermaid 图表（```mermaid 代码块自动渲染）。
- 出处超链接由 Markdown 原生支持。
设计：数据源唯一（Markdown），站点为构建产物；改内容改 Markdown，重跑本脚本即可。
"""

from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path

import markdown
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

AI_MODULES = [
    {"dir": "A-model", "letter": "A", "name": "模型层", "emoji": "🧠", "prio": "中"},
    {"dir": "B-inference", "letter": "B", "name": "推理层", "emoji": "⚡", "prio": "🔴核心"},
    {"dir": "C-compute", "letter": "C", "name": "算力层", "emoji": "🖥️", "prio": "🔴核心"},
    {"dir": "D-serving", "letter": "D", "name": "调度服务层", "emoji": "🎛️", "prio": "🔴核心"},
    {"dir": "E-economics", "letter": "E", "name": "成本经济层", "emoji": "💰", "prio": "🟡锚点"},
    {"dir": "F-landscape", "letter": "F", "name": "竞品供应商格局", "emoji": "🗺️", "prio": "⚪贯穿"},
]

MD_EXT = ["extra", "tables", "fenced_code", "sane_lists", "nl2br"]

# mermaid 代码块（markdown fenced_code 输出）转 <div class="mermaid">
_MERMAID_RE = re.compile(
    r'<pre><code class="language-mermaid">(.*?)</code></pre>', re.DOTALL)


def parse_md(path: Path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            body = parts[2]
    return meta, body


def _restore_mermaid(m: re.Match) -> str:
    code = html_lib.unescape(m.group(1))
    return f'<div class="mermaid">{code}</div>'


def md2html(body: str) -> str:
    out = markdown.markdown(body, extensions=MD_EXT)
    out = _MERMAID_RE.sub(_restore_mermaid, out)
    # 站内 .md 交叉链接改写为 .html（不含 http 外链）
    out = re.sub(r'(<a href="(?!https?:)[^"]+?)\.md(#[^"]*)?"',
                 lambda m: f'{m.group(1)}.html{m.group(2) or ""}"', out)
    return out


def first_paragraph(body: str) -> str:
    """取正文第一段纯文本作为摘要。"""
    for block in body.strip().split("\n\n"):
        b = block.strip()
        if b and not b.startswith(("#", ">", "-", "|", "```", "!")):
            txt = re.sub(r"[*`\[\]()]|https?://\S+", "", b)
            return txt.strip()[:120]
    return ""


def css() -> str:
    return """
:root{--bg:#0f1420;--card:#1a2233;--card2:#212b40;--fg:#e6ecf5;--muted:#8b98b0;
--line:#2c3854;--accent:#5b9dff;--accent2:#7c6cff;--ok:#3ecf8e;--warn:#ffb454;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
background:var(--bg);color:var(--fg);line-height:1.75;font-size:15px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:10;background:rgba(15,20,32,.92);backdrop-filter:blur(8px);
border-bottom:1px solid var(--line);padding:0 20px}
nav{max-width:1080px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:4px;padding:10px 0}
nav .brand{font-weight:700;font-size:16px;margin-right:16px;color:#fff}
nav a{padding:6px 12px;border-radius:8px;color:var(--muted);font-size:14px;white-space:nowrap}
nav a:hover{background:var(--card);text-decoration:none;color:var(--fg)}
nav a.active{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff}
main{max-width:1080px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:26px;margin-bottom:6px}h2{font-size:20px;margin:24px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}
h3{font-size:16px;margin:18px 0 8px;color:var(--accent)}
.sub{color:var(--muted);margin-bottom:24px}
.crumb{color:var(--muted);font-size:13px;margin-bottom:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
.mod-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;
transition:.15s;display:block}
.mod-card:hover{border-color:var(--accent);transform:translateY(-2px);text-decoration:none}
.mod-card .em{font-size:26px}.mod-card .t{font-weight:600;color:#fff;margin:8px 0 2px;font-size:16px}
.mod-card .m{color:var(--muted);font-size:13px}
.badge{display:inline-block;font-size:12px;padding:2px 8px;border-radius:20px;background:var(--card2);
color:var(--muted);border:1px solid var(--line);margin-right:6px}
.badge.core{color:var(--accent);border-color:var(--accent)}
.badge.v{color:var(--ok);border-color:var(--ok)}
.list-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;
margin-bottom:12px;display:block;transition:.15s}
.list-card:hover{border-color:var(--accent);transform:translateY(-2px);text-decoration:none}
.list-card .t{font-weight:600;color:#fff;font-size:17px;margin-bottom:4px}
.list-card .d{color:var(--muted);font-size:14px;margin:6px 0}
.list-card .tags{font-size:12px;color:var(--muted)}
article{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:8px 28px 28px}
article h2:first-of-type{margin-top:14px}
article ul,article ol{padding-left:22px}article li{margin:5px 0}
article blockquote{border-left:3px solid var(--warn);background:var(--card2);
padding:10px 16px;margin:14px 0;border-radius:6px;color:#f0d9b5}
article code{background:#0b1020;padding:2px 6px;border-radius:5px;font-size:13px;color:#9fd}
article pre{background:#0b1020;padding:14px;border-radius:10px;overflow:auto}
article pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:13px;overflow:hidden}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left}
th{background:var(--card2);color:#fff}
.mermaid{background:#f7f9fc;border-radius:10px;padding:16px;margin:16px 0;text-align:center}
.note{background:var(--card2);border:1px solid var(--line);border-radius:10px;padding:14px 18px;color:var(--muted);font-size:14px;margin:16px 0}
footer{max-width:1080px;margin:0 auto;padding:24px 20px;color:var(--muted);font-size:13px;border-top:1px solid var(--line)}
"""


MERMAID_JS = ('<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>'
              '<script>mermaid.initialize({startOnLoad:true,theme:"default"});</script>')


def page(title: str, active: str, content: str, nav_items, need_mermaid=False) -> str:
    nav = '<span class="brand">📚 AI 知识库</span>'
    for href, label, key in nav_items:
        cls = " active" if key == active else ""
        nav += f'<a class="{cls}" href="{href}">{label}</a>'
    mm = MERMAID_JS if need_mermaid else ""
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css()}</style></head>
<body><header><nav>{nav}</nav></header><main>{content}</main>
<footer>MaaS TokenHub · AI 知识库 · 由 Markdown 数据源自动构建 · 内容以联网核实的一手源为准</footer>
{mm}</body></html>"""


def build(domain: str = "ai"):
    root = REPO_ROOT / "knowledge" / domain
    if not root.exists():
        print(f"知识库不存在：{root}")
        return
    site = root / "site"
    site.mkdir(exist_ok=True)
    (site / "modules").mkdir(exist_ok=True)

    nav = [("index.html", "首页", "home")]
    for m in AI_MODULES:
        nav.append((f"modules/{m['dir']}.html", f"{m['letter']} {m['name']}", m["dir"]))
    nav.append(("modules/registry.html", "🗃️ 模型库", "registry"))
    nav.append(("framework.html", "🧭 框架", "framework"))

    def nav_for(depth: int):
        pre = "../" * depth
        return [(pre + h, l, k) for h, l, k in nav]

    total_entries = 0

    for m in AI_MODULES:
        mdir = root / "entries" / m["dir"]
        entries = sorted(p for p in mdir.glob("*.md") if not p.stem.startswith(("_", "TODO", "."))) if mdir.exists() else []
        total_entries += len(entries)
        (site / "modules" / m["dir"]).mkdir(exist_ok=True)

        list_cards = ""
        for e in entries:
            meta, body = parse_md(e)
            title = meta.get("title", e.stem)
            tags = meta.get("tags", []) or []
            level = meta.get("level", "")
            verified = any(s.get("verified") for s in (meta.get("sources") or []) if isinstance(s, dict))
            slug = e.stem
            summary = first_paragraph(body)
            html_body = md2html(body)
            need_mm = "mermaid" in html_body

            # 详情页
            lvl_badge = f'<span class="badge core">{level}</span>' if level == "核心" else (f'<span class="badge">{level}</span>' if level else "")
            v_badge = '<span class="badge v">✓ 一手核实</span>' if verified else ""
            tagline = "　".join(f"#{t}" for t in tags)
            detail = f"""<div class="crumb"><a href="../{m['dir']}.html">← {m['letter']} {m['name']}</a></div>
<h1>{title}</h1><p class="sub">{lvl_badge}{v_badge}　{tagline}</p>
<article>{html_body}</article>"""
            (site / "modules" / m["dir"] / f"{slug}.html").write_text(
                page(f"{title} · AI 知识库", m["dir"], detail, nav_for(2), need_mm), encoding="utf-8")

            # 列表卡片
            badges = (lvl_badge + v_badge)
            list_cards += f"""<a class="list-card" href="{m['dir']}/{slug}.html">
<div class="t">{title}</div><div class="d">{summary}…</div>
<div class="tags">{badges}　{tagline}</div></a>"""

        if not entries:
            list_cards = '<div class="note">该模块暂无条目，将在每日学习中逐步填充。</div>'
        content = f"""<h1>{m['emoji']} {m['letter']} · {m['name']}</h1>
<p class="sub">优先级：{m['prio']}　·　共 {len(entries)} 条</p>{list_cards}"""
        (site / "modules" / f"{m['dir']}.html").write_text(
            page(f"{m['name']} · AI 知识库", m["dir"], content, nav_for(1)), encoding="utf-8")

    # 模型库
    reg = root / "registry"
    (site / "modules" / "registry").mkdir(exist_ok=True)
    reg_content = "<h1>🗃️ 模型档案库（Model Registry）</h1><p class=\"sub\">核心资产 · 结构化模型档案</p>"
    idx = reg / "index.md"
    if idx.exists():
        _, body = parse_md(idx)
        reg_content += md2html(body)
    models = sorted((reg / "models").glob("*.md")) if (reg / "models").exists() else []
    if models:
        reg_content += "<h2>模型档案</h2>"
        for mp in models:
            meta, body = parse_md(mp)
            name = meta.get("name", mp.stem)
            vendor = meta.get("vendor", "")
            slug = mp.stem
            detail = f"""<div class="crumb"><a href="../registry.html">← 模型档案库</a></div>
<h1>{name}</h1><p class="sub">{vendor}</p><article>{md2html(body)}</article>"""
            (site / "modules" / "registry" / f"{slug}.html").write_text(
                page(f"{name} · 模型档案", "registry", detail, nav_for(2)), encoding="utf-8")
            reg_content += f'<a class="list-card" href="registry/{slug}.html"><div class="t">{name}</div><div class="tags">{vendor}</div></a>'
    (site / "modules" / "registry.html").write_text(
        page("模型档案库 · AI 知识库", "registry", reg_content, nav_for(1)), encoding="utf-8")

    # 框架页
    fw = root / "framework.md"
    fw_content = "<h1>🧭 AI 技术侧认知框架</h1>"
    need_mm_fw = False
    if fw.exists():
        _, body = parse_md(fw)
        fw_html = md2html(body)
        need_mm_fw = "mermaid" in fw_html
        fw_content += f"<article>{fw_html}</article>"
    (site / "framework.html").write_text(
        page("认知框架 · AI 知识库", "framework", fw_content, nav_for(0), need_mm_fw), encoding="utf-8")

    # 首页
    mod_cards = ""
    for m in AI_MODULES:
        mdir = root / "entries" / m["dir"]
        n = len(list(mdir.glob("*.md"))) if mdir.exists() else 0
        mod_cards += f"""<a class="mod-card" href="modules/{m['dir']}.html">
<div class="em">{m['emoji']}</div><div class="t">{m['letter']} · {m['name']}</div>
<div class="m">{m['prio']}　·　{n} 条</div></a>"""
    n_models = len(models)
    mod_cards += f"""<a class="mod-card" href="modules/registry.html">
<div class="em">🗃️</div><div class="t">G · 模型档案库</div>
<div class="m">★核心资产　·　{n_models} 个模型</div></a>"""
    home = f"""<h1>📚 AI 知识库</h1>
<p class="sub">MaaS TokenHub 产品经理的 AI 行业学习体系 · 深度锚点：理解技术选择背后的成本与商业含义</p>
<div class="note">共 {total_entries} 条知识条目、{n_models} 个模型档案。
主线：一次推理请求的生命周期（接入→调度→Prefill/Decode→执行→返回）。
点击下方模块进入，或查看 <a href="framework.html">认知框架</a>。</div>
<h2>知识模块</h2><div class="grid">{mod_cards}</div>"""
    (site / "index.html").write_text(page("AI 知识库", "home", home, nav_for(0)), encoding="utf-8")

    print(f"✅ 站点已生成：{site}")
    print(f"   条目 {total_entries} 条，模型档案 {n_models} 个")
    print(f"   打开：{site / 'index.html'}")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "ai")
