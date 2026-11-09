---
title: Google Agent Compute Engine
module: D-serving
tags: [google-cloud, agent, microvm, 沙箱, 治理]
level: 核心
sources:
  - name: Google Cloud《Introducing Agent Compute Engine and expanding agent governance》
    url: https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance
    tier: 一手
    verified: 2026-11-05
created: 2026-11-05
updated: 2026-11-05
status: 已消化
---

## 背景 / 为什么重要

智能体要写代码、调工具、开浏览器，而且会经常停下来等人或外部系统。Google Cloud 在 2026-10-22 的博文里把这件事写成基础设施问题，并发布 Agent Compute Engine。TokenHub 如果接长时智能体，要分开看三件事：沙箱怎么隔离、空闲时占不占机器、凭证会不会进智能体进程。

## 核心概念详解

[这篇博文](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) 说 Agent Compute Engine 已经在支撑 Gemini 的工作任务代理。面向客户的预览要到未来数月。官方描述的运行单元是硬件隔离的 microVM：Cloud Hypervisor 边界、自己的客户机内核和 root。它和 Google 的 Titanium 卸载卡一起用。每个 microVM 有自己的 Hyperdisk，用来留下工作区和上下文。

空闲时的做法是快照。智能体做完一次工具调用、进入等待时，microVM 可以暂停，再从快照恢复。博文写，服务凭证在出网时注入，注入点在 microVM 外面。每个 microVM 还有自己的短期凭证和一个可校验的身份。

同一篇还给了已经在用 Kubernetes 的团队另一条路：GKE 上的开源运行时 Agent Substrate。智能体空闲时，它把活动内存做成快照，把机器还回池子。博文写它可以跑在任何 Kubernetes 集群上，并点名兼容 Claude Code、OpenClaw 和 Hermes。

## 关键机制 / 原理

治理扩展写在同一篇里，还没有全部一般可用：

- Agent Gateway 管客户端到智能体、以及智能体到外部的流量。
- Agent Registry 是已批准的智能体、工具、MCP、技能、模型和端点的清单。
- Agent Identity 用 SPIFFE 给每个智能体一个身份。
- 可观测性按 OpenTelemetry 的智能体语义输出。

博文说，本季度的预览里，Agent Gateway 会加上按智能体和模型管 token 与成本，以及模型路由策略。跨云、混合环境和本机编码代理的治理，写的是「即将预览」。售价这篇没有给。

## 关键数据与事实（已核实）

下面的密度和延迟是 Google 自己的基准口径，不是我方复现：

- Agent Substrate 相对传统计算，密度最高约 **10 倍**，同时保持内核隔离。
- 一组基准：跑 **20 万**个智能体，每秒 **500** 次激活，暂停和恢复延迟 **低于 500 毫秒**。

## 常见误区 / 注意点

- **误区**：客户现在就能买到和 Gemini 内部一样的 Agent Compute Engine。博文写的是它已经支撑 Gemini，客户预览在未来数月。
- **注意**：10 倍和 500 毫秒是厂商基准。采购前要用自己的智能体启停节奏做对比。

## 对我的意义 ★

- 长时智能体的成本不只在模型 token。机器会不会在等待时暂停，决定一张主机上能叠多少会话。
- 文档写的是凭证在 microVM 外注入。接入时要问清客户密钥会不会进沙箱。这和 OpenShell 的 `inference.local` 是同一类问题。
- 本季度预览里的 token 归因和模型路由，会碰到 TokenHub 已经在做的计费和路由。售价没有准确数据，先不要写进报价。

## 原文与参考

- [Google Cloud：Agent Compute Engine](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance)（2026-10-22）
- 关键术语对照：microVM（微型虚拟机）、checkpoint / restore（快照暂停与恢复）、Agent Gateway、SPIFFE。
