# Platform-Specific Configurations

This directory contains ready-to-use configuration files for different AI coding tools. Each file adapts the **learn-any-topic** skill to the target platform's format.

## Supported Platforms

| Platform | File | Install Location |
|---|---|---|
| **Antigravity (Gemini)** | Use the root `SKILL.md` directly | `.agents/skills/learn-any-topic/` |
| **OpenAI Codex** | Use the root `SKILL.md` directly | `.codex/skills/learn-any-topic/` |
| **Cursor** | `cursor/learn-any-topic.mdc` | `.cursor/rules/` |
| **Windsurf** | `windsurf/learn-any-topic.md` | `.windsurf/rules/` |
| **GitHub Copilot** | `copilot/learn-any-topic.instructions.md` | `.github/instructions/` |
| **Claude Code** | `claude/learn-any-topic.md` | `.claude/rules/` |

## Installation

1. Choose the file matching your AI coding tool.
2. Copy it to the corresponding install location in your project root.
3. For **Antigravity** and **Codex**, copy the entire `learn-any-topic/` directory (including `scripts/` and `references/`).
4. For other platforms, copy only the platform-specific file — scripts and references are not supported by those platforms.

## Notes

- **Cursor** and **Windsurf** use rule-based systems with no script execution support. The `review_tutorial.py` script instructions are omitted from those versions.
- **GitHub Copilot** and **Claude Code** have partial support. The skill is embedded as instructions; no agent auto-discovery is available.
- The `references/` and `scripts/` directories are only usable on platforms that support skill subdirectories (Antigravity, Codex).
