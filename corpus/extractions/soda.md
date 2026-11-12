# soda — Experiment-Set Intent Corpus

## Experiment sets

| Exp | Description | Scope verdict | Rationale |
| --- | --- | --- | --- |
| Exp1 | Production session-log analysis (Fig 1) | OUT-OF-SCOPE | Passive production telemetry; no controlled bottleneck; real ISP users [§1] |
| Exp2 | Illustrative RobustMPC session (Fig 3) | IN-SCOPE — low confidence | Lab run; 200s controlled session; all setup params delegated to [17, 22] → underconstrained |
| Exp3 | Throughput-predictor profiling (Fig 7) | OUT-OF-SCOPE | Data-analysis / algorithmic study; no network traffic generated; profiling dataset Not specified [rendering §Exp3] |
| Exp4 | Solver sampling study (Fig 8) | OUT-OF-SCOPE | Purely algorithmic (uniform sampling of optimization problem); no network traffic [§5.3] |
| Exp5 | Numerical simulation campaign (Fig 10) | OUT-OF-SCOPE | Simulator: "a highly optimized ABR simulator in C++ derived from Sabre" [§6.1] |
| Exp6 | Prediction-noise sensitivity simulations (Fig 11) | OUT-OF-SCOPE | Simulator: same C++ simulator as Exp5 with noise injection [§6.1.4] |
| Exp7 | Puffer prototype emulation (Fig 12) | OUT-OF-SCOPE | Simulator-class: browser-level network throttling via Chrome DevTools WebSocket throttle [§6.2]; trace-driven replay, not a physical/kernel-level imposed bottleneck |
| Exp8 | Production A/B at Amazon Prime Video (Fig 13) | OUT-OF-SCOPE | Passive production deployment; real user networks across 10+ countries [§6.3]; no controlled bottleneck |
| ES id | Exp(s) | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| soda-ES1 | Exp2 (Fig 3) | none — single illustrative run with RobustMPC | 1 | 1 (single 200s session [§2]) |

## Shared methodology (quoted from the paper)


No shared block applies (only one in-scope ES; its methodology is underconstrained and
delegated to external papers).

---


## Experiments

### soda-ES1 — Illustrative RobustMPC session (Exp2, Fig 3)

**(i) Raw text.** "Figure 3 shows a RobustMPC session with the exact setup used by [17, 22]"
[§2]. Duration: 200 seconds [§2, "29 rebuffering events over 200 seconds"; Fig 3 x-axis
labeled "Time (sec)" up to 200]. Observed behavior: "beyond 70 seconds, RobustMPC repeatedly
rebuffers but continues to download the highest bitrate (Figure 3 bottom plot), resulting in
29 rebuffering events over 200 seconds" [§2]. The figure shows BW fluctuating in the range
visible in Fig 3 (axis-derived values not extracted per C5 rule; no numeric bandwidth stated
in prose). All setup parameters (topology, link capacity, latency, queue, video source,
segment length, buffer size) are delegated to references [17, 22]; nothing is specified in
this paper beyond the controller identity (RobustMPC [§2]) and session duration (200s [§2]).
Purpose: illustration of RobustMPC's failure mode, not a controlled parametric study.

**(ii) Grammar.**
```
ExperimentSet⟨
  leaves: 1 (single RobustMPC session, no sweep)
⟩;
Experiment = ⟨
  Foreground: Workflow(video-session; params: {abr_controller: RobustMPC [§2]})
  @ path.latency: Not specified (delegated to [17, 22])
  ⊗ Regime⟨
    Static: capacity = Not specified,
            queue: Not specified,
            latency_ms: Not specified
    Dynamic: Not specified (real or emulated network; conditions delegated to [17, 22])
  ⟩
⟩;
Roles⟨client: Not specified, server: Not specified⟩;
cca: Not specified;
iterations: 1 (single session, 200s [§2]);
telemetry: {app_metrics: {rebuffering_events [§2], bitrate_per_chunk [§2], buffer_level [§2]}}
```
