---
title: 自托管 Claude Managed Agents 上线，整套服务可放到客户自己的环境
captured: 2026-11-13
from: intel
module: D
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Claude 产品更新
    url: https://claude.com/resources/product-updates
    tier: 一手
  - name: 自托管与托管服务的差异
    url: https://platform.claude.com/docs/en/managed-agents/self-hosted/differences
    tier: 一手
---

## 是什么

2026-11-12，Claude Platform 发布说明写下了 self-hosted Claude Managed Agents。客户运行的是整套 Managed Agents 服务，不只是以前的自托管沙箱。智能体、会话和会话历史存在客户自己的基础设施上。服务器把模型请求送到客户选择的提供方，默认是 Anthropic。要下载和接入，需要联系 Anthropic 客户团队。产品更新页同一天把这件事写成：可以在自己的云或本地运行，由客户托管智能体、凭证和会话历史，并选择请求发到哪里。

差异页已打开。自托管服务器的 API 与 Anthropic 托管服务相同，除了该页列出的差别。托管服务上的内容不会复制过来，包括会话历史；智能体、skills、保险库凭证和记忆库要在自己的服务器上重建。

只在自托管服务器上有的能力：选择推理提供方、用 OpenID Connect 做单点登录、把新凭证的秘密放到客户自己的秘密管理器、以及给智能体签发短时令牌去调 MCP。文档里 `inference.provider` 出现的取值包括 `anthropic`、`vertex`、`foundry` 和 `gateway`。Bedrock 是否在这一页的提供方列表里，这次没有对上单独一行，待核实。

不可用的包括：云环境（请求会返回 400）、Messages API 和 Models API（SDK 打到这台服务器会 404）、Files API、`mcp_oauth` 凭证、预置的 `docx` / `pdf` / `pptx` / `xlsx` skills、定时部署和 dreams、以及 webhooks。多智能体只接受 `type` 为 `coordinator`、并列出 1 到 20 个智能体的配置；动态工作流、advisor，以及由智能体自己定义的子智能体都不可用。`web_search` 和 `web_fetch` 默认关闭，要在服务器设置里打开。已有的自托管沙箱 worker 可以连到这台新服务器；靠 webhook 拉起的 worker 不会启动，因为服务器不发 webhook。

按提供方，fast mode 的默认模型目录也不一样。默认列出 Claude Opus 5.5、Opus 5、Opus 4.8 和 Opus 4.6。`foundry` 只列出 Opus 5.5。`vertex`，以及 `gateway` 且格式为 `vertex-raw-predict` 时，目录里没有模型。`inference.provider` 为 `anthropic` 时，服务器默认打开 Claude API 的服务端回退：安全分类器拒绝后，可能改由另一个 Claude 模型回答，读会话才能看到那个模型 ID；设 `inference.model_fallback: false` 可以关掉。

这次没有打开标价页。自托管本身有没有单独的平台费，待核实。

猜测挂靠：服务跑在谁的环境里，是 D。客户可选推理提供方，是对标友商和供应商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成调度或服务条目。

## 处置记录

- 2026-11-13：新建，status=open。
