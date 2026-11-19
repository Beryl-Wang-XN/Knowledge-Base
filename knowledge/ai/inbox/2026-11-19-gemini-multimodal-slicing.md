---
title: Gemini API 可按页、表和工作表切片，并只为选中部分计费
captured: 2026-11-19
from: intel
module: E-economics
business: true
status: open
review_after:
entry:
sources:
  - name: Gemini API changelog
    url: https://ai.google.dev/gemini-api/docs/changelog
    tier: 一手
---

## 是什么

Gemini API changelog 在 2026-11-18 另有一节：可以把 Microsoft Office 和 OpenDocument 文件（Word、PowerPoint、Excel）直接传给 Gemini API，并在用户提示和函数响应里切片文档、表格、视频和音频。可选页面范围、工作表标签、单元格范围、时间区间，或内容层（例如页面图像、抽出的文本、公式、视频文字记录），从而只处理和支付需要的部分。指南指向 Document understanding、Video understanding 和 Audio understanding。这三份指南这次没有打开，切片参数和具体单价待核实。

11 月 5 日那条已经记下 PPT、ODP、ODS、DOC 的接入，并写当时 DOCX、PPTX、XLSX 等格式的处理不变。这一条只记 11 月 18 日的切片和按选中部分计费。

猜测挂靠：按选中片段计费在 E。这是计费方式变化，`business: true`。

## 为什么没在当天处理

这是定时拉取，留待用户回顾。当天不写成知识条目。

## 处置记录

- 2026-11-19：新建，status=open。
