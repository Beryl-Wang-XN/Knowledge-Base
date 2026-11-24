---
title: Gemini 4 Carbon 向付费开发者和企业开放，入门价截至 11 月 30 日
captured: 2026-11-11
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Gemini 4 Carbon is now available
    url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
    tier: 一手
  - name: Google 开发者博客 Gemini 4 Carbon for developers
    url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-4-carbon-developers/
    tier: 一手
---

## 是什么

2026-11-10，Google 宣布 Gemini 4 Carbon 向开发者、企业、科研人员和消费者开放。这和 2026-10-29 inbox 里记下的限量预览不是同一件事：那次官方写的是只向一部分网络安全防御方铺开。这次博客写，付费开发者和企业可以在 Google AI Studio 与 Gemini for business 的 API 里使用；Google AI Ultra 订阅用户则在 Google Antigravity、Gemini app 和 Search 的 AI Mode 里陆续开放。

价格写在同一篇博客的脚注里。入门价与 Gemini 4 Argon 相同，每百万 token 输入 $2、输出 $10。入门期到 2026-11-30 结束，之后公开使用的 Carbon 为输入 $4、输出 $20。脚注写明，这只适用于打算公开提供的那一版 Carbon。这篇没有重述 10 月帖子里的缓存折扣。API 模型 ID 这次没有打开模型卡或 Gemini API changelog，标 **待核实**。

网络安全能力仍分开写。博客说 Carbon for cyber 通过 Fairwind Program 申请，按滚动方式给防御方。开发者博客同日只是指向 API 付费层和 Antigravity，没有另一套标价。

同一篇还预览了 Google Antigravity 里的 `/swarm`：一条提示拆成一组可跟踪的智能体，Carbon 负责更深的推理角色，并可以配上更快的模型。多模态知识工作基准 MKA 同日发布，分数和单任务成本写在另一条 inbox 里。这篇自己的说法是：Carbon 在所测模型里质量第 2，平均单任务成本比最高分模型低 6 倍以上。

猜测挂靠：模型档案在 G。公开可用和标价截止日期是对标友商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-11：新建，status=open。
