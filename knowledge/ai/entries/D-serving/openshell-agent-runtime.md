---
title: OpenShell 与智能体运行时
module: D-serving
tags: [openshell, agent, 沙箱, 推理路由, nvidia]
level: 核心
sources:
  - name: NVIDIA Newsroom《OpenShell Reference Architecture》
    url: https://nvidianews.nvidia.com/news/openshell-reference-architecture
    tier: 一手
    verified: 2026-10-22
  - name: NVIDIA OpenShell 文档 · How it works
    url: https://docs.nvidia.com/openshell/latest/about/how-it-works
    tier: 一手
    verified: 2026-10-22
  - name: NVIDIA OpenShell 文档 · Inference Routing
    url: https://docs.nvidia.com/openshell/v0.0.116/sandboxes/inference-routing
    tier: 一手
    verified: 2026-10-22
created: 2026-10-22
updated: 2026-10-22
status: 已消化
---

## 背景 / 为什么重要

智能体不只是多调一次模型。它会跑工具、访问文件、连外网，并且一次任务可能持续很久。TokenHub 如果接智能体流量，要分开看两件事：模型推理走哪条供应商，以及智能体进程被允许做什么。NVIDIA 在 2026-10-21 把这两件事放进同一套参考架构。

## 核心概念详解

[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/openshell-reference-architecture) 说 OpenShell Reference Architecture 已经可用。它站在开源的 OpenShell 安全运行时上，分成三层：

- **Vera Rubin** 跑模型推理，包括 Nemotron 以及闭源、开源模型。
- **Vera CPU** 跑 agent harness 和工具调用。
- **BlueField-4** 上的 NVIDIA Sentry 做带外监控和片内策略执行。边缘侧写到 RTX Spark、DGX Spark 和 DGX Station。

新闻稿里的性能数字是 NVIDIA 自己的说法，没有独立复现：Vera Rubin NVL72 对智能体工作负载「每兆瓦吞吐 30 倍」；Vera CPU 相对 x86「2 倍性能」；智能体越出软件边界时，Sentry「在毫秒级隔离并停止」；Sentry「把智能体容量提高最多 20%」。这些不能写成我方能拿到的收益。

官方文档把运行时拆成 CLI、Gateway 和 Supervisor。Gateway 是控制面，管 API、状态、策略和推理配置。Supervisor 在每个沙箱里，先于智能体进程启动，按策略限制进程、文件系统、网络和凭证。默认什么都不允许，权限靠策略授予，执行点在智能体进程外面。

## 关键机制 / 原理

推理有两条路，见 [Inference Routing](https://docs.nvidia.com/openshell/v0.0.116/sandboxes/inference-routing)：

- 直接访问 `api.openai.com` 这类外部地址，跟其他出网一样，由网络策略允许或拒绝。
- 沙箱里调用 `https://inference.local`。网关去掉调用方自己带的凭证，只转发允许的请求头，再注入已配置的后端凭证，转到选定的模型。

文档写明：同一个网关下，所有沙箱看到的 `inference.local` 是同一个供应商和同一个模型。支持 NVIDIA、Anthropic、Google Vertex、AWS Bedrock，以及兼容 OpenAI 接口的后端。凭证变更和推理配置可以在沙箱不重建的情况下刷新，默认大约 5 秒内生效。

新闻稿点名正在把这套架构接进模型开发流水线的推理服务商：Baseten、DeepInfra、Fireworks、Together AI。云侧包括 CoreWeave、Lambda、Nebius、Oracle Cloud Infrastructure、Vultr 等。ServiceNow 同日宣布个人长时智能体 Arc 一般可用，运行时动作由它自己的控制塔治理，由 OpenShell 执行。

## 常见误区 / 注意点

- **误区**：OpenShell 只是一个沙箱。官方产品页写，沙箱是一次进程隔离；OpenShell 还管凭证、策略、出网、推理路由和审计，覆盖智能体的整个运行期。
- **注意**：30 倍、2 倍、20% 和「毫秒级」都是厂商新闻稿口径。采购或对客户承诺之前，要有自己的负载和对比基线。

## 对我的意义 ★

- 智能体流量的成本和安全不在同一个接口上。模型账单看 `inference.local` 接到哪家供应商；工具和出网看策略有没有把默认拒绝做严。
- 如果推理供应商开始按这套架构交付，TokenHub 要问清：客户的密钥是在网关里，还是会进智能体进程。文档写的是凭证不进沙箱。
- 厂商性能倍数先记成宣传，不进成本模型。

## 原文与参考

- [NVIDIA Newsroom：OpenShell Reference Architecture](https://nvidianews.nvidia.com/news/openshell-reference-architecture)（2026-10-21）
- [How OpenShell Works](https://docs.nvidia.com/openshell/latest/about/how-it-works)
- [Inference Routing](https://docs.nvidia.com/openshell/v0.0.116/sandboxes/inference-routing)
- 关键术语对照：Gateway（控制面）、Supervisor（沙箱内的策略执行）、inference.local（沙箱内的推理入口）、Sentry（带外监控与片内执行）。
