---
title: Anthropic 开放 Claude Duet 研究预览，后台检查计入同一套用量
captured: 2026-10-22
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Anthropic《Introducing Claude Duet》
    url: https://claude.com/resources/articles/claude-duet
    tier: 一手
  - name: Anthropic 产品公告列表（2026-10-21）
    url: https://claude.com/resources/product-announcements
    tier: 一手
---

## 是什么

2026-10-21，Anthropic 开放 Claude Duet 的研究预览，需加入候补。起始范围是美国的 Pro 和 Max 订阅用户。它是独立应用，有 iOS、Android 和 claude.ai，当前不在主 Claude 应用里。官方写明围绕 Claude Opus 5.5 设计。

和用量、产品边界相关的原文：

- 研究预览期间包含在 Pro 和 Max 里，与 Claude 其余功能共享同一套用量上限。后台检查会计入这些上限；做财务模型或演示文稿这类大任务会消耗更多模型轮次和后台工作。官方说它每隔几小时检查已连接账号，因为不停检查会更快用完套餐额度。具体扣费单价标 **待核实**。
- 它带一台有浏览器的虚拟机，不要求用户的电脑或手机保持开机。发送消息、付款、签署、删除之前要展示动作并等待批准。即使批准，也不能交易证券，也不能在账户之间转账。
- 凭证处理沿用 Claude Managed Agents 的设计，官方称它不会直接看到密码或登录令牌。可用 Claude Marketplace 里的连接器。用 Link 或 Shop Pay 付款时，要用户再批准一次花费。

猜测挂靠：F（模型厂商把订阅用量用在常驻智能体上，而不只是对话 API）。若回顾后确认要拆用量如何折算成 token，再挂 E。对标友商的产品形态，`business: true`。

## 为什么没在当天处理

这是 2026-10-22 的定时情报拉取，不是当天主轨。留待用户回顾，不写入竞品或计费条目。

## 处置记录

- 2026-10-22：新建，status=open。
