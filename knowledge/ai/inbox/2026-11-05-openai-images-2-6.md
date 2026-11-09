---
title: OpenAI 发布 Images 2.6（API 模型 Sunburst 与 Flare）
captured: 2026-11-05
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API changelog（2026-11-04）
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: Introducing Images 2.6
    url: https://openai.com/index/introducing-images-2-6/
    tier: 一手
---

## 是什么

OpenAI API changelog 的 2026-11-04 条目，以及同日新闻室帖，发布 Images 2.6。API 侧的模型名是 `gpt-image-2.6-sunburst` 与 `gpt-image-2.6-flare`，接口是 `v1/images/generations` 和 `v1/images/edits`。changelog 写明：可调 complexity、可生成 SVG 和动态 GIF，并为支持的 GPT Image 2.5 与 2.6 增加 markup-guided editing。

新闻室帖写明：Images 2.6 当天在 ChatGPT 与 Codex 全球上线，覆盖全部订阅档，桌面、移动和网页都有。API 提供 Flare 与 Sunburst。帖子把 Flare 放在低质量、更快的一侧，把 Sunburst 放在中/高质量、更强调编辑一致性的一侧。complexity 用来调节模型为请求做多少规划；quality 管画面细节。markup 从 ChatGPT 扩到 API。

帖子里的速度与用量口径（生成比以前快 50%；quality 设为 low 时 Flare 最快可到六秒；ChatGPT、Codex 与 API 合计每周约 40 亿张图）是厂商自己的说法，这条照帖记录，没有另做测量。API 标价这次没有打开定价页，标 **待核实**。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写入模型档案，也不展开成图像生成或计费条目。

## 处置记录

- 2026-11-05：新建，status=open。
