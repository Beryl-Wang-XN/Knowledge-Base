---
title: AgentCore 运行时实例支持 EC2 G7
captured: 2026-11-21
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-ec2-g7/
    tier: 一手
  - name: AgentCore 发布说明
    url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html
    tier: 一手
  - name: AgentCore 定价页
    url: https://aws.amazon.com/bedrock/agentcore/pricing/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-20 写下，Amazon Bedrock AgentCore 的运行时实例支持 Amazon EC2 G7。GPU 是 NVIDIA RTX PRO 4500 Blackwell Server Edition。实例规格从 `g7.2xlarge` 到 `g7.48xlarge`，加进容量提供方允许的实例类型即可。AgentCore 负责装 NVIDIA 驱动，标准容器镜像不用自己带驱动。What's New 的例子是渲染三维场景，或在会话自己的 GPU 上跑视觉模型。会话最长 14 天。

区域是美国东部（弗吉尼亚北部）、美国东部（俄亥俄）、美国西部（俄勒冈）、欧洲（法兰克福）、欧洲（伦敦）、欧洲（斯德哥尔摩）、亚太（孟买）和亚太（悉尼）。发布说明的 2026 年 11 月一节写了同一件事，没有再写一个更细的日。

What's New 写费用是 EC2 费用之外，再收托管已开通计算的管理费。定价页写运行时实例按底层 EC2 的运行时长计费，管理费按公开的 EC2 按需价的一个百分比计算，Savings Plans、预留实例和按需容量预留只作用于 EC2 计算、不作用于管理费。定价页的 CPU 示例把管理费写成按需价的 12%，那一行的机型是 `c7g.2xlarge`，不是 G7。同一页写 G 系列（举例含基于 Graviton 的 gr6）管理费是 7.8%。这一节没有列出 `g7` 的小时单价，What's New 也没有写 7.8% 是否已经套到 G7。G7 的 EC2 小时价这次没有打开 EC2 价格页，待核实。

猜测挂靠：推理运行时的实例和计费在 D。这是供应商的算力选项和价格结构，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改 `registry/`。

## 处置记录

- 2026-11-21：新建，status=open。
