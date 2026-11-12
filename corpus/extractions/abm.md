# abm — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| abm-ES1 | Exp1 (Figs 6+7) | load ∈ {20,40,60,80}% × request_size ∈ {20,40,60}% [§4.2; Fig 6/7 axis ticks] | 4 × 3 = 12 attempted (plus cross: 1×3 + 4×1 = 7 boundary leaves; total sweep product 4 × 3 = 12) | Not specified |
| abm-ES2 | Exp2 (Fig 8) | cubic_load ∈ {20,40,60}% [Fig 8 x-axis] | 3 | Not specified |
| abm-ES3 | Exp3 (Fig 9) | cc_algo ∈ {Cubic, DCTCP, TIMELY, PowerTCP} × request_size ∈ {10,25,50,75}% [§4.2; Fig 9 x-axis ticks] | 4 × 4 = 16 | Not specified |
| abm-ES4 | Exp4 (Fig 10) | queues_per_port ∈ {2,3,4,5,6,7,8} [Fig 10 x-axis ticks; §4.2] | 7 | Not specified |
| abm-ES5 | Exp5 (Fig 11) | buffer_size ∈ {Trident2 9.6 KB, 8 KB, 7 KB, 6 KB, Tomahawk 5.12 KB, Tofino 3.44 KB} × cc_algo ∈ {DCTCP, PowerTCP} [§4.3; Fig 11 x-axis] | 6 × 2 = 12 | Not specified |
| abm-ES6 | Exp6 (Fig 12) | update_interval ∈ {1, 10, 100, 1000} RTTs [§4.4; Fig 12 x-axis ticks] | 4 | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> NS3 network simulator [§4.1, "Our evaluation is based on network simulator NS3 [9]"];
> leaf-spine topology: 8 spine switches, 8 leaf switches, 256 servers (32 per leaf)
> [§4.1]; link capacity 10 Gbps, 4:1 oversubscription [§4.1]; base propagation delay
> 10 μs per link [§4.1, "each link has 10𝜇𝑠 propagation delay"]; switch buffer
> 9.6 KB per-port-per-Gbps following Broadcom TridentII [§4.1] (overridden in ES5);
> workloads: (i) web-search flow-size distribution at loads 20%–80% [§4.1], (ii)
> synthetic incast traffic (each server requests from servers in a different rack),
> request sizes 10%–75% of buffer [§4.1]; BM schemes: ABM, Dynamic Thresholds (DT),
> Flow Aware Buffer (FAB), Complete Sharing (CS), IB (AFD + Elephant trap) [§4.1];
> CCAs: Cubic, DCTCP, TIMELY, PowerTCP, θ-PowerTCP [§4.1]; ABM α = 0.5 for all
> queues unless otherwise specified [§4.1]; experiment duration and repetition count
> Not specified.

---


## Experiments

### abm-ES1 — load × request-size comparison, Cubic-only (Figs 6, 7)

**(i) Raw text.** "In Figure 6a, we show the 99th percentile FCT slowdown for the flows
of incast workload with a fixed request size of 30% of the buffer size, as a function
of the load created by the web-search workload. All flows use Cubic." [§4.2]; "In Figure
7a, we show the 99th percentile FCT slowdown for the flows of incast workload with fixed
web-search load in 40% as a function of the request size of incast traffic." [§4.2];
schemes DT, FAB, CS, IB, ABM [Fig 6/7 legend; §4.1]; load axis 20/40/60/80%
[Fig 6 x-axis]; request-size axis 20/40/60% of buffer [Fig 7 x-axis]; results:
ABM reduces 99-pct FCT slowdown by 12.6% on average at 20% load, 90.12% at 40%,
94% at 80% [§4.2]; buffer-usage reduction 54.2% on average vs DT/FAB/IB [§4.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(load ∈ {20,40,60,80}%[§4.2] ×
request_size ∈ {20,40,60}%[§4.2 Fig 7 axis]) = 4 × 3 = 12; BM_scheme ∈ {ABM, DT,
FAB, CS, IB} is the comparison treatment within each leaf, not a sweep dim (all schemes
run on the same campaign per §4.1)⟩; Experiment = ⟨Workflow(NS3: web-search + incast
synthetic traffic; params: load, request_size) ⊗ Regime⟨Static: capacity 10 Gbps
[§4.1], topology leaf-spine 8×8×256 [§4.1], BM_scheme per-leaf; Dynamic: Not
specified⟩⟩ @ Roles⟨servers: 256 simulated NS3 nodes⟩; iterations Not specified;
telemetry {app_metrics: true (FCT slowdown 99th pct, buffer occupancy, throughput)}.

### abm-ES2 — priority isolation across mixed CCA (Fig 8)

**(i) Raw text.** "To evaluate ABM's performance isolation across different priorities
compared to the default, namely DT" [§4.2]; three priorities with Cubic, DCTCP,
θ-PowerTCP (θ-PowerTCP carries incast, Cubic and DCTCP carry web-search) [§4.2];
Cubic load swept: axis 20, 40, 60% [Fig 8 x-axis]; schemes Default (DT) vs With ABM
[Fig 8 legend]; ABM reduces tail FCT slowdown by up to 90.92% [§4.2]; incast request
size Not specified; DCTCP/θ-PowerTCP load Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cubic_load ∈ {20,40,60}%[Fig 8 x-axis])
= 3; BM scheme ∈ {DT, ABM} is the treatment; topology and parameters INHERITED from
shared methodology⟩; Experiment INHERITED from ES1 except: multi-protocol workload
(θ-PowerTCP for incast, Cubic + DCTCP for web-search, three separate priority queues
per port) [§4.2]; iterations Not specified; telemetry {app_metrics: true (99th-pct FCT
slowdown per priority, buffer occupancy)}.

### abm-ES3 — ABM with advanced CCA sweep (Fig 9)

**(i) Raw text.** "we evaluated it under the following four scenarios. In each scenario
one congestion control algorithm from Cubic, DCTCP, TIMELY or PowerTCP runs at the
hosts" [§4.2]; web-search at 40% load; incast at varying request sizes; axis ticks 10,
25, 50, 75% of buffer [Fig 9 x-axis]; schemes: Default (DT) vs With ABM [Fig 9 legend];
results: at 12.5% request size, ABM reduces FCT slowdown by 39.1% vs Cubic (with DT)
and 10.3% vs DCTCP [§4.2]; at 37.5%, 88% vs Cubic and DCTCP, 33.3% for TIMELY [§4.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cc_algo ∈ {Cubic, DCTCP, TIMELY,
PowerTCP}[§4.2] × request_size ∈ {10,25,50,75}%[Fig 9 x-axis ticks]) = 4 × 4 = 16;
BM scheme ∈ {DT, ABM} is the treatment⟩; Experiment INHERITED from shared methodology
with fixed load 40% [§4.2]; workflow.cca corresponds to the per-host CC algorithm but
datacenter topology and per-switch BM remain outside the grammar; iterations Not
specified; telemetry {app_metrics: true (99th-pct FCT slowdown per CC algorithm)}.

### abm-ES4 — queues-per-port sweep (Fig 10)

**(i) Raw text.** "To evaluate the impact of 𝜇𝑝𝑖 factor on ABM's thresholds" [§4.2];
queues per port varied; axis labeled 2 3 4 5 6 7 8 [Fig 10 x-axis]; web-search at 40%
load, incast request size 25% [§4.2]; CC: Cubic and DCTCP [§4.2]; schemes ABM vs DT
[Fig 10 legend]; at 5 queues ABM reduces 99-pct FCT slowdown of Cubic and DCTCP by
88.9% on average; at 8 queues by 92.6% [§4.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(queues_per_port ∈ {2,3,4,5,6,7,8}
[Fig 10 x-axis]) = 7; cc_algo ∈ {Cubic, DCTCP} run simultaneously (two series); BM
scheme ∈ {DT, ABM} is the treatment; fixed load 40%, request_size 25%[§4.2]⟩;
Experiment INHERITED from shared methodology; iterations Not specified; telemetry
{app_metrics: true (99th-pct FCT slowdown, buffer occupancy)}.

### abm-ES5 — shallow-buffer sweep (Fig 11)

**(i) Raw text.** "evaluate the benefits of ABM with smaller, yet realistic buffer sizes
e.g., Tomahawk" [§4.3]; buffer sizes: Trident2 9.6 KB, 8 KB, 7 KB, 6 KB, Tomahawk
5.12 KB, Tofino 3.44 KB per-port-per-Gbps [§4.3; Fig 11 x-axis]; fixed web-search
40%, incast request_size 25% of Trident2 buffer [§4.3]; CC: DCTCP and PowerTCP
considered separately [§4.3]; schemes: ABM, DT, IB [Fig 11 legend]; ABM reduces
99-pct FCT slowdown by 96% (DCTCP) and 92% (PowerTCP) vs DT and IB at 3.44 KB [§4.3].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(buffer_size ∈ {9.6,8,7,6,5.12,3.44} KB
[§4.3] × cc_algo ∈ {DCTCP,PowerTCP}[§4.3]) = 6 × 2 = 12; BM scheme ∈ {ABM, DT, IB}
is the treatment; fixed load 40%, request_size 25% of Trident2 buffer [§4.3]⟩;
Experiment INHERITED from shared methodology with buffer_size override [§4.3]; iterations
Not specified; telemetry {app_metrics: true (99th-pct FCT slowdown)}.

### abm-ES6 — α update-interval sensitivity (Fig 12)

**(i) Raw text.** "evaluate how sensitive ABM is to the update interval when approximating
ABM on top of DT via periodic control-plane reconfiguration of 𝛼" [§4.4]; web-search
40%, incast request_size 75% [§4.4]; 8 queues per port [§4.4]; update intervals: 1, 10,
100, 1000 RTTs [Fig 12 x-axis; "every 100x RTT (i.e., every 8ms)" §4.4]; baseline DT
[§4.4]; at 10x RTT tail FCT slowdown decreases by 84.05%; at 100x RTT by 44.78% vs DT
[§4.4].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(update_interval ∈ {1,10,100,1000} RTTs
[Fig 12 x-axis ticks]) = 4; BM scheme = ABM-approx-on-DT at each interval, vs DT
baseline; fixed load 40%, request_size 75%, 8 queues/port [§4.4]⟩; Experiment INHERITED
from shared methodology with 8-queue override and request_size = 75% [§4.4]; iterations
Not specified; telemetry {app_metrics: true (99.9th-pct FCT for short flows, median FCT
for long flows)}.
