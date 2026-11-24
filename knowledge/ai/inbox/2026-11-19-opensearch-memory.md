---
title: Amazon OpenSearch Memory 一般可用
captured: 2026-11-19
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: AWS What's New
    url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/
    tier: 一手
---

## 是什么

AWS What's New 在 2026-11-18 写，Amazon OpenSearch Memory 一般可用。它是 Amazon OpenSearch Service 里的无服务器能力，给 AI 智能体加持久记忆：把交互存成可搜索的原始事件，异步抽出结构化记忆，再跨会话检索，这样不必把整段历史重新送给模型。生命周期包括抽取、嵌入、索引、合并（新增、更新或跳过）和检索，检索有关键词、语义和混合。每个记忆库用 IAM 控制，可按 actor 和 session 限定，事件和记忆可以设过期。不用自建集群或索引，抽取和搜索的容量自动伸缩。

区域：美国东部（弗吉尼亚北部、俄亥俄）、美国西部（俄勒冈）、欧洲（法兰克福）、亚太（东京）。定价页这次没有打开，单价待核实。

猜测挂靠：智能体记忆的托管服务在 D。这是供应商新产品，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-19：新建，status=open。
