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
- `README.md` — for humans and for GitHub; it is not an entry file and agents are not routed to it. It carries the ICM attribution line: method is Van Clief & McDermott, arXiv:2603.16021, MIT.
- `.gitignore`
- `LICENSE` — MIT unless the brief says otherwise. ICM is MIT-licensed and these workspaces are derivative of it; shipping without a licence file is an omission, not a neutral default.
- `check-paths.py`, copied in from Foundry's `stages/04_walk-test/references/`. An emitted workspace must be able to re-check its own paths after someone renumbers a stage, without needing Foundry present. This is the one script Foundry duplicates on purpose — the alternative is a workspace that silently rots the first time it is edited.

## What never gets created

- Folders for stages that do not exist yet.
- Empty "misc", "notes", or "assets" buckets.
- Speculative depth. Three real stages beat seven imagined ones.
- A second hand-maintained entry file.
- A `_templates/` folder containing files literally named `AGENTS.md` or `CLAUDE.md` — harnesses auto-load those by name wherever they sit. Prefix them: `entry-AGENTS.md`.

## Emission

- `03_scaffold` writes the new workspace to the **destination path named in the brief**. Foundry does not host what it builds.
- **Default destination: `C:\Users\OmegaSheb\dev\{workspace-name}`.** Used when a brief names a workspace but no path. Emitted workspaces sit beside other code, each its own repo.
- **No remote is created.** `03_scaffold` runs `git init` and one commit, and stops there. Creating a GitHub remote is a human decision made after the walk test passes — a workspace that failed its walk test should not already have a URL.
- The destination must be empty or must not exist. If it holds files, stop and hand it to the human — that is a Restructure job, which Foundry does not do.
- Every emitted workspace is initialized as its own git repo with one commit. It is a separate history from Foundry's.
- After the walk test passes, file a card in `library/` from `_templates/library-record.md`. The card, never a copy of the tree.

## Runtimes this targets

Claude Code, Cowork, and any harness that reads `AGENTS.md`. The convention above is chosen so that a harness nobody has heard of yet costs one pointer file, not a migration.

## When a workspace is warranted

**Three.** A process must have run three times before it gets a workspace instead of a saved prompt or a skill.

This is the same number ICM uses for cross-team patterns — one occurrence is a gripe, three independent occurrences are structure — and one threshold is easier to hold than two. `01_interview` asks the count and records it in the brief; a brief reporting fewer than three is not a failed interview, it is a correct one, and the right output is a saved prompt plus a note to revisit.

The ladder: chat -> saved prompt or skill -> folders plus one agent. Only climb when the rung below is genuinely automated and repeating.

## Contract voice

Plain declarative English, second person to the agent, no filler. Beyond that, two habits are deliberate and emitted contracts keep them:

- **A "Do NOT load" line carries its reason, in one sentence.** Not `Do NOT load: _shared/forms.md` but that plus *why* — "choosing a form in this stage is the single most common way a run goes wrong." A prohibition without a reason gets edited away by the first person who doesn't know what it was protecting. One sentence, never a paragraph.
- **A rule may carry an aphorism when the aphorism is the memorable half.** "A blank is information; an invented answer is damage." "Correction is cheapest at the earliest gate." These survive being half-remembered, which is how rules actually get applied. One per contract at most — past that it reads as a writer enjoying themselves, and the reader starts skimming.

Both habits exist for the same reason: a contract is read by someone who was not in the room when it was written. Write for that person.

The model for every emitted contract is `stages/01_interview/CONTEXT.md`.

## Overrides log

When a brief overrides a convention, record it here in one line: date, workspace, what was overridden, why. Three independent overrides of the same convention means the convention is wrong — change it here rather than overriding a fourth time.

| Date | Workspace | Override | Why |
|---|---|---|---|
| 2026-09-01 | Foundry (itself) | Shipped despite failing its own over-structure check | The cold walk returned "this should have been a skill": ~9.5k tokens total, no long-running state, no branching, and zero runs in `library/`. Kept anyway, deliberately. The claim to test is that the `01_interview` and `02_blueprint` gates earn their keep against a real interview — which is not knowable by argument. **Revisit when `library/` holds two cards.** If neither card's walk report shows a gate that changed the outcome, collapse `stages/` into a skill and keep only `_shared/`, `_templates/`, and `library/`. |
