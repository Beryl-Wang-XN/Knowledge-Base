---
title: 决策模型与生成式模型的结构差别
captured: 2026-11-09
from: followup
module: A-model
business: false
status: promote
review_after:
entry:
sources:
  - name: TypeSafe《Introducing System One Models & Jev》
    url: https://typesafe.ai/blog/introducing-system-one-models-and-jev
    tier: 一手
  - name: OpenAI Decisions API 开发指南
    url: https://developers.openai.com/api/docs/guides/decisions
    tier: 一手
  - name: OpenAI《Build more responsive apps with the Decisions API》
    url: https://openai.com/index/decisions-api/
    tier: 一手
---

## 是什么

单独一课，讲 Jev 和 Decisions API 的模型结构与生成式模型有什么不同。要回答的是：为什么它们可以一次给出带类型、带概率的决定，而聊天模型要一个 token 一个 token写字符串。

已经写回档案、这节不再讲的部分：场景是答案范围事先写死的分类、路由、打分和决定下一步。答案空间由程序事先设定，调用由程序或已配置的触发器发起。用量只有分渠道的切片，没有全球占比。

这节开课时要分开两层。产品层已经有一手说法：输出空间事先定好，采样一次给出全部结果，每项带概率。Jev 的博文还写了新的模型结构和 RLCD，但没有给参数量、网络图和算法。Decisions API 的公告写它基于 GPT-6 Luna。两边内部是不是同一类做法，开课前再对文档和论文，没有一手说明就标待核实。

## 为什么没在当天处理

2026-11-09 是看完 11 月 5 日每日页之后的追问。用户要求以后单独开一课，当天不展开。

## 处置记录

- 2026-11-09：新建。场景、调用方式与用量已写回 `registry/models/jev.md` 和 `entries/E-economics/token-billing.md`。结构差别写入 `learning-plan.md`「从回顾排入的课」，status=promote。
