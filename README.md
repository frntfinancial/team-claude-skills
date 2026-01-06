# FRNT Team Claude Skills

Shared Claude Code skills for the FRNT team. These skills abstract implementations across different tech stacks (Node.js, Python) so any team member can use them.

## Installation

```bash
# Clone the repo
git clone git@github.com:frntfinancial/team-claude-skills.git ~/team-claude-skills

# Symlink into your Claude skills directory
ln -s ~/team-claude-skills ~/.claude/skills/team
```

## Usage

Once installed, skills are available in Claude Code. Just describe what you need:

- "Give me the morning notes" → runs `generating-morning-notes`
- "Create a handoff summary" → runs `generating-handoff-context`

## Directory Structure

```
team-claude-skills/
├── backend/                     # Brandon's domain (Node.js/backend)
├── frontend/                    # Adnan's domain (UI/React)
├── research/                    # Strah's domain (Python/data)
└── shared/                      # Cross-functional skills
```

## Skill Authoring Standards

Per [Anthropic best practices](https://console.anthropic.com/docs/en/agents-and-tools/agent-skills/best-practices):

### Naming Convention
Use gerund form (verb + -ing):
- `generating-morning-notes`
- `analyzing-market-data`
- `creating-components`

### Structure
```
skill-name/
├── SKILL.md          # Main instructions (< 500 lines)
├── REFERENCE.md      # Detailed docs (loaded on demand)
├── EXAMPLES.md       # Usage examples (optional)
└── scripts/          # Executable utilities (optional)
```

### SKILL.md Format
```markdown
---
name: skill-name-here
description: Third-person description including trigger phrases. Max 1024 chars.
---

## Quick Start
[How to invoke the skill]

## What This Does
[Brief explanation]

## Detailed Reference
See [REFERENCE.md](REFERENCE.md) for details.
```

## Contributing

1. Create a new directory under the appropriate domain
2. Follow the naming and structure standards above
3. Test with multiple models (Sonnet, Haiku, Opus)
4. Submit a PR for team review

## Team

- **Brandon** - Backend skills (Node.js, infrastructure)
- **Adnan** - Frontend skills (React, UI components)
- **Strah** - Research skills (Python, data analysis)
