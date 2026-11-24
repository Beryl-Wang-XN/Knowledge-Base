---
title: Claude 文本水印扩到 Opus 4.6、Opus 4.5、Sonnet 4.5 和 Haiku 4.5
captured: 2026-11-17
from: intel
module: F-landscape
business: true
status: open
review_after:
entry:
sources:
  - name: Claude Platform release notes
    url: https://platform.claude.com/docs/en/release-notes/overview
    tier: 一手
  - name: Text watermark
    url: https://platform.claude.com/docs/en/build-with-claude/text-watermark
    tier: 一手
  - name: How Claude marks AI-generated content
    url: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
    tier: 一手
---

## 是什么

2026-11-16 的 Claude Platform 发布说明写明：Claude Opus 4.6、Claude Opus 4.5、Claude Sonnet 4.5 和 Claude Haiku 4.5 生成的文本，会在「How Claude marks AI-generated content」列出的平台上带 Anthropic 的 text watermark。请求若把 `temperature`、`top_p` 或 `top_k` 设成非默认值，文本可能不带水印。11 月 4 日那条记下的是 Mythos 5、Opus 4.7 和 Sonnet 4.6；当时帮助中心的限制节提到 Opus 4.6，但 11 月 3 日的发布说明没有把它列进新增范围。这一条是发布说明新点名的四款。

同日打开的 Text watermark 文档，把采样限制写给 Claude Opus 4.6、Claude Sonnet 4.6、Claude Opus 4.5、Claude Sonnet 4.5、Claude Haiku 4.5，以及需申请才能访问的 Claude Opus 3。水印不改变含义、质量或可读性，不增加 token，也不加入隐藏字符，不携带用户或组织信息。依赖水印时不要传这三项采样参数，包括框架或客户端库代为设置的值。Opus 3 出现在这份采样节里，没有出现在 11 月 16 日的发布说明那一句里。

帮助中心文章抓取时显示 Updated today。模型表列出了上述型号，也列出 Fable、Mythos、Opus 5.5、Opus 4.8、Sonnet 5.5 和 Haiku 5.5 等。勾选列这次抓取没有保留，各列是否全开标 **待核实**。脚注写：Amazon Bedrock 的铺开可能再要几天；Opus 4.6、Opus 4.5、Opus 3、Sonnet 4.6、Sonnet 4.5 和 Haiku 4.5 在非默认采样下，文本水印可能不可靠。

猜测挂靠：F（友商模型的输出标记与转售合规）。不写入模型档案。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。11 月 4 日那条已经记下更早的一批型号，这一条不并进去。

## 处置记录

- 2026-11-17：新建，status=open。
