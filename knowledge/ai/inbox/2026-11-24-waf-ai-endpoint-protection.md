---
title: AWS WAF 用 Bedrock Guardrails 发现并保护 LLM、MCP 和 A2A 端点
captured: 2026-11-24
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/waf-ai-endpoint-discovery-protection/
    tier: 一手
---

## 是什么

AWS What's New 的发布日是 Nov 23, 2026。自动发现并保护 AI 端点一般可用：在 Amazon API Gateway、Application Load Balancer 和 Amazon CloudFront 后面，跨 AWS Organization 找出语言模型、Model Context Protocol 和 Agent2Agent 端点，再用 AWS WAF 保护。

发现走新的 API Gateway API Portal，从流量日志和服务配置里认出 AI 端点，不用部署代理，也不用转发日志。没有写进文档、又暴露在公网的 MCP 服务器会显示成影子 API。未保护的端点可以打开 WAF。

保护走新的 AWS WAF AI Security 托管规则组。WAF 做协议识别和合规检查，拦住格式不对的 MCP 和 A2A 消息。打开内容检查后，规则组调用 Amazon Bedrock Guardrails 的 InvokeGuardrailsCheck API，检查请求里的提示注入、越狱和有害内容，以及响应里的敏感信息。可以和别的 AWS 托管规则或自定义规则一起用。

What's New 写另有附加费，内容检查的调用由 Amazon Bedrock 另行计费。没有写单价。API Portal 可用区域写了 32 个，清单指向 Amazon API Gateway FAQ，这次没有打开。AI Security 写出的区域是美国东部（弗吉尼亚北部）、美国东部（俄亥俄）、美国西部（俄勒冈）、欧洲（伦敦）、欧洲（斯德哥尔摩）、亚太（东京）和亚太（悉尼）。

猜测挂靠：请求路径上的防护和计费在 D。这是供应商的新产品和附加费，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-24：新建，status=open。
