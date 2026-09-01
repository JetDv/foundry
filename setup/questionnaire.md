# Setup — configure Foundry once

These answers go into `_shared/conventions.md`, into the sections marked **[unset]**. Every run reads them. **No run should ever ask them again** — if a run finds itself asking, the answer never got written down, and writing it down is part of finishing.

**Answered 2026-09-01. All five are written into `_shared/conventions.md`.** Re-run only if a convention stops fitting.

Answer what you know. A blank stays blank; a plausible guess written into the factory propagates into every workspace Foundry ever emits.

---

**1. Default destination root.** When someone names a new workspace but not a path, where do emitted workspaces go by default?
-> `_shared/conventions.md`, Emission

**2. Git remote convention.** Does every emitted workspace get a remote created automatically, and under which account or org? Public or private by default?
-> `_shared/conventions.md`, Emission

**3. Contract voice.** Paste one `CONTEXT.md` you consider well-written, and one you consider bad. The difference is what emitted contracts should sound like.
-> `_shared/conventions.md`, Voice and defaults

**4. Your non-negotiables.** Anything every workspace you build must have that the ten invariants do not already cover — a licence header, a specific `.gitignore`, a status badge, a particular README section.
-> `_shared/conventions.md`, What every emitted workspace gets

**5. Where the line sits.** How many times must a process have repeated before you want a workspace built for it rather than a saved prompt? `01_interview` asks this of every brief; your answer is the threshold it measures against.
-> `_shared/conventions.md`, a new section

---

When an answer is captured: write it into `_shared/conventions.md`, delete the `[unset]` marker on that section, and note the date. The questionnaire stays as it is — it is the schema, not the record.
