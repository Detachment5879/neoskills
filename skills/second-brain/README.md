# 🧠 Second Brain Skill

> *把 AI Agent 变成你的第二大脑——自动将碎片信息转化为结构化的 Obsidian 知识库。*

[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-blueviolet)](https://github.com/neolaf2/neoskills)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-7C3AED)](https://obsidian.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 这是什么

**Second Brain** 是一个为 Hermes Agent 设计的 Skill，让 AI Agent 充当你的**知识架构师**：

- 🎯 **输入任意碎片信息** — 会议记录、聊天截图、阅读笔记、突发灵感、行业资讯
- 🧹 **自动去噪提纯** — 过滤口水话，只提取高信息密度的干货
- 🧠 **知识建模** — 自动生成标签、提取实体、建立双向链接
- 📝 **生成 Obsidian Markdown** — 标准化的、可被 Obsidian 完美渲染的知识节点
- 🔗 **知识图谱** — 实体关联、WikiLink、自动维护索引
- 🔍 **智能检索** — 基于知识库回答问题，并在回答中保持知识库的同步更新

## 效果预览

### 输入 → 输出

<table>
<tr>
<td width="50%"><strong>你输入的碎片信息</strong></td>
<td width="50%"><strong>Agent 自动生成的笔记</strong></td>
</tr>
<tr>
<td>

```
今天和张三讨论新项目架构。
决定用微服务，后端 Go，前端 React。
每个团队负责一个模块。
```

</td>
<td>

```markdown
---
tags:
  - #programming
  - #architecture
  - #meeting-note
date: 2026-05-11
type: meeting-note
---

# 新项目架构讨论

## 核心决议
- 采用 [[微服务架构]]
- 后端：[[Go]]
```

</td>
</tr>
</table>

### 知识库结构

```
second-brain/
├── meetings/       # 会议记录
├── readings/       # 阅读笔记
├── ideas/          # 灵感
├── insights/       # 行业洞察
├── technical/      # 技术笔记
├── people/         # 人物笔记
├── concepts/       # 概念解释
├── inbox/          # 待整理
├── logs/           # 操作日志
└── .index.md       # 自动维护的索引
```

## 安装

### 通过 neoskills

```bash
# 如果你使用 neoskills 管理 Hermes Skills
neoskills tap add second-brain https://github.com/Detachment5879/neoskills
neoskills link second-brain
```

### 手动安装

```bash
# 克隆 neoskills 仓库
git clone https://github.com/Detachment5879/neoskills ~/.neoskills/taps/neoskills

# 或直接复制 skill 目录
cp -r skills/second-brain ~/.hermes/skills/second-brain
```

### 配置

设置知识库路径（可选，默认 `~/Documents/second-brain`）：

```bash
echo 'OBSIDIAN_VAULT_PATH="$HOME/Documents/my-knowledge-base"' >> ~/.hermes/.env
```

## 使用

### 模式 1：知识录入

```
@brain 今天和张三讨论新项目架构。决定用微服务，后端 Go...

@brain 记下来：我发现一个有意思的心理学概念叫"心流"...

帮我整理这段会议记录：[粘贴内容]

保存这个灵感：[粘贴内容]
```

### 模式 2：知识查询

```
@brain 查一下微服务相关的内容

@brain 我记得之前讨论过关于 React 状态管理

@brain 关于 [[张三]] 我们有哪些记录？
```

### 模式 3：知识库维护

```
@brain maintain
```

## 支持的内容类型

| 类型 | 说明 | 存储目录 |
|------|------|---------|
| `meeting-note` | 会议/沟通记录 | `meetings/` |
| `reading-note` | 学习笔记/阅读摘录 | `readings/` |
| `insight` | 行业资讯/文章 | `insights/` |
| `idea` | 个人灵感/想法 | `ideas/` |
| `retrospective` | 经验教训/复盘 | `retrospectives/` |
| `technical-note` | 技术文档/教程 | `technical/` |
| `person` | 人物笔记 | `people/` |
| `concept` | 概念解释 | `concepts/` |

## 技术栈

- **Hermes Agent** — CLI AI Agent 平台
- **Obsidian** — 个人知识库前端（完美渲染 Markdown + WikiLink + 图谱）
- **Python 3** — 笔记写入工具

## 原理

```
用户输入碎片信息
    ↓
Hermes Agent + Second Brain Skill
    ↓  (1. 判断类型  2. 提取实体  3. 建模标签)
    ↓
生成标准化的 Obsidian Markdown 笔记
    ↓
存入知识库 + 更新索引 + 记录变更
    ↓
后续查询 → 检索知识库 → 综合回答
```

## License

MIT
