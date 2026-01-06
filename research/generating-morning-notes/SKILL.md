---
name: generating-morning-notes
description: Generates daily crypto morning note from both analysis scripts. Use when user asks for "morning notes", "morning note", or "daily report".
---

# Morning Note Skill

Generate the daily crypto morning note by running both analysis scripts and saving the output to a file.

## Instructions

1. Run `python3 morning_note_netcoinsversion.py` in `~/.claude/skills/team/research/generating-morning-notes/scripts/`
2. Run `python3 morning_note.py` in `~/.claude/skills/team/research/generating-morning-notes/scripts/`
3. Combine the outputs into a single markdown file named `morning-note-YYYY-MM-DD.md` (using today's date)
4. The output file should be structured as:

```markdown
# Morning Note - [DATE]

## Netcoins Version
- **FRNT Crypto Index:** [value]%
- **Top Performer:** [name] ([symbol]) [change]%
- **Top Underperformer:** [name] ([symbol]) [change]%

## Global (Top 20 by Market Cap)
- **FRNT Crypto Index:** [value]%
- **Top Performer:** [name] ([symbol]) [change]%
- **Top Underperformer:** [name] ([symbol]) [change]%
```

5. Report the file path to the user when complete
