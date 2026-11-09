---
title: Amazon Bedrock 为 Kimi K3 增加印度境内推理
captured: 2026-11-04
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Introducing India-based inference for Kimi K3 on Amazon Bedrock
    url: https://aws.amazon.com/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/
    tier: 一手
---

## 是什么

AWS 机器学习博客于 2026-11-03 发布：除全球和美国推理外，Amazon Bedrock 现在支持 Kimi K3 的印度境内推理，面向要求数据留在境内的工作负载。博文给出的 cross-Region inference profile 是：

- 全球：`global.moonshotai.kimi-k3`，博文称为多数场景的推荐项，成本最低、可用范围最广
- 印度地理：`in.moonshotai.kimi-k3`，推理处理留在 Mumbai 与 Hyderabad

请求从 source Region 进入，由 Bedrock 在符合该 profile 的 destination Region 处理；博文写明传输中加密，且数据留在 AWS 网络内。示例把 source 设为 `ap-south-1`。博文同时说明可走 Chat Completions、Responses、Converse 和 InvokeModel。

两档 profile 的价差，这次没有打开 Bedrock 定价页核对，标 **待核实**。博文里的客户用量与降本比例是客户引言，不当成 AWS 的产品指标。

猜测挂靠：F（云厂商的区域推理供给）。若回顾后重点是数据驻留路由，再决定是否改挂 D。

## 为什么没在当天处理

这是定时情报拉取，留待用户回顾。当天不写成供应商条目。

## 处置记录

- 2026-11-04：新建，status=open。
