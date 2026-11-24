---
title: vLLM、SGLang、TensorRT-LLM 与卡、模型、Agent、后训练的关系
captured: 2026-11-09
from: followup
module: B-inference
business: false
status: promote
review_after:
entry: entries/B-inference/inference-frameworks.md
sources:
  - name: vLLM 官方文档
    url: https://docs.vllm.ai/en/latest/
    tier: 一手
  - name: SGLang 官方文档（LMSYS）
    url: https://docs.sglang.ai/
    tier: 一手
  - name: TensorRT-LLM 官方文档（NVIDIA）
    url: https://nvidia.github.io/TensorRT-LLM/
    tier: 一手
  - name: LMSYS《Announcing the SGLang AWS Trainium Plugin Beta》
    url: https://www.lmsys.org/blog/2026-10-22-sglang-trainium-beta/
    tier: 一手
---

## 是什么

单独一课，讲 vLLM、SGLang、TensorRT-LLM 这三套推理引擎分别做什么，以及它们和这些东西的关系：加速卡、模型权重、Agent、HuggingFace、后训练、强化学习框架。

查阅条目 `entries/B-inference/inference-frameworks.md` 已有选型对比和 Trainium beta。10 月 22 日、11 月 5 日、11 月 9 日的每日课只分别碰到 KV Cache、Trainium rollout、连续批处理。这节要把关系讲成一张图：引擎拿 HuggingFace 上的权重要做服务，跑在哪类卡上，Agent 和工作流在哪一层调用它，后训练里的强化学习框架又在哪一步用它生成 rollout。开课前按当时的官方文档核实，条目里已有的数字不重新当成新测量。

## 为什么没在当天处理

2026-11-09 用户要求排进学习计划。当天的学习日已经是连续批处理，排在前面的下一课是决策模型与生成式模型的结构差别。这节不插到它前面，也不在当天展开。

## 处置记录

- 2026-11-09：新建。写入 `learning-plan.md`「从回顾排入的课」第二条，status=promote。
