---
title: Bedrock Web Search 增加五种语言和可选国家
captured: 2026-11-22
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/web-search-amazon-bedrock/
    tier: 一手
---

## 是什么

AWS What's New 的发布日是 2026-11-21。Amazon Bedrock 上的 Web Search 在 Amazon Bedrock AgentCore 和 Amazon Bedrock 上新增五种语言，外加非美国英语：西班牙语、法语、德语、意大利语、日语。使用这些语言的智能体会得到更多本地语言来源。

另外新增可选的 country 字段。传入 ISO 3166-1 alpha-2 国家代码，例如 “JP” 或 “DE”，把结果偏向该国来源。What's New 举的用途是多国用户、答案取决于所在地的问题，以及区域来源。

AgentCore 上写明的区域是 US East (N. Virginia)、US East (Ohio)、US West (Oregon)、Asia Pacific (Sydney)、Asia Pacific (Tokyo)、Europe (Ireland)。Bedrock 上的 Web Search 写的是 US Regions。查询在调用的区域里处理。已有客户不用改代码就会得到新语言。原文写各语言价格相同，没有写出单价，定价页这次没有打开。

猜测挂靠：智能体检索工具的接入在 D。这是云厂商能力，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-22：新建，status=open。
