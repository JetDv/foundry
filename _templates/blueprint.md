---
workspace: "{name}"
form: "{Pipeline | Umbrella}"
destination: "{absolute path}"
stages: {n}
---

# Blueprint — {workspace name}

## The repeating unit

{one line, from the brief}

## Form

**{Pipeline | Umbrella}** — {why this one, in one or two sentences}

Rejected: {the form considered and dropped, and what would have to be true for it to win}

## Stages

| Stage | One job (five words, no "and") | Inputs | Output | Human check |
|---|---|---|---|---|
| `01_{name}` | {job} | {exact paths} | `output/{file}` | {something a person does} |
| `02_{name}` | {job} | `../01_{name}/output/{file}` | `output/{file}` | {something a person does} |

## Factory files

| File | Holds | Source in the brief |
|---|---|---|
| `_shared/{name}.md` | {what} | {which "always" item} |

## Decisions and rejections

- {stage merged, and why}
- {gate dropped because they would blow through it}
- {convention overridden, and why — also log this in `_shared/conventions.md`}

## Count check

{n} stages. {If more than five: one line justifying each, or merge.}
