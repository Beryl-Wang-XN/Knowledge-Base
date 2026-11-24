---
title: Microsoft Ignite 更新 Foundry 模型目录、路由和托管计算
captured: 2026-11-18
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Microsoft Foundry 博客
    url: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/from-model-choice-to-your-durable-advantage-build-ai-that-keeps-improving/4573609
    tier: 一手
---

## 是什么

Microsoft Foundry 博客写于 2026-11-17，页末更新时间也是当天。这是 Ignite 上的一篇目录和平台公告。MAI-Code-2 与 Flash 另记，这里不重复订阅范围。帖子没有给出下面这些型号的 token 单价，标 **待核实**。

当天写进目录或状态有变化的：

- Microsoft-Decision-1.1 一般可用。博客写它基于 Gemma，用于路由、分类、优先级和校验，并支持图像输入。
- MAI-Image-2.7 与 MAI-Image-2.7-Flash 在 Foundry 公开预览。模型预览本身已在 2026-10-28 的条目里，这一行只记 Foundry 目录。
- 经 fal 合作进入 Foundry Models 的视频模型：Kling v3 Pro、MiniMax H3 Max、MiniMax H3 Max Turbo、LTX-2.5 Pro、LTX-2.5 Fast。
- MAI-Cyber-2-Flash 写成将通过 Codename MDASH 提供，帖子没有写已经一般可用。
- Meta 的 Muse Wonder、Muse Spark 1.3、Muse Ember 写成即将进入 Foundry，还不是当天可调用。

模型路由：支持的 Foundry 项目里，自动选模型默认打开，不必先部署路由器。路由器现在从 OpenAI、Anthropic、xAI、DeepSeek、Meta 等共 44 个模型里选。AI Gateway 客户也可以打开这个路由器。

Baseten on Microsoft Foundry 公开预览，作为微软第一方服务提供 Baseten 优化过的开源权重，点名 Kimi-K3、GLM 5.3、GLM-5.3-Flash、DeepSeek V4.1-Flash-1017。可以按量无服务器调用，范围是全球或美国 Data Zone；预留吞吐从 12 月开始。Fireworks 在 Foundry 上已经一般可用，这一句是对照，不是新发布。

训练：Managed Training 是原先的 managed fine-tuning。Programmed Training 公开预览，用 Python 写采样、评分和权重更新，Foundry 在无服务器 GPU 上跑。示例食谱里的开源权重包括 `gpt-oss-120b` 和 Qwen3.8-27B。

Managed Compute 一般可用，按小时 GPU 费率计费，并有 Data Zone。小时单价这次没有在帖子里看到，标 **待核实**。

猜测挂靠：云模型目录、路由和托管供给在 F。这是供应商的可买范围，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-18：新建，status=open。
