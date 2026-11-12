# mutant — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| mutant-ES1 | E1 | static.cca ∈ {cubic, hybla, bbr2, vegas} × env ∈ 6 named × flow-config ∈ {single, multi} | 24 (single-flow); multi-flow pairing unstated → Not specified [§2] | Not specified |
| mutant-ES2 | E2 | application.workflow ∈ {mutant_system, sage} [Fig 2] | 2 | Not specified |
| mutant-ES3 | E3 | static.cca ∈ {mutant_system + 11-CCA pool} × env ∈ 15 named (3 LTE + 3 5G [Fig 4 a–f], 3 wired [Fig 4 g–i], 3 LTE + 3 5G [Fig 15 a–f]) | 12 × 15 = 180 | Not specified |
| mutant-ES4 | E4 [OOS] | application.workflow ∈ 15 × path ∈ {intra-, inter-continental} [Fig 6] | 30 | 10 [§6.2] |
| mutant-ES5 | E5 | application.params.k ∈ {2..11} × env (one cellular + all test envs) | k-axis 10; env-axis Not specified → total Not specified | Not specified |
| mutant-ES6 | E6 | application.params.pool_strategy ∈ {mpts, random, mixed} × env ∈ 6 [§6.3; Fig 9] | 3 × 6 = 18 | Not specified |
| mutant-ES7 | E7 | solo: static.cca ∈ {cubic, bbr2, hybla, vegas, mutant_system} (5) + pair: mutant_system ⊗ competitor ∈ same 5 | 10 [§6.4; Fig 10] | Not specified |
| mutant-ES8 | E8 | application.params.delta ∈ {10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 0.5, 1} s × env ∈ all test envs | δ-axis 6; env-axis Not specified → total Not specified | Not specified |
| mutant-ES9 | E9 | application.params.feature_config ∈ {full, static, raw_all, raw_static} × flow-family ∈ {single, multi} × env | 4 × 2 Not specified → total Not specified | Not specified |
| mutant-ES10 | E10 | scenario ∈ 4 5G × application.workflow ∈ {mutant_system + K=4 pool} | 4 × 5 = 20 | Not specified |

## Experiments

### mutant-ES1 — motivation: 4 protocols × 6 environments, single- + multi-flow (Fig 1)

**(i) Raw text.** "no protocol is dominant in all the cases for single-flow
settings" [§2]; protocols Cubic, Hybla, BBR2, Vegas [Fig 1 legend]; six
environments: "fixed bandwidth, low capacity, high rtt, large queue i.e., buffer
of the bottleneck router, mixed conditions i.e., large queue with high RTT, step
i.e., with regular and abrupt channel bandwidth fluctuations" [§2]; metrics =
tput/delay (single-flow panel) and harm (multi-flow panel) [Fig 1 caption]. Exact
bandwidth/RTT/queue per env, competing-flow composition, duration, repetitions:
Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(static.cca ∈
{cubic, hybla, cca⟨algo:bbr,version:v2alpha,build:non-mainline⟩, vegas}
× env ∈ 6 condition classes × flow-configuration ∈ {single-foreground,
multi-foreground — NOT a spec field; flow-count is a Workflow.params axis and
the Foreground cardinality)) = 24 single-flow + Not specified multi-flow⟩;
Experiment = ⟨Workflow(iperf3, shell [§6.1]) ⊗ Regime⟨Static: values Not
specified within §6.1 wired ranges; step class: bottleneck-capacity-change →
OUT-OF-SCOPE; Dynamic: Not specified (silence, §5b.2) for single-flow; multi-flow
panel: Foreground = {Workflow_α @ node_client, Workflow_β @ node_client_2}⟩⟩ @
Roles⟨client, server: Linux host [§6.1]⟩; iterations Not specified; telemetry
{pcap: true (throughput + delay), app_metrics: true (harm accounting)}.

### mutant-ES2 — learning-time vs offline RL (Fig 2)

**(i) Raw text.** Mutant vs Sage (offline RL), link utilization over 0–10 s
[Fig 2]. Conditions: Not specified. [§2; Fig 2 legend]

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈
{mutant_system@sha, sage_system@sha}) = 2⟩; Experiment = ⟨Workflow(iperf3-class
bulk transfer, program workflow per system) ⊗ Regime⟨Static: Not specified;
Dynamic: Not specified (silence)⟩⟩ @ Roles⟨client, server⟩; iterations Not
specified; telemetry {pcap: true (link utilization derived from
metrics.transport.throughput_mbps_ts)}.

### mutant-ES3 — main emulated campaign: 15 environments × (Mutant + 11-CCA pool) (Fig 4, 5, 14, 15)

**(i) Raw text.** "compare Mutant against the pool of schemes it learns from"
[§6.2]; Pantheon + Mahimahi, iperf3, 2 minutes per protocol [§6.1]; k=6,
δ=10⁻² s [§6.1]. 9 environments Fig 4: AT&T/T-Mobile/Verizon LTE (3 LTE),
Beach Stat. / Beach Stat. 2 / Park Stat. 5G (3 5G), wired Low BW / "Step with
large queue" / High RTT (3 wired) [Fig 4 subcaptions]; 6 additional environments
Fig 15: Walking Times Sq. / Bus Riding / Stationary Times Sq. LTE (3 LTE) +
Corniche / Corniche Walking / City Drive 5G (3 5G) [Fig 15 subcaptions]; traces
from [2] and [6] [App B]. Wired ranges [12,96] Mbps / [10,120] ms / [1,20]×BDP.
Repetitions, per-trace numeric conditions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈
{mutant_system@sha (§2 program-workflow) + 11 pool schemes: static.cca ∈ {cubic,
hybla, cca⟨algo:bbr,version:v2alpha⟩, westwood, veno, vegas, yeah, bic, htcp,
highspeed, illinois}} × env ∈ 15) = 12 × 15 = 180⟩; Experiment = ⟨Workflow(iperf3,
shell; params.duration = 2 min [§6.1]) ⊗ Regime⟨Static: **wired** leaves (2/15
envs: Low BW, High RTT) = fixed {capacity_down ∈ [12,96] mbps, latency ∈
[10,120] ms, queue.args ∈ [1,20]×BDP} (exact values Not specified →
default-with-echo); **step + all cellular/5G leaves (13/15 envs) = OUT-OF-SCOPE**
(bottleneck capacity change / trace-driven capacity schedule — CORPUS_PROMPT_v4
§2); Dynamic: Not specified (silence)⟩⟩ @ Roles⟨client, server: Linux host⟩;
iterations Not specified; telemetry {pcap: true, app_metrics: true (reward +
embedding log for Fig 14 view)}.

### mutant-ES4 — Fabric real-world validation (Fig 6) [OUT OF SCOPE]

**(i) Raw text.** "validate Mutant on real-world network environments" [§6.2];
"different hosts across the US and Europe using Fabric [10] testbed" [§6.2];
intra- and inter-continental runs [Fig 6 subcaptions]; 15 schemes [Fig 6 legend];
"run one flow for 30 seconds and repeat the experiment 10 times" [§6.2]. Host
locations/hardware, path conditions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈ 15 ×
path ∈ {intra, inter}) = 30⟩; Regime⟨Static: none imposed — inhabited real WAN
paths; Dynamic: none⟩; Roles⟨client, server: Fabric nodes, third-party⟩;
iterations 10 [§6.2]; telemetry {pcap: true}.

### mutant-ES5 — MPTS k-sweep (Fig 7, 8)

**(i) Raw text.** "varying k between 2 and 11" [§6.3]; k ∈ {2,4,6,8,10} [Fig 7];
"best-reward rate across all our network test environments" [§6.3]; "cellular link"
for Fig 7, "all network scenarios" for Fig 8 [Fig 7/8]; T=100 MPTS rounds
[§6.3]. Specific cellular link, env count, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.params.k ∈
{2..11} × env ∈ {one cellular link [Fig 7]} ∪ {all test envs [Fig 8], Not
specified}) — k-axis 10, total Not specified⟩; Experiment = ⟨Workflow(iperf3
under mutant_system; params.k swept; MPTS T=100 workload-internal) ⊗ Regime⟨Static:
cellular env (Fig 7) → OUT-OF-SCOPE (trace-driven capacity); all-test-envs (Fig 8):
mixed static/cellular — static-wired sub-family SATISFIED, cellular sub-family
OOS; Dynamic: Not specified (silence)⟩⟩; Roles⟨client, server⟩; iterations Not
specified; telemetry {pcap: true, app_metrics: true}.

### mutant-ES6 — pool-selection-strategy comparison (Fig 9)

**(i) Raw text.** Strategies: MPTS k=6, random k=6, mixed [§6.3]; "six different
network environments sampled from the sets in Section 6.1" [§6.3]; 2 minutes
each [§6.3]; metric = average normalized reward [Fig 9]. Env 0–5 identities,
repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.params.pool_strategy
∈ {mpts, random, mixed} × env ∈ 6) = 18⟩; Experiment = ⟨Workflow(iperf3 under
mutant_system; params.k=6, params.pool_strategy swept; duration 2 min) ⊗
Regime⟨Static: env identities Not specified (sampled from §6.1 — may include
fixed-wired or step/cellular; identity unstated); Dynamic: Not specified⟩⟩;
Roles⟨client, server⟩; iterations Not specified; telemetry {app_metrics: true,
pcap: true}.

### mutant-ES7 — harm / fairness on an emulated cellular link (Fig 10, 11)

**(i) Raw text.** "tested some protocols in Mutant's pool on an [emulated
cellular link]" [§6.4]; protocols Cubic, BBR2, Hybla, Vegas + Mutant self-harm
[Fig 10]; harm h_t = (x−y)/x, h_d = (y−x)/y [§6.4]; h_t ∈ {0.280, 0.258,
0.094, 0.310, 0.135}, h_d ∈ {0.016, 0.033, 0.097, 0.062, 0.015} [Fig 10].
Cellular-link parameters, durations, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves:
solo sweep(static.cca ∈ {cubic, cca⟨algo:bbr,version:v2alpha⟩, hybla, vegas,
Not specified for mutant_system [program workflow]}) = 5, Dynamic: none
(positive solo statement, §5b.9) +
pair sweep(Foreground = {Workflow_α=mutant_system, Workflow_β = competitor}) ×
competitor ∈ same 5 = 5, Foreground n-party) — 10 total⟩; Experiment =
⟨Workflow(iperf3) ⊗ Regime⟨Static: one emulated cellular link, trace-driven
capacity → OUT-OF-SCOPE (CORPUS_PROMPT_v4 §2); Dynamic: none (solo) |
Foreground = {α,β} (pairs, in-grammar v2)⟩⟩ @ Roles⟨client, server⟩;
iterations Not specified; telemetry {pcap: true (both flows' throughput/delay
for harm calculation), app_metrics: true}.

### mutant-ES8 — step-duration δ sweep (Fig 12)

**(i) Raw text.** δ axis {10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 0.5, 1} s [Fig 12 x-axis];
"best reward rate across all our network test environments" [§6.5]; δ
percentages {14.12, 35.15, 56.34, 51.74, 21.31, 12.92}% [§6.5]. Per-run
duration, repetitions, env count: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.params.delta ∈
{10⁻⁴,10⁻³,10⁻²,10⁻¹,0.5,1} × env ∈ all test envs, Not specified) — total Not
specified⟩; Experiment = ⟨Workflow(iperf3 under mutant_system; params.delta
swept) ⊗ Regime⟨Static: §6.1 test envs (mixed fixed-wired + step/cellular);
Dynamic: Not specified⟩⟩; Roles⟨client, server⟩; iterations Not specified;
telemetry {app_metrics: true, pcap: true}.

### mutant-ES9 — input-feature ablation (Fig 13)

**(i) Raw text.** Configs: full Mutant, Mutant-STATIC, Raw-ALL, Raw-STATIC [§6.5];
"single and multi-flow environments" [§6.5; Fig 13 legend]. Envs, competing-flow
counts, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.params.feature_config
∈ {full, static, raw_all, raw_static} × flow-family ∈ {single-foreground,
multi-foreground} × env, Not specified) — config axis 4 × 2, total Not specified⟩;
Experiment = ⟨Workflow(iperf3 under mutant_system variant — ablated feature
config is an application param if variant is a param-controlled build, or a
distinct workflow@sha if a separate artifact) ⊗ Regime⟨Static: §6.1 envs,
mixed (Not specified); Dynamic: Not specified (single); multi-flow panel:
Foreground = {Workflow_α, Workflow_β} (n-party, in-grammar v2)⟩⟩; Roles;
iterations Not specified; telemetry {app_metrics: true, pcap: true}.

### mutant-ES10 — reward vs optimal, four 5G scenarios (Fig 16)

**(i) Raw text.** MPTS K=4; "trained to convergence and subsequently tested on
network traces for 1500 steps and δ=10⁻²" [App B]; scenarios: 5G Cell. Beach
Stat., Beach Stat. 2, City Drive, Park Stationary [Fig 16 subcaptions]; per-
scenario pools in Fig 16 legends; metric = reward per step 0–1500 [Fig 16].
Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scenario ∈ 4 × application.workflow
∈ {mutant_system + K=4 pool}) = 4 × 5 = 20⟩; Experiment = ⟨Workflow(iperf3;
mutant_system params: K=4, δ=10⁻², in-run train-then-test = workload-internal)
⊗ Regime⟨Static: 5G trace-driven capacity → OUT-OF-SCOPE; Dynamic: Not specified
(silence)⟩⟩; Roles⟨client, server⟩; iterations Not specified; telemetry
{app_metrics: true (per-step reward series), pcap: true}.

## Tier-1 gate (pipeline/corpus/gate_tier1.py)

**Result:** 5 flags → route to Tier-2.
