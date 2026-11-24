---
title: PolyAI Dialog-RSN-1 进入 SageMaker JumpStart 和 Marketplace
captured: 2026-11-20
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: AWS 机器学习博客
    url: https://aws.amazon.com/blogs/machine-learning/polyai-dialog-rsn-1-is-now-on-amazon-sagemaker-jumpstart/
    tier: 一手
  - name: PolyAI Dialog-RSN-1 介绍帖
    url: https://poly.ai/blog/polyai-dialog-rsn-1
    tier: 一手
---

## 是什么

AWS 机器学习博客在 2026-11-19 写，PolyAI 的 Dialog-RSN-1 当天可在 AWS Marketplace 和 Amazon SageMaker JumpStart 使用。这是进入 Marketplace 的第一款 PolyAI 模型。模型本身的介绍帖日期是 2026-07-30，不并进这一条。

PolyAI 2026-07-30 的介绍帖现在也写着可以在自己的 AWS 环境里用 SageMaker 跑，但没有写 Marketplace 或 JumpStart 的上架日。这一条只记 11 月 19 日这篇 AWS 公告里的渠道。

客户订阅后，把它部署成自己账号里的 SageMaker 端点，也可以从 SageMaker Studio 的 JumpStart 一键部署。端点在客户自己的 VPC 里，走客户的 IAM，用 CloudWatch 看日志和指标，费用出在客户的 AWS 账单上。编排、电话接入和业务逻辑仍归客户。端点说的是 OpenAI Realtime 协议，已有的 Realtime 客户端经 PolyAI 的桥改 base URL 即可连。输入音频是 16-bit PCM 单声道，16 或 24 kHz，G.711 或 Opus 要先转码。连接最长 30 分钟。模型目前只做英语。

JumpStart 给出四个优化档：时延、吞吐、成本和均衡。部署前展示 P50 时延、首 token 时间和吞吐，帖子没有写出这些数字，待核实。Marketplace 的订阅单价这次没有打开，待核实。

猜测挂靠：第三方语音模型的云上可买渠道在 F。这是供应商上架，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-20：新建，status=open。
