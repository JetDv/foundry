# library — one card per shipped ICM

One job: keep a record of what Foundry has built, why it took the shape it did, and where it lives.

This is a Record library nested inside a Pipeline. The unit is a record, not a run.

## Inputs
- Working (this run): `../stages/04_walk-test/output/walk-report.md`
- Working (this run): `../stages/02_blueprint/output/blueprint.md`
- Reference (every run): `../_templates/library-record.md`

## Process
1. Copy `../_templates/library-record.md` to `{slug}.md` here. The slug is kebab-case and matches the emitted workspace's folder name.
2. Fill it from the blueprint (why this shape, what was rejected) and the walk report (rounds, fixes, over-structure verdict).
3. Fill "What this taught the factory" honestly, including "nothing".
4. Rebuild the index: `python3 _index/rebuild.py`.

## Outputs
- `{slug}.md` -> `library/`
- `_index/log.md` -> regenerated, never hand-edited

## Human check
Open the card six weeks from now and ask whether it explains a decision you no longer remember making. If it does not, it is a filing receipt rather than a record — add the contested call.

## The card is not the tree

A record links to the emitted workspace; it never copies it. One home per fact. If you want to know what is in a workspace, open the workspace.

## Reading the library backwards

Three cards whose "What this taught the factory" says the same thing means `_shared/conventions.md` is wrong. One card saying it is a gripe. Change the convention rather than overriding it a fourth time.
