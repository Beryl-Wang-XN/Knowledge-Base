---
title: Gemini API 接受旧版 Office 与 OpenDocument，函数响应可回传更多文件
captured: 2026-11-06
from: intel
module:
business: false
status: open
review_after:
entry:
sources:
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
---

## 是什么

Gemini API changelog 的 2026-11-05 另有两条，与同日的 Omni 1.2 Flash 不是一件事。

文件输入：API 现在接受 PowerPoint 97-2003（PPT）、OpenDocument Presentation（ODP）和 OpenDocument Spreadsheet（ODS），并为 Word 97-2003（DOC）增加按页渲染成图像的处理。DOC、PPT、ODP 都按页面图像处理。ODS 只把第一张表的数据和公式交给模型。DOCX、DOTX、ODT、PPTX、XLSX、XLS 的处理方式不变。

函数响应：工具现在可以把 Office、OpenDocument、音频和视频交回模型。GenerateContent 的函数响应除图像、PDF 和纯文本外，还可带这些文件；也可以用 `fileData` 交 Files API 的 URI，而不必内联字节。`displayName` 可用于 `inlineData` 和 `fileData`。视频部分接受 `mediaProcessing`，取值为 `STATIC` 或 `AGENTIC`。Interactions API 的 `function_result` 除文本和图像外，还可带 `document`、`audio`、`video`，用内联 `data` 或 `uri`。视频块在 `v1beta` 和 `v1alpha`，并接受 `processing`。

没有单独标价。处理页和函数调用页本次没有再打开，上面的范围以 changelog 这一节为准。

挂不上框架里的单个模块，`module` 留空。不是友商对标或价格变化，`business: false`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-06：新建，status=open。
