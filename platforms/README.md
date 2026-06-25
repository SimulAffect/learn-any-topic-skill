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

Instead of manual copying, you can install the configuration directly in your project root using the following commands:

### For Single-File Rule IDEs
Download the rule file directly using `curl` (macOS/Linux) or PowerShell (Windows):

- **Cursor**:
  - *macOS/Linux:* `curl -fsSL --create-dirs https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/cursor/learn-any-topic.mdc -o .cursor/rules/learn-any-topic.mdc`
  - *PowerShell:* `New-Item -ItemType Directory -Force -Path .cursor/rules; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/cursor/learn-any-topic.mdc" -OutFile ".cursor/rules/learn-any-topic.mdc"`
- **Windsurf**:
  - *macOS/Linux:* `curl -fsSL --create-dirs https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/windsurf/learn-any-topic.md -o .windsurf/rules/learn-any-topic.md`
  - *PowerShell:* `New-Item -ItemType Directory -Force -Path .windsurf/rules; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/windsurf/learn-any-topic.md" -OutFile ".windsurf/rules/learn-any-topic.md"`
- **GitHub Copilot**:
  - *macOS/Linux:* `curl -fsSL --create-dirs https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/copilot/learn-any-topic.instructions.md -o .github/instructions/learn-any-topic.instructions.md`
  - *PowerShell:* `New-Item -ItemType Directory -Force -Path .github/instructions; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/copilot/learn-any-topic.instructions.md" -OutFile ".github/instructions/learn-any-topic.instructions.md"`
- **Claude Code**:
  - *macOS/Linux:* `curl -fsSL --create-dirs https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/claude/learn-any-topic.md -o .claude/rules/learn-any-topic.md`
  - *PowerShell:* `New-Item -ItemType Directory -Force -Path .claude/rules; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/SimulAffect/learn-any-topic-skill/master/platforms/claude/learn-any-topic.md" -OutFile ".claude/rules/learn-any-topic.md"`

### For Full-Skill Platforms (Antigravity / Codex)
Download the entire directory using `git clone` or `npx degit`:
- *Git Clone (macOS/Linux):* `git clone --depth 1 https://github.com/SimulAffect/learn-any-topic-skill.git .agents/skills/learn-any-topic && rm -rf .agents/skills/learn-any-topic/.git`
- *Git Clone (PowerShell):* `git clone --depth 1 https://github.com/SimulAffect/learn-any-topic-skill.git .agents/skills/learn-any-topic; Remove-Item -Recurse -Force .agents/skills/learn-any-topic/.git`
- *npx degit:* `npx degit SimulAffect/learn-any-topic-skill .agents/skills/learn-any-topic`

## Notes

- **Cursor** and **Windsurf** use rule-based systems with no script execution support. The `review_tutorial.py` script instructions are omitted from those versions.
- **GitHub Copilot** and **Claude Code** have partial support. The skill is embedded as instructions; no agent auto-discovery is available.
- The `references/` and `scripts/` directories are only usable on platforms that support skill subdirectories (Antigravity, Codex).
