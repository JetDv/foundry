# The ten invariants

Every ICM obeys these, whatever its form, at every level of nesting. When a structural call is contested, this file settles it. Adapted from icm-architect (MIT).

1. **One folder, one job.** Each folder does a single step or holds a single kind of thing, and states its own purpose in a file inside itself. The structure is the documentation.
2. **A small, stable entry file.** `AGENTS.md` at the root answers "where am I, where does everything live, where do I go for task X" — and nothing else. Target under ~60 lines. It routes; it never holds content.
3. **Numbering encodes order.** `01_`, `02_`, … wherever sequence matters. Renaming folders reorders the pipeline — that is the point.
4. **Every folder-level contract is explicit.** A `CONTEXT.md` per working folder: what it reads, what it does, what it writes, what a human checks.
5. **Factory vs. product.** Reference material — rules, voice, schemas, templates, stable across runs — lives structurally apart from working artifacts, which are new every run. Configure the factory once; the product is what each run emits.
6. **Every output is an edit surface.** Intermediate outputs are plain files a human can open, edit, and save before the next step reads them. Nothing moves forward until a person has read the last output.
7. **Load only what the step needs.** An agent executing a step reads its contract, its references, and its inputs — not the whole workspace. The healthy per-step range is in `icm-core.md`, Token discipline.
8. **Plain text, linkable, queryable.** Markdown plus YAML frontmatter. Links make it a graph; frontmatter labels make it queryable. One home per fact — a link beats a copy.
9. **The filesystem is the state machine.** Status is derivable by scanning what exists in output folders. Generated indexes are rebuilt by script, never hand-edited.
10. **Instantiate by copying.** New unit of work = copy a template folder, not a blank page. Templates live together in `_templates/`.

## The three that get violated first

In practice, decay starts here — check these before the others:

- **#2**, when the entry file starts absorbing content because it was convenient. Symptom: it is over 60 lines. Fix: move the payload to a shelf, leave a pointer.
- **#8**, when a fact gets copied instead of linked "just this once." Symptom: two files state the same rule and one is now wrong. Fix: pick one home, link from the other.
- **#9**, when someone hand-edits a generated index. Symptom: the index and the tree disagree. Fix: regenerate, and script the rebuild.
