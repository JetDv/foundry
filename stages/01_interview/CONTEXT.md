# 01_interview — surface their structure

One job: get the person's actual process onto paper. Do not design anything here.

## Inputs
- Working (this run): the conversation with the person
- Reference (every run): `references/question-set.md`
- Reference (every run): `../../_shared/invariants.md`

Do NOT load: `../../_shared/forms.md`. Choosing a form in this stage is the single most common way a run goes wrong — you start steering answers toward the shape you already picked. The form is `02`'s job.

## Process
1. Work through `references/question-set.md`. A few questions at a time, never all at once.
2. Write down their words, not your paraphrase. "It has to sound like Dave wrote it" goes in as that sentence.
3. Where they pause to check something, mark it as a candidate gate. Where they say "it always has to X", mark it as candidate factory reference.
4. Fill `../../_templates/brief.md`. Leave anything they did not say blank. **A blank is information; an invented answer is damage.**
5. Ask the destination path and write it down. `03` cannot emit without it.

## Outputs
- `brief.md` -> `output/`

## Human check
Read the brief back to them, out loud or pasted in. They should recognize their own process, including the parts that are messy. If they say "well, sort of, but…", that "but" is the real structure — go back to step 2. Edit the brief in place; `02` reads whatever is here.
