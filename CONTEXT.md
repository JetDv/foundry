# Foundry — the pipeline

The flow in one line: **interview the person, decide the shape, write the tree, walk it cold.**

| Stage | Job | Reads | Writes | Human check |
|---|---|---|---|---|
| `01_interview` | surface their structure | the conversation | `output/brief.md` | the brief describes *their* process, not a shape we imposed |
| `02_blueprint` | choose form, stages, gates | `01`'s brief | `output/blueprint.md` | every stage is one job; every gate is a place they actually pause |
| `03_scaffold` | write the tree and contracts | `02`'s blueprint | the emitted workspace + `output/emit-manifest.md` | open the tree; every path in the manifest exists |
| `04_walk-test` | validate cold | the emitted tree | `output/walk-report.md` | every check passes, or the structure changed until it did |

**Factory** (stable, every run): `_shared/` — invariants, canon, forms, house conventions, walk-test protocol.
**Product** (new every run): each stage's `output/`, plus the emitted workspace at its destination.

## Where the product goes

Foundry does not host the ICMs it builds. `03_scaffold` writes the new workspace to a **destination path the human names in the brief** — its own repo, its own project folder. `library/` keeps one record per shipped ICM: what it is, why it took the shape it did, where it lives. One home per fact; the record is a card, never a copy of the tree.

## Status

Status is whatever exists. A stage is COMPLETE when its `output/` holds a real artifact. `.gitkeep` is not an artifact.

A run in flight looks like this:

```
stages/01_interview/output/brief.md     <- exists  -> 01 done
stages/02_blueprint/output/blueprint.md <- exists  -> 02 done
stages/03_scaffold/output/              <- empty   -> you are here
```

## Scope

Two of ICM's six forms: **Pipeline** and **Umbrella**. The other four are sketched in `_shared/forms.md`, which says what to do when a brief lands on one.
