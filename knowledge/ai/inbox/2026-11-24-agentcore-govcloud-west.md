---
title: AgentCore 运行时实例在 GovCloud（美国西部）一般可用
captured: 2026-11-24
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-runtime-instances-govcloud
    tier: 一手
---

## 是什么

AWS What's New 的发布日是 Nov 23, 2026。Amazon Bedrock AgentCore 运行时实例在 AWS GovCloud（美国西部）一般可用。实例跑在客户自己账号的 Amazon EC2 上，AgentCore 负责开通、补丁、伸缩和生命周期。

What's New 写，GovCloud（美国）里的团队可以给智能体选 GPU、内存优化或计算优化实例，会话最长 14 天。智能体实例、存储卷和会话数据留在 GovCloud（美国西部）。它和默认的无服务器 microVM 运行时并存，部署和调用方式不变。

费用写成：已开通计算的管理费，再加上 Amazon EC2 费用。管理费比例和小时单价这次没有打开定价页，待核实。已有条目记下的是 2026-11-20 的 AgentCore G7 规格，不是这个区域，不并进去。

猜测挂靠：推理运行时的区域和计费在 D。这是供应商的可用范围和价格结构，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改已有的 G7 条目。

## 处置记录

- 2026-11-24：新建，status=open。
