# Walk report format

```markdown
# Walk report — {workspace name}

Destination: {path}
Walked: {date}
Rounds: {how many times the checks were run}

## Verdict

{PASS | PASS WITH FIXES | FAIL} — {one sentence}

## Over-structure check

Could this have been a saved prompt? **{yes | no}** — {one sentence of reasoning}

## Checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Orientation | PASS | AGENTS.md line 12 routes "new episode" -> stages/01_source/ |
| 2 | Contracts | FAIL -> fixed | 03_edit named no input path; now line 6 |
| … | | | |

## Fixes made

- {what moved, and which check it was fixing}

## Known gaps

- {anything left as {TODO}, and who owes the answer}
```

## Rules

- **Evidence is a path, a line number, a count, or a quote.** "Looks good" is not evidence.
- **A fix gets its own row in Fixes made**, naming the check it served. That list is what the library record summarizes.
- **Round count matters.** One round means the checks were run once and everything passed — rare and worth being suspicious of. Three or more rounds on the same check means the form is probably wrong; say so and send it back to `02_blueprint`.
- **Known gaps are not failures**, but an unrecorded gap is. Every surviving `{TODO}` goes in the list with the name of whoever owes the answer.
