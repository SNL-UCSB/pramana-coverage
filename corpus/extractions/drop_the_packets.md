# drop_the_packets — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| drop_the_packets-ES1 | Exp1 | service ∈ {Svc1, Svc2, Svc3} × session ∈ external-trace-driven conditions [§4.1] | 2,111 (Svc1) + 2,216 (Svc2) + 1,440 (Svc3) = 5,767 sessions ATTEMPTED [§4.1] | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> "browser-based automation framework" streams sessions under "emulated network conditions
> using publicly available bandwidth traces representing a diversity of network environments
> including fixed broadband, 3G and LTE" [§4.1, refs 2, 27, 32]; three popular streaming
> services anonymized as Svc1, Svc2, Svc3 (YouTube, Netflix, Hulu) [§1; §4.1]; session
> duration 10–1200 seconds [§4.1]; ground-truth QoE via JavaScript injection using HTML5
> Video API [§4.1]; TLS transactions collected via transparent-proxy concept [§2.2];
> network emulation tool Not specified; base latency Not specified; CCA Not specified;
> queue Not specified; cross traffic Not specified.


## Experiments

### drop_the_packets-ES1 — Emulated-network video-streaming collection (three services)

**(i) Raw text.** "browser-based automation framework" streams video under emulated
conditions driven by publicly available bandwidth traces (fixed broadband, 3G, LTE)
[§4.1]; "2, 111 sessions for Svc1, 2, 216 for Svc2, and 1, 440 for Svc3" [§4.1];
duration range "10-1200 seconds" [§4.1]; ground-truth QoE injected via JavaScript
[§4.1]; network emulation tool Not specified; CCA Not specified; base latency Not
specified; queue Not specified; cross traffic Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow.service ∈ {Svc1, Svc2, Svc3}
× session ∈ external-bandwidth-trace pool [§4.1]); count: 5,767 sessions
ATTEMPTED [§4.1]⟩; Experiment = ⟨Workflow(browser; automated video stream from
live service) ⊗ Regime⟨Static: capacity driven by external bandwidth traces
(time-varying) [§4.1]; Dynamic: Not specified⟩⟩ @
Roles⟨client: automation node, server: real live service endpoints (Svc1/Svc2/Svc3)⟩;
iterations Not specified; telemetry {app_metrics: true (per-second QoE via HTML5
Video API [§4.1]), pcap: true (TLS transactions + packet traces [§4.1])}.
