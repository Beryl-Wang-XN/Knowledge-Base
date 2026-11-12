---
title: 火山方舟个人版套餐启动下线 kimi-k3，11 月 25 日停服
captured: 2026-11-12
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: 火山方舟 Agent Plan 个人版模型下线说明
    url: https://docs.volcengine.com/docs/ark/agent-plan-personal-model-deprecation-announcement
    tier: 一手
  - name: 火山方舟 Coding Plan 个人版模型下线说明
    url: https://docs.volcengine.com/docs/ark/coding-plan-personal-model-deprecation
    tier: 一手
  - name: 火山方舟 Agent Plan 企业版模型下线说明
    url: https://docs.volcengine.com/docs/ark/agent-plan-enterprise-model-deprecation
    tier: 一手
---

## 是什么

火山方舟个人版 Agent Plan 和 Coding Plan 的下线说明都有「2026.11.11 启动模型下线」。对象是 `kimi-k3`，建议迁到 `kimi-k3.1-pro`。两页的时间一样，都是北京时间：2026-11-11 10:00 启动并通知，同时停止向新用户提供；2026-11-25 14:00 正式停服。新用户的定义按套餐分开写：买了对应个人版套餐、但还没用过该模型的人。页上写到期没迁会影响业务。这次没有打开按量价格页，停服后的目录价标待核实。

同一页的 `latest` 对照表仍把 `kimi-latest` 写成 `kimi-k2.7-code`。该模型在这两页的已下线表里是 10 月 28 日，和这次建议的 `kimi-k3.1-pro` 不是同一行。

Agent Plan 企业版下线页本次打开时，最新一节仍是 2026-10-19 的 `minimax-m3`，没有 2026-11-11 的 `kimi-k3`。Coding Plan 企业版页面这次没有打开。

猜测挂靠：云厂商套餐里的模型进退在 F。供应商侧下线是对标供货变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-12：新建，status=open。
