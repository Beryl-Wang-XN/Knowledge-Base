---
title: NVIDIA CUDA 13.5 把 Vera Rubin 支持标为正式可用
captured: 2026-11-05
from: intel
module: C-compute
business: true
status: open
review_after:
entry:
sources:
  - name: NVIDIA CUDA 13.5 Brings NVIDIA Vera Rubin GA Support
    url: https://developer.nvidia.com/blog/nvidia-cuda-13-5-brings-nvidia-vera-rubin-ga-support/
    tier: 一手
---

## 是什么

NVIDIA 技术博客 2026-11-04 的帖：CUDA 13.5 正式可用。Vera Rubin 的支持从早期开发者访问变成正式可用。Windows on Arm 从 CUDA 13.4 起已是正式可用，13.5 把它扩到 NVIDIA DGX Station for Windows。同帖还写了用 locality domains 和 Multi-Process Service 更细地安排 GPU 上的工作。

关于 Windows 驱动，帖子写明：从 Rubin 架构起，CUDA 支持 WDDM 和 MCDM，其中 MCDM 是只做计算的驱动模型；Rubin 及之后的 GPU 不支持 TCC。假设 TCC 的应用和部署工具要改用 WDDM 或 MCDM。

cuBLAS 一节说 Vera Rubin 上的 NVFP4 与 MXFP8 matmul 做了启发式和 kernel 调整，覆盖 MoE 训练形状，但没有给出加速倍数。倍数标 **待核实**。页首有一段自动摘要，这条不采用那段，只采用正文。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不改 GPU 规格或并行策略条目。

## 处置记录

- 2026-11-05：新建，status=open。
