---
title: Gemini 4 Hydrogen 一般可用，标准价输入 $1.50、输出 $7.50
captured: 2026-11-13
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Introducing Gemini 4 Hydrogen
    url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
    tier: 一手
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
  - name: Gemini 4 Hydrogen 模型页
    url: https://ai.google.dev/gemini-api/docs/models/gemini-4-hydrogen
    tier: 一手
  - name: Gemini API 定价页 Gemini 4 Hydrogen
    url: https://ai.google.dev/gemini-api/docs/pricing#gemini-4-hydrogen
    tier: 一手
  - name: Gemini API 速率限制
    url: https://ai.google.dev/gemini-api/docs/rate-limits
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

2026-11-12，Google 博客和 Gemini API changelog 都写下了 Gemini 4 Hydrogen（`gemini-4-hydrogen`）一般可用。changelog 写它在免费层可用，付费层标价是每百万输入 token $1.50、每百万输出 token $7.50，并成为 Gemini Managed Agents 里 Antigravity agent 的默认模型。思考档是 `low`、`medium`、默认 `high`，以及新的 `xhigh`。

模型页已打开。输入是文本、图片、视频、音频和 PDF，输出是文本。统一上下文窗口 1,048,576 token。默认同步最大输出 65,536 token；打开 long decode 后最多 1,048,576 token。上下文缓存只支持隐式，显式缓存不可用。Batch API 支持。图片生成和音频生成标成不支持。

定价页已打开，没有另一档长上下文加价。标准档：免费层输入和输出不收费；付费层输入 $1.50，输出（含思考 token）$7.50，上下文缓存 $0.075。Batch 与 Flex 都没有免费层，付费层输入 $0.75、输出 $3.75、缓存 $0.0375。Priority 免费层不收费，付费层输入 $2.70、输出 $13.50、缓存 $0.135。Contributor 是邀请制私人预览，付费层输入 $0.75、输出 $3.75、缓存 $0.0375，并且付费层内容会用来改进产品；标准、Batch、Flex、Priority 的付费层写的是不用于改进产品。标准档和 Priority 的付费层都写了 Google Search 接地：所有 Gemini 3 及更新模型共用每月 5,000 次免费搜索，之后每 1,000 次 $14，每日上限 1,500 次；Google Maps 同样是共用每月 5,000 次免费，之后每 1,000 次查询 $14。定价页写明，思考 token、以及使用接地时的内部工具说明和函数声明，都计入计费。

速率限制页打开了。Batch 排队 token 表的 Tier 1 写 Gemini 4 Hydrogen 为 3,000,000。交互请求的 RPM、TPM、RPD 这次没有对上单独一行，待核实。

同一篇博客写，Hydrogen 按整个 100 万 token 上下文统一定价，并铺到 Google AI Studio 的各层、Gemini API、Gemini for business、Gemini app、面向所有用户的 Google Search，以及付费 Google AI Pro / Ultra 在 Google Antigravity 里。Gemini app 的免费用户通过自动选模使用。博客还介绍了 Antigravity 里的 Orchestrator：同一次会话里在 Carbon 和 Hydrogen 之间切换。博客写，在 Terminal-Bench 4.0 上，成功率接近 Carbon，平均少用 24% 配额、快 19%。

Artificial Analysis changelog 同日只有这一个模型的分数：Intelligence Index 为 Low 27、Medium 41、High 51、Xhigh 54，并写 Google 的性能结果可用。博客自己把默认 high 的 51 和 Argon 的 50 放在一起，xhigh 写成 54。Argon 的 50 没有出现在当天 changelog 里。

猜测挂靠：新模型和标价在 G。Orchestrator 是同帖里的路由能力，这次不另开一条。新模型 ID 和标价是对标友商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-13：新建，status=open。
