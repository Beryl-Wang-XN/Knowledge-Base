---
title: DeepSeek Search/Fetch 按次计费窗口打开，腾讯云后付费同步
captured: 2026-11-01
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: DeepSeek 模型与价格（中文）
    url: https://api-docs.deepseek.com/zh-cn/quick_start/pricing
    tier: 一手
  - name: DeepSeek Models & Pricing（英文）
    url: https://api-docs.deepseek.com/quick_start/pricing
    tier: 一手
  - name: DeepSeek Search & Fetch 指南
    url: https://api-docs.deepseek.com/guides/search
    tier: 一手
  - name: 腾讯云 TokenHub：DeepSeek 原厂联网搜索计费通知
    url: https://cloud.tencent.com/announce/detail/2538
    tier: 一手
  - name: 腾讯云 TokenHub 产品公告列表
    url: https://cloud.tencent.com/document/product/1823/130758
    tier: 一手
---

## 是什么

DeepSeek 原厂定价页写明：Search 与 Fetch 是独立 API，按成功请求计费。中文页单价是每 1,000 次成功请求 5 元；英文页与 Search & Fetch 指南写的是每 1,000 次成功请求 $0.75。指南里的成功口径是 HTTP 200 且有结果（Search 要返回非空结果，Fetch 要返回网页正文）；失败、空结果和超时不计费。

同一页注明：在 DeepSeek Harness、Claude Code、Codex 里使用 DeepSeek API 时，服务端工具调用已经会打到 Search/Fetch，这部分目前未计费，北京时间 2026-11-01 00:00 起按次收费。DeepSeek API 更新日志里对应的搜索 API 开放条目日期是 2026-10-17，不是这次新发的模型。本次拉取时该时刻已过，定价页仍用「目前未计费，并将于…起」的句子，没有改成已生效。账单是否已经按次扣费，标待核实。

腾讯云 TokenHub 公告写：只对名称带「原厂直供」的 DeepSeek 模型、经内置联网搜索工具产生的 Search/Fetch 收费。后付费 API 自北京时间 2026-11-01 00:00:00 起，Search 与 Fetch 各 5 元/千次成功请求；TokenPlan 个人版各 100 积分/千次、企业版各 500 积分/千次，自北京时间 2026-11-18 00:00:00 起。公告列表上这条的发布日期是 2026-10-28，列表页最近更新时间是 2026-10-31 13:53:30。其余模型的联网搜索不在这次调整里。

模型 token 标价这次没有看到改动。`deepseek-flash` 与 `deepseek-v4-pro` 的单价不在这条里重抄。

猜测挂靠：E（按次计费）。对标供应商的价格变化，`business: true`。

## 为什么没在当天处理

这是定时情报拉取，留待用户回顾。当天不写成成本条目，也不改模型档案。

## 处置记录

- 2026-11-01：新建，status=open。
