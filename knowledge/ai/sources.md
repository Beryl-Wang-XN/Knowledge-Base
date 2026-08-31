# AI 知识库 · 信息来源地图

> 本文件登记各模块的**可靠信息来源**及其分级，供更新与入库时引用。
> 配合 `framework.md` 使用。来源会持续增补，变更请记录在文末「版本记录」。

## 信息处理原则

1. **一手优先**：尽量取一手源（常为英文原版），翻译成中文入库，关键术语保留英文原词。
2. **鲜度**：所有模块以联网核实的最新信息为准；入库事实（规格/价格/榜单分数）一律回到 🥇 一手源核对。
3. **二手仅补充**：中文二手博客（CSDN/知乎/掘金等）仅用于快速入门，不作入库依据。
4. **多媒体源处理**：AI 无法直接看视频/听音频。视频与课程类源优先抓取其**配套文字**（讲义/字幕转录/博客/GitHub）；纯视频内容由用户消化后回传要点。若为 AI 认为优质但**找不到文字载体**的视频/课程，直接返回链接给用户自学（或用户另想办法）。
5. **内部源**：由用户按需同步；每个学习阶段起点主动询问一次。

## 分级图例

- 🥇 一手权威：官方文档 / 公认榜单 / 论文原文 / 顶级从业者 —— 可直接入库
- 🥈 优质二手：分析媒体 / 优质博客 —— 需交叉验证
- 🛠 工具站：实时数据聚合 —— 方便但需甄别

## 按模块来源

| 模块 | 🥇 一手权威源 | 🥈/🛠 补充源 |
|------|-------------|-------------|
| **A 模型原理** | Hugging Face 课程与文档（huggingface.co/learn, /docs）；arXiv 论文原文；高校课程：斯坦福 CS224N / CS336 / CS25 | 🥇视频 3Blue1Brown（Transformer 可视化）、Karpathy（LLM 讲解）；🥈 The Illustrated Transformer（jalammar.github.io） |
| **B 推理** | vLLM 官方文档（docs.vllm.ai）、TensorRT-LLM（GitHub）、SGLang 官方；论文：PagedAttention / FlashAttention / Speculative Decoding | 🥈 中文横评（知乎/掘金，仅对比参考） |
| **C 算力** | NVIDIA 官方 datasheet/白皮书（H100/H200/B200/GB200） | 🥈 SemiAnalysis（硬件+成本深度）；云厂商 GPU 实例文档 |
| **D 调度服务** | 论文：Orca（continuous batching）等；vLLM / Kubernetes 官方架构文档；云厂商架构指南 | 🥈 生产架构博客（需甄别） |
| **E 成本经济** | 各厂商官方定价页；Artificial Analysis（artificialanalysis.ai，Blended price）；**OpenRouter**（openrouter.ai，多供应商真实报价） | 🛠 LLM Price Watch / AI Cost Calculator；🥈 SemiAnalysis 成本拆解 |
| **F 竞品供应商** | 各厂商官方发布博客/公告；国内云厂商官方（火山方舟 / 阿里百炼 / 腾讯混元等）；**OpenRouter Rankings**（真实调用量信号） | 🥈 行业分析（The Information、a16z）、机器之心/量子位；访谈类视频（Lex Fridman、Dwarkesh Patel） |
| **G 模型档案库** ★ | **LMArena**（lmarena.ai，人类盲评 Elo）、**Artificial Analysis**（智能/速度/价格）、**LiveBench**（livebench.ai，抗污染）；各厂商官方 model card + 定价页；**OpenRouter**（使用排名 + 多供应商对比） | 🛠 llm-stats.com（聚合 300+ 模型，需甄别） |

## 重点组合建议

- **G（核心资产）黄金组合**：LMArena + Artificial Analysis + LiveBench 三榜单交叉（人类偏好 / B端选型 / 客观抗污染）＋ 厂商官方 model card 与定价页（一手规格与价格）＋ OpenRouter（真实调用与多供应商报价）。
- **原理打底**：高校课程（CS224N/CS336）+ 3Blue1Brown/Karpathy 视频（找文字载体）。

## 待补充

- [ ] 用户内部源：实际对标友商、实际采购的算力/模型供应商、内部竞品分析与成本模型（涉密仅记类别，按需同步）。

## 版本记录

| 日期 | 变更 |
|------|------|
| 2026-08-31 | 初版来源地图（A–G 分级来源 + 处理原则 + OpenRouter/高校课程/顶级视频源） |
