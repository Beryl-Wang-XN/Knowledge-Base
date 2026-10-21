---
title: DeepSeek 推理框架开源（DeepInfer）及能否集成
captured: 2026-10-21
from: followup
module: B-inference
business: true
status: open
review_after:
entry:
sources:
  - name: DeepInfer 仓库
    url: https://github.com/deepseek-ai/DeepInfer
    tier: 一手
  - name: DeepInfer 部署问答 inference_deployment_qa.md
    url: https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md
    tier: 一手
  - name: 早期「推理引擎开源路径」说明（open-infra-index）
    url: https://github.com/deepseek-ai/open-infra-index/tree/main/OpenSourcing_DeepSeek_Inference_Engine
    tier: 一手
---

## 是什么

用户要求把「DeepSeek 推理框架开源集成」记入 inbox。按 2026-10 的官方仓库，先对应 **DeepInfer**：DeepSeek 称其为支撑大规模线上服务的高性能推理框架，此次开源的是离线推理和一批核心能力。仓库列出的支持模型是 **DeepSeek-V4.1-Flash**。同批还开源了 **deepseek-recipe**（请求与 token 序列的转换，官方称与 DeepSeek API 的处理逻辑对齐）。官方 Q&A 写明：后续模型的推理代码会继续放进这个仓库。

和「能不能集成进现有服务」直接相关、但本次不写入条目的边界（均出自上述官方 Q&A，回顾时再逐段核对）：

- KV cache 管理、负载均衡和内部基础设施绑在一起，**这次没有完全开源**。因此开源仓库还不是一套可直接上线的完整服务。
- 官方 Q&A 里的规模与收入口径（单集群每天 token 量、谷值定价下每 GPU 小时收入）标 **待核实**，不在这条里抄数字。
- 硬件支持范围、和 vLLM / SGLang 的关系标 **待核实**。知识库里已有推理引擎对比，回顾时只补差异，不另起一篇重复的框架综述。

另有一份更早的 open-infra-index 说明：当时认为内部引擎从旧版 vLLM 分叉、和内部集群绑定，选择把能力拆回现有开源项目，而不是整体开源。回顾时要把这份旧说明和 DeepInfer 分开，避免当成同一件事。

猜测挂靠：B（推理框架）。若回顾后确认重点是调度、多机 Prefill/Decode 或供应商格局，再决定是否同时挂 D 或 F。对标友商的推理栈，`business: true`。

## 为什么没在当天处理

这是用户点名要暂存的第二条，不是当天的主轨。当天不写成推理框架条目，也不改 `registry/models/deepseek.md`。

## 处置记录

- 2026-10-21：按用户要求新建，`status: open`，等待 inbox 回顾。
