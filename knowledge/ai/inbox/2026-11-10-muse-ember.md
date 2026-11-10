---
title: Meta 发布 Muse Ember，短上下文标价 $0.10 / $0.50
captured: 2026-11-10
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Meta 研究博客 Introducing Muse Ember
    url: https://research.meta.ai/blog/muse-ember
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

2026-11-09，Meta 发布 Muse Ember，模型名 `muse-ember-1.0`。官方博客把它放在重复的编码和智能体步骤上：工具调用、编码子任务、路由、抽取和长文档解析。可用位置写的是 Muse Code 和 Meta Model API，并支持 Responses API。文末另写，Muse Ember、Muse Spark 和 Muse Wonder 现在可以在 Google Cloud 和 Oracle Cloud 上使用。

博客的 Availability 一节写明：上下文窗口 100 万 token，最大输出 512K token。提示不超过 200K token 时，每百万 token 输入 $0.10、缓存输入 $0.004、输出 $0.50。脚注写，更长的提示是输入 $0.30、缓存输入 $0.012、输出 $1.50。同页前面还有一句只写了输入 $0.10、输出 $0.50，没有缓存价；完整三档以 Availability 和脚注为准。

Artificial Analysis changelog 同日写，Muse Ember（Max）的 Intelligence Index 是 36，Xhigh 是 34，并称它是得分 36 的模型里每任务成本最低的，与 Claude Haiku 5.5（max）持平、每任务成本约三分之一。Meta 博客的对照表把 Intelligence Index 写成 36，每任务成本约 $0.14；同页另一张图里，max 一档的分数是 35.8、每任务 $0.136。其余分项基准留在原文。

猜测挂靠：模型档案在 G。新模型和标价是对标友商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-10：新建，status=open。
