---
title: SageMaker AI 跨区域推理路由不加价
captured: 2026-11-19
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-cross-region-routing/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-18 写，Amazon SageMaker AI 支持跨区域推理路由。一个区域容量不足或端点不健康时，可以把请求送到其他 AWS 区域和其他账号里已经部署的端点。开发者建一个 inference router，登记已有的实时端点、异步端点和 inference components，应用改指这个路由器。路由器优先本区域；错误升高时把新请求转到其他区域的健康目的地，本地恢复后再逐步把流量转回来。已有端点、模型和容器不用改。

端点拥有者用端点策略决定其他账号的哪些路由器可以用这个端点，还可以设跨区域流量上限，给本地调用方留容量。实时响应会标出实际服务的端点和原因。CloudWatch 里有路由器指标。实时推理覆盖 32 个商业区域，异步推理覆盖 25 个区域。

公告写，跨区域推理路由没有额外费用。端点仍按 SageMaker AI 标准价，路由器指标按 CloudWatch 标准价。跨区域数据传输出方向的费用这次没有在公告里看到，待核实。

猜测挂靠：推理请求的跨区域路由在 D。这是供应商路由能力，并写明路由器本身不加价，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-19：新建，status=open。
