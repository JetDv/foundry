# ICM core

The canon, distilled from arXiv:2603.16021 and production workspaces. Read when writing contracts or checking a workspace against the method.

## The five design principles

1. **One stage, one job** (Unix / Parnas). A stage that fetches does not also filter; a stage that filters does not also format.
2. **Plain text as the interface** (Kernighan & Pike). Stages communicate through markdown and JSON. No binary formats, no databases in the loop. Any human with a text editor can inspect or modify any artifact.
3. **Layered context loading.** Agents load only what the current stage needs — prevention, not compression. Reference material (internalize as constraints) stays structurally separate from working artifacts (process as input), because they ask different things of the model.
4. **Every output is an edit surface** (Horvitz / Shneiderman). The next stage reads whatever the human left there.
5. **Configure the factory, not the product** (continuous delivery). Set up voice, brand, rules and structure once; every run emits a new deliverable from the same configuration.

The consequence, stated once: *stage sequencing is the folder numbering; context scoping is the folder hierarchy; state management is the files on disk; coordination is one folder's output being another folder's input.* The filesystem does the work a framework would do in code.

## The five-layer context hierarchy

| Layer | Typical file | Question it answers | Role | Size |
|---|---|---|---|---|
| L0 | `AGENTS.md` | Where am I? | routing | 300–800 tokens |
| L1 | root `CONTEXT.md` | Where do I go? | routing | 200–500 tokens |
| L2 | stage `CONTEXT.md` | What do I do? | **the control point** | 200–500 tokens |
| L3 | `_shared/`, `references/` | What rules apply? | factory (stable) | 500–2k tokens |
| L4 | `output/`, run artifacts | What am I working with? | product (per-run) | varies |

- L0–L2 are the catalog: small, stable, no content payload.
- L2 is the control surface of the whole system. Its Inputs section is what makes context selection explicit, editable and auditable instead of left to agent judgment.
- L3 vs L4 is the factory/product split. L3 = the recipe (`voice.md`, `schema.md`). L4 = the ingredients and the dish (`research.md`, `draft.md`).
- Large L3 collections get their own internal `CONTEXT.md` router — the L1 pattern applied recursively. The hierarchy is self-similar at every depth.

## Stage contract format

Copy `_templates/stage-CONTEXT.md`. The shape:

```markdown
# 02_script — turn research into a script

One job: write the script from the research output.

## Inputs
- Working (this run): ../01_research/output/research.md
- Reference (every run): ../../_shared/voice.md

Do NOT load: other stages' references, prior runs, the whole _shared folder.

## Process
1. Read the research output.
2. Draft to the structure in structure.md, in the tone of voice.md.
3. Keep under 90 seconds spoken.

## Outputs
- script_draft.md -> output/

## Human check
Read the draft aloud. Verify the argument order survived from research. Edit in place; the next stage reads whatever is here.
```

Rules: inputs are exact paths, split working vs reference. The process is numbered and short — constraints live in L3 files, not restated here. Exactly one human check, stated as something a person *does*, never a vague "review."

## Naming

- Stage folders `NN_kebab-name` (`01_research`). Ordinal-only prefixes (`00-tracker.md`) for ordered files inside a folder.
- Meta folders take an underscore and sort to the top: `_shared/`, `_templates/`, `_index/`, `_archive/`. Underscore means "about the workspace, not of the work."
- Entry file `AGENTS.md`; `CLAUDE.md` is a pointer to it, never a second copy.
- Templates are blank, named for what they produce, and live together.

## Token discipline

A stage's full context — entry + contract + references + inputs — should land around **2,000–8,000 tokens**. A monolithic everything-prompt for the same pipeline typically runs 30k–50k, most of it irrelevant to the current step. ICM never loads those tokens rather than compressing them later. If a stage balloons: split the stage, tighten the Inputs list, or push detail into an L3 file the contract points at but does not inline.

## Where ICM loses

Name these honestly rather than overclaiming:

- **Real-time multi-agent collaboration** — tight response loops need message-passing infrastructure; file handoffs are too slow.
- **High concurrency** — many users on one pipeline needs queueing, state isolation, deployment. ICM is local-first by design.
- **Automated mid-pipeline branching** — a *human* choosing stage 3a vs 3b is natural; the *system* branching on AI output mid-run pushes ICM toward becoming the framework it replaced.

The claim is not that ICM replaces frameworks everywhere. It is that for sequential, human-reviewed, repeatable work — most knowledge work — a framework is more complexity than the problem requires, and that complexity costs opacity, fragility, and developer dependency.
