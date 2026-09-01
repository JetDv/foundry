# 04_walk-test — validate cold

One job: prove a stranger can run the emitted workspace from the files alone.

## Inputs
- Working (this run): the emitted workspace at the destination in `../03_scaffold/output/emit-manifest.md`
- Reference (every run): `../../_shared/walk-test.md`
- Reference (every run): `references/report-format.md`
- Reference (every run): `references/check-paths.py`

Do NOT load: `../01_interview/output/brief.md` or `../02_blueprint/output/blueprint.md` **until the checks are scored**. Reading them first is how a workspace passes a walk test it should have failed — you fill gaps from memory without noticing. Read them afterward, only to explain a failure.

## Process
1. Run `python3 references/check-paths.py {destination}` first. Check 2 is not verifiable by reading, and a broken input path stays invisible until the run that needs it.
2. Run all ten checks in `../../_shared/walk-test.md` against the emitted tree, in order.
3. Score each PASS / FAIL / N/A with one line of evidence: a path, a line count, a quote. Bare verdicts are not evidence the test ran.
4. Run the over-structure check last and answer it honestly, including when the answer is embarrassing.
5. For each FAIL, fix the structure — move, split, cut. Never fix it by adding an explanation to a file.
6. Re-run **all ten** after any fix. Fixes interact; a fix for orientation routinely breaks the catalog-holds-no-books check.
7. Write the report using `references/report-format.md`.

## Outputs
- `walk-report.md` -> `output/`

## Human check
Read the over-structure verdict first, before the ten checks. If it says this could have been a saved prompt, that is the decision to make, on the terms `../../_shared/walk-test.md` sets out. If it passes, file the library record from `../../_templates/library-record.md` and the run is closed.
