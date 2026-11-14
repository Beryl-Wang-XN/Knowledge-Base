---
title: ChatGPT Wallet 开始向美国 Pro 用户铺开，代理付款不接触真实卡号
captured: 2026-11-14
from: intel
module: F
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI 新闻室 Introducing ChatGPT Wallet
    url: https://openai.com/index/introducing-chatgpt-wallet/
    tier: 一手
---

## 是什么

2026-11-13，OpenAI 新闻室写下了 ChatGPT Wallet。用户先存入一张卡，每次购买前核对商品、总额和所选卡，再用 Face ID 或指纹这类安全检查批准。批准之后，支付网络给出一张支付令牌，带卡号、安全码和有效期，扣在所选卡上。新闻室写，ChatGPT Wallet 和代理都拿不到用户的真实卡信息。已有的卡奖励，以及符合条件的争议保护，仍然留在原来的卡上。

合作方写的是 American Express、Mastercard 和 Visa。先在 dots 里铺开，让用户的 dot 代为完成购买。首批是美国、年满 18 岁、持有符合条件的美国发行卡片的 ChatGPT Pro 订阅用户。新闻室没有写钱包本身的手续费或 token 标价。

同一篇还写了给商家的做法：在 ChatGPT 认领商家并上传带价格和库存的商品信息；用 Web Bot Auth 让 CDN 或防火墙认出签过名的请求，避免误拦；浏览器访问不需要插件或商品信息流。支付令牌走现有结账，但风控系统仍可能把代理发起的合法购买标成异常。文中点名正在合作的反欺诈方有 Forter、Riskified、Sardine、Signifyd，支付服务商有 Adyen、Checkout.com、Stripe。网站还可以做插件，或加上 WebMCP 工具。Commerce Partner Playbook 这次没有打开。

文中把「按消费上限、品类或时段预先批准、再完全交给代理」写成以后的预期，不是这次已经开放的能力。

猜测挂靠：这是友商的代理商务产品，在 F。合作方和购买资格是供应商与商业口径，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成竞品条目。

## 处置记录

- 2026-11-14：新建，status=open。
