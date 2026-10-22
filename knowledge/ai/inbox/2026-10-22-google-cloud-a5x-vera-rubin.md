---
title: Google Cloud A5X（Vera Rubin）计划下月一般可用，并声称支持超出 HBM 的 KV Cache
captured: 2026-10-22
from: intel
module: C-compute
business: true
status: open
review_after:
entry:
sources:
  - name: Google Cloud Blog《Google Cloud infrastructure at NVIDIA GTC Berlin 2026》
    url: https://cloud.google.com/blog/topics/ai-infrastructure/google-cloud-infrastructure-at-nvidia-gtc-berlin-2026
    tier: 一手
  - name: NVIDIA Blog《Google Cloud and NVIDIA Announce General Availability of NVIDIA Vera Rubin Infrastructure》
    url: https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/
    tier: 一手
---

## 是什么

2026-10-21，Google Cloud 与 NVIDIA 在 GTC Berlin 宣布基于 NVIDIA Vera Rubin NVL72 的裸金属实例 A5X。两边都写：一般可用在下个月，不是当天已全量开放。Google 同时写明会把可用范围扩到新的本地区域，以支持 EMEA 的数据驻留和主权要求。NVIDIA 的表述是计划把可用范围扩到欧洲。具体区域和下月中的哪一天标 **待核实**。

同一篇 Google 公告里、和推理成本直接相关的说法（均为厂商自述，本次不另做基准核对）：

- Virgo Network 用无阻塞的楼内/楼间 mesh 做横向扩展。单站点集群可扩到 80,000 张 Rubin GPU，跨站点最多 960,000 张。NVIDIA 博文写 Google Cloud 计划把 Vera Rubin 基础设施扩到最多 960,000 张 Rubin GPU。
- A5X 将支持把上下文记忆扩到 GPU HBM 之外的 KV caching：高速缓存层把上下文卸载到多层存储并复用，用来减少重复计算、降低 TTFT、提高每美元的 inference goodput。缓存介质、命中率和实测倍数标 **待核实**。
- A5X 上的 Managed Lustre 将支持 NVIDIA GPUDirect Storage，训练和推理数据可经 RDMA 从并行文件系统进 GPU 显存。
- 实例组合写明还包括 NVIDIA ConnectX-9 SuperNICs，以及 Google Cloud 第四代液冷。单机规格（GPU 数、显存、价格）标 **待核实**。

同日同文还宣布了相邻的供给变化，回顾时不要和 A5X 一般可用混成一件事：Google Distributed Cloud 上的 NVIDIA HGX B300 一般可用；机密计算方面，带 NVIDIA RTX PRO 6000 Blackwell Server Edition 的 G4 机密实例一般可用，HGX B200 的 A4 当天已提供机密计算，并介绍基于 GB300 NVL72 的 A4X Max 机密裸金属。这些实例的区域和价格标 **待核实**。

猜测挂靠：C（新的云上 GPU 平台与供给）。KV Cache 卸载若回顾后要单独讲成本，再决定是否另挂 B 或 E。算力供应商变化，`business: true`。

## 为什么没在当天处理

这是 2026-10-22 的定时情报拉取，不是当天主轨。留待用户回顾，不写入算力规格或推理条目。

## 处置记录

- 2026-10-22：新建，status=open。
