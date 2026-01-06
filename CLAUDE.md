# Team Claude Skills Repository

This repository contains shared Claude Code skills for the FRNT team.

## Skill Authoring Rules

1. **Naming**: Use gerund form (verb + -ing), lowercase, hyphens only
2. **SKILL.md**: Keep under 500 lines, use progressive disclosure
3. **Descriptions**: Third-person, include trigger phrases, max 1024 chars
4. **References**: Keep file references one level deep from SKILL.md

## Directory Ownership

- `backend/` - Brandon (Node.js, infrastructure, APIs)
- `frontend/` - Adnan (React, UI, components)
- `research/` - Strah (Python, data analysis, market research)
- `shared/` - Cross-functional (anyone can contribute)

## Testing Skills

Before merging, test with:
1. Sonnet (default) - does it work?
2. Haiku - does it need more guidance?
3. Opus - is anything over-explained?

## Common Patterns

### Tech-Agnostic Wrapper
Wrap implementation details so users don't need to know the underlying tech:
```markdown
description: Generates X by executing Y scripts. Use when user asks for "X".
```

### Handoff Context
Generate summaries for async team handoffs with full context.
