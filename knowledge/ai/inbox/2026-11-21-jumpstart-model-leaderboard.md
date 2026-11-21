---
title: SageMaker JumpStart 上线模型排行榜，不另收费
captured: 2026-11-21
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/1/sagemaker-jumpstart-model-leaderboard/
    tier: 一手
---

## 是什么

AWS What's New 写明发布日是 2026-11-20。Amazon SageMaker JumpStart 在 SageMaker Studio 里提供模型排行榜，用来并排比较基础模型的吞吐、时延和成本，再部署或定制。What's New 写 AWS 用同一套评测设置，在 BIG-Bench Hard、GPQA Diamond 和 MMLU-Pro 上评每个模型，并在 SageMaker 上测量每种 JumpStart 部署配置的首 token 时间、吞吐和实例成本。可以沿用 JumpStart 已有的筛选，例如提供方、许可证、输入和输出模态，也可以选一个用例配置和优化目标（均衡、成本、时延或吞吐）。上线时覆盖超过 70 个 LLM，提供方包括 Meta、Google、Qwen、IBM 和 Arcee。

排行榜在已提供 SageMaker Studio 的全部 AWS 商业区域可用，不另收费。各模型的分数、时延和实例单价这次没有打开方法页，待核实。

猜测挂靠：可比较的模型质量、速度和成本在 G。这是供应商的选型工具，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-21：新建，status=open。
