<!-- Released verbatim except 12 lines marked [redacted]. The prompt also asked workers to match each experiment against the Pramana implementation and Mininet; that match step and its inputs are not released, and the public extractions omit it. -->
# Experiment-Intent Corpus — Hardened Generation Prompt (v4)

**Purpose.** Generate the per-experiment intent corpus for the remaining ~55
papers with a *fraction* of the red-teaming the gold-13 wave needed. The gold
wave took ~17 red-team findings per paper (55 BLOCK + 163 FIX across 13 papers)
because the conventions were being discovered mid-wave, workers re-derived
(and re-hallucinated) reference facts, and the v1 grammar lacked fields papers
needed. v4 freezes all of that and moves the anti-hallucination check from
expensive codex judgment to a cheap mechanical gate.

**Status: draft for team review ([team member] + others).** Iterate here. The "Open
questions" section at the end lists the decisions still to settle.

**How to run.** One worker per paper, in isolation (worktree, per
`CALIBRATION.md` §5). The worker is handed the Reference Pack (below), renders
the paper against grammar v2, self-checks, and emits `papers/<slug>.md`. Then
the two-tier gate runs. No per-paper codex gauntlet by default.

---

## 1. The Reference Pack (handed to every worker — never re-derived)

The gold wave's G2/G4/G5 findings came from workers re-deriving these. Freeze
them; the worker *selects from* them, never invents.

1. **Grammar v2 vocabulary (the closed menu).** Source of truth:
> [redacted: reference to the Pramana implementation or its internal capability sheet]
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   - **Bottleneck link** (shared, precise): `Regime = Static⟨capacity↓↑, queue⟩ ⊗ Dynamic⟨pressure⟩`.
   - **Rest of path** (per-workflow, approximate): `path = ⟨latency, jitter, loss, reorder, dup⟩`
     (no capacity, no queue).
   - `cca = ⟨algo, stack, version, params, flags, build⟩` per workflow;
     `queue = ⟨discipline, size, params, ecn, mode⟩`;
     `iterations = int | until(event(metric,target),min,max)`;
     `Foreground = { Workflow_i @ node_i }`.
   **Rule G2/G3:** every field name in a translation MUST be one of these or an
   A5 field in `PRAMANA_INTERFACE_DEFINITIONS.md`. A term not in the menu is a
   mechanical error, not a judgment call.

2. **Verified Implementation-Capability Sheet (PREREQUISITE — author once,
   carefully).** One authoritative, `file:line`-pinned statement of what is
> [redacted: reference to the Pramana implementation or its internal capability sheet]
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   wired CCAs and the host-kernel gate; `load`-mode status (CTP replay shipped,
   closed-loop co-scheduling not); QUIC/userspace status. This is the artifact
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   papers. Frozen here, workers stop re-reading code and re-hallucinating.
> [redacted: reference to the Pramana implementation or its internal capability sheet]

3. **Mininet capability grammar.** `mininet-capability.md` (exists). All Mininet
   verdicts ground in its clauses (rule G5); verdict = min across axes.

4. **Calibration rules (the 15 §5b learnings), as hard output rules.** The
   ones that caused the most G1 churn, restated as MUST:
   - Leaf spaces are ATTEMPTED spaces (post-hoc validity is a result, never a
     leaf filter).
   - Silence ≠ `mode: none` → `Not specified` (compile default-with-echo).
   - Queue size ≠ queue discipline.
   - Stated no-pressure baseline = `Dynamic: none` family; silence stays
     `Not specified`.
   - Protocol-internal repeats are workflow states, not iterations.
   - Leaf arithmetic must close EXACTLY (explicit product, no "≥N" / "N+some").
   - Verdict inheritance explicit ("INHERITED from ESk, delta: …").
   - Implementation grounding pins venue + sha + `file:line`.
   - OUT-OF-SCOPE design → `Implementation: n/a` (never GAP-IMPL).
   Full list: `CALIBRATION.md` §5b.

---

## 2. Per-paper procedure (render against v2)

For paper `<slug>` (rendering at `paper_extraction/fig_to_exp/<slug>_rendering.md`,
PDF under `paper_extraction/.../paper_pdf/` or `<pdf dir>/`):

1. **Tier the experiments.** Each collection-split "Exp" row = an ExperimentSet
   (`CALIBRATION.md` §1). Identify sweep dims, leaf counts (ATTEMPTED), and
   iterations. Do NOT apply the cascade pass yet (measure-then-configure stays a
   single ES for now; the cascade re-extraction is a later, separate pass).
2. **Per ES, emit the four blocks** (match the `papers/ccanalzyer.md` exemplar
   exactly): (i) raw text with locators; (ii) grammar-v2 translation; (iii)
   requirements in A5 vocabulary; (iv) three-level capability match
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   grammar), every verdict with a grounded reason.
3. **Render conditions per the v2 model:** bottleneck knobs → `Regime`;
   per-endpoint path characteristics → per-workflow `path`; CCA → per-workflow
   structured `cca`; time-varying *load* → `Dynamic.pressure` (NOT a scheduled
   envelope — that intent is re-expressed, per the v2 boundary). If a paper
   varies the bottleneck *capacity* over time, mark OUT-OF-SCOPE (the model does
   not schedule the bottleneck).

---

## 3. Mandatory pre-emit self-checks (failure-ranked; run before emitting)

The top gold-wave failure modes, front-loaded so the worker catches its own:

- **[G1] Leaf arithmetic closes.** Every ES states its leaf count as an explicit
  product (e.g. `15 cca × 9 settings × 2 = 270`) and the worker verifies it. No
  `≥N`, no `N + some`. Post-hoc validity is a result, not a leaf filter.
- **[C9] Figure→experiment grounded.** Every figure assignment cites that
  figure's OWN caption or in-text reference, not a sibling's. Re-analyses of one
  collection never spawn a new ES.
- **[C5] Values grounded.** Every non-`Not specified` value carries a
  grep-precise locator (`5 Mbps [§3.3.1]`). Silence = `Not specified`, NEVER
  inferred from a sibling, a tool default, or an unlabeled axis.
- **[G2/G3] Vocabulary closed.** Every grammar/field term is in the Reference
  Pack menu. No invented productions or axis labels.
- **[G4] Verdicts grounded.** Every design/impl/Mininet verdict has a reason
> [redacted: reference to the Pramana implementation or its internal capability sheet]
  No bare verdicts; no re-derived implementation claims.

---

## 4. Output format (structured so the gate is mechanical)

Match `papers/ccanalzyer.md`. In addition, for machine-checkability:
- Leaf counts as explicit arithmetic strings.
- Every value line: `field: value [locator]` or `field: Not specified`.
- Verdict tokens from the closed set: design ∈ {SATISFIED, GAP-DESIGN,
  OUT-OF-SCOPE}; impl ∈ {SATISFIED, GAP-IMPL, n/a}; mininet ∈ {M-SAT, M-PARTIAL,
  M-UNSAT}.
- **Confidence tag per ES:** `confidence: high | low` + a one-line `interpreted:`
  note whenever the worker had to choose. Low-confidence ES route to Tier-2.

---

## 5. The two-tier gate (replaces per-paper codex)

**Tier 1 — mechanical, every paper, ~free (`gate_tier1.py`, to be written).**
No judgment; catches the bulk:
- **C5:** extract every `value [locator]` pair; grep the value in the PDF text
  near the cited locator. Miss = flag. (This is the anti-hallucination check
  that gold triangulation used to provide — now a grep, more reliable than an
  LLM for value-grounding.)
- **G1:** parse every leaf-count arithmetic string; verify the product equals
  the stated total.
- **G2/G3:** every field/grammar term ∈ the frozen vocabulary set.
- **Token/consistency:** verdict tokens in-set; OUT-OF-SCOPE ⇒ impl `n/a`;
  inheritance references resolve.

**Tier 2 — codex/adversarial deep review, SAMPLED.** Runs only on: (a) a
1-in-N sample of papers; (b) any paper Tier-1 flagged; (c) any ES self-tagged
`confidence: low`. Judgment checks (C9 reasoning, verdict *quality*) live here.

---

## 6. Validation before scaling (cheap insurance)

Run v4 (prompt + Tier-1) on 2–3 already-done gold papers (prudentia, cambrian,
cake) and confirm it **reproduces the gold verdicts** and that Tier-1 catches
the errors the gold red-team caught. Reproduces without codex → methodology
proven; diverges → the divergence names the check to harden. Only then, the
55-wave.

---

## 7. Open questions (for [team member] + team to settle)

1. **Tier-2 sample rate** — 1-in-5 (lighter) vs 1-in-3 (safer, no gold
   triangulation on the 55). Recommend 1-in-3 for the first ~15, then relax if
   the flag rate is low.
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   (kills the biggest re-derivation finding class). Recommend yes, one careful
   pass, before any 55-wave worker runs.
3. **Cascade pass timing** — v4 deliberately does NOT apply the
   measure-then-configure cascade (keeps ES flat). Apply it as a separate pass
   after the 55 are rendered, together with the grammar-v2 re-render of the
   gold 13, so all 68 land on one convention.
4. **Parallelism cap** — the 10-way fan-out tripped the spend limit. Recommend
   3–4 concurrent workers for the 55.
5. **Papers with no gold matrix** — the 55 have [team member]'s renderings but no gold.
   The v3 grounding protocol + Tier-1 grep is the substitute; confirm the
   renderings are trustworthy enough to seed extraction, or flag which need a
   manual pre-pass.

---

## Execution plan (Arpit, 2026-07-06)

1. **Prerequisites first** (or v4 re-derives the very facts it exists to freeze):
> [redacted: reference to the Pramana implementation or its internal capability sheet]
   and write `gate_tier1.py`.
2. **Validate on the gold 13 = the v2 calibration re-render.** Re-render all 13
   gold papers against grammar v2 + v4 (this doubles as the long-wanted
   v2-calibrated gold corpus). Red-team at the end (Tier-1 all + sampled
   Tier-2). **Success test: the v4 finding rate is a fraction of the gold wave's
   ~17/paper, and verdicts match the known v2-adjusted expectation.** If v4
   lands, the method is proven; if not, the divergence names the fix.
3. **Then the 55**, Tier-1-gated with sampled Tier-2, 3–4 workers.

## Related documents

- `CALIBRATION.md` — conventions, §5b learnings, gates.
- `SPEC_FEEDBACK.md` — the design refinements the gold wave surfaced (SR/G).
- `mininet-capability.md` — Mininet verdict grammar.
- `papers/ccanalzyer.md` — the format exemplar.
> [redacted: reference to the Pramana implementation or its internal capability sheet]
> [redacted: reference to the Pramana implementation or its internal capability sheet]
