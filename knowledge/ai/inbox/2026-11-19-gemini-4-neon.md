---
title: Gemini 4 Neon 一般可用，标准价输入 $3、输出 $15
captured: 2026-11-19
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Google 博客 Introducing Gemini 4 Neon
    url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
    tier: 一手
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
  - name: What's new in Gemini 4 Neon
    url: https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-neon
    tier: 一手
  - name: Gemini 4 Neon 模型页
    url: https://ai.google.dev/gemini-api/docs/models/gemini-4-neon
    tier: 一手
  - name: Gemini API 定价页 Gemini 4 Neon
    url: https://ai.google.dev/gemini-api/docs/pricing#gemini-4-neon
    tier: 一手
  - name: Gemini 4 Neon 模型卡
    url: https://deepmind.google/models/model-cards/gemini-4-neon/
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

2026-11-18，Google 博客、Gemini API changelog 和 What's new 页都写下了 Gemini 4 Neon（`gemini-4-neon`）一般可用。changelog 写它只在付费层，标价是每百万输入 token $3.00、每百万输出 token $15.00。思考档是 `low`、`medium`、默认 `high`，以及 `xhigh`。统一上下文 1M token，long decode 到 1M token。

模型页已打开。输入是文本、图片、视频、音频和 PDF，输出是文本。统一上下文窗口 1,048,576 token。默认同步最大输出 65,536 token；打开 long decode 后最多 1,048,576 token。上下文缓存只支持隐式，显式缓存不可用。Batch、Flex、Priority 标成支持。图片生成、音频生成和 Live API 标成不支持。What's new 写，`generateContent` 和 Interactions API 都能用；从 Carbon、Argon 或 Hydrogen 换过来只改模型 ID。`minimal` 会被拒绝。`temperature`、`top_p`、`top_k` 若在范围内会被忽略，超出范围返回 400。

定价页的 Neon 一节已打开，没有另一档长上下文加价，也没有免费层。付费层：输入 $3.00，输出（含思考 token）$15.00，上下文缓存 $0.15，并写明只支持隐式缓存。What's new 把缓存写成提示至少 4,096 token 时默认隐式缓存，命中后输入按 95% 折扣，即每百万 $0.15。思考 token，以及使用接地时的内部工具说明和函数声明，都计入计费。Google Search 接地：所有 Gemini 3 及更新模型共用每月 5,000 次免费搜索，之后每 1,000 次 $14，每日上限 1,500 次；Google Maps 同样是共用每月 5,000 次免费，之后每 1,000 次查询 $14。付费层写的是不用于改进产品。定价页这一节没有列出 Batch、Flex、Priority 的单价，待核实。速率限制页这次没有打开，待核实。

博客写，即日起铺到 Gemini API 的 Google AI Studio、Gemini for business（API 和模型下拉）、付费 Google AI Pro / Ultra 的 Google Antigravity，以及 Pro / Ultra 的 Gemini app。开发者还写到 Android Studio。网络安全向 Fairwind Program 的合格成员在接下来几天开始开放。模型卡发布日是 2026-11-18，写它由 Gemini 4 Carbon 改编，知识截止是 2026 年 3 月。安全报告写着即将发布。

Artificial Analysis changelog 在 2026-11-18 给出 Intelligence Index：Low 44、Medium 55、High 60、Xhigh 61，并把相对 Gemini 4 Carbon 写成智能小幅提高、Cost per Task 大约低 17%。博客自己把 xhigh 的 61 写成总榜第 3，并把默认 high 相对 Carbon 的 Cost per Task 写成低 32%。两处百分比都照原文分开写。同日 changelog 里的 K2 Horizon 32B 只是分数点，不另记。

同日 changelog 的多模态切片，以及 GitHub Copilot 渠道，另记。

猜测挂靠：新的模型 ID 和标价在 G。这是厂商型号和价格，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-19：新建，status=open。
