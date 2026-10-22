---
title: OpenAI 更新使用政策，模型路由与 AI 网关需事先审批
captured: 2026-10-22
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI《Broad access through consistent standards》
    url: https://openai.com/index/broad-access-through-consistent-standards
    tier: 一手
---

## 是什么

2026-10-21，OpenAI 发文说明正在把安全要求对齐到所有提供其模型的服务，并更新 Usage Policies。新政策生效日写的是 **2026-11-20**。

和转售、网关相关的原文要点：

- 政策覆盖直接通过 OpenAI 访问、合作方托管，以及 reseller partners。提供访问的合作方要维持与 OpenAI 一致的防护，调查违规，并在跨服务执行上协调，避免限制在一家失效。
- 更新后的 Usage Policies 要求：提供对 OpenAI 模型直接访问的服务，例如 model routers 或 AI gateways，在提供该访问之前要先经过 OpenAI 的 review and approval。
- 文中把 GPT-6 Astra 当作能力扩大后的例子，没有在这篇里给新价格或新模型规格。
- 另提到与客户推进 SafetyIDs：客户可提供标识，帮助 OpenAI 在调查中区分终端用户，同时 OpenAI 不获知这些用户身份。具体接口标 **待核实**。

猜测挂靠：F（供应商准入与转售条件）。若回顾后确认重点是计费或调度网关的合规设计，再决定是否同时挂 E 或 D。对标供应商条款，`business: true`。

## 为什么没在当天处理

这是 2026-10-22 的定时情报拉取，不是当天主轨。留待用户回顾，不写成合规或供应商条目。

## 处置记录

- 2026-10-22：新建，status=open。
