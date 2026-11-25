---
title: Artificial Analysis Intelligence Index 调到 v5.0.2
captured: 2026-11-25
from: intel
module: G
business: false
status: open
review_after:
entry:
sources:
  - name: Artificial Analysis Changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
  - name: Intelligence Benchmarking methodology
    url: https://artificialanalysis.ai/methodology/intelligence-benchmarking
    tier: 一手
  - name: Artificial Analysis Intelligence Index
    url: https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
    tier: 一手
---

## 是什么

Artificial Analysis 更新日志把 2026-11-24 标为 Intelligence Index 方法变更：v5.0.2 把 Terminal-Bench 换到 4.1，任务仍是 66 个，但验证器更新了；FrontierCode 2.0 换上最新的 trajectory scanner。

方法页写的是同一版。Terminal-Bench 4.1 保留 4.0 的 66 个任务、说明和智能体环境，更新任务验证器，用来提高可靠性和抗奖励投机。已经在 4.0 上评过的模型，用 4.1 的验证器重打保存下来的输出，不重跑任务。4.0 写明被 4.1 取代，它一直用到 v5.0.1。指数里这项权重是 10%。

FrontierCode-AA 2.0 的评分更新写着 2026 年 11 月：采用 Cognition 更新后的 trajectory scanner，并对扫描只给出提示的尝试做 LLM judge 复核，然后在各模型已有的尝试上重评，作为 v5.0.2 的一部分。这项权重是 15%。changelog 没有给出各模型分数移动多少，也没有写名次是否变化，这两项标 **待核实**。

指数页确认当前版本是 v5.0.2，九项构成与方法页一致。同日更新日志里 DeepInfra、Modular、Verda、Nebius 的行是已有模型的性能点，不另开条目，也不把榜上的分数抄进来。

猜测挂靠：G（档案库使用的智能指数）。不把分数写进模型档案。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目，也不抄榜单分数。

## 处置记录

- 2026-11-25：新建，status=open。
