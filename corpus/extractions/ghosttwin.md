# ghosttwin — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| ghosttwin-ES1 | Exp1 (text-only, §3) | No parameterized sweep described | Not specified | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Two programmable Tofino-based routers (EdgeCore Wedge 100-32X) as the physical testbed
> [§3]; hardware-based SmartNIC network emulator based on P7 [§3]; P4 code forwards IP
> network traffic [§3]; GhostTwin agent periodically transmits probing packets and collects
> residual bandwidth in local registers [§3]; digital twin runs on a single SmartNIC [§3];
> scale limit: "typically restricts its use to a few dozen switches" [§3]. All network
> parameters (bandwidth/latency/loss values, topology layout, flow count, duration,
> repetitions): Not specified.


## Experiments

### ghosttwin-ES1 — PoC/live demo deployment (text-only, §3)

**(i) Raw text.** "two programmable Tofino-based routers (EdgeCore Wedge 100-32X)" as
physical testbed [§3]; "hardware-based SmartNIC network emulator based on P7" [§3];
"P4 code to forward IP network traffic" [§3]; "custom probing packet structure" triggers
data collection stored in "local registers" [§3]; collected metric: "residual bandwidth"
[§3]; "real-time traffic replay and metric visualization" shown at demo [§3]; "single
SmartNIC" execution [§3]. Network bandwidth, latency, loss, topology, duration,
repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: Not specified (no parameterized sweep)⟩;
Experiment = ⟨Workflow(IP traffic forwarding on Tofino-based physical switches;
P4 programmed) ⊗ Regime⟨Static: capacity Not specified; latency Not specified;
queue Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨physical switches (EdgeCore Wedge 100-32X), SmartNIC digital twin⟩;
iterations Not specified; telemetry {app_metrics: true (residual bandwidth
via P4 probing [§3])}.
