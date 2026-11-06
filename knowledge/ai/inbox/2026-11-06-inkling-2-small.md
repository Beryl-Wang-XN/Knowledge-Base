---
title: Thinking Machines 发布 Inkling 2 Small，先在 Tinker 闭源提供
captured: 2026-11-06
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Introducing Inkling 2 Small
    url: https://thinkingmachines.ai/news/inkling-2-small/
    tier: 一手
  - name: Tinker Models and Pricing
    url: https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

Thinking Machines Lab 于 2026-11-05 发布 Inkling 2 Small。公告写它是 MoE，总参数 594B，每 token 激活 17B，支持图像输入和可变 effort，不支持音频。起初只在 Tinker 提供，权重关闭。公告写外部安全测试和红队结束后，打算在下一周以 Apache 2.0 放出完整权重；权重放出后检查点才可下载。公告还写，安全测试完成后数周内会到更多平台。

公告和 Artificial Analysis 2026-11-05 changelog 都给出 Intelligence Index 31。公告里的分项榜单本次不抄。公告的 RL 一节写上下文窗口 256K，更长轨迹用 compaction；评测一节写轨迹上限是 1M tokens。这两处不要当成同一个对外上下文产品规格。

Tinker 定价页写价格按每百万 tokens。本次打开的表：`thinkingmachines/Inkling-2-Small` 为 64K，prefill $0.30，缓存 prefill $0.03，sample $1.00，train $1.50。`thinkingmachines/Inkling-2-Small:peft:262144` 为 256K，prefill 与 sample 相同，train $3.00。同页还有一条 NVFP4 采样变体，不在这里展开。

猜测挂靠：模型档案在 G。有对外采样和训练标价，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-06：新建，status=open。
