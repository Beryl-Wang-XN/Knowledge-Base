---
title: Claude Enterprise Frontier Safeguards 在三个平台进入 beta
captured: 2026-11-24
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Enterprise Frontier Safeguards 概述
    url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview
    tier: 一手
---

## 是什么

2026-11-09 的新闻室已经把 Enterprise Frontier Safeguards 写成进入私有 beta，那一句在 `2026-11-10-claude-fable-5-2` 里。这一条只记 2026-11-23 平台发布说明和概述页写出的范围。

发布说明写，EFS 在 Claude Platform、Claude Platform on AWS，以及 Claude Models on Google Cloud（Anthropic 托管）进入 beta。它把 EFS 说成符合条件、使用 Claude 最强模型的组织可用的 Zero Data Retention：Anthropic 不保留提示和响应；加密副本叫做 Sealed Safety Data，写到客户自己云账号里的存储桶。工作区若用 Anthropic 托管存储，就不算开了 EFS，因为那份 Sealed Safety Data 仍由 Anthropic 存着。

概述页写，EFS 仍是 beta，条款和行为在 beta 期间可能变。例子点了 Claude Fable 5.1。Sealed Safety Data 包含提示、响应和模型推理，即使用户自己的桶也读不了。Safety Cases 由客户自己的人审，Anthropic Human Review 始终关闭。Anthropic 不另收 EFS 的费用，也不改变模型行为、API 标价或速率限制。存储的读、写和出站流量由云厂商按原价计，概述页没有写单价。

EFS 覆盖已配置工作区里的全部 Messages API 请求，不论模型，也包括原本不要求保留数据的模型。不覆盖平台功能自己存的数据，即使发生在一次 Messages API 请求里：代码执行容器、Files API 上传、Batch API 结果，以及 Claude Managed Agents 会话。概述指向 FAQ 的 Data and retention，那一页这次没有打开。工作区一旦生效就整区适用；只想覆盖一部分流量，要用分开的工作区。在 Claude Platform 接受 EFS 和 Enterprise Data Controls 条款后两者都有：可以用客户自管密钥，或在 Anthropic 托管存储上关掉 Anthropic Human Review；两种做法都会为组织打开 Access Transparency。

同日发布说明还有 `external_storage.failed` 和 `external_storage.recovered`，另记一条，不并进这里。设置指南这次没有打开。

猜测挂靠：供应商的数据保留和商业条款在 F。这是友商的保留政策，并且写明不另收费、不改 API 标价，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不改已有的 Fable 5.2 条目。

## 处置记录

- 2026-11-24：新建，status=open。
