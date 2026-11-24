---
title: Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2，标准价降至 $8/$40
captured: 2026-11-10
from: intel
module: G
business: true
status: open
review_after:
entry:
sources:
  - name: Anthropic 新闻室 Claude Fable 5.2 and Mythos 5.2
    url: https://www.anthropic.com/claude-fable-and-mythos-5-2
    tier: 一手
  - name: Claude Platform 发布说明
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: AWS 机器学习博客 Claude Fable 5.2 on AWS
    url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-fable-5-2-on-aws/
    tier: 一手
  - name: Claude Code changelog 2.1.321
    url: https://code.claude.com/docs/en/changelog
    tier: 一手
  - name: Artificial Analysis changelog
    url: https://artificialanalysis.ai/changelog
    tier: 一手
---

## 是什么

2026-11-09，Anthropic 发布 Claude Fable 5.2（`claude-fable-5-2`）和 Claude Mythos 5.2（`claude-mythos-5-2`）。新闻室写，两者是同一个底层模型：Fable 带更强的网络安全和生物安全防护，向所有用户开放；Mythos 只给通过 Life Sciences 或 Cyber Verification Program 验证的组织。

平台发布说明写明：上下文窗口 100 万 token，最大输出 128k token，自适应思考始终打开。标准价是每百万 token 输入 $8、输出 $40。同节写 Claude Fable 5.1 与 Claude Mythos 5.1 是输入 $10、输出 $50。新闻室写，生成速度比 5.1 最多快 30%。

可选 fast mode：新闻室写两个模型都能把 token 生成最多加快 2.5 倍，价格是输入 $16、输出 $80。可用范围写了 Claude Code、Claude Platform、Claude Models on Google Cloud（Anthropic 托管和 Google 托管），以及 Microsoft Foundry（Anthropic 托管）；Mythos 的 fast mode 只给验证计划内的组织。平台发布说明的对应条目只写了 Claude API 上 Fable 5.2 的 Messages API：设置 `speed: "fast"`，不需要 beta header，输出 token 每秒最多高 2.5 倍，价格同样是 $16 / $80。

平台发布说明列出的 Fable 5.2 上架范围：Claude API、Claude Platform on AWS、Claude Models on Google Cloud（Anthropic 托管和 Google 托管）、Amazon Bedrock、Microsoft Foundry。AWS 机器学习博客同日宣布 Bedrock 与 Claude Platform on AWS 提供这两个模型。新闻室还写，符合条件的付费方案本周有额外 Fable 用量：含 Fable 的方案和席位按订阅时长给 1 到 3 次 Fable 重置；Pro 以及 Team 标准席位的每周用量上限里，Fable 最多占 50%。促销页这次没有另开。

同日平台说明里的接口约束：两个模型对所有账号年龄都做前缀检查；若改了 `system`、`tools` 或更早的消息，再把后一轮的 thinking block 送回去，会返回 400。在 Claude API 和 Google 托管的 Claude Models 上，对话切到这两个模型时会保留其他模型（包括 Opus 5.5、Sonnet 5.5、Haiku 5.5）的推理；切走时，它们产出的 thinking block 会被丢掉，请求仍然成功。Computer use 用 `computer_toolset_20260801`；旧的 `computer_20251124` 除 Amazon Bedrock 外会 400。Advisor 工具仍是 beta：这两个模型做 executor 时，advisor 只能是它们二者之一。Thinking block 只在产出它的账号或关联账号里有效。两者和 5.1 一样要求 30 天数据保留，除非 Anthropic 明确授权，否则不能用 zero data retention。

新闻室另写，Enterprise Frontier Safeguards 进入私有 beta，把安全监测放到客户自己的基础设施里存储的提示和响应上，从而可以和 zero data retention 并存。符合条件的客户可以在接上这套监测之前，继续以 zero data retention 使用这两个模型；其他客户为安全监测保留 30 天。这和平台说明里「除非明确授权，否则不能 ZDR」是同一天的两处写法，授权范围留在原文。

Claude Code changelog 的 2.1.321（2026-11-09）把 `claude-fable-5-2` 写成默认的 Fable 模型，并写 100 万上下文、$8 / $40 per MTok，缓存读取 $0.20 per MTok。其余 CLI 变更不另记。

Artificial Analysis changelog 的 2026-11-09 给出 Claude Fable 5.2 的 Intelligence Index：Max 65，High 62，Xhigh 62，Medium 56，Low 54，标注都是 Default Fallback。新闻室自己的对照表这次不逐格抄。

猜测挂靠：模型档案在 G。新模型和标价是对标友商，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成模型条目，也不改 `registry/`。

## 处置记录

- 2026-11-10：新建，status=open。
