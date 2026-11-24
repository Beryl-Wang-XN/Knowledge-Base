---
title: Google 宣布 TPU 8tx 与 TPU 8i Max
captured: 2026-11-10
from: intel
module: C-compute
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Our newest TPUs: 8tx and 8i Max
    url: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/
    tier: 一手
---

## 是什么

2026-11-09，Google 博客宣布第八代 TPU 再增加两套系统：TPU 8tx 和 TPU 8i Max。帖子写，这是同一年里第四套新 TPU 系统，与今年 4 月的 TPU 8t、TPU 8i 放在一起。帖子没有给出这两套新系统的售价，也没有写一般可用日期。

TPU 8tx 面向机密推理，也可做小规模训练。博客写它用的是和 TPU 8t 相同的芯片，搭配第五代 AMD EPYC 主机，并把安全做进硬件层，使数据和模型权重在使用中仍然隔离。它采用为实时推理做的低延迟 Boardfly 网络，相对 TPU 8t 延迟最多低 2 倍，性能损失接近于零。

TPU 8i Max 把两颗低延迟的 TPU 8i 放在同一个封装上。博客写，算力、SRAM 和 HBM 带宽都是 TPU 8i 的两倍，并在现有机柜占地里放进两倍的芯片，用来扛更大的上下文和更高的机柜算力密度。

同一篇还写了配套软件，不另开条目。TPU Sync 开源，把片上 HBM、主机 DRAM、共享存储和数据中心网络做成一层模型状态，并写可以把 KV 传输延迟和 TTFT 降低 90% 以上。Cloud Pathways 在 GKE 上一般可用。GKE dynamic slicing 一般可用，博客写任务启动最多快 5 倍、故障恢复最多快 4.5 倍。TorchTPU 写成上个月已经开源。Agent Compute Engine 的暂停和恢复已在 2026-10-23 的 inbox 里记过，这里不另记。

帖子回顾 4 月的 TPU 8t、8i 时，写相对上一代训练性能最多 2.7 倍、推理性价比好 80%。这是对已有系统的描述，不是这两套新系统的指标。

猜测挂靠：算力层在 C-compute。新的加速器系统是供应商变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-10：新建，status=open。
