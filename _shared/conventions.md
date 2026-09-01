# House conventions

The decisions Foundry does not re-litigate. Every emitted workspace inherits these unless a brief overrides one *and says why*. This file is the reason Foundry exists: it is the information that would otherwise be re-explained on every new ICM.

Filled by `setup/questionnaire.md`. Sections marked **[unset]** have not been configured yet — a run should ask once and write the answer here, not ask again next time.

## Entry files

- **`AGENTS.md` is canonical.** It holds the identity and the routing table. Every emitted workspace gets one.
- **`CLAUDE.md` is a pointer**, three lines, no content: a title, a link to `AGENTS.md`, and a line saying it is a pointer.
- Any future harness with its own convention gets the same treatment — a new pointer file, never a second copy. If a harness ever demands real content in its own file, generate that file from `AGENTS.md` with a script and say so in the workspace's README.
- **Rationale:** duplicated entry files that drift are the single most common ICM failure. One home per fact applies to the entry file first.

## Naming

The scheme is in `icm-core.md`, Naming. It is not restated here; that file is the one home.

The house additions to it:

- Machine-facing throughout, no exceptions by default. If a workspace will be browsed daily by a human in Obsidian, Title Case is the one permitted exception — decide it once per workspace and write the choice into that workspace's schema. Drift between a declared convention and the actual filenames is the most common form of decay.
- Zero-padded stage numbers always, even below ten. `01_`, never `1_`.

## What every emitted workspace gets

Non-negotiable, regardless of form:

- `AGENTS.md` (within the cap in `invariants.md` #2) + `CLAUDE.md` pointer
- root `CONTEXT.md` — the pipeline or schema in one screen
- one `CONTEXT.md` per working folder, with Inputs / Process / Outputs / Human check
- `_shared/` for anything stable across runs
- `_templates/` if any unit of work repeats
- `README.md` — for humans and for GitHub; it is not an entry file and agents are not routed to it
- `.gitignore`

## What never gets created

- Folders for stages that do not exist yet.
- Empty "misc", "notes", or "assets" buckets.
- Speculative depth. Three real stages beat seven imagined ones.
- A second hand-maintained entry file.
- A `_templates/` folder containing files literally named `AGENTS.md` or `CLAUDE.md` — harnesses auto-load those by name wherever they sit. Prefix them: `entry-AGENTS.md`.

## Emission

- `03_scaffold` writes the new workspace to the **destination path named in the brief**. Foundry does not host what it builds.
- The destination must be empty or must not exist. If it holds files, stop and hand it to the human — that is a Restructure job, which Foundry does not do.
- Every emitted workspace is initialized as its own git repo with one commit. It is a separate history from Foundry's.
- After the walk test passes, file a card in `library/` from `_templates/library-record.md`. The card, never a copy of the tree.

## Runtimes this targets

Claude Code, Cowork, and any harness that reads `AGENTS.md`. The convention above is chosen so that a harness nobody has heard of yet costs one pointer file, not a migration.

## Voice and defaults — [unset]

Run `setup/questionnaire.md`. Until then, emitted contracts use plain declarative English, second person for instructions to the agent, and no filler.

## Overrides log

When a brief overrides a convention, record it here in one line: date, workspace, what was overridden, why. Three independent overrides of the same convention means the convention is wrong — change it here rather than overriding a fourth time.

| Date | Workspace | Override | Why |
|---|---|---|---|
| 2026-09-01 | Foundry (itself) | Shipped despite failing its own over-structure check | The cold walk returned "this should have been a skill": ~9.5k tokens total, no long-running state, no branching, and zero runs in `library/`. Kept anyway, deliberately. The claim to test is that the `01_interview` and `02_blueprint` gates earn their keep against a real interview — which is not knowable by argument. **Revisit when `library/` holds two cards.** If neither card's walk report shows a gate that changed the outcome, collapse `stages/` into a skill and keep only `_shared/`, `_templates/`, and `library/`. |
