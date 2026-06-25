# Learn Any Topic Skill

An advanced AI coding agent skill designed to help you learn and master any common topic for which sufficient resources can be found on the internet. 

Unlike typical one-off AI explanations that often lack depth or structure, this skill uses a highly structured, loop-based approach to prepare comprehensive, publication-grade learning materials for you. It guides the AI agent through a rigorous 7-step cycle—from framing the learning objectives and mapping authoritative sources to designing knowledge structures, drafting continuous explanations, generating formatted artifacts, and running automated programmatic quality checks.

### Key Highlights
- **Multi-Platform Integration**: Native configurations tailored for Antigravity (Gemini), OpenAI Codex, Cursor, Windsurf, GitHub Copilot, and Claude Code.
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

| Platform | Format | Install Path |
|---|---|---|
| **Antigravity** (Gemini) | SKILL.md + scripts + references | `.agents/skills/learn-any-topic/` |
| **OpenAI Codex** | SKILL.md + scripts + references | `.codex/skills/learn-any-topic/` |
| **Cursor** | `.mdc` rule file | `.cursor/rules/` |
| **Windsurf** (Codeium) | `.md` rule file | `.windsurf/rules/` |
| **GitHub Copilot** | `.instructions.md` file | `.github/instructions/` |
| **Claude Code** (Anthropic) | `.md` rule file | `.claude/rules/` |

## Installation

### Antigravity / Codex (full skill with scripts)

Copy the entire directory to your project:

```bash
cp -r learn-any-topic/ .agents/skills/learn-any-topic/   # Antigravity
cp -r learn-any-topic/ .codex/skills/learn-any-topic/     # Codex
```

### Cursor / Windsurf / Copilot / Claude Code (rules only)

Copy the platform-specific file from `platforms/`:

```bash
# Cursor
cp platforms/cursor/learn-any-topic.mdc .cursor/rules/

# Windsurf
cp platforms/windsurf/learn-any-topic.md .windsurf/rules/

# GitHub Copilot
cp platforms/copilot/learn-any-topic.instructions.md .github/instructions/

# Claude Code
cp platforms/claude/learn-any-topic.md .claude/rules/
```

## Directory Structure

```
learn-any-topic/
├── SKILL.md                    # Core skill (Antigravity/Codex format)
├── README.md                   # This file
├── scripts/
│   └── review_tutorial.py      # Automated tutorial quality checker
├── references/
│   ├── source-quality.md       # Source evaluation guidelines
│   └── tutorial-framework.md   # Chapter skeleton and depth controls
└── platforms/
    ├── README.md               # Platform comparison and install guide
    ├── cursor/
    │   └── learn-any-topic.mdc
    ├── windsurf/
    │   └── learn-any-topic.md
    ├── copilot/
    │   └── learn-any-topic.instructions.md
    └── claude/
        └── learn-any-topic.md
```

## Platform Differences

- **Full skill support** (Antigravity, Codex): The agent can read `references/` files for deeper guidance and run `scripts/review_tutorial.py` for automated quality checks.
- **Rules only** (Cursor, Windsurf, Copilot, Claude Code): The workflow instructions are embedded directly in the rule file. Script execution and reference file reading are not supported; the essential content from `references/` is inlined into these versions.

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

这是一个先进的 AI 编程助手 Skill，旨在帮助你系统地学习和掌握任何一个在网络中能获得足够资料的常见主题。

与常见的、往往缺乏深度或结构的一次性 AI 回答不同，本 Skill 采用了一种**结构化的闭环（Loop）方式**来为你准备高质量、系统化的学习资料。它引导 AI 助手遵循严格的 7 步循环工作流——从明确学习目标与受众、梳理权威来源地图，到设计知识地图与大纲、撰写连贯的教学内容、生成规范的交付文档，并最终通过自动化脚本进行针对性的质量审查与迭代优化，确保交付结果具有极高的完整性与实用价值。

### 核心亮点
- **多平台深度集成**：原生适配 Antigravity (Gemini)、OpenAI Codex、Cursor、Windsurf、GitHub Copilot 以及 Claude Code，提供量身定制的配置与指令。
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

## 支持平台

| 平台 | 格式 | 安装路径 |
|---|---|---|
| **Antigravity**（Gemini） | SKILL.md + 脚本 + 参考文档 | `.agents/skills/learn-any-topic/` |
| **OpenAI Codex** | SKILL.md + 脚本 + 参考文档 | `.codex/skills/learn-any-topic/` |
| **Cursor** | `.mdc` 规则文件 | `.cursor/rules/` |
| **Windsurf**（Codeium） | `.md` 规则文件 | `.windsurf/rules/` |
| **GitHub Copilot** | `.instructions.md` 文件 | `.github/instructions/` |
| **Claude Code**（Anthropic） | `.md` 规则文件 | `.claude/rules/` |

## 安装方式

### Antigravity / Codex（完整 skill，含脚本）

将整个目录复制到项目中：

```bash
cp -r learn-any-topic/ .agents/skills/learn-any-topic/   # Antigravity
cp -r learn-any-topic/ .codex/skills/learn-any-topic/     # Codex
```

### Cursor / Windsurf / Copilot / Claude Code（仅规则文件）

从 `platforms/` 目录复制对应平台的文件：

```bash
# Cursor
cp platforms/cursor/learn-any-topic.mdc .cursor/rules/

# Windsurf
cp platforms/windsurf/learn-any-topic.md .windsurf/rules/

# GitHub Copilot
cp platforms/copilot/learn-any-topic.instructions.md .github/instructions/

# Claude Code
cp platforms/claude/learn-any-topic.md .claude/rules/
```

## 目录结构

```
learn-any-topic/
├── SKILL.md                    # 核心 skill（Antigravity/Codex 格式）
├── README.md                   # 本文件
├── scripts/
│   └── review_tutorial.py      # 自动化教程质量检查脚本
├── references/
│   ├── source-quality.md       # 来源评估指南
│   └── tutorial-framework.md   # 章节骨架与深度控制
└── platforms/
    ├── README.md               # 平台对比与安装指引
    ├── cursor/
    │   └── learn-any-topic.mdc
    ├── windsurf/
    │   └── learn-any-topic.md
    ├── copilot/
    │   └── learn-any-topic.instructions.md
    └── claude/
        └── learn-any-topic.md
```

## 平台差异

- **完整 skill 支持**（Antigravity、Codex）：AI 助手可以读取 `references/` 下的参考文档以获得更深入的指导，并运行 `scripts/review_tutorial.py` 进行自动化质量检查。
- **仅规则文件**（Cursor、Windsurf、Copilot、Claude Code）：工作流指令直接嵌入规则文件中。不支持脚本执行和参考文件读取；`references/` 中的核心内容已内联到这些版本中。

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
