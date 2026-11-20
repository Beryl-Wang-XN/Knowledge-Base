---
title: NVIDIA 写 Foundry 扩大 Nemotron 3.5，并接到 Azure Local
captured: 2026-11-20
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: NVIDIA 博客
    url: https://blogs.nvidia.com/blog/microsoft-ignite-accelerated-computing-azure-windows-pcs/
    tier: 一手
---

## 是什么

同一篇 NVIDIA 博客在 2026-11-19 写，Microsoft Foundry 上的 NVIDIA 开源模型和定制能力在扩大客户可用范围。Foundry Managed Compute 增加部署自定义模型权重，把定制和微软托管的部署接起来。Programmed Training 的公开预览已在 2026-11-17 的 Foundry 条目里，不重复那一篇的食谱和模型列表。这篇把 EY 用 Programmed Training 改编 Nemotron、在其评测集上准确率提高 55%、成本相对专有前沿模型低 15 倍，写成客户例子。

帖子列出的 Foundry Managed Compute 上的 Nemotron 3.5：Super 用于长程智能体，Lightning 用于要快响应和工具调用的应用；配套还有 Embed、Rerank、Parse 和 Content Safety。Bolt 写成面向高吞吐、低时延推理，Transcribe 用于语音识别，两者都是即将推出。Lightning 和 Super VL 更早已经出现在 Foundry 的帖子里，这篇没有逐个写上架日，不把它们当成 11 月 19 日首发。token 单价这篇没有写，待核实。

本地和边缘：Foundry Local 扩大对 Nemotron 3.5 的支持，覆盖推理、代码和会用工具的智能体，并写到 Azure Local。Azure Local 还将支持硬件伙伴的 NVIDIA RTX PRO 6000 Blackwell，并扩展到 Jetson Thor 和 Jetson Orin。Cosmos 等物理 AI 模型写的是正在接到 Foundry Local。Windows 365 的 GPU Cloud PC 增加 Direct Stream，有限预览开放报名，公开预览计划在 2027 年初，帖子写最多两路 4K、60 帧。科学目录写 BioNeMo Agent Toolkit 和 ALCHEMI Toolkit 进入 Microsoft Discovery，起初接入与华盛顿大学合作的 RFD4-Proteina。微软 AI 自己用 NVIDIA Dynamo 做后训练里的强化学习采样推理。这些句子都没有单价。

同帖的 Azure Vera Rubin NVL72 另记。

猜测挂靠：云模型目录和本地部署渠道在 F。这是供应商的可买范围，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-20：新建，status=open。
