---
title: SGLang 在 AWS Trainium 上的推理与 RL rollout 进入 beta
captured: 2026-10-23
from: intel
module: B-inference
business: true
status: open
review_after:
entry:
sources:
  - name: LMSYS《Announcing the SGLang AWS Trainium Plugin Beta》
    url: https://www.lmsys.org/blog/2026-10-22-sglang-trainium-beta/
    tier: 一手
---

## 是什么

2026-10-22，SGLang 团队在 LMSYS 博客宣布 AWS Trainium 插件进入 beta，构建在 AWS 的 PyTorch 后端 TorchNeuron 上。beta 覆盖 Trainium2 与 Trainium3 的两类负载：LLM 推理服务，以及后训练时的 RL rollout。

博客列出的首批模型是 Qwen3 稠密、Qwen3-MoE-30B-A3B、DeepSeek-V2-Lite、GLM-4，以及 GLM-5.2 / 5.3。写出的特性是数据并行、张量并行、专家并行、Radix Cache、BF16 / FP8 和异步调度。文中的异构 RL 示例是：SGLang 在 Trainium3 上为 Qwen3-MoE-30B-A3B 生成 rollout，Miles 用 Megatron 在单台 H200 上训练 GRPO 策略。吞吐、单价，以及相对 GPU 的价差，这篇没有给出数字，标待核实。beta 目前只对少量团队开放，需要申请。

## 为什么没在当天处理

这是 2026-10-23 的定时情报拉取，不是当天的学习主轨。先留在 inbox，等用户回顾后再决定要不要核进推理框架或算力供应商相关条目。

## 处置记录

- 2026-10-23：新建，status=open。
