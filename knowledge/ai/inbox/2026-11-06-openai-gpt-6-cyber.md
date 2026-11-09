---
title: OpenAI 发布 GPT-6 Cyber，经 Daybreak Red 提供 API
captured: 2026-11-06
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: OpenAI 新闻室 Introducing GPT-6 Cyber
    url: https://openai.com/index/introducing-gpt-6-cyber/
    tier: 一手
  - name: OpenAI API changelog
    url: https://developers.openai.com/api/docs/changelog
    tier: 一手
  - name: GPT-6-Cyber 模型页
    url: https://developers.openai.com/api/docs/models/gpt-6-cyber
    tier: 一手
---

## 是什么

2026-11-05，OpenAI 新闻室发布 GPT-6 Cyber，API changelog 同日列出模型 `gpt-6-cyber`。新闻室把它放在 Daybreak Red，用来在授权范围内调查漏洞、复现并验证修复。这是新模型，不是上一窗口已经记下的「GPT-5.6 Cyber 经 Daybreak Red 进入 AWS GovCloud」。

模型页写明：组织需要 Daybreak Red 访问权限和批准才能调用。输入是文本和图像，输出是文本。上下文窗口 1,050,000，最大输入 922,000，最大输出 128,000，支持 reasoning token。Chat Completions 与 Responses 支持，Batch 不支持。新闻室写，起初只向一批已批准的 Daybreak Red 客户开放 API 和 Codex，随后扩大到全部 Daybreak Red 客户；同时把 GPT-5.6 Cyber 开放给全部 Daybreak Red 客户。

模型页列出的标准短上下文价格，按每百万 tokens：输入 $20，缓存输入 $2，缓存写入 $25，输出 $100。同页注明短上下文缓存写入是 30 分钟 $25，或 12 小时 $50。该页摘录没有另列长上下文价格，长上下文标价待核实。

新闻室把该模型在 Preparedness Framework 的网络安全等级标为 Critical，并写 GPT-5.6 Cyber 为 High。同文给出的 ExploitGym 分数是 48.5%，GPT-5.6 Cyber 为 32.1%。同文还写了 Firefox 与 Linux 上的研究数量，具体口径留在原文，这里不展开成操作说明。

同文一并写了配套限制：Daybreak Red 的 API 默认要求 IP allowlist；使用 Zero Data Retention 的 API 客户通常必须使用 Private Safety Processing，加密记录留在客户存储中 30 天，不向 OpenAI 人员暴露提示和响应。系统卡本次没有打开。

猜测挂靠：模型档案在 G。价格和准入条件是对标友商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-06：新建，status=open。
