---
title: OpenAI 新模型不再支持 Flex 处理
captured: 2026-11-22
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI API changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: OpenAI Flex processing
    url: https://developers.openai.com/api/docs/guides/flex-processing
    tier: 一手
  - name: OpenAI API changelog 2026-11-20 存档
    url: https://docswatch.stevetoth.ai/archive/20261120104830/https://developers.openai.com/api/docs/changelog/
    tier: 二手
---

## 是什么

API changelog 里 2026-11-17 的后台完成窗口那一节，现在多了两句：新模型不会支持 Flex processing；已经支持的模型在 beta 收尾期间仍可使用。这一节的日期标题仍是 Nov 17，没有单独的 2026-11-21 节。2026-11-20 10:48 UTC 的同一页存档里没有这两句。文档监测站把首次看见写在 2026-11-21 10:28 UTC。

Flex 指南现在写：可以在仍支持的模型上继续用 Flex，beta 正在收尾。Flex 不用于 GPT-6.2 Astra 和 GPT-6.2 Sol，以后的模型也不会加。退役日期和迁移说明要等日期确定后再写在这一页，这次没有日期。调用方式仍是 `service_tier` 设为 `flex`。指南写 token 按 Batch API 费率计价，并叠加提示缓存的额外折扣。Batch 费率的具体比例这次没有打开定价页，待核实。资源不足时返回 `429 Resource Unavailable`，这种情况不收费。

指南把可以异步跑的工作指向 Responses API 的后台完成窗口，并写两小时窗口比标准价低 30%、八小时低 40%。这组和已记的 2026-11-17 后台窗口是同一件事，不另开一条。

猜测挂靠：服务档和标价在 E。这是价格档变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改已有的后台窗口条目。

## 处置记录

- 2026-11-22：新建，status=open。
