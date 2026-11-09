---
title: Google Cloud 上线 Anthropic 托管的 Claude 部署选项
captured: 2026-10-24
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Google Cloud 博客
    url: https://cloud.google.com/blog/products/ai-machine-learning/expanding-claude-availability-on-google-cloud
    tier: 一手
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
---

## 是什么

Google Cloud 博客日期为 2026-10-23，宣布 Claude 在 Google Cloud 上的 Anthropic 托管部署一般可用，与原来的 Google 托管选项并存。Anthropic 的 Platform 发布说明把同一项上线写在 2026-10-22，比这次拉取窗口早一天。10 月 23 日这篇是 Google 的正式说明；inbox 里还没有这条，因此记在这里，回顾时不要把它和 22 日的发布说明当成两件事。

两边都写：两种部署都是模型首日可用、同一套价格、走 Google Cloud 账单。差别是谁做数据处理器，以及新的平台功能何时可用。

- Anthropic 托管：Anthropic 在 Google Cloud 基础设施上运营，按 Anthropic 商业条款做数据处理器。身份用 Google Cloud IAM，保留 Cloud Audit Logging，花费计入现有 Google Cloud 账单和符合条件的承诺消费。Claude Managed Agents（beta）、skills、代码执行等一方功能首日可用。
- Google 托管：Google Cloud 按现有客户协议做数据处理器，提供 VPC Service Controls、客户管理加密密钥，以及美国、欧盟、亚太数据驻留。新的 Claude 平台功能要等接入 Google 托管基础设施之后才有。可接 BigQuery 和 Model Armor。

博客点名当前可访问的模型包括 Claude Fable 5.1、Sonnet 5.5、Haiku 5.5、Opus 5.5。发布说明另写：Opus 5.5 的 Fast mode 已在 Anthropic 托管选项上可用。Fast mode 的速度倍数和标价不在 10 月 23 日这篇 Google 博客里，待核实。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成供应商条目。

## 处置记录

- 2026-10-24：新建，status=open。
