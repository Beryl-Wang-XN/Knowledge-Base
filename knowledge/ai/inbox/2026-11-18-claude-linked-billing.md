---
title: Claude Platform 公开测试关联计费
captured: 2026-11-18
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Claude 关联计费说明
    url: https://claude.com/resources/articles/linked-billing-on-claude-platform
    tier: 一手
---

## 是什么

Claude Platform 发布说明在 2026-11-17 写，关联计费以 beta 推出，beta header 是 `user-profiles-billing-2026-10-01`。客户把自己的 Claude 组织连上之后，第三方应用里的 Claude 用量可以由客户自己的组织支付，不必交出 API key。应用在每次 `/v1/messages` 或 `/v1/chat/completions` 请求上设置 `billing_policy`，决定由谁付。客户可以在 Claude Console 里给该应用设支出上限，或解除关联。发布说明写，这适用于组织直接向 Anthropic 支付 API 费用的客户。

产品文补充：平台可以看到每个已关联客户的用量；客户用一次关联覆盖整个组织，审批角色是 Owner、Admin 或 Billing。可以按平台设月度支出上限，或设一个对每个平台生效的默认值。每次请求可以选择平台付或终端客户付。请求跑在平台的组织里，客户组织上的 IP allowlist、加密密钥和数据保留不作用于这些请求。文中点名当时支持的平台：Asana、ClickHouse、Factory、Gumloop、Harness、Higgsfield AI、Kilo Code、Linear、Major、Mintlify、Omni、OpenArt、Niteshift、Railway、Ramp、Runlayer、Tessera、Tines、Warp。没有单独的 token 标价。

猜测挂靠：谁为 API 用量付费在 E。这是友商的计费方式，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-18：新建，status=open。
