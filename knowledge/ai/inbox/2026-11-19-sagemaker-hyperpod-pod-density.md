---
title: SageMaker HyperPod 提高 EKS 集群的每节点 Pod 密度
captured: 2026-11-19
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-higher-pod-density/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-18 写，Amazon SageMaker HyperPod 在 EKS 编排的集群上提高每个节点能放的 Pod 数。监控、日志和安全用的 DaemonSet 之外，应用能占更多位置，节点上的 GPU、CPU 和内存利用率可以提高，同样的工作可以用更少实例。Pod 变多时，Amazon VPC CNI 会自动给节点加网络容量。Karpenter 扩容也会按更高的 Pod 容量来要新节点。

公告举的例子包括：在每个 GPU 实例上放更多推理副本或更多模型，含 ml.g5、ml.g6 这类较小机型；在 ml.p5en.48xlarge 上把 Multi-Instance GPU 的每个切片放进自己的 Pod。要先更新集群的 IAM 权限、集群软件和 Amazon VPC CNI 附加组件。可用范围是提供 SageMaker HyperPod 的全部 AWS 区域。没有新的单价。具体 Pod 上限这次没有打开文档，待核实。

猜测挂靠：同一 GPU 上放更多推理副本在 D。这是供应商调度能力的变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-19：新建，status=open。
