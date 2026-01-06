---
name: generating-handoff-context
description: Generates comprehensive context summaries for async team handoffs. Use when user says "create handoff", "handoff summary", "I'm leaving for the day", or needs to pass work to another team member.
---

## Quick Start

Say: "Create a handoff summary for this work"

## What This Does

Generates a structured handoff document including:
- Current work state (what's done, what's in progress)
- Open issues and blockers
- Recent changes (git commits, file modifications)
- Next steps and recommendations
- Any context the next person needs

## Output Format

```markdown
# Handoff Summary - [Date]

## Current State
[Summary of where things stand]

## Completed
- [x] Item 1
- [x] Item 2

## In Progress
- [ ] Item 3 (blocked by X)

## Blockers
- [Description of any blockers]

## Recent Changes
- [Recent commits or file changes]

## Next Steps
1. [Recommended next action]
2. [Follow-up item]

## Context Notes
[Any additional context the next person needs]
```

## Usage Scenarios

1. **End of day**: "I'm done for today, create a handoff"
2. **Vacation**: "Create a handoff summary before I leave"
3. **Pairing**: "Summarize where we are for Adnan to continue"
