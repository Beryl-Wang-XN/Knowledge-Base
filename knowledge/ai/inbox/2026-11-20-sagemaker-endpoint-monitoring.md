---
title: SageMaker 默认监控生成式推理端点的时延和空闲 GPU
captured: 2026-11-20
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-monitors-endpoints/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-19 写，Amazon SageMaker AI 默认监控生成式推理端点的响应时间和 GPU 使用，并在响应变慢、GPU 大部分空闲，或配置落后时通知客户。客户可以跑 GenAI Inference Recommendations，用近期流量试能恢复响应时间或降低成本的配置，生产端点在客户采用结果之前不会被改。

公告写，监控看的是响应时间、GPU 容量使用和端点配置，不读客户的请求或响应。发现项包括变慢、未使用的 GPU 容量，以及配置缺口，例如更旧的服务容器、没有推测解码，或没有 GPU kernel 调优。变化持续了一周，或发现配置缺口时，每个端点在控制台收一条 AWS Health 通知。通知链到 SageMaker Studio 里的 Agentic Experience，端点和近期流量已经填好。推荐比较当前配置和备选，看响应时间、扛住的流量，以及每百万 token 成本。测试不碰生产端点。监控可以关掉。

监控不另收费。推荐任务按标准计算费用计。可用区域是美国东部（弗吉尼亚北部、俄亥俄）、美国西部（俄勒冈）、欧洲（爱尔兰、法兰克福）、亚太（新加坡、东京）。推荐任务的具体单价这次没有打开定价页，待核实。公告指向的博客这次没有打开。

猜测挂靠：推理端点的时延、利用率和配置检查在 D。这是云厂商的推理服务能力，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-20：新建，status=open。
