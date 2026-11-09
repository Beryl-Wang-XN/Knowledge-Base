---
title: GitHub Copilot Fusion 一般可用，并预览本地模型路由
captured: 2026-10-29
from: intel
module: D-serving
business: true
status: open
review_after:
entry:
sources:
  - name: GitHub Changelog：Route and orchestrate models with GitHub Copilot Fusion
    url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/
    tier: 一手
  - name: GitHub Changelog：Copilot Fusion local models
    url: https://github.blog/changelog/2026-10-28-github-copilot-fusion-now-supports-selection-of-local-models/
    tier: 一手
  - name: Artificial Analysis changelog（2026-10-28）
    url: https://artificialanalysis.ai/changelog
    tier: 工具站
---

## 是什么

2026-10-28，GitHub 宣布 **Copilot Fusion** 一般可用。选中它并不是选定某一个模型，而是让 Copilot 按任务路由、编排模型。用户选努力档：Standard（日常编码）、High（更难的任务）、Max（要求最高的任务）。编排方式包括：单模型直接做完（Single）；较省的模型先起草，质检不通过再升级（Cascade）；一个模型起草、另一个评审、原模型再改（Critique）。

管理员只能让 Fusion 使用企业和组织策略里已启用的模型，也可以单独关掉某个模型在 Fusion 中的使用，而不影响其他人直接选用。企业托管设置里可以把任一努力档设为默认。研究预览里的 auto、HydraFusion、HydraFusion Max 会自动对应到 Fusion 的努力档。

计费：按它实际调用的每个模型的标准价计。付费 Copilot 方案在限时内使用 Fusion 有 **30%** 折扣。折扣截止日原文没写。客户端：全部 Copilot 方案，覆盖 VS Code、GitHub Copilot app、Copilot CLI、JetBrains；其他客户端未写日期。

GitHub 引用 Artificial Analysis Coding Agent Index：Fusion Max **60** 分，与 Claude Code + Opus 5.5 Max 相差在 2 分以内；平均每次任务的 API 成本约一半，token 约一半，时间约少 **40%**。对比任务的具体构成标 **待核实**（本次只打开了 GitHub 这篇 changelog 和 Artificial Analysis 当日 changelog，没有打开该指数的方法页）。Artificial Analysis 当日 changelog 另写：Fusion 在 Anthropic 与 OpenAI 模型之间编排，Coding Agent Index 上比 Claude Code 里的 Opus 5.5 低 2 分，每次任务成本约一半。GitHub 正文只写「策略中启用的模型」，没有点名供应商。

同日第二篇 changelog：本地模型的智能路由进入实验预览。Fusion 可在支持的端侧模型与云端模型之间选择，覆盖 Copilot CLI、Copilot app 和 VS Code。Windows 上可通过 Windows ML 托管下载 **MAI Code 1.1 Flash**；选 Fusion Standard 后由 Copilot 在本地与云端之间选。CLI 也可在 Windows、macOS、Linux 上，用本地 OpenAI 兼容服务自行配置 MAI Code 1.1 Flash 或 **Qwen3.8 Flash Next**。Copilot app 的智能路由目前只覆盖托管的 Windows ML 模型。路由决定仍在云端做出，本地推理不等于离线会话。更早的本地模型说明日期是 2026-10-07，不是这次新发布的模型。

猜测挂靠：D（路由）。折扣和按模型计费也碰到 E。对标编程助手的模型路由与价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成调度或计费条目。

## 处置记录

- 2026-10-29：新建，status=open。
