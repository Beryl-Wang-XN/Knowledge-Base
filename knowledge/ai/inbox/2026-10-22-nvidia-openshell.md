---
title: NVIDIA 发布 OpenShell 参考架构，把智能体运行时和推理基础设施绑在一起
captured: 2026-10-22
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: NVIDIA Newsroom《NVIDIA Launches OpenShell Reference Architecture for Safe AI Agents》
    url: https://nvidianews.nvidia.com/news/openshell-reference-architecture
    tier: 一手
---

## 是什么

2026-10-21，NVIDIA 宣布 OpenShell Reference Architecture 现已可用。它在开源的 OpenShell 安全运行时之上，把三层拼成智能体基础设施：Vera Rubin 跑模型推理（含 Nemotron 以及闭源、开源模型），Vera CPU 跑 agent harness 和工具调用，BlueField-4 DPU 上的 NVIDIA Sentry 做带外监控和片内策略执行。边缘侧覆盖 RTX Spark、DGX Spark 和 DGX Station。

新闻稿中的性能说法都是 NVIDIA 自述，本次没有独立复现，回顾前不要当已核实基准：Vera Rubin NVL72 对智能体工作负载「每兆瓦吞吐 30 倍」；Vera CPU 相对 x86「2 倍性能」；若智能体越出软件边界，Sentry「在毫秒级隔离并停止」；Sentry 在 BlueField-4 上「把智能体容量提高最多 20%」。对比基线和测试条件标 **待核实**。

和推理服务供应商相关的原句：Baseten、DeepInfra、Fireworks、Together AI 正在把该参考架构集成进模型开发流水线。云侧点名包括 CoreWeave、Crusoe、GMI Cloud、Lambda、Nebius、Oracle Cloud Infrastructure、Vultr 等。ServiceNow 同日宣布个人长时智能体 ServiceNow Arc 一般可用，运行时动作由 Super Intelligence Control Tower 治理，并由 OpenShell 执行。

操作系统与编排写明覆盖 Canonical、SUSE、Red Hat 的 Linux 和 Kubernetes，以及 Microsoft Windows 上的 Microsoft Execution Containers，并可跑在 AWS、Google Cloud、Microsoft Azure 的云操作系统上。

猜测挂靠：D（智能体沙箱、策略执行和推理实例怎么放在同一套服务里）。若回顾后确认重点是 GPU 平台而不是调度，再改挂 C。供应商的服务栈，`business: true`。

## 为什么没在当天处理

这是 2026-10-22 的定时情报拉取，不是当天主轨。留待用户回顾，不写成调度或推理服务条目。

## 处置记录

- 2026-10-22：新建，status=open。
