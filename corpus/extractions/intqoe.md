# intqoe — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| intqoe-ES1 | Exp1 (text-only, §3) | single decision-making run | 1 | Not specified |
| intqoe-ES2 | Exp2 (§4, Fig 3) | scheme ∈ {IntQOE, WRR+E2E, LB+E2E} [§4.2] | 3 | Not specified |

## Experiments

### intqoe-ES1 — Runtime test of the existing two-level decision-making algorithm (text-only, §3)

**(i) Raw text.** "We tested the algorithm using a public live streaming dataset [3], while a single time global load balance decision making spent over half an hour" [§3]; algorithm: "maximum bipartite matching based two-level decision making algorithm proposed by [17]" [§3]. Network bandwidth, RTT, queue size, topology: Not specified. Hardware: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(algorithm timing test; no network traffic generated) ⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨Not specified⟩; iterations: Not specified; telemetry {app_metrics: true (decision latency ≈ 30+ min)}.

### intqoe-ES2 — Trace-driven microbenchmark simulation (§4, Fig 3)

**(i) Raw text.** "We evaluate IntQOE using trace-driven simulations for a live streaming application" [§4]; "We implemented a live streaming simulator using Python" [§4.1]; hardware: "16 cores of 3.70GHz Intel Xeon processer and 64GB RAM" [§4.1]; dataset: public live streaming dataset [3], "which collects 24-hour live streaming events from Facebook" [§4.1]; network latency: "collected from the global ping statistics [4]" [§4.1]; server-side delay: cubic spline extrapolation from Cassandra benchmark data [§4.1]. Schemes compared: IntQOE, WRR+E2E, LB+E2E [§4.2]. Result: IntQOE "can improve the overall QoE by 10% – 40%" [§4.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scheme ∈ {IntQOE, WRR+E2E, LB+E2E}) = 3⟩; Experiment = ⟨Workflow(custom Python GSLB simulator; input: live streaming trace, ping latency trace, server delay model) ⊗ Regime⟨Static: Not specified (trace-driven; no bottleneck imposed); Dynamic: Not specified⟩⟩ @ Roles⟨Not specified⟩; iterations: Not specified; telemetry {app_metrics: true (normalized QoE per epoch)}.
