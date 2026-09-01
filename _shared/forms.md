# The forms

One skeleton, six jobs. Every form obeys the ten invariants; what changes is what the repeating unit is and what the structure optimizes for.

**Foundry builds two of them.** Pipeline and Umbrella are documented here in full. The other four are sketched so a run can *recognize* them and say "this is not a pipeline" instead of forcing a bad fit. When a brief lands on one of the four, stop and say so — a wrong form is more expensive than no workspace.

## Selection — ask one question first

**What is the repeating unit of work?**

| The unit is… | Form | Built here? |
|---|---|---|
| a run (same stages, new deliverable each time) | Pipeline | yes |
| several kinds of runs sharing one identity | Umbrella | yes |
| a record that accumulates (person, client, session) | Record library | sketch only |
| the knowledge itself (claims, notes, evidence) | Knowledge bundle | sketch only |
| an organization (teams, processes, data, handoffs) | Context map | sketch only |
| a folder later agents must edit (code or vault) | System map | sketch only |

## 1. Pipeline — the production line

The canonical shape. The same sequence runs repeatedly with different input, a human reviews at each boundary, a deliverable leaves at the end.

```
workspace/
├─ AGENTS.md               identity + routing table
├─ CLAUDE.md               pointer to AGENTS.md
├─ CONTEXT.md              the pipeline in one screen
├─ stages/
│  ├─ 01_research/    {CONTEXT.md, references/, output/}
│  ├─ 02_script/      {CONTEXT.md, references/, output/}
│  └─ 03_production/  {CONTEXT.md, references/, output/}
├─ _shared/                factory: voice.md, rules.md
├─ _templates/
└─ setup/questionnaire.md  configures the factory once
```

**Defining moves**

- Handoff = one stage's `output/` is the next stage's input. A human edits the file in between; the next stage reads whatever is there.
- Each contract carries an explicit "load this / do NOT load that" inputs table.
- Status is answered by scanning `stages/*/output/` for files.
- Stage boundaries sit where the human naturally pauses to check. Surfacing the judgment call — an outline, a structural plan — as an editable file *before* the expensive downstream work is the whole trick. Correction is cheapest at the earliest gate.

**Expect a U-curve of human editing.** Heavy at the first stage (direction-setting), light in the middle (constrained by both anchors), heavy at the last (aligning output with earlier decisions). Design the first and last outputs to be especially easy to edit.

**Watch for:** stages that do two jobs (split them); contracts that restate reference material (point instead); pipelines built before the process has actually repeated (don't).

## 2. Umbrella — a portfolio of pipelines

Several distinct production lines share one brand, voice, and reference layer. The root is a map, not a sequence.

```
workspace/
├─ AGENTS.md               the map: which pipeline for which job
├─ 01-pillars/             shared factory: positioning
├─ 02-brand-voice/         shared factory: voice, style
├─ 03-video-production/    a full Pipeline workspace (own AGENTS.md)
├─ 04-scene-generation/    a full Pipeline workspace (own AGENTS.md)
└─ 05-animation-studio/    a full Pipeline workspace (own AGENTS.md)
```

**Defining moves**

- Each sub-pipeline is self-contained with its own entry file. They do not share state except through the root reference layers.
- The root entry file routes by task ("talking-head video -> 03; animating a diagram -> 05") and holds nothing else.
- A sub-pipeline may host sibling *patterns* — two variants of the same line — which is the routing move recursing one level down.

**Watch for:** the root map going stale as pipelines evolve (state only what rarely changes; details live in each pipeline); shared reference duplicated down into sub-pipelines (link up instead).

**Reach for Umbrella over Pipeline when** the person describes two or more workflows that "always have to sound the same" but otherwise share no steps. If they share steps, it is one pipeline with a branch at a human gate, not two pipelines.

## The four Foundry does not build yet

Recognize, name, and stop.

- **Record library** — the unit is a record that accumulates (client, person, session). Nothing runs to completion. A new record is a *copy of a template folder*, and an `_index/log.md` is the declared source of truth for what exists and its status.
- **Knowledge bundle** — the deliverable is navigable knowledge itself: a brain, a domain model. Typed YAML frontmatter makes it queryable; layered loading (always-load, then task-relevant, then evidence) is the reading protocol.
- **Context map** — the subject is an organization. Closed set of node types in `_meta/schema.md`; process nodes carry scoring frontmatter; the workshop *is* the data event, and ends in node files rather than slides.
- **System map** — the subject is a tree someone will change. Object cards for nouns, process cards for verbs, an `effects/` index answering "what else moves if I change X."

If a brief lands here, say which form it is, say Foundry does not build it, and offer either a hand-built structure or [icm-architect](https://github.com/RinDig/icm-architect), which does.

## Composing

The forms nest, because the invariants are recursive. A pipeline can emit into a record library; an umbrella can draw on one knowledge bundle as its factory layer. Foundry itself is a Pipeline with a Record library (`library/`) attached.

One rule is absolute when composing: **each level has its own small catalog, and no level's catalog describes the internals of the level below.** It links down and stops.
