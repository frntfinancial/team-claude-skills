---
name: generating-morning-notes
description: Generates daily crypto morning notes by running FRNT Crypto Index analysis scripts. Use when user asks for "morning notes", "morning note", "crypto index", "daily report", or "market analysis".
---

## Quick Start

Say: "Give me the morning notes" or "Run the morning note"

## Prerequisites

```bash
pip install requests pandas
```

## Instructions

1. Run BOTH scripts from the skill's scripts directory:
```bash
cd ~/.claude/skills/team/research/generating-morning-notes/scripts
python3 morning_note_netcoinsversion.py
python3 morning_note.py
```

2. Extract ONLY these values from each script's output:
   - FRNT Crypto Index percentage
   - Top Performer name, symbol, and change %
   - Top Underperformer name, symbol, and change %

3. Save to `morning-note-YYYY-MM-DD.md` using EXACTLY this format (no tables, no extra data):

```markdown
# Morning Note - [Full Date]

## Netcoins Version
- **FRNT Crypto Index:** [value]%
- **Top Performer:** [name] ([symbol]) [change]%
- **Top Underperformer:** [name] ([symbol]) [change]%

## Global (Top 20 by Market Cap)
- **FRNT Crypto Index:** [value]%
- **Top Performer:** [name] ([symbol]) [change]%
- **Top Underperformer:** [name] ([symbol]) [change]%
```

4. Report the file path when complete.

IMPORTANT: Keep output concise. Do NOT add tables, market commentary, asset lists, or additional sections. Just the 6 data points above.
