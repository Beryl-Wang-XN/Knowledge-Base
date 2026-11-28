---
title: Neptune Graph Sessions 给智能体单独开图并可缩到零
captured: 2026-11-28
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-neptune-graph-sessions-generally-available/
    tier: 一手
  - name: Amazon Neptune 定价
    url: https://aws.amazon.com/neptune/pricing/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-27 写，Amazon Neptune 增加 Neptune Graph Sessions。这是给智能体用的一种计算模式：内存和 CPU 自动伸缩，空闲后缩到零。每个智能体、用户或任务可以有自己的图，不必再按预置图最低 16 m-NCU 付费。创建时可选 4 s-NCU 或 8 s-NCU 作为起始工作内存。s-NCU 是 sessions Neptune capacity units。

图从所选大小起步，加载数据和跑查询时内存余量最多到这个大小的两倍：4 s-NCU 最多到 8，8 s-NCU 最多到 16。按图实际占用的内存计费，能放进较小一档就按较小一档计。空闲 15 分钟后自动缩到零，下一次查询在数秒内恢复。图和数据保留，不用为每次会话重新加载，缩到零期间不付运行中的价格。可用控制台、CLI 或 SDK 创建，并用 openCypher 查询，和其它 Neptune Analytics 图一样。文中点名的场景是 GraphRAG 助手、AI 智能体和按用户拆开的分析。

定价页写，Graph Sessions 在隔离的 Lambda MicroVM 里跑 Neptune Analytics 引擎。每个 s-NCU 是 1 GB 内存和 0.25 vCPU。图在运行时按秒计计算费；停掉之后不算计算费，只算存储。页面上的 s-NCU 小时单价和存储的 GB-月单价由前端再加载，这次没有拿到数字，标 **待核实**。What's New 没有写开放区域，区域 **待核实**。

猜测挂靠：按会话伸缩的图服务在 D。这是供应商的新产品和计费方式，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-28：新建，status=open。
