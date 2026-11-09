---
title: OpenAI 与 Google 将支持 robots.txt 共用的 AI 训练偏好信号
captured: 2026-10-31
from: intel
module: F-landscape
business: false
status: open
review_after:
entry:
sources:
  - name: OpenAI：Making it easier for websites to express AI training preferences
    url: https://openai.com/index/helping-websites-express-ai-training-preferences
    tier: 一手
  - name: Google Search Central：Supporting a shared AI training control for websites
    url: https://developers.google.com/search/blog/2026/10/ai-training-control
    tier: 一手
  - name: IETF 个人草案 draft-kelley-aipref-training-preference-signal-00
    url: https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/
    tier: 一手
---

## 是什么

2026-10-30，OpenAI 与 Google 分别宣布将支持 robots.txt 里的一套共用信号，让网站用一次声明，向多家 AI 提供商表达内容能否用于基础生成式模型训练。两边都把它接在 IETF AI Preferences（AIPREF）工作组正在做的事情上，并写明不取代各自已经在用的爬虫控制。

OpenAI 新闻室：将尊重这个共用信号，打算在未来几个月内实现，实现细节另发；现有 robots.txt 控制继续有效。该帖没有写出 token 字符串，也没有列出同日宣布的全部参与方。

Google Search Central 同日：网站可以用 robots.txt 里的共享 policy token 表达训练偏好。若站点用该 token 选择退出训练，且没有单独写明 Google-Extended，Google 计划把它理解为禁止 Google-Extended。按公司区分的既有控制继续有效。明确允许 Google-Extended 的网站，仍可出现在 Gemini 应用的 grounding 回复里并获得点击。Google 写的目标是与其他 AI 提供商一起，在 2027 年支持这套控制。

同日的 IETF 个人草案 `draft-kelley-aipref-training-preference-signal-00`（日期 2026-10-30，作者栏署名为 Anthropic 的 Kevin Kelley）用例子说明 policy token：`User-Agent: __usage_ai-training`。草案页写明这是个人 Internet-Draft，未经 IETF 背书。Anthropic 新闻室当天没有对应的产品或承诺帖，不能把草案作者单位写成 Anthropic 已经宣布采用。

除上述两家原文里的实现口径外，还有哪些厂商已经上线，标 **待核实**。

猜测挂靠：F（模型厂商对网页训练数据偏好的口径）。不是价格或供应商上架，`business: false`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成竞品或数据条款条目。

## 处置记录

- 2026-10-31：新建，status=open。
