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
| **D** | **调度服务层** | **✅ 4 条已核实重写；有 P0/P1/P2 待核实** | 本窗口 |
| **E** | **成本经济层** | **✅ 3 条已核实重写；有 P0/P1/P2 待核实** | 本窗口 |
| F | 竞品供应商格局 | 待补充 | 其他窗口 |
| **G** | **模型档案库** | **✅ 5 个档案及总表已核实重写；有 P0/P1/P2 待核实** | 本窗口 |

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

## D · 调度服务层 Serving　【本窗口，已推进】

> 目录：`entries/D-serving/`

### 已完成（存档，无需再做）

- [x] `scheduling-and-sla.md`：Orca 论文（OSDI'22，36.9× 吞吐）、vLLM V1 博客、vLLM 调优文档、vLLM 架构文档，及 **SchedulerConfig.policy 官方文档 + scheduler.py 源码**（fcfs/priority 抢占逻辑）——已核实重写。
- [x] `load-balancing-routing.md`：K8s Gateway API Inference Extension（推理感知路由/EPP/KV-Cache 感知）、vLLM DP Coordinator，及 **OpenRouter Provider Routing**（多供应商负载均衡/故障转移/性能百分位阈值）——已核实重写。
- [x] `autoscaling-cold-start.md`：K8s HPA 文档（同步周期/公式/容差/稳定窗口/Scale-to-Zero）、K8s Node Autoscaling（Cluster Autoscaler vs Karpenter），及 **Google Cloud Run GPU 最佳实践**（模型加载路径/量化/GGUF/启动探针）——已核实重写。
- [x] `tidal-scheduling-colocation.md`：AntMan 论文（Alibaba OSDI'20，内存+42%/算力+34%），及 **NVIDIA A100 MIG 官方博客**（切 7 实例/全路径隔离/故障隔离/QoS 实测）——已核实重写。
- [x] 站点已重生成（25 条目 / 5 档案）；4 条 front matter 均加 `verified: 2026-08-31`。

### P0 · 影响调度/成本结论准确性（最重要）

- [ ] **LLM 权重加载的冷启动绝对耗时区间**　`entries/D-serving/autoscaling-cold-start.md`
  - 现状：Cloud Run 官方只给了**降冷启动的方法**，未给统一的秒/分钟量化区间；"1–10 分钟"未从一手源证实，已标待核实。
  - 动作：查 vLLM/TensorRT-LLM 部署文档或云厂商实测数据，按模型规模 × 存储介质 × 带宽给出实测区间。
- [ ] **潮汐调度集群级策略 / 在离线混部抢占阈值 / SLA 保障参数**　`entries/D-serving/tidal-scheduling-colocation.md`
  - 现状：多为各厂工程实践，缺统一一手源；AntMan 给了利用率量级但非策略参数。
  - 动作：找工程博客/论文（如各厂 GPU 集群调度实践）交叉验证，二手源注明 `tier: 二手`。

### P1 · 数据补全（增强交叉验证）

- [ ] **推理感知负载均衡"降延迟/提利用率"的具体百分比**　`entries/D-serving/load-balancing-routing.md`
  - 现状：K8s Gateway API Inference Extension 官方只有定性结论，未给数字。
  - 动作：查该项目 benchmark / llm-d 相关性能报告回填。
- [ ] **MIG 跨型号支持（H100 / A30 / B 系列）**　`entries/D-serving/tidal-scheduling-colocation.md`
  - 现状：仅核实 A100（最多 7 实例）；其他型号实例数与 profile 差异未核实。
  - 动作：查各型号 datasheet 或 MIG User Guide 的 Supported GPUs 子页（首页为 JS 渲染，正文未返回）。
- [ ] **语义路由（按难度选大/小模型）的权威定义与降本数据**　`entries/D-serving/load-balancing-routing.md`
  - 现状：业界常见降本思路，但本次两个官方源未直接定义，已标待核实（勿与"模型感知路由"混淆）。
  - 动作：找路由框架（如 RouteLLM 论文/官方）核实机制与效果后再入库。

### P2 · 口径完善

- [ ] **准入控制（Admission Control）的具体实现口径**　`entries/D-serving/scheduling-and-sla.md`
  - 现状：vLLM 未给统一策略，已标待深入。
  - 动作：结合业务自定义 priority 值 + 网关限流的落地方案，补一段实践口径（可标二手/自拟）。
- [ ] **故障转移健康检查/重试/熔断阈值**　`entries/D-serving/load-balancing-routing.md`
  - 现状：属工程实践，已标待深入；OpenRouter 给了"30 秒故障剔除"可作参考。
  - 动作：补充网关侧健康检查/熔断的常见口径，注明来源层级。

---

## E · 成本经济层 Economics　【本窗口，已推进】

> 目录：`entries/E-economics/`

### 已完成（存档，无需再做）

- [x] `token-billing.md`：OpenAI 定价页、Anthropic 定价页、OpenRouter 列表页（交叉验证）——已核实重写。
- [x] `cost-composition.md`：NVIDIA H100 / DGX B200 规格、Lambda 租赁价——已核实重写。
- [x] `unit-economics.md`：Lambda 小时价、Artificial Analysis 吞吐、OpenRouter 报价+调用量排名——已核实重写。
- [x] 站点已重生成（25 条目 / 5 档案）。

### P0 · 影响成本模型准确性（最重要）

- [ ] **单卡聚合吞吐（batching 后总 tokens/s）**　`entries/E-economics/unit-economics.md`
  - 现状：示例用的 3,000 tok/s 是**示意值**；Artificial Analysis 只给单请求速度。
  - 动作：用实测/压测聚合吞吐替换。候选源：vLLM 官方 benchmark、NVIDIA 推理性能页、MLPerf Inference。
- [ ] **自建单卡真实小时成本拆解**　`entries/E-economics/cost-composition.md`
  - 待核实：PUE、工业电价（$/kWh）、机房/带宽/存储/人力金额、GPU 折旧年限。
  - 动作：用实际采购电价 + 目标机房 PUE 填参；或找公开 TCO 拆解交叉验证。
- [ ] **input / output 每 token 成本拆分系数**　`entries/E-economics/unit-economics.md`
  - 待核实：Prefill 与 Decode 的单位成本比例。
  - 动作：查 B 模块 Prefill/Decode 性能数据或压测得出。

### P1 · 数据补全（增强交叉验证）

- [ ] **SemiAnalysis 的 GPU TCO / 集群经济学具体数字**　`entries/E-economics/cost-composition.md`
  - 现状：站点反爬（JS 校验），web_fetch 拿不到正文，已标待核实。
  - 动作：订阅账号或人工浏览器打开后回填；或换等价公开源。
- [ ] **单卡 B200 独立 TDP**　`entries/E-economics/cost-composition.md`
  - 现状：DGX B200 页只给整机 ~14.3 kW。
  - 动作：查 NVIDIA B200 单卡 datasheet 或 Blackwell 架构白皮书。
- [ ] **GPT / Claude / Gemini 在 OpenRouter 的报价（含多供应商差价）**　`entries/E-economics/token-billing.md`
  - 现状：列表页默认未展示，需进各模型详情页；官方牌价已核实。
  - 动作：按 slug 逐个 web_fetch `openrouter.ai/models/<slug>`。
- [ ] **Anthropic 1 小时扩展缓存价格、长上下文分档**　`entries/E-economics/token-billing.md`
  - 动作：查 Anthropic 官方 docs（platform.claude.com/docs）缓存与长上下文专项页。

### P2 · 口径完善

- [ ] **token 换算口径（1 token≈0.75 词 / 汉字 1~2 token）**　`entries/E-economics/token-billing.md`
  - 现状：已标注"行业通识、未核实"。
  - 动作：查 OpenAI Tokenizer 官方说明 / tiktoken 文档核实后更新标注。

---

## F · 竞品供应商格局 Landscape

> 待其他窗口补充。

- [ ] （待补充）

---

## G · 模型档案库 Model Registry　【本窗口，已推进】

> 目录：`registry/`；模型档案：`registry/models/`。

### 已完成（存档，无需再做）

- [x] `models/deepseek-v3.md`：历史文件名保留，主体已更新为 DeepSeek-V4 Pro 0813；核实官方版本、1M/384K、峰谷价、缓存价、API 兼容与 Artificial Analysis。
- [x] `models/qwen3.8-max.md`：核实百炼托管版规格、地域价、限流，以及 `Qwen3.8-2.4T-A95B` 开放权重配置；明确两者能力边界。
- [x] `models/openai-gpt.md`：更新为 GPT-5.6 Sol；核实 1.05M/128K、Standard/Batch/Flex/Fast、缓存及 272K 长上下文阶梯价。
- [x] `models/anthropic-claude.md`：更新为 Claude Fable 5；核实 1M/128K、缓存、Batch、美国境内推理、数据保留与 Artificial Analysis 口径。
- [x] `models/google-gemini.md`：更新为 Gemini 3.1 Pro Preview；核实多模态、1M/64K、200K 阶梯价、Batch、缓存与官方基准。
- [x] 五个模型均已逐页核实 OpenRouter 模型页与 Endpoints API，补充模型 ID、Provider、渠道价格、缓存和参数支持。
- [x] `registry/index.md`：已更新旗舰对比、官方价格结构、OpenRouter 渠道对比、来源优先级及 MaaS/TokenHub 选型摘要。
- [x] 站点已重新生成并检查：25 条目 / 5 档案；`git diff --check` 与相关文件 lint 均通过。

### P0 · 影响选型与成本结论

- [ ] **我方真实商业数据**　`registry/models/*.md`
  - 待核实：`our_price`、`cost`、`gross_margin`、`call_volume`、供应商折扣、汇率、税费和失败重试成本。
  - 动作：接入我方结算与调用数据，按模型/Provider/地域/处理层计算真实单位成本和毛利。
- [ ] **我方链路性能与稳定性**　`registry/models/*.md`
  - 待核实：P50/P95 TTFT、输出吞吐、429/5xx、超时、中断率、任务成功率与 SLA。
  - 动作：对官方直连与 OpenRouter 各主要 Provider 使用统一请求集压测；不能用 Artificial Analysis 或 OpenRouter 公共监控替代我方实测。
- [ ] **云渠道合同与数据条款**　`models/openai-gpt.md`、`models/anthropic-claude.md`、`models/google-gemini.md`
  - 待核实：Azure、AWS Bedrock、Google Vertex、BYOK 的合同价、区域、数据保留、数据驻留和服务等级。
  - 动作：以我方实际合同/控制台为准；OpenRouter 公共端点价只作渠道参考。

### P1 · 榜单与模型字段补全

- [ ] **LMArena 当前 Elo**　`registry/models/*.md`、`registry/index.md`
  - 现状：官方域名重定向到 Arena，web_fetch 被 Cloudflare 阻断，当前保留 `null`。
  - 动作：等待官方可抓取榜单、官方导出/API，或人工提供榜单截图/数据后按精确模型版本回填。
- [ ] **LiveBench 总分与分项**　`registry/models/*.md`、`registry/index.md`
  - 现状：官网仅返回 JavaScript 应用壳，无法核实 reasoning/coding/math 等分项，当前保留 `null`。
  - 动作：查找 LiveBench 官方导出、官方仓库数据或可直接访问的官方接口；禁止抄录二手榜单。
- [ ] **厂商未公开技术字段**　`registry/models/*.md`
  - 待核实：DeepSeek V4、GPT、Claude、Gemini 的参数量、架构、激活参数和精度；厂商未公开前保持 `null`。
- [ ] **固定版本与生命周期**　`models/openai-gpt.md`、`models/qwen3.8-max.md`、`models/google-gemini.md`
  - 待核实：GPT 不可变快照 ID、Qwen 托管 Max 固定快照、Gemini 3.1 Pro 稳定版时间表及知识截止日期。

### P2 · 渠道与运营口径完善

- [ ] **OpenRouter 价格时效机制**　`registry/models/*.md`、`registry/index.md`
  - 待核实：GPT-5.6 Sol 50% 促销截止日期，以及各 Provider 价格、折扣和状态码的更新频率。
  - 动作：后续复核时保存抓取时间，区分模型厂商直连价、OpenRouter 渠道价和我方合同价。
- [ ] **Qwen 开放权重许可证与自部署 TCO**　`models/qwen3.8-max.md`
  - 待核实：`Qwen3.8-2.4T-A95B` 权重许可证、最低硬件、量化损失、吞吐和总拥有成本，以及与托管 Max 的严格等同性。
- [ ] **限流与能力矩阵复核**　`registry/models/*.md`
  - 待核实：各厂商/地域的 RPM、TPM、并发、工具参数、结构化输出和缓存支持；重点补齐当前仍为 `null` 的 `rate_limit`。

---

## 通用备注（跨模块）

- 价格/规格随时变动，已核实数据均标 `verified: 日期`；跨过较长时间再引用前回官方页复核。
- web_fetch 踩坑记录：
  - OpenAI 主定价页 `openai.com/api/pricing` 返回 **403**，改用 `platform.openai.com/docs/pricing`。
  - Anthropic `anthropic.com/pricing` **重定向**到 `claude.com/pricing`。
  - SemiAnalysis 有 **JS 反爬**，web_fetch 取不到正文。
  - vLLM `performance/optimization.html`、`serving/engine_args.html` 均 **404**，改用 `configuration/optimization.html` 与 `api/vllm/config/scheduler.html`（+ GitHub raw 源码）核实。
  - NVIDIA **MIG User Guide 首页为 JS 渲染**、正文只返回导言，改用 NVIDIA A100 MIG 官方技术博客核实 7 实例/隔离机制。
- code-explorer subagent **无联网能力**，联网核实一律走主线程 web_fetch。

---

## 📅 每日学习机制 · 运行 Prompt（明天起新窗口直接用）

> 用途：每天新开一个窗口，把下面【每日运行 Prompt】整段复制发给 AI 即可启动当天的学习共建。
> 机制设计见 `learning-plan.md`；流程规范见 skill `ai-kb-daily`。默认「方式一·会话触发」。

### 【每日运行 Prompt】（复制这段）

```
请加载 ai-kb-daily skill，为我执行今天的 AI 知识库每日学习共建。项目：/Users/beryl/Desktop/Knowledge-Base，知识库在 knowledge/ai/。

我是 MaaS TokenHub 产品经理，深度锚点：理解技术选择背后的成本与商业含义。每天学习 20-30 分钟，偶尔会跳过，请如实打卡。

请严格按以下顺序执行每日流程：

1. 【报告进度】读 knowledge/ai/progress.md，告诉我上次学到哪、当前阶段/模块、以及 TODO.md 里有没有到期该处理的待核实项。

2. 【确认状态】问我今天是「学习」还是「跳过」。若跳过，只在 progress.md 记一笔就结束。

3. 【副轨·情报 5-10 分钟】用 web_fetch 联网拉取过去 24h 的 AI 行业重要更新（依 sources.md 的一手源优先：厂商官方、OpenRouter、Artificial Analysis 等）。每条尝试挂回框架某模块（降价/新价→E/G，新模型→G 建档或更新，技术突破→B/C…）；挂不上的存入 knowledge/ai/inbox/。与我业务强相关（对标友商/供应商动态、模型价格变化）的特别标记提醒我。

4. 【主轨·学习 15-20 分钟】按 learning-plan.md 当前阶段推进【一个】知识点（控制在 20 分钟内，不贪多）。必须用 web_fetch 打开一手源核实后再写，未核实数字标"待核实"，绝不凭记忆编造。若产出/更新条目，按 _templates/entry.md 的完整结构写入对应 entries/<模块>/（含 mermaid 图、超链接出处、「对我的意义★」）；涉及模型的更新 registry/。

5. 【生成呈现物】就今天学的内容，产出：
   - 一份精简的「今日学习卡片」（供我 20-30 分钟消化的推送版，比条目精简）；
   - 基于今日内容出 3-5 题 quiz（选择/判断 + 答案解析）；
   - 一篇小红书文案（标题/正文/标签），配图用 image_gen 生成，存 knowledge/ai/publish/xhs/，提醒我手动发布；
   - 一份播客口播稿存 knowledge/ai/publish/podcast/，提醒我用 TTS 转音频。
   （呈现物的具体形态今天和我边做边确认；我们说好今天首次共建每日页+quiz+小红书+播客。）

6. 【收尾打卡】更新 progress.md（日期/学习或跳过/主轨学了什么/副轨情报要点），并运行 python3 scripts/build_site.py ai 重新生成站点。

能力边界请遵守：你无法生成音频（播客只出文字稿）、无法自动发布（小红书只出文案+配图）、无法看视频（优先找文字载体）。code-explorer subagent 无联网能力，联网一律走主线程 web_fetch。
```

### 备注

- 若想改成**定时自动化**（方式二），可让 AI 用 automation 工具把上面流程建成每日定时任务（如每早 8:30 自动拉情报入 inbox），我有空再看主轨。
- 每日机制会随磨合迭代；如流程有调整，同步更新 skill `ai-kb-daily` 与 `learning-plan.md`。
