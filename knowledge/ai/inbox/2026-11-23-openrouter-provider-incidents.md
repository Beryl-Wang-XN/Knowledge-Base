---
title: OpenRouter 下架三家推理供应商并收回 125 个零留存端点
captured: 2026-11-23
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: OpenRouter 公告
    url: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/
    tier: 一手
  - name: OpenRouter 公告列表
    url: https://openrouter.ai/blog/announcements/
    tier: 一手
---

## 是什么

OpenRouter 公告的署名日期是 11/22/2026，公告列表写 November 22, 2026。帖子说，本周早些时候安全研究人员报告，某些推理供应商的数据被泄露，或有证据表明没有遵守自己的数据政策。OpenRouter 写，这些发现没有显示 OpenRouter 自身被攻破或被未授权访问。

已经采取的动作：根据调查下架三家供应商；把 125 个端点移出 Zero Data Retention（ZDR）资格，其中包含研究人员点名的供应商，也包含 OpenRouter 预防性移除的端点；已通知所有可能受影响的客户。帖子没有写出被下架的三家供应商名字。

帖子列出已收到的供应商安全公告：Atlas Cloud、Novita、Phala、Together。并写，并非所有受影响的供应商都发了公开帖，即使用户那边没有公开帖，受影响用户也已通知。这四份公告的正文这次没有打开。

还在做的事：把研究人员的测试方法改成可以持续跑；核对网络路径，看请求和响应有没有被转到第三方；被拿掉 ZDR 资格的端点，要先有相应保证和验证才会恢复。帖子感谢 Dragos 的报告。Dragos 原文这次没有打开。

猜测挂靠：供应商去留和数据政策在 F。这是推理供应商变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-23：新建，status=open。
