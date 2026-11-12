<!-- Released verbatim except 5 lines marked [redacted]. Same redaction policy as PROMPT.md. -->
# Intent-Corpus Calibration — Conventions and Gates

> [redacted: reference to the Pramana implementation or its internal capability sheet]
> [redacted: reference to the Pramana implementation or its internal capability sheet]
- `docs/PRAMANA_DESIGN_SPEC.md` (grammar + taxonomy, §2)
- `docs/PRAMANA_INTERFACE_DEFINITIONS.md` (field-level truth: A5 schema, §8.11
  closed enums, context keys)

The local synthesis doc (`Pramana/hotnets/synthesis_abstraction_grammar_
architecture.md`) is NOT authoritative; where it disagrees with the spec, the
spec wins and the disagreement is logged in the Spec-gap register below.

## 1. The taxonomy fix (the reason this corpus exists)

Spec §2, verbatim productions:

```
ExperimentSet = compile(Intent, Answers) | user-written Spec (same gate)
ExperimentSet = ⟨ nodes, mapping, secrets, leaves ⟩       (leaves flat/expanded)
sweep         : Experiment × dim → ExperimentSet          (client-side)
Experiment    = ⟨ Workflow(params) ⊗ Regime ⟩ @ Roles × iterations
identity(e)   = H_rfc8785(workflow@sha, params, static, dynamic)
Regime        = Static⟨capacity↓↑, latency, queue⟩ ⊗ Dynamic⟨pressure⟩
pressure      = replay(ctp) | load(Workflow* ↦ Node*) | both
collect       = deploy ; prepare ; verify ; run ; publish  (AI-free)
Taxonomy: intent · experiment set · experiment (leaf; identity-hashed) ·
iteration (no teardown by default)
```

**Mapping rule (normative for this corpus):** a rendering's collection-split
"Exp N" (one data-collection campaign) is an **ExperimentSet**. Each unique
parameter combination inside the campaign (one point of the sweep:
⟨workflow@params, static, dynamic⟩) is a **leaf Experiment**. Stated
repetitions are **iterations** of a leaf. Leaves are represented by their
sweep dimensions and cardinality (`sweep(cca × buffer × flow-pattern) = 3×4×2
= 24 leaves`), enumerated only when ≤ ~10 and non-factorial.

Field-level vocabulary for requirements comes from the INTERFACE DEFINITIONS
(A5 static block includes `cca`, `loss_pct`, `reorder_pct`, `dup_pct`; context
required keys per §8.11; verify tolerances per §8). The coarse grammar block
omits these fields; the interface definitions are the finer truth.

## 2. IDs and file layout

- Paper slug = its `fig_to_exp/<slug>_rendering.md` basename.
- Experiment set: `<slug>-ES<k>` (k follows the calibrated ordering, which may
  merge or split the rendering's Exp rows; record the mapping).
- Leaf (only when enumerated): `<slug>-ES<k>-L<j>`.
- One synthesis file per paper: `papers/<slug>.md`. `MASTER.md` indexes every
  experiment set and carries the progress chart.

## 3. Per-entry format (every experiment set)

1. **Raw text.** Verbatim paper quotes with locators (v3 grounding protocol:
   every value `[§x / Fig y caption]`; silence = `Not specified`, never
   inferred).
2. **Grammar translation.** The ExperimentSet written in spec productions:
   Workflow(params), Regime static/dynamic, Roles, sweep dims + leaf count,
   iterations, telemetry selection.
3. **Requirements.** What realizing this set demands, expressed only in spec
   vocabulary (fields from the A5 schema; pressure modes; persistence;
   endpoint roles; telemetry keys). Per-intent demands, never backend
   requirements (R1–R9 belong to the paper, not to corpus entries).
4. **Capability match, three levels, every verdict with a grounded reason:**
> [redacted: reference to the Pramana implementation or its internal capability sheet]
     production/field) / OUT-OF-SCOPE (exogenous data or physical-layer, per
     spec scope).
> [redacted: reference to the Pramana implementation or its internal capability sheet]
     `EugeneVuong/netgent`): SATISFIED (cite module/file) / GAP-IMPL (name the
     module and the addition required).
   - (c) **Mininet** (against `mininet-capability.md`, the reduced capability
     grammar in this directory): M-SAT / M-PARTIAL / M-UNSAT + reason
     (vocabulary defined in that file: declarative surface vs hand-authored
     machinery vs structurally outside the model).

## 4. Red-team gates (codex, every iteration)

Inherited text gates: C5 (every value greps against paper text), C9 (every
figure→set assignment justified). New corpus gates:
- **G1** tiering: ES/leaf/iteration assignment conforms to the spec taxonomy;
  re-analyses of one collection never create a new ES.
- **G2** translation type-checks: every grammar term used exists in spec §2 or
  the interface definitions; no invented productions.
- **G3** requirements use spec vocabulary only; every field name exists in A5.
- **G4** every match verdict carries a reason grounded in spec text, repo code
  path, or the Mininet grammar; no bare verdicts.
- **G5** Mininet verdicts ground in `mininet-capability.md` clauses.

## 5. Commit protocol

One commit per iteration: `intent-corpus: <slug> ES<k> [extract|translate|
match|redteam]` or `intent-corpus: calibration [note]`. MASTER.md chart
updated in the same commit. Calibration learnings (convention changes) edit
this file and note the affected prior entries.

## 5b. Calibration learnings from the anchor paper (propagate to all papers)

1. **Leaf spaces are ATTEMPTED spaces.** Post-hoc validity/success (site
   unresponsive, RTT filter, all-invalid) are outcomes recorded in results,
   never leaf-space filters (red-team G1, ccanalzyer-ES9).
2. **Silence is never `mode: none`.** A paper that does not mention cross
   traffic gets Dynamic: Not specified (compile default-with-echo), not
   `none` (C5, ES4/5/6/11).
3. **Queue discipline vs queue size.** Papers that state only a queue SIZE
   get `queue: discipline Not specified`; pfifo/bfifo realization is a
   compile default, not extraction (C5).
4. **Implementation grounding must name its venue + pin.** Every code-path
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   cannot see must say so (G4).
5. **Mininet verdict = min across axes** (envelope, workflow, telemetry,
   campaign). Hand-built telemetry caps at M-PARTIAL even when the envelope
   is trivially emulable (G5).
6. **Verdict inheritance must be explicit** ("INHERITED from ESk, delta: …"),
   never "same as above" (G4).
7. **Leaf arithmetic must close.** Every ES row's leaf count is exact or
   `Not specified` — never "N (+ some more)" or "≥N" (G1; re-confirmed
   prudentia-ES6).
8. **Mixed-feasibility leaf spaces**: Mininet verdict = M-PARTIAL with the
   leaf split named ("2/3 leaves realizable"), never an unqualified verdict
   (G5; prudentia-ES4/ES6).
9. **Stated no-pressure baselines are `Dynamic: none` leaf families** (a
   positive statement in the paper, e.g. Solo in Prudentia Fig 6) — distinct
   from silence, which stays Not specified (§5b.2 unchanged).
10. **Protocol-internal repeats are workflow states, not iterations**
    (Prudentia's 10 timed page loads; iterations = the trial count only).

## 6. Spec-gap register (running)

| # | Observation | Status |
|---|---|---|
| 1 | Grammar block Regime.Static shows ⟨capacity↓↑, latency, queue⟩; interface defs carry `loss_pct/reorder_pct/dup_pct` + `cca`. Use interface defs for fields. | resolved (interface defs finer) |
| 3 | Adaptive iteration counts (CI-driven stopping, Prudentia §3.3) are not expressible: A5 `iterations` is a fixed int. | open (prudentia-ES1) |
| 4 | Per-flow latency: A5 carries one `latency: Quantity` per regime; per-service RTT normalization (Prudentia §3.1) has no production. | open (prudentia-ES1..8) |
| 5 | `cca` enum carries no kernel-build qualifier; BBR@4.15 vs BBR@5.15 (Prudentia Fig 9b) is inexpressible. | open (prudentia-ES7/8) |
| 6 | Time-varying static envelopes (conditions "varied at random intervals" within a session, NetMicroscope §4.1) have no production: A5 static is fixed per experiment and hashed once. | open (netmircoscope-ES2) |
| 7 | Multi-endpoint foreground (CAKE host isolation: 2 src × 4 dst hosts whose per-flow goodput is the result): Experiment foreground is one Workflow @ Roles⟨client, server⟩; `load()` places workflows but the spec defines no result-plane telemetry attribution for pressure workflows. | open (cake-ES2) |
| 2 | `jitter` IS in A5 (`Static.jitter: Quantity|None`, interface defs §2) with NetReplica knob range 0–500ms (§8.2); `Impair{loss_pct, reorder_pct, dup_pct}` likewise (§8.1 RT-4). Jitter/impair intents are in-grammar. | resolved (present) |
