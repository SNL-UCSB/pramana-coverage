# web_qoe_encrypted — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| web_qoe_encrypted-ES1 | Exp1 | page ∈ Alexa top-500 non-landing × network_condition ∈ varied (latency, loss, etc.) [§2.1] | Not specified (~10,000 experiments total [§2.1]; neither axis enumerated) | 20 runs per page [§2.1] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Instrumented WebPagetest collecting simultaneously HTTP Archive (HAR) from the
> browser and PCAP traces from the network [§2.1, "We instrument WebPagetest to
> collect simultaneously HTTP Archive files (HAR) from the browser and PCAP
> traces from the network"]. Pages: non-landing pages from the Alexa top-500,
> including different subpages of the same Alexa domain [§2.1]. Network
> conditions: varied — "different network conditions (latency, loss, etc.), to
> ensure generality and diversity" [§2.1]; specific values Not specified.
> Repetitions: 20 runs per page [§2.1, "We perform 20 runs on non-landing pages
> from the Alexa top-500"]. Total dataset: ~10,000 experiments after discarding
> failed runs [§2.1, "about 10,000 experiments"]. Analysis observation window
> limited to T = 10 s [§2.3]. Bandwidth, base latency values, loss values, queue
> configuration, CCA, cross traffic, topology, hardware, duration per run, and
> collection date: Not specified.


## Experiments

### web_qoe_encrypted-ES1 — WebPagetest paired HAR + PCAP collection under varied network conditions

**(i) Raw text.** "We instrument WebPagetest to collect simultaneously HTTP
Archive files (HAR) from the browser and PCAP traces from the network" [§2.1].
"We perform 20 runs on non-landing pages from the Alexa top-500" [§2.1].
"different network conditions (latency, loss, etc.), to ensure generality and
diversity in the collection process" [§2.1]. "about 10,000 experiments" total
"after discarding failed runs" [§2.1]. "For each Web site and set of network
conditions, we collect simultaneously L7 browser and L3 encrypted packet traces"
[§2.2]. Target QoE metrics: SpeedIndex, ByteIndex, PageLoadTime (PLT), ATF
[§2.3]. ML analysis: XGBoost, RandomForest, CNN; 5-fold validation, 80% train /
20% test [§2.3]. "median error for SpeedIndex is less than 500ms (Q1: 164ms,
Q3: 1015ms), with a relative error of 18%" [§2.3]. Input featurization: per-flow
byte counts at 100 Hz, observation window T = 10 s; all flows of a session
aggregated [§2.3].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(page ∈ Alexa top-500 non-landing
subpages [§2.1] × network_condition ∈ varied {path.latency, path.loss, …}
[§2.1]); count Not specified (neither axis enumerated; ~10,000 post-discard total
[§2.1])⟩; Experiment = ⟨Workflow(page_load; params.url ← page [§2.1]) @
path⟨latency: swept (Not specified values [§2.1]), loss: swept (Not specified
values [§2.1])⟩ ⊗ Regime⟨Static: capacity Not specified, queue: Not specified;
Dynamic: Not specified (no cross-traffic statement — the demo "focus[es] on
single sessions" [§2])⟩⟩ @ Roles⟨client: WebPagetest instrumented browser,
server: real Alexa page endpoints⟩; iterations = 20 per page [§2.1];
telemetry {pcap: true (L3 PCAP [§2.1, §2.2]), app_metrics: true (HAR +
SpeedIndex, ByteIndex, PLT, ATF [§2.2, §2.3])}.
