---
title: Claude 文本水印扩到 Mythos 5、Opus 4.7、Sonnet 4.6
captured: 2026-11-04
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

2026-11-03 的 Claude Platform 发布说明写明：Claude Mythos 5、Claude Opus 4.7、Claude Sonnet 4.6 生成的文本，会在「How Claude marks AI-generated content」列出的平台上带 Anthropic 的 text watermark。Sonnet 4.6 上，请求若把 `temperature`、`top_p` 或 `top_k` 设成非默认值，生成文本可能不带水印。

同日打开的 Text watermark 文档写明：水印不改变含义、质量或可读性，不增加 token，也不加入隐藏字符，不携带用户或组织信息，请求和响应处理都不用改。若依赖水印，这三项采样参数都不要传，包括框架或客户端库代为设置的值。

帮助中心文章抓取时显示 Updated today，没有单独的时钟。文章把这套标记放在欧盟《人工智能法案》第 50 条透明度实践准则之下，并写明支持的模型会在 Claude Platform（API）、Claude、Claude Code、Claude Cowork、Claude Tag，以及 AWS、Google Cloud、Microsoft Foundry 上带文本水印。检测仍是 private preview，对象是准则里的合格组织，以及需要核对自己 Claude 输出的企业。页末有两条脚注：Amazon Bedrock 的铺开将在 11 月 10 日前完成；Sonnet 4.6 在上述非默认采样下，水印可能不可靠。限制一节还写到 Claude Opus 4.6 在同样的非默认采样下可能没有可检测水印，但 11 月 3 日的发布说明没有把 Opus 4.6 列进这次新增范围。模型表的勾选列这次抓取没有保留，各列是否全开标 **待核实**。

猜测挂靠：F（友商模型的输出标记与转售合规）。不写入模型档案。

## 为什么没在当天处理

这是定时情报拉取，留待用户回顾。当天不写成知识条目，也不改模型档案。

## 处置记录

- 2026-11-04：新建，status=open。
