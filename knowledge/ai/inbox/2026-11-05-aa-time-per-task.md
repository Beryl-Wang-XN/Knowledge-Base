---
title: Artificial Analysis 用 Time per Task 作为性能主指标
captured: 2026-11-05
from: intel
module: B-inference
business: false
status: open
review_after:
entry:
sources:
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

Artificial Analysis changelog 在「03 Nov 2026」下新增 Performance Benchmarking v3.0.0。正文是：比较模型时，主指标改为 Time per Task。Output Speed 覆盖整次请求，含等到第一个 token 的时间，并对单请求和多轮 agent 负载取平均。token 数改用各供应商 API 的计数。端点侧失败会计入该端点，每个端点展示 Endpoint Error Rate。

同一日期标题下还有已经记过的 Intelligence Index v5.0.1，这次不重复那条。上次拉取读到的 11 月 3 日 changelog 只记下了 v5.0.1，没有这段性能方法。changelog 本身没有给出分数位移、名次或各模型的 Time per Task。模型页上的实时分钟数这次不抄，标 **待核实**。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不改推理指标条目，也不把榜单数字写进档案。

## 处置记录

- 2026-11-05：新建，status=open。
