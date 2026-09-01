# Emit order

Write in this order. It is not arbitrary: each step is checkable before the next one depends on it.

1. **Destination check.** Per `../../../_shared/conventions.md`, Emission.
2. **Directory skeleton.** All folders, no files. Now you can see the shape and compare it to the blueprint before any content exists.
3. **Stage contracts** (`CONTEXT.md`, one per working folder). Write these *before* the entry file — the entry file's routing table is derived from them, and deriving it the other way round produces routes to folders that do not do what the route claims.
4. **Root `CONTEXT.md`.** The stage table, condensed from the contracts you just wrote.
5. **`AGENTS.md`.** Identity plus routing. Now check the line count: over 60 means content leaked in.
6. **`CLAUDE.md` pointer.** Three lines.
7. **`_shared/` files.** Named by the blueprint, content from the brief.
8. **`_templates/`**, if any unit of work repeats.
9. **`README.md`, `.gitignore`,** `setup/questionnaire.md` if needed.
10. **`git init` and one commit.**
11. **Manifest.**

## Rules while writing

- **Copy, then fill.** Every file starts as a template from `../../../_templates/`. Composing from memory is how conventions drift.
- **Placeholder discipline.** A template slot you cannot fill from the brief stays as an obvious marker — `{TODO: ...}` — never a plausible invention. A plausible invention is indistinguishable from a real answer six weeks later.
- **Exact paths in contracts.** `../01_research/output/research.md`, never "the previous stage's output". The path is the interface.
- **No `.gitkeep` in a folder that has real content coming this run.** Use it only for `output/` folders that are genuinely empty until the first run.
- **Never name a template file `AGENTS.md` or `CLAUDE.md`** — prefix them. Reason: `../../../_shared/conventions.md`, What never gets created.

## Before you call it done

- Line-count `AGENTS.md` against the cap in `../../../_shared/invariants.md` #2. Over it is a fail, not a style note.
- Grep the tree for `{` — any surviving template placeholder should be a deliberate `{TODO}`, not a forgotten `{stage-name}`.
- Confirm every relative path in every contract resolves. A broken input path is invisible until the run that needs it.
