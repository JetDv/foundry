# 03_scaffold — write the tree

One job: build exactly what the blueprint specifies, at the destination named in the brief.

## Inputs
- Working (this run): `../02_blueprint/output/blueprint.md`
- Working (this run): `../01_interview/output/brief.md` — for the destination path and the person's own wording only
- Reference (every run): `../../_shared/conventions.md`
- Reference (every run): `references/emit-order.md`
- Reference (every run): `../../_templates/` — copy from here; do not compose from memory

Do NOT load: `../../_shared/forms.md`. The form was decided in `02`. Re-deciding it here means the blueprint and the tree disagree, and the tree wins silently.

## Process
1. Check the destination. It must be empty or must not exist. If it holds files, **stop** and hand it back — restructuring an existing folder is not a job Foundry does.
2. Create the tree from the blueprint's stage table. Create nothing the blueprint does not name.
3. Copy templates and fill them: `entry-AGENTS.md` -> `AGENTS.md`, `entry-CLAUDE.md` -> `CLAUDE.md`, `root-CONTEXT.md` -> `CONTEXT.md`, `stage-CONTEXT.md` -> one per stage.
4. Write the `_shared/` files the blueprint named. Content comes from the brief's "always" items, in the person's own words.
5. Write `README.md`, `.gitignore`, and `setup/questionnaire.md` if the factory needs per-user configuration.
6. `git init`, one commit. The emitted workspace has its own history.
7. Write `emit-manifest.md`: every path created, one per line, and the destination.

## Outputs
- the emitted workspace -> the destination path in the brief
- `emit-manifest.md` -> `output/`

## Human check
Open the destination folder in a file browser and read `AGENTS.md` first, as a stranger would. Every path in the manifest should exist and nothing should be there that the blueprint did not ask for. Do not fix problems by editing the manifest.
