# KSTAR Loop Record — Task 4

## Task: Create a new neoskills skill (`git-snapshot`) from scratch

### K — Knowledge (已知/目标)

**目标：** 为 neoskills 仓库贡献一个实用的新 skill。neoskills 是一个管理 AI agent skill 的工具。我需要创建一个能在仓库中快速捕获 git 状态快照的 skill。

**已知：**
- neoskills 的 skill 结构：每个 skill 是一个目录，含 `SKILL.md` 文件
- 已有 skills 示例：`skills/bank-status/SKILL.md`、`skills/skill-dedup/SKILL.md`
- Skill 使用 YAML frontmatter + Markdown body 格式
- neoskills 的框架：skills 放在 `skills/` 目录下

### S — Search (搜索/探索)

**探索已有参考：**
- 查看了 `skills/bank-status/SKILL.md` — 学习 frontmatter 格式（name, description, tags）
- 查看了 `skills/skill-dedup/SKILL.md` — 学习了 scripts/ 目录结构
- 查看了仓库的 tructure：skills/ 目录下放 skill 子目录

**关键发现：**
- Skill 需要清晰的 Instructions 部分
- Output Format 部分让 skill 有标准输出
- 可以附加 scripts/ 目录包含可执行代码

### T — Think (思考/规划)

**设计决策：**
- 名称：`git-snapshot` — 简洁明了
- 内容：快速捕获 git 状态（status + recent commits + diff stat）
- 格式：使用 SKILL.md 标准 frontmatter + 三个主要 section
- 输出：标准化的 markdown 报告格式

**为什么不加脚本？**
- 这个 skill 主要是 agent 的 instructions，不需要额外脚本
- git 命令本身就是"工具"，SKILL.md 告诉 agent 如何使用它们

### A — Act (行动/执行)

**实际操作：**
1. 创建了目录 `skills/git-snapshot/`
2. 创建了 `skills/git-snapshot/SKILL.md` 文件
3. 编写了 frontmatter (name, description)
4. 编写了 Instructions section（三步流程）
5. 编写了 Output Format section（结构化报告模板）
6. 将文档与 KSTAR 循环记录一起 commit

### R — Reflect (反思/总结)

**学到了什么：**
- neoskills 的 skill 格式非常简洁：SKILL.md + 可选 scripts/
- Frontmatter 的标准化设计让 skill 可被自动发现和索引
- Skill 本质上是一份"给 AI agent 的指令文档"，不需要复杂实现

**改进点：**
- 未来可以给 git-snapshot 添加一个 `scripts/git-snapshot.py` 自动化脚本
- 可以添加 `ontology.yaml` 让它升级到 L1（Tagged）级别

**KSTAR 循环价值：** 从知道要做什么 → 搜索参考 → 思考设计 → 动手执行 → 反思总结，这个循环让每次创作都更有效率，而不是盲目开始。

---

## Verification

新 skill 路径：`skills/git-snapshot/SKILL.md`

```bash
# 验证：可以在仓库中找到它
ls skills/git-snapshot/
```

内容预览：
- name: git-snapshot
- description: Quick git status snapshot
- 包含 Instructions (3步) 和 Output Format (结构化模板)
