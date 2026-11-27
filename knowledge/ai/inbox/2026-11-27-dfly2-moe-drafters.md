---
title: 混元开源 DFly2 的三份 MoE 草稿权重
captured: 2026-11-27
from: intel
module: B
business: true
status: open
review_after:
entry:
sources:
  - name: Tencent AngelSpec
    url: https://github.com/Tencent/AngelSpec
    tier: 一手
  - name: Hy4-flash DFly2 模型卡
    url: https://huggingface.co/AngelSlim/Hy4-flash-DFly2-B6
    tier: 一手
  - name: DeepSeek-V4.1-Flash DFly2
    url: https://huggingface.co/AngelSlim/DS-V4.1-Flash-DFly2-B6
    tier: 一手
  - name: GLM-5.3-Flash DFly2
    url: https://huggingface.co/AngelSlim/GLM-5.3-Flash-DFly2-B6
    tier: 一手
---

## 是什么

腾讯混元 AngelSpec 仓库的最新消息写着 2026/11/26：完整开源 DFly2 的权重、训练代码和技术报告。报告链接是 arXiv 2611.34776。同一行写，除了 Hy4 和 Hy4 flash，DFly2 现在也能在 DeepSeek-V4.1-Flash 和 GLM-5.3-Flash 上训练，并放出三份新的 MoE 草稿模型。11 月 18 日和 11 月 20 日的消息分别是 Hy4 flash、Hy4 的训练支持，不并进这一条。仓库没有目录价。

三份权重建仓时间都在 2026-11-26，许可证标签都是 Apache-2.0。`AngelSlim/Hy4-flash-DFly2-B6` 的 `createdAt` 是 2026-11-26T04:46:16Z，safetensors 合计 3,119,838,752。`AngelSlim/DS-V4.1-Flash-DFly2-B6` 是 2026-11-26T04:58:03Z，合计 14,400,493,794，配置里的量化方式是 fp8。`AngelSlim/GLM-5.3-Flash-DFly2-B6` 是 2026-11-26T04:49:26Z，合计 10,339,281,506。

README 写 DFly2 是块并行草稿模型。每一层复用目标模型对应稀疏注意力层已经缓存的 KV，以及索引器已经选出的位置，自己不再维护 KV cache，也不做索引。每个草稿 token 最多关注大约 2K 个 key，开销不随上下文变长。它不参与 prefill；prefill 到 decode 只多传目标模型最后一层的 hidden state。Hy4 flash 模型卡写这份权重是 3 层 MoE，每层 128 个路由专家，块大小 6（1 个锚点 token 加 5 个草稿 token），精度 BF16，嵌入和 LM head 与目标模型共用、不在这个仓库里。卡上写 vLLM 投机解码的支持还在进行中。DeepSeek 和 GLM 那两份卡的层数这次没有打开，标 **待核实**。

加速比是相对目标模型自身解码，贪心、并发为 1，格子里是解码加速 / 端到端加速。README 的长上下文平均和智能体平均：DeepSeek-V4.1-Flash 为 2.87× / 2.11× 和 3.10× / 1.50×；GLM-5.3-Flash 为 2.45× / 1.64× 和 2.61× / 1.22×；Hy4 flash 为 3.06× / 2.12× 和 3.41× / 1.67×。Hy4 flash 卡上的一般任务平均接受长度是 3.96 / 3.95（温度 0 / 0.9），测在一张 TP8 的 H20 上。逐项对照表留在原文。

猜测挂靠：投机解码和 KV 复用在 B。这是供应商放出的草稿模型和推理加速，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-27：新建，status=open。
