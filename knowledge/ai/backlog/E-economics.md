# AI 知识库 · 整体待办与待核实清单

> 建立：2026-08-31　｜　更新：2026-09-01
> 用途：全库（A–G 模块 + 模型档案）的**统一待办与待核实登记**。各模块在自己的窗口推进，进度回填到这里，保持单一总览。
> 原则见 `framework.md` / `sources.md`：只写 web_fetch 核实到的内容，未核实标"待核实"，禁凭记忆编造；一手优先，关键术语保留英文。

## 使用约定

- 每个模块一节。条目格式：`- [ ] 待办描述　目标文件　（现状 / 动作 / 候选源）`。
- 完成后把 `[ ]` 改 `[x]` 并移至该模块「已完成」区（或直接勾选保留）。
- 优先级：**P0**=影响结论准确性　**P1**=增强交叉验证/补全　**P2**=口径完善。
- 每次改完 Markdown 跑 `python3 scripts/build_site.py ai` 重生成站点。

## 全局进度总览

| 模块 | 名称 | 状态 | 负责窗口 |
|------|------|------|---------|
| A | 模型层 | 待补充 | 其他窗口 |
| B | 推理层 | 待补充 | 其他窗口 |
| C | 算力层 | 待补充 | 其他窗口 |
| D | 调度服务层 | 待补充 | 其他窗口 |
| **E** | **成本经济层** | **✅ 3 条已核实重写；有 P0/P1/P2 待核实** | 本窗口 |
| F | 竞品供应商格局 | 待补充 | 其他窗口 |
| G | 模型档案库 | 待补充 | 其他窗口 |

---

## A · 模型层 Model

> 待其他窗口补充。可登记：需一手源核实重写的条目、待核实数据、缺失条目。

- [ ] （待补充）

---

## B · 推理层 Inference

> 待其他窗口补充。

- [ ] （待补充）

---

## C · 算力层 GPU/Infra

> 待其他窗口补充。

- [ ] （待补充）

---

## D · 调度服务层 Serving

> 待其他窗口补充。

- [ ] （待补充）

---

## E · 成本经济层 Economics　【本窗口，已推进】

### 已完成（存档，无需再做）

- [x] `token-billing.md`：OpenAI 定价页、Anthropic 定价页、OpenRouter 列表页（交叉验证）——已核实重写。
- [x] `cost-composition.md`：NVIDIA H100 / DGX B200 规格、Lambda 租赁价——已核实重写。
- [x] `unit-economics.md`：Lambda 小时价、Artificial Analysis 吞吐、OpenRouter 报价+调用量排名——已核实重写。
- [x] 站点已重生成（25 条目 / 5 档案）。

### P0 · 影响成本模型准确性（最重要）

- [ ] **单卡聚合吞吐（batching 后总 tokens/s）**　`unit-economics.md`
  - 现状：示例用的 3,000 tok/s 是**示意值**；Artificial Analysis 只给单请求速度。
  - 动作：用实测/压测聚合吞吐替换。候选源：vLLM 官方 benchmark、NVIDIA 推理性能页、MLPerf Inference。
- [ ] **自建单卡真实小时成本拆解**　`cost-composition.md`
  - 待核实：PUE、工业电价（$/kWh）、机房/带宽/存储/人力金额、GPU 折旧年限。
  - 动作：用实际采购电价 + 目标机房 PUE 填参；或找公开 TCO 拆解交叉验证。
- [ ] **input / output 每 token 成本拆分系数**　`unit-economics.md`
  - 待核实：Prefill 与 Decode 的单位成本比例。
  - 动作：查 B 模块 Prefill/Decode 性能数据或压测得出。

### P1 · 数据补全（增强交叉验证）

- [ ] **SemiAnalysis 的 GPU TCO / 集群经济学具体数字**　`cost-composition.md`
  - 现状：站点反爬（JS 校验），web_fetch 拿不到正文，已标待核实。
  - 动作：订阅账号或人工浏览器打开后回填；或换等价公开源。
- [ ] **单卡 B200 独立 TDP**　`cost-composition.md`
  - 现状：DGX B200 页只给整机 ~14.3 kW。
  - 动作：查 NVIDIA B200 单卡 datasheet 或 Blackwell 架构白皮书。
- [ ] **GPT / Claude / Gemini 在 OpenRouter 的报价（含多供应商差价）**　`token-billing.md`
  - 现状：列表页默认未展示，需进各模型详情页；官方牌价已核实。
  - 动作：按 slug 逐个 web_fetch `openrouter.ai/models/<slug>`。
- [ ] **Anthropic 1 小时扩展缓存价格、长上下文分档**　`token-billing.md`
  - 动作：查 Anthropic 官方 docs（platform.claude.com/docs）缓存与长上下文专项页。

### P2 · 口径完善

- [ ] **token 换算口径（1 token≈0.75 词 / 汉字 1~2 token）**　`token-billing.md`
  - 现状：已标注"行业通识、未核实"。
  - 动作：查 OpenAI Tokenizer 官方说明 / tiktoken 文档核实后更新标注。

---

## F · 竞品供应商格局 Landscape

> 待其他窗口补充。

- [ ] （待补充）

---

## G · 模型档案库 Model Registry

> 待其他窗口补充。可登记：档案的规格/定价/榜单分数待核实项。

- [ ] （待补充）

---

## 通用备注（跨模块）

- 价格/规格随时变动，已核实数据均标 `verified: 日期`；跨过较长时间再引用前回官方页复核。
- web_fetch 踩坑记录：
  - OpenAI 主定价页 `openai.com/api/pricing` 返回 **403**，改用 `platform.openai.com/docs/pricing`。
  - Anthropic `anthropic.com/pricing` **重定向**到 `claude.com/pricing`。
  - SemiAnalysis 有 **JS 反爬**，web_fetch 取不到正文。
- code-explorer subagent **无联网能力**，联网核实一律走主线程 web_fetch。
