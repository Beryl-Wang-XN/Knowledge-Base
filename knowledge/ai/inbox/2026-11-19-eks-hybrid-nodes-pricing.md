---
title: EKS Hybrid Nodes 大主机按最多 32 vCPU 计费
captured: 2026-11-19
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-hybrid-nodes-pricing-change/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-18 写，Amazon EKS Hybrid Nodes 调低大节点价格：每个节点计费的 vCPU 封顶 32，超过部分不再计费。公告点名包括带 GPU 的大型服务器，用于必须留在本地的 AI/ML 训练和推理。

在第一档价格下，64 vCPU 的节点比调整前少 50%，256 vCPU 的节点少 88%，因为两者都只按 32 vCPU 计。新混合节点自动适用。已经挂在集群上的节点要拆掉再挂上，新价格才生效。32 vCPU 及以下仍按实际 vCPU 计，原有分档价格仍在，月用量上去之后有效单价下降。

每 vCPU 的绝对单价这次没有打开 EKS 定价页，待核实。可用范围是提供 Hybrid Nodes 的全部 AWS 区域。

猜测挂靠：本地 GPU 节点的计费在 E。这是价格变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-19：新建，status=open。
