---
title: Lambda 托管实例支持 GPU，管理费 9.75%
captured: 2026-11-19
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-gpu-managed-instances/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-18 写，Lambda 托管实例上的 Event Functions 可以用 EC2 G 系列做 GPU 加速，工作负载包括 AI 推理、媒体处理、三维渲染、科学计算和金融模拟。同一个执行环境里可以并发多次调用，并按 GPU 利用率、CPU 利用率和并发来伸缩。事件源与其他 Event Functions 相同，帖子写是 200 多个。

基础镜像预装了 vLLM、SGLang 和 PyTorch。大工件可以用容器镜像，NVMe 临时存储最多 32 GB。启动可以用 Seekable OCI 懒加载，也可以直接从 Amazon S3 流式读取。容量提供者可以允许多代 G 系列；Lambda 先用满足要求的最新一代，容量不够再退回更老的一代。

可用范围是同时有 Lambda 托管实例和 EC2 G 系列的全部 AWS 商业区域。配置方式包括控制台、CLI、SDK、CloudFormation、CDK 和 SAM，也可以给 Kiro、Claude Code 或 Codex 装上 Agent Toolkit for AWS 里的 Lambda Managed Instances skill。

价格写在这篇公告里：实例按 EC2 按需价（Savings Plans 和 Reserved Instances 适用），另加 9.75% 的 Lambda 管理费，以及每百万次请求 $0.20。Lambda 定价页这次没有打开，按需单价待核实。

猜测挂靠：推理服务的托管和计费在 D。这是供应商和价格变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-19：新建，status=open。
