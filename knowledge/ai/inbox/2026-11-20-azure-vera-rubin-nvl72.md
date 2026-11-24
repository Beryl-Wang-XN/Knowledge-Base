---
title: NVIDIA 写 Azure 正在运行 Vera Rubin NVL72 预览
captured: 2026-11-20
from: intel
module: C-compute
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

NVIDIA 博客在 2026-11-19 写，微软 Ignite 上两家把合作扩到 Azure 上的基础设施、工业系统和 Windows PC。Azure 数据中心里已经在跑 NVIDIA Vera Rubin NVL72，面向高要求的推理、智能体应用，以及大规模训练和推理。帖子把 Azure 上的这一档称为 Vera Rubin preview。实例名、显存、区域和售价都没有写，待核实。2026-11-16 那条 Rubin HPC 是另一款、预计 2028 年的 GPU，不并进去。

同一节写，两家在把机密计算扩到裸金属和机架级 AI 基础设施，用机密计算和证明在释放模型、数据或密钥之前核对环境。这句写的是正在合作扩展，不是已经一般可用。另外写正在用 NVIDIA MaxLPS 合作做能效，没有给出节电比例。

帖子用已有的 Blackwell 成绩作对照，不是 Rubin 的新测速：MLPerf Training v6.1 里，Azure 用 GB200 NVL72 在 DeepSeek-V3 上扩到 10,240 张 NVIDIA GPU，是该轮最大规模；MLPerf Inference v6.1 里，Azure 的 GB300 NVL72 在 DeepSeek-R1 交互吞吐的云提交中领先超过 10%，出处写的是 Signal65。

同帖的 Foundry 模型目录和本地部署另记。

猜测挂靠：云上的新 GPU 机架在 C。这是算力供应商的可买范围，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-20：新建，status=open。
