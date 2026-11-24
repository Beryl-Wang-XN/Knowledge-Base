---
title: AppConfig 可以单独发布 AI 模型调用配置和提示词
captured: 2026-11-20
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-appconfig-native-ai-model-invocation-prompt-configurations/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-19 写，AWS AppConfig 增加两种配置档案：AI 模型调用配置，和 AI 提示词配置。应用运行中可以改模型设置和提示词，不必重新部署代码，并沿用渐进发布和自动回滚。

模型调用配置存放调用模型时用的设置，包括模型标识、temperature、最大 token 等推理参数，以及系统提示和示例对话。供应商专有选项放在自定义参数里，同一套 schema 跨供应商。提示词配置把提示词做成单独有版本的产物，可以只改提示词、不改模型配置，并在多个应用里复用。

发布可以按流量比例递进，公告举例是 10%、20%、30%。过程中可以看运营指标、客户体验和 token 用量。CloudWatch、Datadog、New Relic 或其他可观测告警在发布中触发时，可以自动回到上一版。

两种配置在提供 AppConfig 的全部区域可用，不另收费。用户指南这次没有打开，档案字段的完整列表待核实。

猜测挂靠：运行中切换模型参数和提示词的发布方式在 D。这是云厂商给生成式应用加的配置能力，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-20：新建，status=open。
