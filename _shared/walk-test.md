# The walk test

The validation protocol. An ICM is finished when an agent **with no memory of building it** can orient, act, and report status from the files alone. Not when it looks tidy.

Run this against the emitted tree in `04_walk-test`, reading only what a cold agent would read. Do not use anything you remember from `01`–`03`; that knowledge is exactly what the test is checking the files carry on their own.

## The checks

| # | Check | Passes when |
|---|---|---|
| 1 | **Orientation** | Opening the root, you can answer *where am I* and *where do I go for the current task* from the entry file plus at most two more reads. |
| 2 | **Contracts** | Pick any working folder. Its `CONTEXT.md` names exact input paths, the single job, the output filename, and one concrete human check. |
| 3 | **Status** | You can state where a run stands purely by scanning `output/` folders — no log file, no memory, no asking. |
| 4 | **Catalog holds no books** | No routing file (`AGENTS.md`, root `CONTEXT.md`) carries content payload. If one does, move the payload to a shelf and leave a pointer. |
| 5 | **One home per fact** | No fact is stated in two files. If it is, pick one home and link from the other. |
| 6 | **Token budget** | Entry file + one contract + its declared inputs lands inside the band in `icm-core.md`, Token discipline. Measure the largest stage, not the smallest. |
| 7 | **Entry files** | Exactly one canonical entry file. Every other one is a pointer, and says so in its own text. |
| 8 | **No empty scaffolding** | Every folder that exists holds something real, with one exemption: a stage `output/` folder awaiting its first run may hold only `.gitkeep`. Any other `.gitkeep`-only folder is filled or removed. |
| 9 | **Gates are real** | Each human check names something a person physically does. "Review the output" fails; "read it aloud and confirm the argument order survived" passes. |
| 10 | **The one rule is stated** | The workspace says somewhere, in its own words, that nothing advances until a person has read the last output. |

## Scoring

Report each check as PASS, FAIL, or N/A with one line of evidence — a path, a line count, a quote. A walk report with ten bare PASSes is not evidence that the test was run.

## When a check fails

**Fix the structure, not the explanation.** The failure mode to avoid is adding a paragraph telling the agent what it should have been able to see. Move a file, split a folder, cut a section, delete a stage. Then re-run the whole test — fixes interact, and #4 is routinely broken by a fix for #1.

If two full rounds do not clear it, the form is probably wrong. Go back to `02_blueprint` rather than patching further.

## The over-structure check

Run this last, and answer it honestly:

> Could this have been a saved prompt?

The ladder runs chat -> saved prompt or skill -> folders plus one agent. Only climb when the rung below is genuinely automated and repeating. **A workspace for a thing someone has done twice is scaffolding, not architecture.** If the answer is yes, say so in the walk report and let the human decide. Shipping a workspace nobody needed is a worse outcome than a short conversation.
