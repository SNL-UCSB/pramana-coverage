# Intent grammar (v2) vocabulary

The closed menu every extraction draws on (the paper's Figure 2).

   - **Bottleneck link** (shared, precise): `Regime = Static⟨capacity↓↑, queue⟩ ⊗ Dynamic⟨pressure⟩`.
   - **Rest of path** (per-workflow, approximate): `path = ⟨latency, jitter, loss, reorder, dup⟩`
     (no capacity, no queue).
   - `cca = ⟨algo, stack, version, params, flags, build⟩` per workflow;
     `queue = ⟨discipline, size, params, ecn, mode⟩`;
     `iterations = int | until(event(metric,target),min,max)`;
     `Foreground = { Workflow_i @ node_i }`.
