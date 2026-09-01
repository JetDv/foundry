# {Workspace name} — the pipeline

The flow in one line: {plan it, make it, check it, ship it — in their words}.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `01_{name}` | {five words} | {what it reads} | `output/{file}` | {what a person verifies} |
| `02_{name}` | {five words} | `01`'s output | `output/{file}` | {what a person verifies} |
| `03_{name}` | {five words} | `02`'s output | `output/{file}` | {what a person verifies} |

**Factory** (stable, every run): `_shared/{voice.md, rules.md, …}`
**Product** (new every run): each stage's `output/`

## Status

Status is whatever exists. A stage is COMPLETE when its `output/` holds a real artifact — a `.gitkeep` holding an empty folder in git does not count.
