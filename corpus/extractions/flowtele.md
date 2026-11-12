# flowtele — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Scope | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| flowtele-ES1 | Exp1 | OUT-OF-SCOPE (passive data collection) | n/a | n/a |
| flowtele-ES2 | Exp2 | OUT-OF-SCOPE (passive measurement + Markov simulation) | n/a | n/a |
| flowtele-ES3 | Exp3 | OUT-OF-SCOPE (analytical simulation) | n/a | n/a |
| flowtele-ES4 | Exp4 | OUT-OF-SCOPE (exogenous Internet path) | n/a | n/a |
| flowtele-ES5 | Exp5 | OUT-OF-SCOPE (exogenous Internet path) | n/a | n/a |
| flowtele-ES6 | Exp6 | In scope: lab tc-emulated bottleneck | Not specified (multiple sweep dims across sub-figures) | Not specified |
| flowtele-ES7 | Exp7 | OUT-OF-SCOPE (exogenous GENI + real-user cross traffic) | n/a | n/a |
| flowtele-ES8 | Exp8 | OUT-OF-SCOPE (exogenous GENI, dynamic/unknown bottleneck) | n/a | n/a |
| flowtele-ES9 | Exp9 | OUT-OF-SCOPE (exogenous ISP residential link) | n/a | n/a |
| flowtele-ES10 | Exp10 | OUT-OF-SCOPE (time-varying tc-replayed FCC traces) | n/a | n/a |
| flowtele-ES11 | Exp11 | OUT-OF-SCOPE (exogenous GCP-to-ISP path) | n/a | n/a |
| flowtele-ES12 | Exp12 | OUT-OF-SCOPE (exogenous GENI measurement) | n/a | n/a |
| flowtele-ES13 | Exp13 | OUT-OF-SCOPE (exogenous GENI dynamic bottleneck) | n/a | n/a |
| flowtele-ES14 | Exp14 | OUT-OF-SCOPE (CPU overhead measurement) | n/a | n/a |
| flowtele-ES15 | Exp15 | OUT-OF-SCOPE (analytical simulation) | n/a | n/a |
| flowtele-ES16 | Exp16 | OUT-OF-SCOPE (analytical simulation) | n/a | n/a |
| flowtele-ES17 | Exp17 | In scope: lab tc-emulated, calibrator sweep | 8 calibrator fractions [Fig 24 x-axis] | Not specified |
| flowtele-ES18 | Exp18 | OUT-OF-SCOPE (time-varying tc-replayed FCC traces) | n/a | n/a |
| flowtele-ES19 | Exp19 | OUT-OF-SCOPE (analytical simulation) | n/a | n/a |

## Shared methodology (raw text, for ES6 and ES17) (quoted from the paper)


> FlowTele prototype ("roughly 9900 lines of code (mostly in Python and C++)" [§6]);
> fShaper modifies `tcp_congestion_ops->cong_control()` to overwrite cwnd; update
> interval T = 0.1 second; in-flight estimation interval t = 10 ms [§5.1, §B.1];
> vAlloc control interval = 1 second [§6.1]; 25% of FlowTele flows randomly selected
> as calibrator flows [§6.1, §C.2]; user values sampled from Weibull distribution
> modeled after top-10 AdWords [§6.1]; synthetic video chunks at CBR YouTube-
> recommended bitrates [§6.1]; metric: total user value normalized to benchmark
> [Fig 11/13/14 y-axis]; transport: TCP. Any field not overridden is Not specified.

---


## Experiments

### flowtele-ES1 — AdWords value collection + Facebook-profile synthesis

**(i) Raw text.** Google AdWords API queried with all two-letter prefixes, yielding
>6000 AdWords across 14 U.S. cities [§3.1]; 120 Facebook profiles from the ADS
dataset [§3.1]; Figs 2, 3, 30, 31.

**(ii) Grammar.** No network experiment; web-API data collection + profile synthesis.
No Workflow, no Regime, no bottleneck. OUT-OF-SCOPE for Pramana grammar.

### flowtele-ES2 — Residential BW measurements + Markov p_wl simulation

**(i) Raw text.** Available-bandwidth measurements of "several residential networks"
[§3.2]; Markov simulation over typical bitrate/buffer-time sets; video session 260 s
[§3.2]; Fig 5.

**(ii) Grammar.** Passive network measurement + mathematical simulation. No
controlled bottleneck, no synthetic traffic generation, no testbed.

### flowtele-ES3 — Standalone vAlloc analytical simulations

**(i) Raw text.** Analytical simulation of the vAlloc bandwidth allocator; schemes:
vAlloc / fairness / fairness w/ removal; parameter sweeps across p_wl, p_dl,
quadratic coefficient, Weibull k [§3.4]; Figs 6, 7, 8.

**(ii) Grammar.** Pure allocation-algorithm simulation; no network testbed or
packet-level traffic. OUT-OF-SCOPE for Pramana grammar.

### flowtele-ES4 — Standalone fShaper, US network setting

**(i) Raw text.** GCP Los Angeles (content) → Illinois (users), cross-traffic
sender at GCP Montréal; RTT provider-user ~55 ms, cross-traffic-user ~31 ms
[Table 2]; up to 1 Gbps; 200/100 FlowTele flows [§5.2]; Fig 10, Tab 2.

**(ii) Grammar.** Real Internet path; bottleneck = last-mile ISP link (exogenous,
not under Pramana's control). OUT-OF-SCOPE.

### flowtele-ES5 — Standalone fShaper, Asia network setting

**(i) Raw text.** GCP Tokyo (content) → Taiwan (users), cross-traffic sender at
GCP Taiwan; RTT provider-user ~40 ms, cross-traffic-user ~7 ms [Table 2]; up to
1 Gbps [§C.2]; Figs 22, Tab 10, Figs 23/25 (assumed).

**(ii) Grammar.** Real Internet path; exogenous bottleneck. OUT-OF-SCOPE.

### flowtele-ES6 — Integration evaluation, lab controlled environment (Table 3 setting 1)

**(i) Raw text.** "We impose a first-hop link capacity of 200Mbps–1Gbps using
droptail buffers using the tc command" [§6.1, L2131-2132]; "The control interval
of vAlloc is 1 second, and fShaper updates cwnd every 0.1 second. We randomly
selected 25% of FlowTele flows as calibrator flows" [§6.1, L2123-2125]; RTT
~10–40 ms [Table 3 row 1, L1716]; 100 FlowTele flows, capacity sweep 200Mbps–1Gbps
[§6.1, L2133]; flow-count sweep 20–150 [Fig 11(b) x-axis]; churn: 5 new flows every
5 s, each exits after 60 s, 1Gbps [§6.1, L2197-2199]; CCA/RTT interaction: 80
FlowTele + 80 cross-traffic flows, CCAs {NewReno, Vegas, BBRv2, Cubic} [§6.1,
L2205]; §6.2 throttling comparison: 80 FlowTele + 80 Cubic, 1Gbps [§6.2, L3018];
video encoding: CBR at YouTube-recommended bitrates, synthetic chunks [§6.1]; all
within one lab/tc campaign (Table 3 setting 1).

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(
  Regime.Static.capacity_down ∈ 200–1000 Mbps [§6.1] ×
  Regime.Static.queue: droptail, tc [§6.1] ×
  flow_count [Fig 11(b)] ×
  calibrator_cca × cross_traffic_cca [§6.1/Fig 12];
  total count Not specified — multiple sub-sweeps in distinct figures)⟩;
Experiment = ⟨Workflow_F(FlowTele video streaming session; params: bitrate
selection by vAlloc; cca: ⟨algo: fshaper, stack: tcp_congestion_ops_kernel_module⟩
[§B.1, L3518-3520]; params.calibrator_pct: 0.25 [§6.1]) @ path.latency: 10–40 ms
[Table 3 row 1] ⊗ Regime⟨Static: capacity_down ∈ 200–1000 Mbps, queue: droptail
(tc); Dynamic: pressure = load(iperf × N_cross, cca: ⟨algo: cubic⟩ ↦ cross-
traffic node)⟩⟩; iterations Not specified; telemetry {app_metrics: true (total
user value, normalized; TCP-friendliness ratio), pcap: Not specified}.

### flowtele-ES7 — Integration over GENI: Chicago InstaGENI → Illinois

**(i) Raw text.** GENI path, Chicago InstaGENI → Illinois; up to 1 Gbps, RTT
~12 ms [Table 3 row 2]; dynamic bottleneck; cross traffic: real user Internet
traffic via proxy (50–100 Mbps) [§6.1]; 50 FlowTele + 50 Cubic flows [§6.1];
15 runs [§6.1]; Fig 13(a), Tab 5.

**(ii) Grammar.** GENI inter-site path with dynamic/real-user bottleneck.
Exogenous infrastructure → OUT-OF-SCOPE.

### flowtele-ES8 — Integration over GENI: Vermont InstaGENI → Texas InstaGENI

**(i) Raw text.** Vermont InstaGENI → Texas InstaGENI; up to 0.5 Gbps, RTT ~40 ms
[Table 3 row 3]; "Both the bottleneck and total capacity are dynamic and unknown a
priori" [§6.1]; 20 FlowTele + 20 Cubic flows [§6.1]; 15 runs [§6.1]; Fig 13(b), Tab 5.

**(ii) Grammar.** Exogenous GENI path; dynamic/unknown bottleneck → OUT-OF-SCOPE.

### flowtele-ES9 — Cloud→ISP: GCP Ohio → Illinois residential link

**(i) Raw text.** GCP Ohio → Illinois; "a real ISP residential link with 1Gbps
advertised downstream bandwidth" [§6.1]; RTT ~15 ms [Table 3 row 4]; 100 FlowTele
+ 100 Cubic flows [§6.1]; experiments run "every 2 hours for a day" [§6.1];
Fig 14(a), Tab 5.

**(ii) Grammar.** Exogenous ISP residential link bottleneck → OUT-OF-SCOPE.

### flowtele-ES10 — Cloud→ISP: Digital Ocean NY → Toronto, FCC-trace-emulated ISP

**(i) Raw text.** Digital Ocean NY → Toronto; bottleneck "emulated by tc... replay
the bottleneck capacity based on the bandwidth traces using the tc command" [§6.1,
L2558-2559]; RTT ~13 ms [Table 3 row 5]; FCC Datasets [§6.1]; ~2Gbps ISP capacity
(510 flows) [§6.1]; 200 FlowTele flows [§6.1]; Fig 14(b), Figs 27-29.

**(ii) Grammar.** Time-varying bottleneck (FCC bandwidth traces replayed via tc,
varying capacity within session) → OUT-OF-SCOPE.

### flowtele-ES11 — Cloud→ISP: GCP Ohio → Illinois, fShaper vs MulCubic

**(i) Raw text.** GCP Ohio → Illinois; "roughly 1Gbps bottleneck" [§6.1, L2564];
RTT ~20 ms [Table 3 row 6]; 100 FlowTele + 100 Cubic flows [§6.1]; comparison:
FlowTele vs MulCubic; 15 runs (x-axis of Fig 14(c)); Fig 14(c), Tab 5.

**(ii) Grammar.** Real GCP-to-ISP Internet path; bottleneck is the real ISP link.
Exogenous → OUT-OF-SCOPE.

### flowtele-ES12 — Co-bottleneck detection accuracy (Pathneck-MF)

**(i) Raw text.** Controlled GENI testbed; content provider "located in the Midwest",
next-hop controlled via tc; destinations: GENI nodes NW/UW/MI [§6.3]; 20 probes per
scenario [§6.3]; precision/recall per scenario (Table 6); Tab 6.

**(ii) Grammar.** GENI measurement experiment (co-bottleneck detection probe campaign
with ground-truth verification). The measurement subject is the detection algorithm,
not network traffic generation. OUT-OF-SCOPE.

### flowtele-ES13 — Dynamic bottleneck FlowTele run (Pathneck-MF)

**(i) Raw text.** Multiple-bottleneck GENI environment (2nd setting of Table 6);
30 FlowTele flows across NW/UW/MI sites; content provider upstream capacity
dynamically changed from 500Mbps downward [§6.3]; 15 runs [§6.3]; Fig 17.

**(ii) Grammar.** Exogenous GENI infrastructure + dynamic/within-session capacity
change → OUT-OF-SCOPE (both exogenous-path and time-varying-capacity grounds).

### flowtele-ES14 — CPU overhead measurement (GCP VM)

**(i) Raw text.** GCP VM "64-core, 128-thread AMD EPYC 7B12 CPUs; Our VM had 4
threads and 4GB memory" [§6.3]; sar used to measure CPU utilization difference;
flow counts {10, 20, 50, 100, 200} [Table 7]; Table 7.

**(ii) Grammar.** System overhead measurement (CPU utilization) on a GCP cloud VM.
No bottleneck, no controlled topology. OUT-OF-SCOPE.

### flowtele-ES15 — Standalone qAlloc simulation, Group One

**(i) Raw text.** Simulated platform with emulated network links + virtual video
clients; 10 end-user links, shared link 40Mbps/50Mbps; simulations run 180 s [§C.1];
Tab 8, Fig 20.

**(ii) Grammar.** Analytical simulation of the qAlloc QoE allocator. No testbed, no
physical traffic. OUT-OF-SCOPE.

### flowtele-ES16 — Standalone qAlloc simulation, Group Two

**(i) Raw text.** Same simulated platform; 100 end-user links, random bandwidth
Uniform [10, 30] Mbps; 5 sets × 2 runs [§C.1]; Tab 9, Fig 21.

**(ii) Grammar.** Analytical simulation → OUT-OF-SCOPE.

### flowtele-ES17 — Calibrator-flow-percentage sweep

**(i) Raw text.** "we ran 80 FlowTele flows and 80 cross traffic flows with Cubic
using 1Gbps bandwidth and RTT 20 ms" [§C.2, L4261-4262]; swept factor: percentage
of calibrator flows; x-axis ticks {1, 5, 15, 20, 25, 30, 35, 45}% [Fig 24 x-axis];
metrics: friendliness of FlowTele flows and aggregate goodput variance at 1-second
intervals [§C.2]; "as we use fewer than 15% calibrator flows, goodput variance
increases. We conservatively chose 25% of flows as calibrator" [§C.2]; Fig 24.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(calibrator_fraction ∈
{1, 5, 15, 20, 25, 30, 35, 45}% [Fig 24]) = 8 × 1 = 8⟩;
Experiment = ⟨Workflow_F(FlowTele video streaming; cca: ⟨algo: fshaper,
stack: tcp_congestion_ops_kernel_module⟩ [§B.1]) @ path.latency: 20 ms [§C.2]
⊗ Regime⟨Static: capacity_down = 1000 Mbps [§C.2], queue: Not specified (tc
implied; discipline not stated); Dynamic: pressure = load(iperf × N_cross,
cca: ⟨algo: cubic⟩ ↦ cross-traffic node [§C.2])⟩⟩; iterations Not specified;
telemetry {app_metrics: true (friendliness ratio, goodput variance per 1 s
intervals [§C.2])}.

### flowtele-ES18 — Q-FlowTele evaluation vs MulCubic/Minerva/Cubic

**(i) Raw text.** "the fifth network setting from Table 3" (Digital Ocean NY →
Toronto, FCC-trace-emulated bottleneck, tc replay [§D.1]); flow settings from
Table 4 (ISPs A, B, E, F); 3 runs per scheme × setting [§D.1]; Fig 26.

**(ii) Grammar.** Time-varying bottleneck (FCC-trace-replayed tc) → OUT-OF-SCOPE.

### flowtele-ES19 — Customized-user-model learning simulation

**(i) Raw text.** Simulation learning per-user p_wl from watch histories; "180
simulated hours" per training round [§E]; average bottleneck bandwidth 25–200 Mbps
shared by 12 users [Fig 32 x-axis]; Fig 32.

**(ii) Grammar.** Learning simulation (no network testbed) → OUT-OF-SCOPE.
