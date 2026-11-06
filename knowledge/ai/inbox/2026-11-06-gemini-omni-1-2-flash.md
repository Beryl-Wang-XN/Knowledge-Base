---
title: Gemini Omni 1.2 Flash 一般可用，视频输出降价
captured: 2026-11-06
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
  - name: Gemini API 定价页 Omni 1.2 与 1.1
    url: https://ai.google.dev/gemini-api/docs/pricing#gemini-omni-1.2-flash
    tier: 一手
  - name: Gemini API 速率限制页 Omni Flash
    url: https://ai.google.dev/gemini-api/docs/rate-limits#gemini-omni-flash-rate-limits
    tier: 一手
---

## 是什么

Gemini API changelog 的 2026-11-05 写明：`gemini-omni-1.2-flash` 一般可用。更新日志描述它支持最长 15 秒视频生成，以及对话式编辑（首尾帧插值 3 到 10 秒，逐轮延长每次 3 到 10 秒、总长最多 30 秒），并可用最多 6 张参考图保持主体一致。

定价页付费档、每百万 tokens：输入 $1.50（文本 / 图像 / 视频）；输出含思考 token，文本 $9.00，视频 $12.00。免费档不可用。同页的 `gemini-omni-1.1-flash` 输入仍是 $1.50，文本输出仍是 $9.00，视频输出是 $17.50。更新日志把 1.2 的视频输出称为低 30%，并写成 $12.00。定价页脚注按输出 token 计费，720p 为每秒 5,792 tokens，并给出按分辨率折算的大约每秒价格，具体秒价留在原文。

自 2026-12-03 起，对 `gemini-omni-1.1-flash` 的请求会自动转到 `gemini-omni-1.2-flash`，并按 1.2 的价格计费。changelog 与定价页都这么写。

速率限制页列出 `gemini-omni-1.2-flash` 的标准交互限制：免费档不支持；Tier 1 为 8 RPM、40 RPD；Tier 2 为 16 RPM、200 RPD；Tier 3 为 40 RPM、2,000 RPD。更新日志写付费档速率限制加倍。1.1 的旧限额没有出现在这次打开的该节里，旧数值待核实。

同日 changelog 还有 Office 文件支持，另记一条，不并进这个模型。

猜测挂靠：模型档案在 G。视频输出价格变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-06：新建，status=open。
