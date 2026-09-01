# Foundry

The ICM that builds ICMs. One run in, one new workspace out.

Built on ICM — Interpretable Context Methodology (Van Clief & McDermott, arXiv:2603.16021, MIT): folders carry sequencing, hierarchy carries context scoping, plain files carry state. The structure is the documentation. If something needs explaining, the explanation goes in that folder's `CONTEXT.md` — not in a wiki, not in your head.

## Where things live

| Folder | What it holds |
|---|---|
| `stages/` | the four stages of a design run, in execution order |
| `_shared/` | factory: the canon plus this workspace's house conventions. Stable across every run. |
| `_templates/` | blank starters. New work is a copy, never a blank page. |
| `setup/` | one-time configuration of this factory |
| `library/` | one record per ICM shipped from here |

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| someone wants a new ICM | `stages/01_interview/CONTEXT.md` | human reads `brief.md` |
| the brief is approved | `stages/02_blueprint/CONTEXT.md` | human reads `blueprint.md` |
| the blueprint is approved | `stages/03_scaffold/CONTEXT.md` | human opens the emitted tree |
| the tree is written | `stages/04_walk-test/CONTEXT.md` | human reads `walk-report.md` |
| the walk test passes | `library/CONTEXT.md` | record filed, run closed |
| asked for status | scan `stages/*/output/` | report what exists |
| a structural call is contested | `_shared/invariants.md`, then `_shared/icm-core.md` | — |
| configuring Foundry itself | `setup/questionnaire.md` | answers land in `_shared/conventions.md` |

## The one rule

Nothing moves to the next stage until a person has read the output of the last one.

## Entry files

`AGENTS.md` is canonical here and in everything Foundry emits; `CLAUDE.md` is a pointer. Rationale and the rule: `_shared/conventions.md`.
