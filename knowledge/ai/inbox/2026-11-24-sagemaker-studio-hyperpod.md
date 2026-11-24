---
title: SageMaker Studio 可向 HyperPod 提交训练并部署模型
captured: 2026-11-24
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-studio-hyperpod/
    tier: 一手
---

## 是什么

AWS What's New 的发布日是 Nov 23, 2026。Amazon SageMaker Studio 给 Amazon EKS 编排的 SageMaker HyperPod 集群加了界面：用单页表单提交分布式 PyTorch 和 Ray 训练，并从 Amazon SageMaker JumpStart、Amazon S3 或 Amazon FSx 部署模型，表单里有实时 YAML 预览。计算配置是可复用的资源预设，提交训练或部署时选用。

详情页嵌了指标和日志，来自 HyperPod Observability 和 Amazon Managed Service for Prometheus，包括 Kubernetes 状态和事件、CloudWatch 日志。开了 HyperPod task governance 的团队可以在一个队列里看训练任务和推理服务的待处理任务，并直接改任务的优先级类。

可用范围写成：当前同时支持 HyperPod 和 SageMaker Studio 的全部区域。没有新的单价。同日另有一则 HyperPod 控制台改版，只讲创建 EKS 集群的界面，不并进这一条。

猜测挂靠：在集群上提交训练和部署推理在 D。这是供应商的部署路径，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-24：新建，status=open。
