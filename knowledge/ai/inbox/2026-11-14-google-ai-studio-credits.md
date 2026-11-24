---
title: Google AI Studio 里可以直接领取开发者计划的 Cloud 额度
captured: 2026-11-14
from: intel
module: E
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Claim your Google Cloud Credits in Google AI Studio
    url: https://blog.google/innovation-and-ai/technology/developers-tools/google-cloud-credits-gdp-ai-studio/
    tier: 一手
---

## 是什么

2026-11-13，Google 博客写下，Google Developer Program 的 Cloud 额度可以在 Google AI Studio 里领取和管理。Google AI Pro 和 Ultra 订阅本身带有按月重复发放的 Google Cloud 额度；没有开发者计划资料时，在 AI Studio 里兑换会自动建一份。额度可用于 Gemini API 的提示、构建和部署。博客写，每月发放额随 AI 计划档位变化，具体金额指向另一份指南，这次没有打开，待核实。

博客写明的规则：每笔月度额度自发放起 12 个月有效，按月滚动累加；订阅额度用完后可以用这些额度继续使用付费层模型和超出部分；升级 AI 计划会提高每月发放额；只有主订阅人能用，不能在家庭成员之间共享。用 Cloud 账单调用 Gemini API、并靠这些促销额度抵扣时，需要至少 $5 的预付和余额。

领取流程写的是：登录后在左侧看到未领取额度和余额；在同一个对话框里建立开发者计划资料并领取；可以在同一流程里建立 Cloud 账单，先花最早到期的额度，之后的月度发放自动套用；领取后挂上付费层 API key，在 `aistudio.google.com/billing` 看余额和用量。

猜测挂靠：额度如何抵 Gemini API 账单，在 E。这是友商的订阅额度和预付门槛，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成成本条目。

## 处置记录

- 2026-11-14：新建，status=open。
