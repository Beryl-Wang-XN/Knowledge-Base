---
title: Mistral 与 NVIDIA 合作做工程仿真与智能体评测，并重申 Large 4 与算力路线
captured: 2026-10-22
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Mistral《Mistral Advances AI for Engineering with NVIDIA》
    url: https://mistral.ai/news/mistral-nvidia-ai-for-industrial-engineering/
    tier: 一手
---

## 是什么

2026-10-21，Mistral 宣布与 NVIDIA 做面向工业工程的合作。新的部分是：用 Mistral Large 4、Mistral 的数据生成和物理建模流水线，加上 NVIDIA CUDA-X、Warp 和 Omniverse，把仿真、模型开发和工程设计连成闭环；并准备公开的物理模型基准和开放数据集，以及面向 CAE、EDA 的智能体评测。评测要看智能体能否使用工程工具、走完多步流程、给出技术上正确的结果，同时测量执行时间和计算成本。基准本身尚未在这篇公告里发布。

同一篇把已有合作又说了一遍，避免和「当天新发布一个模型」混在一起：

- Mistral Large 4（公开预览，又称 Le Chonk）被描述为约 1 万亿总参数、490 亿激活参数的多模态模型，在欧洲由 Mistral 运营的数据中心里用 3,800 张 NVIDIA Grace Blackwell GPU 训练。权重计划在 10 月底发布。这些数字是本篇转述，模型卡和训练细节标 **待核实**。
- 双方此前合作过 Mistral NeMo，并在 NVIDIA Nemotron Coalition 里做开源权重的前沿基座模型。
- Mistral 称正在按 2030 年 1 GW 算力路线图上线更多 NVIDIA 基础设施。这是路线图目标，不是当期可采购容量。

猜测挂靠：F（模型厂商和算力供应商的绑定，以及开源权重发布时间）。算力规模和激活参数若回顾后要进档案，再挂 G 或 C。对标供应商，`business: true`。

## 为什么没在当天处理

这是 2026-10-22 的定时情报拉取，不是当天主轨。留待用户回顾，不写入模型档案或供应商条目。

## 处置记录

- 2026-10-22：新建，status=open。
