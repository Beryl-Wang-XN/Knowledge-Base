---
title: AgentCore Memory 的短期记忆保留最长可到 10 年
captured: 2026-11-18
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-memory-10-year-retention/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-17 写，Amazon Bedrock AgentCore Memory 的短期记忆事件最长可以保留 10 年，之前是 1 年。保留时间设在 memory resource 上，在事件创建时生效，已有事件保持原来的保留期。帖子写，保存期间仍按标准的短期记忆存储费计费。单价页这次没有打开，标 **待核实**。

可用范围是 AgentCore Memory 已经提供的全部 AWS 区域。11 月 17 日那条记的是 runtime instances 的区域，不并进这一条。

猜测挂靠：智能体会话记录的保留在 D。这是云供应商的服务变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-18：新建，status=open。
