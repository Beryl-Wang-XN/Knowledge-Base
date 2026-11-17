---
title: Bedrock AgentCore 运行时实例再开六个区域
captured: 2026-11-17
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-aws-regions/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-16 07:30:00 GMT 写明，Amazon Bedrock AgentCore 的 runtime instances 新增六个区域：美国西部（加利福尼亚北部）、加拿大（中部）、欧洲（伦敦）、欧洲（巴黎）、欧洲（斯德哥尔摩）和亚太（首尔）。扩完之后列出的区域是：美国东部（弗吉尼亚北部）、美国东部（俄亥俄）、美国西部（加利福尼亚北部）、美国西部（俄勒冈）、加拿大（中部）、欧洲（法兰克福）、欧洲（爱尔兰）、欧洲（伦敦）、欧洲（巴黎）、欧洲（斯德哥尔摩）、亚太（孟买）、亚太（首尔）、亚太（新加坡）、亚太（悉尼）和亚太（东京）。

帖子写，这些实例在 Amazon EC2 上跑智能体，由 AgentCore 负责供给、补丁、伸缩和生命周期。它把 GPU、内存优化或计算优化实例，以及最长 14 天的会话，写成这次区域里可以使用的既有能力。费用写成：除 Amazon EC2 费用外，还为所管理的预置计算付费。单价页这次没有打开，标 **待核实**。

猜测挂靠：智能体运行时的区域和实例供给在 D。这是云供应商的服务范围，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-17：新建，status=open。
