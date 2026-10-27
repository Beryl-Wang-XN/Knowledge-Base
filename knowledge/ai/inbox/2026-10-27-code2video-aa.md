---
title: Artificial Analysis 发布 Code2Video-AA 视频代码评测
captured: 2026-10-27
from: intel
module: G
business: false
status: open
review_after:
entry:
sources:
  - name: Code2Video-AA 发布说明
    url: https://artificialanalysis.ai/articles/code2video-aa
    tier: 一手
  - name: Code2Video-AA 榜单
    url: https://artificialanalysis.ai/evaluations/code2video-aa
    tier: 一手
---

## 是什么

2026-10-26，Artificial Analysis 发布 **Code2Video-AA**。这是他们对 HeyGen Code2Video Bench 的独立实现：114 条产品与品牌短视频设计说明，模型一次调用、不给工具，交回一份 HyperFrames HTML（HTML 排版，GSAP 动画），再渲染成视频。总分是五个评审轴 Elo 的平均，锚定在 GPT-5.5（xhigh）= 1000。文章中的数字截止 2026-10-26，数据集版本 0.3.0。现行名次以榜单页为准。

发布文里的头条：Claude Opus 5.5（max with fallback）1536，领先下一名 93 分，且五个轴都是第一。并列第二附近是 Claude Sonnet 5.5（max with fallback）1443 与 GPT-6 Astra（max）1427；GPT-6.1 Sol（max）第四，1369。每任务成本从 $0.01 到 $3.89，相差 300 倍以上；文中举例 GPT-6.1 Sol（max）约 $0.31，Claude Opus 5.5（max with fallback）约 $3.08。开源权重领先的是 DeepSeek V4.1 Flash（max）1053，以及 MiMo-V2.6-Flash / Pro，均为 1052。27 个模型里，3042 / 3078 个任务渲染成功（98.8%）。

评审用的具体模型、采样和 Elo 拟合在方法论页。这次没有逐段打开方法论，评审模型标 **待核实**。完整名次表不抄进这里。

猜测挂靠：G。这是新的能力评测，不是厂商调价。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不把榜单写进模型档案，也不写成知识条目。

## 处置记录

- 2026-10-27：新建，status=open。
