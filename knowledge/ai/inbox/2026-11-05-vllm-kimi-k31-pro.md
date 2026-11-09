---
title: vLLM 发布 Kimi K3.1 Pro 的 day-0 推理支持说明
captured: 2026-11-05
from: intel
module: B-inference
business: true
status: open
review_after:
entry:
sources:
  - name: vLLM Delivers Day-0 Support for Kimi K3.1 Pro
    url: https://vllm.ai/blog/2026-11-04-kimi-k31-pro
    tier: 一手
  - name: Hugging Face API moonshotai/Kimi-K3.1-Pro
    url: https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro
    tier: 一手
---

## 是什么

vLLM 博客 2026-11-04 的帖，写的是对月之暗面 Kimi K3.1 Pro 的 day-0 推理支持。帖子的对照表把 K3 与 K3.1 Pro 都写成 93 层（69 层 KDA + 24 层全注意力）、总参数 2.8T、上下文 1M，MoE 仍是 896 个专家、每 token 激活 16 个。变化在注意力：24 层全注意力从稠密 MLA 改成 MLA 加 DSA indexer，topk 为 2048。帖子说 NVIDIA GPU、AMD GPU、Google TPU 和阿里巴巴 T-Head 真武 PPU 当天可用，示例命令指向 `moonshotai/Kimi-K3.1-Pro`。

帖子里的 TTFT、decode 倍数、每用户 tok/s 和 KV 容量是作者在指定机器上的测量。这条不逐项抄录，具体倍数标 **待核实**。

Hugging Face 模型 API 在这次拉取时能打开 `moonshotai/Kimi-K3.1-Pro`：公开、非 gated，96 个 safetensors 分片。`createdAt` 与 `lastModified` 都是 2026-11-02T04:13:51.000Z，`usedStorage` 为 1561355732732 字节。权重仓库的时间戳不在这次 24 小时里，所以这条只记 11 月 4 日的推理支持帖，不把权重发布再记成当天的另一件事。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不改推理框架条目，也不新建 Kimi 模型档案。

## 处置记录

- 2026-11-05：新建，status=open。
