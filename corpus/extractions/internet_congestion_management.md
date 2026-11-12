# internet_congestion_management — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Leaves | Notes |
| --- | --- | --- | --- |
| icm-ES1 | Exp1 — Random-model MILP | 18,723 topologies [Tab 1] | MILP computation, no packets |
| icm-ES2 | Exp2 — CAIDA-model MILP | 2,897 topologies [Tab 1] | MILP computation, no packets |
| icm-ES3 | Exp3 — Best-reply agent dynamics (text-only) | 1,030 topologies [§5.3] | Game-theory simulation |
| icm-ES4 | Exp4 — Simplified-CCA dynamics (text-only) | 1,052 topologies [§5.3] | Game-theory simulation |
| icm-ES5 | Exp5 — Mininet scheduler comparison | sweep(scheduler × topology × cca_assignment) = 4 × 10 × 10 = 400 [§6.2] | Custom HDWRR prototype required |
| icm-ES6 | Exp6 — Bursty-traffic emulation | sweep(burstiness ∈ {Regular, Burst Over, Burst Under}) = 3 [§6.3]; iterations 20 [§6.3] | Custom scheduler + CAIDA trace workload |
| icm-ES7 | Exp7 — Incremental-adoption emulation | sweep(RCS_domains ∈ {0,1,2,3,4}) = 5 [§6.4]; iterations 5 [§6.4] | Custom scheduler; partial deployment |

## Experiments

### icm-ES1 — Random-model MILP equilibrium analysis (§5.2, Table 1 row "Random")

**(i) Raw text.** "a mixed-integer linear program (MILP) formulation that determines whether multiple game-theoretic equilibria exist" [§5]; "fully-connected 10-node topology" [§5.2]; "generate 40 4-hop streams" [§5.2]; "random weights at each ingress" [§5.2]; 18,723 topologies [Table 1]; solver: "We use a commercial MILP solver [37]" (Gurobi) [§5.2]. Application, bandwidth, RTT, queue: Not specified ("analytic MILP model; no packet-level parameters given" — rendering).

**(ii) Grammar.** ExperimentSet⟨leaves: 18,723 topology instances⟩; Experiment = ⟨Workflow(Gurobi MILP solver; no network traffic) ⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨Not specified⟩; iterations: Not specified; telemetry {app_metrics: true (Nash/Stackelberg equilibrium counts)}.

### icm-ES2 — CAIDA-sampled-model MILP equilibrium analysis (§5.2, Table 1 row "CAIDA-sampled")

**(i) Raw text.** Same MILP framework as ES1; topology generation: "topologies sub-sampled from the CAIDA AS relationships dataset [15]" [§5.2]; additional constraint (6) for recursive-weight enforcement [§5.2]; 2,897 topologies [Table 1]; result: 0 topologies with multiple Nash or non-Nash Stackelberg equilibria [§5.2]. Bandwidth, RTT, queue: Not specified.

**(ii) Grammar.** INHERITED from icm-ES1, delta: topology source = CAIDA AS relationships dataset [§5.2], count = 2,897 [Table 1], extra MILP constraint (6) [§5.2].

### icm-ES3 — Best-reply agent dynamics simulation (text-only, §5.3)

**(i) Raw text.** "will reasonable CCAs–which myopically adjust their behavior–reach this single Nash equilibrium?" [§5.3]; "best-reply" agent iterating sending rates [§5.3]; 1,030 8-stream topologies from the CAIDA topology generator [§5.3]; sender-only (606) and sender-and-receiver (424) weight configurations [§5.3]; result: "In all of these topologies, the agents converged to a single equilibrium" [§5.3]. Bandwidth, RTT, queue size, transport, hardware: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1,030 topology instances⟩; Experiment = ⟨Workflow(best-reply simulator; no real network packets) ⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨Not specified⟩; iterations: Not specified; telemetry {app_metrics: true (convergence outcome per topology)}.

### icm-ES4 — Simplified-CCA dynamics simulation (text-only, §5.3)

**(i) Raw text.** "more realistic dynamics" [§5.3]; simplified versions of CBR, AIMD, BBR, Decongestion Control, Latency-sensitive [§5.3]; 1,052 topologies [§5.3]; "in 1,052 topologies, the agents converged to a single equilibrium" [§5.3]. Topology generator, stream counts, bandwidth, RTT, queue: Not specified.

**(ii) Grammar.** INHERITED from icm-ES3, delta: CCA set = simplified {CBR, AIMD, BBR, Decongestion Control, Latency-sensitive} [§5.3], topology count = 1,052 [§5.3].

### icm-ES5 — Mininet scheduler comparison (§6.2, Figs 2–3)

**(i) Raw text.** "packet emulations (using Mininet [29])" [§6]; "HDWRR implemented in ~150 lines of Rust as a user-space TUN/TAP device" [§6.2]; scheduler configs: FIFO, DRR, One-Hop, HDWRR [§6.2]; CCAs: "Reno, Cubic, and BBR, randomly assigned per stream" [§6]; 8- and 15-stream topologies [§6.2]; 10 CAIDA-sampled topologies [§6.2]; 10 random CCA assignments per topology [§6.2]; topology generated with CAIDA-sampling generator [§6.2]; metric: % error from Ideal RCS [Fig 2 caption]. Bandwidth, base latency, queue size, queue management, duration: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scheduler ∈ {FIFO, DRR, One-Hop, HDWRR} [§6.2] × topology_instance ∈ 10 CAIDA-sampled [§6.2] × cca_assignment ∈ 10 random [§6.2]) = 4 × 10 × 10 = 400⟩; Experiment = ⟨Workflow(bulk TCP; cca: ⟨algo: per-assignment ∈ {reno, cubic, bbr}⟩) ⊗ Regime⟨Static: capacity Not specified, latency Not specified, queue: discipline = per-scheduler-config, size Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨multi-hop CAIDA topology; 8- and 15-stream hosts⟩; iterations: Not specified; telemetry {app_metrics: true (% error from Ideal RCS, bandwidth per flow)}.

### icm-ES6 — Bursty-traffic emulation (§6.3, Fig 4)

**(i) Raw text.** "RCS on a simple topology where two aggregates feed into a single shared bottleneck" [§6.3]; weights: "fixed aggregate a weight twice that of the bursty aggregate" [§6.3]; burstiness configs: Regular, Burst Over (50% above Ideal-RCS allocation), Burst Under (50% below) [§6.3]; bursty workload: "short flows with sizes drawn by analyzing packet traces from an Internet core router [15]" [§6.3]; "20 experiment iterations per burstiness configuration" [§6.3]; Emulator, bandwidth, RTT, queue, duration: Not specified (§6.3 does not restate the emulator; rendering flags Mininet as assumed-not-stated). One aggregate fixed to TCP Cubic [§6.3].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(burstiness ∈ {Regular, Burst Over, Burst Under} [§6.3]) = 3⟩; Experiment = ⟨Workflow(short-flow bursty generator sourced from CAIDA Internet-core-router traces × Cubic fixed aggregate) ⊗ Regime⟨Static: capacity Not specified, queue: discipline Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨two aggregates on a shared bottleneck⟩; iterations: 20 [§6.3]; telemetry {app_metrics: true (% deviation from Ideal-RCS allocation)}.

### icm-ES7 — Incremental-adoption emulation (§6.4, Fig 5)

**(i) Raw text.** "a generated 12-stream topology" [§6.4]; stream under test: "path length of at least 4" [§6.4]; incremental sweep: 0 to 4 RCS domains activated along the stream's path [§6.4]; "five 30-second iterations per deployment depth" [§6.4]; 17 non-RCS domains remain [§6.4]; metric: allocation % error [§6.4]. CCA, emulator, bandwidth, RTT, queue: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(rcs_domain_count ∈ {0, 1, 2, 3, 4} [§6.4]) = 5⟩; Experiment = ⟨Workflow(bulk TCP; cca: Not specified) ⊗ Regime⟨Static: capacity Not specified, latency Not specified, queue: discipline Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨12-stream multi-hop topology; 4-hop path under test; 17 non-RCS domains⟩; iterations: 5 [§6.4]; telemetry {app_metrics: true (allocation % error per deployment depth)}.
