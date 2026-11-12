# fusing_speed_index — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| fusing_speed_index-ES1 | Exp1 (BBC illustration) | 2 loading processes (A, B) [§2] | 2 | Not specified |
| fusing_speed_index-ES2 | Exp2 (Alexa top-1000) | site ∈ Alexa top-1,000 [§3.1] × device ∈ 5 [Table 1] × network ∈ {4 BW + 3 lat} (PC) / {LTE, 5G} (smartphone) | Not specified (multiple test-group sweeps) | 30 groups (3 time-of-day × 10 rep) [§3.1] |
| fusing_speed_index-ES3 | Exp3 (background tabs, PC-3) | background_tabs ∈ {0, 20, 40, 60} [§3.2] × page ∈ {Amazon, MSN, Pinterest} [§3.2] | 4 × 3 = 12 | Not specified |
| fusing_speed_index-ES4 | Exp4 (viewport sweep, YouTube) | viewport_width ∈ 500–2600 px [§3.2]; viewport_height ∈ 200–1500 px [§3.2] | Not specified (step size not stated) | Not specified |
| fusing_speed_index-ES5 | Exp5 (end-to-end evaluation) | page ∈ 300-page corpus [§6.1] × system ∈ {SipLoader, Vroom, Fawkes, default} × network ∈ {1,10,100 Mbps × 10,25,50,75 ms} (PC) / {LTE, 5G} (smartphone) × cache ∈ {cold, 3 h, 6 h} | Not specified (complex factorial; partial results shown) | 5 [§6.1] |
| fusing_speed_index-ES6 | Exp6 (component ablation, PC-3) | ablation_config ∈ 4 variants (①–④) [§6.3] | 4 | Not specified |
| fusing_speed_index-ES7 | Exp7 (scheduling efficiency) | algorithm ∈ {greedy_inference, topological_sort} × page ∈ 300-page corpus [§6.3] | 2 × 300 = 600 | Not specified |
| fusing_speed_index-ES8 | Exp8 (optimality study, text-only) | page ∈ 134 Alexa-top-2000 pages [§6.3] | 134 | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Web pages loaded in Chrome 91.0 [§3.1]; cold cache unless stated; SI computed with
> Speedline [§6.1]; Chrome DevTools used for client-side bandwidth/latency throttling
> in Exp2 (throttle to {1,10,100,1000} Mbps at 25 ms latency, and latency to
> {10,25,50} ms at 100 Mbps [§3.1]); Mahimahi record-and-replay used for Exp5 [§6.1];
> live real web pages (Alexa top-1,000 / 300-page corpus) as server endpoints; CCA
> Not specified; queue Not specified; cross traffic Not specified; imposed single
> bottleneck: Not applicable (client-side throttling or Mahimahi trace replay, not
> a tc-imposed network bottleneck).


## Experiments

### fusing_speed_index-ES1 — BBC loading-processes illustration

**(i) Raw text.** "two different page loading processes of the landing page of BBC" [§2];
Process A (large crucial elements first): SI = 1.18 s; Process B (small crucial
elements first): SI = 1.88 s; both finish at "3,000 ms" [§2]; device, network
conditions, browser: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 2 (loading process A vs B)⟩; Experiment =
⟨Workflow(browser; BBC landing page load) ⊗ Regime⟨Static: Not specified;
Dynamic: Not specified⟩⟩ @ Roles⟨client: Not specified, server: real BBC web
endpoint⟩; iterations Not specified; telemetry {app_metrics: true (SI value,
visual completeness [§2])}.

### fusing_speed_index-ES2 — Alexa top-1,000 measurement campaign

**(i) Raw text.** "Alexa top 1,000 sites" as of "Jul. 16th, 2021" [§3.1]; 5 devices
(3 PCs + 2 smartphones) [§3.1; Table 1]; PCs throttled via Chrome DevTools to
{1, 10, 100, 1,000} Mbps at 25 ms latency, and latency to {10, 25, 50} ms at
100 Mbps [§3.1]; smartphones on "real LTE and 5G networks" [§3.1]; "30 groups of
tests" per day (3 time-of-day × 10 repetitions) [§3.1]; Chrome 91.0, cold cache
[§3.1]; device specs per Table 1.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(site ∈ Alexa top-1,000 × device
∈ 5 × network ∈ {{1,10,100,1000} Mbps / {10,25,50} ms (PC), LTE/5G (smartphone)});
count Not specified (complex factorial × 30 groups)⟩; Experiment =
⟨Workflow(browser page load; Chrome 91.0) ⊗ Regime⟨Static: Chrome DevTools
client-side throttling, NOT a tc-imposed network bottleneck [§3.1]; Dynamic:
Not specified⟩⟩ @ Roles⟨client: PC/smartphone, server: real Alexa top-1,000
web endpoints⟩; iterations: 30 groups [§3.1]; telemetry {app_metrics: true
(SI values per page/device/network [§3.1])}.

### fusing_speed_index-ES3 — Background-tabs measurement (PC-3)

**(i) Raw text.** PC-3 (Intel E5-2420 1.90 GHz, 32 GB, 1920×1080 [Table 1]); background
tabs ∈ {0, 20, 40, 60} [§3.2]; pages: Amazon, MSN, Pinterest [§3.2]; "Chrome DevTools"
for network control [§3.2]; exact bandwidth/latency Not specified; repetitions Not
specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(background_tabs ∈ {0, 20, 40, 60} ×
page ∈ {Amazon, MSN, Pinterest}) = 4 × 3 = 12⟩; Experiment =
⟨Workflow(browser page load with preloaded background tabs) ⊗ Regime⟨Static:
Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: PC-3, server: real live web endpoints (Amazon, MSN, Pinterest)⟩;
iterations Not specified; telemetry {app_metrics: true (SI values [§3.2])}.

### fusing_speed_index-ES4 — Viewport-size sweep on YouTube

**(i) Raw text.** YouTube landing page loaded under viewport widths 500–2600 px
(1080 px height) and heights 200–1500 px (1920 px width) [§3.2]; step size Not
specified; screenshots at 500 px, 872 px, 1128 px [§3.2; Fig 7 caption];
device/network/browser: Not specified beyond Chrome 91.0 scope assumption.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(viewport_width ∈ [500,2600] px ×
viewport_height ∈ [200,1500] px); count Not specified (step size unstated)⟩;
Experiment = ⟨Workflow(browser page load; Chrome 91.0; viewport parameterized)
⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Not specified, server: real YouTube endpoint⟩;
iterations Not specified; telemetry {app_metrics: true (SI values, visual layout
[§3.2])}.

### fusing_speed_index-ES5 — End-to-end evaluation: SipLoader vs. Vroom vs. Fawkes

**(i) Raw text.** "300 websites randomly chosen from the Alexa top 1,000" [§6.1];
Mahimahi web record-and-replay [§6.1]; server: "Ubuntu 20.04, 2.9 GHz × 16 core CPU,
16-GB memory, 1-Gbps NIC" [§6.1]; client devices per Table 1; PC bandwidth
{1, 10, 100} Mbps × latency {10, 25, 50, 75} ms [§6.1]; LTE and 5G for smartphones
[§6.1]; cache ∈ {cold, 3 h warm, 6 h warm} [§6.1]; Chrome 91.0 [§6.1];
"5 repetitions per environment configuration" [§6.1]; SI via Speedline [§6.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(page ∈ 300-corpus ×
system ∈ {SipLoader, Vroom, Fawkes, default} × bandwidth ∈ {1,10,100} Mbps ×
latency ∈ {10,25,50,75} ms × cache ∈ {cold,3h,6h}); count Not specified (partial
results shown — "omit other configurations as trends are basically the same" [§6.2])⟩;
Experiment = ⟨Workflow(browser page load; Chrome 91.0; Mahimahi replay) ⊗
Regime⟨Static: driven by Mahimahi trace replay (time-varying bandwidth traces from
real captured sessions); Dynamic: Not specified⟩⟩ @
Roles⟨client: PC/smartphone device, server: local Mahimahi replay server
(not a real third-party endpoint)⟩; iterations: 5 [§6.1]; telemetry {app_metrics:
true (SI via Speedline, AFT, PLT [§6.1])}.

### fusing_speed_index-ES6 — Component-ablation campaign (PC-3)

**(i) Raw text.** PC-3 [§6.3]; 300 corpus pages [§6.3]; 100 Mbps network [§6.3];
cold cache [§6.3]; ablation variants ①–④ by incrementally enabling components:
region forest only → +greedy inference → +reactive co-scheduling [§6.3]; results
32.24% SI improvement at ④ [§6.3]. Latency Not specified; repetitions Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(ablation_config ∈ {①,②,③,④}) = 4;
page ∈ 300 corpus⟩; Experiment = ⟨Workflow(browser page load with component-disabled
SipLoader variant) ⊗ Regime⟨Static: Not specified (100 Mbps stated [§6.3]; emulation
tool unstated); Dynamic: Not specified⟩⟩ @
Roles⟨client: PC-3, server: local Mahimahi replay server⟩; iterations Not specified;
telemetry {app_metrics: true (SI improvement % [§6.3])}.

### fusing_speed_index-ES7 — Scheduling-computation efficiency benchmark

**(i) Raw text.** "compare the efficiency and the optimality of dependency-merged greedy
inference with the topological sort-based approach" [§6.3]; Fig 18: "for all of the
300 corpus web pages, we can obtain the nearly SI-optimal scheduling in 12.08 ms on
average" [§6.3]; Fig 17: topological sort at 12 objects averages "1,261 ms" [§6.3];
computation time benchmark; no network conditions.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(algorithm ∈ {greedy_inference,
topological_sort} × page ∈ 300 corpus) = 2 × 300 = 600⟩; Experiment =
⟨Workflow(scheduling algorithm computation; no network) ⊗ Regime⟨Static: Not
applicable (computation benchmark); Dynamic: Not applicable⟩⟩ @
Roles⟨client: compute node, server: Not applicable⟩; iterations Not specified;
telemetry {app_metrics: true (computation time ms [§6.3])}.

### fusing_speed_index-ES8 — Optimality ground-truth study (text-only)

**(i) Raw text.** "134 pages' SI-optimal schedulings as the ground truth" [§6.3];
pages from Alexa top-2,000 sites, solvable by topological sort within 20 minutes [§6.3];
"no substantial difference in the optimality" between greedy and optimal [§6.3];
no figure; text-only results; device/network/browser: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 134 pages [§6.3]⟩; Experiment =
⟨Workflow(SI-optimal scheduling computation + greedy comparison) ⊗ Regime⟨Static:
Not applicable; Dynamic: Not applicable⟩⟩ @
Roles⟨client: compute node, server: Not applicable (pages loaded locally)⟩;
iterations Not specified; telemetry {app_metrics: true (scheduling optimality
comparison [§6.3])}.
