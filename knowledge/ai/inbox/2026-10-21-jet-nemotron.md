---
title: Jet 模型（暂按 Jet-Nemotron 记）
captured: 2026-10-21
from: followup
module: G
business: false
status: open
review_after:
entry:
sources:
  - name: Jet-Nemotron 论文
    url: https://arxiv.org/abs/2508.15884
    tier: 一手
  - name: NVIDIA Jet-Nemotron 仓库
    url: https://github.com/NVlabs/Jet-Nemotron
    tier: 一手
  - name: Hugging Face jet-ai/Jet-Nemotron-2B 与 4B
    url: https://huggingface.co/jet-ai
    tier: 一手
---

## 是什么

用户要求把「jet 模型」记入 inbox，留待回顾。按公开名称，先对应 NVIDIA 的 **Jet-Nemotron**（混合架构语言模型，仓库列出 2B 与 4B）。论文与仓库把它描述成：用 PostNAS 从预训练的全注意力模型改架构，并用 JetBlock 线性注意力，在保持准确率的同时提高生成吞吐。

具体吞吐倍数、对比模型和实验条件（上下文长度、batch）本次不抄进知识库，标 **待核实**。回顾时打开上面的论文和模型卡再决定是否入库。

若用户指的不是 Jet-Nemotron，而是投机解码方向的 JetSpec，回顾时改标题，不要并进同一条。

猜测挂靠：模型档案在 G；若回顾后确认它主要说明「线性注意力如何改变 Decode 成本」，再决定要不要另挂 B 或 E。

## 为什么没在当天处理

这是用户点名要先暂存的一条，不是当天的主轨知识点。当天不展开成第二课，也不写入 `registry/`。

## 处置记录

- 2026-10-21：按用户要求新建，`status: open`，等待 inbox 回顾。
