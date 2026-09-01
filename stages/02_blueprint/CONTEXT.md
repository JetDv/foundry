# 02_blueprint — decide the shape

One job: turn the brief into a named form, a stage list, and a gate at every boundary. Write it down before anything gets built.

## Inputs
- Working (this run): `../01_interview/output/brief.md`
- Reference (every run): `../../_shared/forms.md`
- Reference (every run): `../../_shared/icm-core.md`
- Reference (every run): `../../_shared/conventions.md`

Do NOT load: the destination folder, `../../_templates/`, or anything under `../03_scaffold/`. Nothing is written this stage.

## Process
1. Answer the selection question from `forms.md`: what is the repeating unit? Name the form. If it is one of the four Foundry does not build, stop here and say so in the blueprint — that is a complete and correct output.
2. Derive stages from the brief's gates. **Their pauses are the boundaries.** One job per stage; if a stage's description needs an "and", split it.
3. For each stage write the row: name, the one job in five words, inputs, output filename, and the human check as something a person physically does.
4. Split the brief's "always" items into `_shared/` files and name each one.
5. Write down what you rejected and why — the form you did not pick, the stage you merged. `04` and the library record both read this.
6. Sanity-check the count against `../../_shared/conventions.md`, What never gets created. More than five stages means justify each one in writing, or merge.

## Outputs
- `blueprint.md` -> `output/`

## Human check
Walk the stage table with the person. For each gate ask: "would you actually stop here?" A gate they would blow straight through is not a gate — merge those stages. Edit in place; `03` builds exactly what this file says.
