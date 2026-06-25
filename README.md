# Learn Any Topic Skill

An advanced AI agent skill designed to help you learn and master any common topic for which sufficient resources can be found on the internet. 

Unlike typical one-off AI explanations that often lack depth or structure, this skill uses a highly structured, loop-based approach to prepare comprehensive, publication-grade learning materials for you. It guides the AI agent through a rigorous 7-step cycle—from framing the learning objectives and mapping authoritative sources to designing knowledge structures, drafting continuous explanations, generating formatted artifacts, and running automated programmatic quality checks.

### Key Highlights
- **Multi-Platform Support**: Installs as a full Skill folder for Antigravity (Gemini), OpenAI Codex, Cursor, Windsurf, GitHub Copilot, and Claude Code.
- **Authority-Backed Source Ladder**: Replaces generic search results with a strict 5-tier evaluation system prioritizing official standards, textbooks, and recognized reference materials.
- **Coherent Scaffolding**: Moves beyond fragmented bullet points to deliver continuous explanations, clear mental models, progressive examples, and practical self-checks.
- **Automated Quality Review**: Features an integrated Python linting script (`review_tutorial.py`) that scans drafts for placeholders, weak structures, and vague phrasing to ensure a high-fidelity final output.

## What It Does

When activated, the agent follows a structured 7-step workflow:

1. **Confirm Tutorial Language** — Confirm with the user which language to write in
2. **Frame the Learning Job** — Identify topic, learner, depth, output format
3. **Build the Source Map** — Prioritize authoritative sources using a 5-tier ladder
4. **Design the Knowledge Map** — Structure prerequisites, concepts, terms, examples, practice
5. **Write the Tutorial** — Produce clear, connected explanations (not disconnected bullet lists)
6. **Generate the Artifact** — Output as Markdown, Word, PDF, or other requested format
7. **Review, Find Gaps, Revise** — Run quality checks on coverage, sources, terminology, coherence

## Supported Platforms

Install this repository as a full Skill folder. The final directory should contain `SKILL.md`, `scripts/`, and `references/`.

| Platform / Tool | Project Skill location |
| :--- | :--- |
| **Antigravity (Gemini)** | `.agents/skills/learn-any-topic/SKILL.md` |
| **OpenAI Codex** | `.agents/skills/learn-any-topic/SKILL.md` |
| **Cursor** | `.cursor/skills/learn-any-topic/SKILL.md` |
| **Windsurf (Codeium)** | `.windsurf/skills/learn-any-topic/SKILL.md` |
| **GitHub Copilot** | `.github/skills/learn-any-topic/SKILL.md` |
| **Claude Code** | `.claude/skills/learn-any-topic/SKILL.md` |

## Installation

There are two ways to install this skill: using the automated CLI or downloading it manually.

### 1. Automated Installation (Recommended)

If you have Node.js installed, the easiest way is to use the `skills` CLI. It will automatically detect which AI tool you are using (like Cursor, Windsurf, or Claude Code) and place the skill files in the correct directory for you.

```bash
npx skills add SimulAffect/learn-any-topic-skill
```

### 2. Manual Installation (`git clone`)

If you prefer to install it manually, you can clone this repository. You will need to know the specific folder where your AI tool expects Skill folders to be placed (replace `<your-skills-dir>` with that path):

```bash
git clone --depth 1 https://github.com/SimulAffect/learn-any-topic-skill.git <your-skills-dir>/learn-any-topic
```

To update the skill later, run:

```bash
cd <your-skills-dir>/learn-any-topic && git pull
```

### 3. Codex Installation

If you are using OpenAI Codex, it has its own built-in installer. Run this command inside Codex:

```text
$skill-installer install https://github.com/SimulAffect/learn-any-topic-skill
```

After installing, please restart Codex so it can recognize the new skill.

## Directory Structure

```
learn-any-topic/
├── SKILL.md                    # Core skill file
├── README.md                   # This file
├── scripts/
│   └── review_tutorial.py      # Automated tutorial quality checker
└── references/
    ├── source-quality.md       # Source evaluation guidelines
    └── tutorial-framework.md   # Chapter skeleton and depth controls
```

## review_tutorial.py

A lightweight Python 3 script (standard library only) that checks tutorial drafts for common issues:

- Placeholder patterns (`TODO`, `TBD`, `FIXME`, `{{...}}`)
- Negative openings (defining what something is *not* before what it *is*)
- Overuse of generic wording ("better", "great", "simple", etc.)
- Missing source references, glossary, or practice sections
- Weak heading structure in long documents

Supports both English and Chinese text.

```bash
python3 scripts/review_tutorial.py path/to/your-tutorial.md
```

## License

This skill is released as open source. See LICENSE for details.

---

# Learn Any Topic Skill（中文说明）

这是一个先进的 AI Agent Skill，旨在帮助你系统地学习和掌握任何一个在网络中能获得足够资料的常见主题。

与常见的、往往缺乏深度或结构的一次性 AI 回答不同，本 Skill 采用了一种**结构化的闭环（Loop）方式**来为你准备高质量、系统化的学习资料。它引导 AI 助手遵循严格的 7 步循环工作流——从明确学习目标与受众、梳理权威来源地图，到设计知识地图与大纲、撰写连贯的教学内容、生成规范的交付文档，并最终通过自动化脚本进行针对性的质量审查与迭代优化，确保交付结果具有极高的完整性与实用价值。

### 核心亮点
- **多平台支持**：以完整 Skill 文件夹的方式安装到 Antigravity (Gemini)、OpenAI Codex、Cursor、Windsurf、GitHub Copilot 以及 Claude Code。
- **权威来源分级**：告别泛泛的网络搜索，采用严格的 5 级来源评估机制，优先采用官方标准、学术教材和行业规范。
- **渐进式连贯讲解**：杜绝碎片化的要点堆砌，以连贯的叙事逻辑、清晰的思想模型、渐进式的实例和实用的自测练习，构筑完整的认知闭环。
- **自动化质量把控**：内置 Python 质量审查脚本（`review_tutorial.py`），智能检测占位符、否定性定义、空泛词汇及结构缺陷，以代码级别的严谨性保障教程品质。

## 功能概述

激活后，AI 助手将遵循结构化的 7 步工作流：

1. **确认教程语言** — 与用户确认教程应以何种语言撰写
2. **明确学习任务** — 确定主题、学习者、深度、输出格式
3. **构建来源地图** — 使用 5 级来源分级体系优先选取权威资料
4. **设计知识地图** — 组织前置知识、核心概念、术语、示例、练习
5. **撰写教程** — 产出清晰、连贯的讲解（而非零散的要点列表）
6. **生成交付物** — 输出为 Markdown、Word、PDF 或其他指定格式
7. **审查、查漏、修订** — 对覆盖度、来源质量、术语、连贯性进行质量检查

## 支持的平台

请把这个仓库作为完整 Skill 文件夹安装。最终目录里应同时包含 `SKILL.md`、`scripts/` 和 `references/`。

| 平台 / 工具 | 项目级 Skill 位置 |
| :--- | :--- |
| **Antigravity (Gemini)** | `.agents/skills/learn-any-topic/SKILL.md` |
| **OpenAI Codex** | `.agents/skills/learn-any-topic/SKILL.md` |
| **Cursor** | `.cursor/skills/learn-any-topic/SKILL.md` |
| **Windsurf (Codeium)** | `.windsurf/skills/learn-any-topic/SKILL.md` |
| **GitHub Copilot** | `.github/skills/learn-any-topic/SKILL.md` |
| **Claude Code** | `.claude/skills/learn-any-topic/SKILL.md` |

## 安装方式

你可以选择使用自动化工具安装，或者手动克隆代码。

### 1. 自动安装（推荐）

如果你安装了 Node.js，最简单的方法是使用 `skills` 命令行工具。它会自动识别你正在使用的 AI 编辑器（例如 Cursor、Windsurf 或 Claude Code），并将文件下载到正确的目录中，无需你手动指定路径。

```bash
npx skills add SimulAffect/learn-any-topic-skill
```

### 2. 手动安装（Git Clone）

如果你想手动安装，可以直接克隆这个仓库。你需要知道你的 AI 工具通常把 Skill 文件夹放在哪个目录（请将下方代码中的 `<your-skills-dir>` 替换为实际的路径）：

```bash
git clone --depth 1 https://github.com/SimulAffect/learn-any-topic-skill.git <your-skills-dir>/learn-any-topic
```

如果后续需要更新，可以运行：

```bash
cd <your-skills-dir>/learn-any-topic && git pull
```

### 3. Codex 平台

如果你使用的是 OpenAI Codex，它内置了自己的安装命令。请在 Codex 中运行：

```text
$skill-installer install https://github.com/SimulAffect/learn-any-topic-skill
```

安装完成后，请重启 Codex 以使新 skill 生效。

## 目录结构

```
learn-any-topic/
├── SKILL.md                    # 核心 skill 文件
├── README.md                   # 本文件
├── scripts/
│   └── review_tutorial.py      # 自动化教程质量检查脚本
└── references/
    ├── source-quality.md       # 来源评估指南
    └── tutorial-framework.md   # 章节骨架与深度控制
```

## review_tutorial.py

一个轻量级的 Python 3 脚本（仅依赖标准库），用于检查教程草稿中的常见问题：

- 占位符模式（`TODO`、`TBD`、`FIXME`、`{{...}}`）
- 否定式开头（先说某事物「不是什么」而非「是什么」）
- 泛化用词过多（如 "更好"、"很好"、"简单" 等）
- 缺少来源引用、术语表或练习部分
- 长文档中标题结构薄弱

支持英文和中文文本检测。

```bash
python3 scripts/review_tutorial.py path/to/your-tutorial.md
```

## 许可证

本 skill 以开源形式发布。详见 LICENSE 文件。
