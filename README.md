# Foundry

An ICM workspace whose product is other ICM workspaces.

ICM — [Interpretable Context Methodology](https://arxiv.org/abs/2603.16021) (Van Clief & McDermott, MIT) — replaces orchestration code with structure: numbered folders carry sequencing, hierarchy carries context scoping, plain markdown carries state. One agent reading the right files at the right moment does the work of a multi-agent framework, and a human can open any folder and see exactly what state the system is in.

Foundry exists so that designing a new ICM does not mean re-explaining ICM. The canon and the house conventions live once, in `_shared/`. Every run reads them; no run re-derives them.

**Start here:** [AGENTS.md](AGENTS.md) — then [CONTEXT.md](CONTEXT.md) for the pipeline.

## A run

1. `stages/01_interview` — surface the person's actual process. Their pauses become stage boundaries; their "it always has to sound like X" becomes factory reference.
2. `stages/02_blueprint` — pick Pipeline or Umbrella, name the stages, place the human gates. Written down before anything is built.
3. `stages/03_scaffold` — write the tree and every contract to the destination named in the brief.
4. `stages/04_walk-test` — an agent with no memory must orient, act, and report status from the files alone. If it cannot, the structure changes.

Then the run is filed in `library/`.

## Credit

Method: Van Clief & McDermott, *Interpretable Context Methodology: Folder Structure as Agent Architecture*, arXiv:2603.16021. Community: [Clief Notes](https://www.skool.com/cliefnotes). The invariants, forms taxonomy, and walk test in `_shared/` are adapted from [RinDig/icm-architect](https://github.com/RinDig/icm-architect) (MIT).
