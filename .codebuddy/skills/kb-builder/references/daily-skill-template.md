# 每日 skill 生成模板 (daily-skill-template)

> 被 kb-builder 的 SKILL.md 引用（步骤 5）。指导为新领域生成 `<domain>-kb-daily` skill。
> 参考实现样板：`.codebuddy/skills/ai-kb-daily/`。

## 生成步骤

1. 初始化：
   ```bash
   python3 <skill-creator>/scripts/init_skill.py <domain>-kb-daily --path <repo>/.codebuddy/skills
   ```
2. 删除生成的示例文件（scripts/example.py、assets/example_asset.txt、references/api_reference.md）。
3. 按下方结构写 `SKILL.md` 与 `references/presentation.md`。
4. 校验打包（会自动先校验）：
   ```bash
   python3 <skill-creator>/scripts/package_skill.py <repo>/.codebuddy/skills/<domain>-kb-daily ./dist
   ```
   校验通过后删除临时 `dist/`。
5. **注意**：frontmatter 的 `description` **不得含尖括号 `<` `>`**（校验器会拒绝）；用普通引号字符串，勿用 YAML `>-` 折叠语法。

## SKILL.md 必备内容

### frontmatter
- `name`: `<domain>-kb-daily`
- `description`: 一段话，含触发语（「开始今天的学习」「拉最新资讯」「做今天的小红书/播客」「backfill」）与该 skill 做什么。**无尖括号**。

### 正文段落
1. **目的**：驱动 `knowledge/<domain>/` 的每日共建与首次全量填充。
2. **何时使用**：列触发意图。
3. **关键背景**：骨架文档位置（framework/sources/learning-plan/progress）、用户画像与深度锚点、节奏（每天 X 分钟、可跳过、必打卡）。
4. **能力边界（必须诚实声明）**：
   - 无后台自动运行（仅对话时联网，默认会话触发）。
   - 无法生成音频（播客只出文字稿，需用户 TTS）。
   - 无法自动发布（小红书只出文案+AI 配图，用户手动发）。
   - 无法看视频/听音频（优先找文字载体，否则返回用户自学）。
   - 信息鲜度（事实联网核实，`null` 不瞎填）。
5. **两种运行模式**：`backfill`（全量首建，广度优先）/ `daily`（每日增量）。
6. **每日流程（按序）**：
   1) 读 progress.md 报告进度 → 2) 确认今天学习/跳过 → 3) 副轨情报（联网拉 24h，挂框架/进 inbox）
   → 4) 主轨学习（一手源翻译，按模板写入 entries/，含「对我的意义」，更新 registry）
   → 5) 生成呈现物（HTML+quiz / 小红书 / 播客） → 6) 更新 progress.md 打卡。
7. **数据写入规范**：条目进 `entries/<模块>/`；实体档案进 `registry/`；情报进 `inbox/`；来源可追溯。
8. **呈现层**：引用 `references/presentation.md`。
9. **迭代**：实跑发现卡点则更新 skill 与骨架文档。

## references/presentation.md 必备内容

- **数据流图**：唯一数据源 `knowledge/<domain>/*.md` → 构建脚本 → HTML/quiz/小红书/播客。
- **静态站点结构**：`site/` 下 index / daily/YYYY-MM-DD / modules/ / assets/。
- **quiz**：基于当天内容出 3-5 题，内嵌当日页，纯前端交互。
- **小红书**：`publish/xhs/YYYY-MM-DD.md`（标题/正文/标签 + AI 配图），待用户手动发布。
- **播客**：`publish/podcast/YYYY-MM-DD.md`（口播全文 + 分段标记），待用户 TTS 转音频。
- **构建脚本约定**：复用 `shared/`；站点为构建产物，改源不改产物；待积累若干真实条目后再落地脚本。

## 领域差异提示

- 「主轨学什么」依赖该库 `framework.md` 的模块与阶段。
- 「registry 写什么」依赖该库 `registry/_schema.md` 的实体字段。
- 「情报挂哪」依赖该库 framework 的模块划分。
- **呈现形态因领域而异**：HTML/小红书/播客只是 AI 库的选择。新领域可能改用数据表格、时间线、看板等，甚至不做社媒/音频呈现。呈现形态须在 kb-builder 步骤 4 与用户确认，不照搬。
- **前端复用优先**：需要构建 HTML/前端时，先查找可复用的成熟前端 skill（find-skills 或 GitHub），不从零手写。
- 生成时把上述占位替换为该领域的实际模块名、实体名、深度锚点。
