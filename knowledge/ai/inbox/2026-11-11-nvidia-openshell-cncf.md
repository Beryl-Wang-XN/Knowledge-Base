---
title: NVIDIA 把 OpenShell 捐给 CNCF，并预览推理副本快照
captured: 2026-11-11
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: NVIDIA 博客 OpenShell donation and AI infrastructure
    url: https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/
    tier: 一手
---

## 是什么

2026-11-10，NVIDIA 博客宣布在 KubeCon 上把开源智能体运行时 OpenShell 贡献给 CNCF，作为 Sandbox 项目。这和 2026-10-22 inbox 里已经记下的 OpenShell 参考架构不是同一件事：那次是 2026-10-21 的硬件参考架构，这次是把运行时交给基金会，并加上一组 Kubernetes 组件。

同一篇还写，NVIDIA 参与 Google 牵头、已进入 CNCF Sandbox 的 Agent Substrate，让它与 NVIDIA Dynamo 的模型推理和 KAI Scheduler 的集群分配一起工作。Agent Substrate 在任务之间保留智能体环境，空闲时释放算力，用挂起和恢复来共用一组智能体，而不必为每个会话一直占着机器。NVIDIA 与 Google 还在做 OpenShell 和 Agent Substrate 的集成。

DSX AI Factory Platform 增加三个开源组件。NVIDIA Kubernetes Engine（NVKE）和 NVIDIA Kubernetes Recipes（NVKR）进入公共预览，用来在 GPU 基础设施上提供托管 Kubernetes，包括集群生命周期和带签名、版本固定的镜像。NVIDIA Snapshot 用来恢复已经做了检查点的推理副本，博客写不需要重新加载模型或预热。设计伙伴 Crusoe 和 Saturn Cloud 在 NVIDIA HGX B300 上做过自己的测试：Crusoe 在 Crusoe Cloud 上跑 GLM-5.3，工作负载变为就绪的时间从大约 8 分钟降到 31 秒；Saturn Cloud 测从零扩容的 vLLM，启动时间从 2 到 8.5 分钟降到 6 到 34 秒。这些是伙伴自述，对比条件留在原文。

猜测挂靠：调度服务在 D-serving。供应商的推理与智能体运行时变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-11：新建，status=open。
