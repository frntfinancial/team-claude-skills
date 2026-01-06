---
name: generating-morning-notes
description: Generates daily crypto morning notes by running FRNT Crypto Index analysis scripts. Use when user asks for "morning notes", "morning note", "crypto index", "daily report", or "market analysis".
---

## Quick Start

Say: "Give me the morning notes" or "Run the morning note"

## What This Does

Calculates the **FRNT Crypto Index** - a market-cap weighted index of the top 20 cryptocurrencies (excluding stablecoins and wrapped tokens). Fetches live data from CoinGecko API.

Runs two analysis scripts:
1. **Netcoins version** - Index + top/bottom performers from Netcoins asset list (63 assets)
2. **Global version** - Index + top/bottom performers from top 20 by market cap globally

## Prerequisites

```bash
pip install requests pandas
```

## Execution

Run from the skill's scripts directory:

```bash
cd ~/.claude/skills/team/research/generating-morning-notes/scripts
python3 morning_note_netcoinsversion.py
python3 morning_note.py
```

## Output Format

Save combined output to `morning-note-YYYY-MM-DD.md`:

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

Report the file path when complete.
