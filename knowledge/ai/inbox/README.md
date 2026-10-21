# inbox

8:00 的定时任务把过去 24 小时的情报放在这里。看完每日页后、当天不展开的追问也放在这里。

每天学习从这份待回顾列表开始。待回顾 = `status` 为 `open`，或 `later` 且已到 `review_after`。已写入学习计划的 `promote` 不再每天重列。

你点名哪些今天和计划里的下一课一起学。点名的会联网核实，写入条目，并出现在当天的每日页、小红书草稿和播客里。可以一条都不点。

没点名的，你逐条说一个结果：

| 你的话 | status | 做什么 |
| --- | --- | --- |
| 今天一起学 | `merged` | 和计划下一课一起核实，写入条目，`entry` 填路径 |
| 不管了 | `dropped` | 写明原因，文件留着，不再当作待回顾 |
| 写到学习计划里 | `promote` | 追加到 `learning-plan.md` 的「从回顾排入的课」，离开每日待回顾列表 |
| 留在回顾里下次处理 | `open` | 下次继续出现。指定了日期才改 `later` 并填 `review_after` |

队列不用一次清空。单条格式见 `knowledge/ai/_templates/inbox.md`。流程见 `learning-plan.md` 与 skill `ai-kb-daily`。
