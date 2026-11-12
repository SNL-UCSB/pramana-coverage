# ccanalzyer — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| ccanalzyer-ES1 | Exp1 | workflow.cca.algo ∈ {newreno, bbr, cubic, bic} [Fig 1 caption] | 4 | Not specified |
| ccanalzyer-ES2 | Exp2 | (single trace, usps.com) [§3.2] | 1 | Not specified |
| ccanalzyer-ES3 | Exp3 | target ∈ CrUX Top-10K [§5.1; Fig 4] | 10,000 | Not specified |
| ccanalzyer-ES4 | Exp4 | queue.size ∈ figure-axis set, Not specified [Fig 5] | Not specified | Not specified |
| ccanalzyer-ES5 | Exp5 | queue.size ∈ figure-axis set, Not specified [Fig 6] | Not specified | Not specified |
| ccanalzyer-ES6 | Exp6 | (train) cca 15 × setting 9, iperf@AWS-Va; (test) cca 15 × setting 9, wget@Azure-East [§3.3.1–2] | 15 × 9 × 2 = 270 | 3 (train), 5 (test) [§3.3.1] |
| ccanalzyer-ES7 | Exp7 | cca 15 × setting 4, server AWS-Ohio [§3.3.4; Table 2] | 15 × 4 × 1 = 60 | Not specified |
| ccanalzyer-ES8 | Exp8 | tool ∈ {gordon_client, ig_client} × cca ∈ 15 [§4.2] | 2 × 15 = 30; IG-faithful Azure-train+test sub-campaign leaf count Not specified [§4.2] | Gordon: 75 traces/CCA [§4.2]; IG: 20 [§4.2] |
| ccanalzyer-ES9 | Exp9 | site ∈ Top-10K × setting ∈ 4 accurate [§5.1; §3.4] | 10,000 × 4 = 40,000 attempted (unresponsive/RTT>85ms/all-invalid are OUTCOMES [Table 3], not leaf filters) | 1 [§3.4] |
| ccanalzyer-ES10 | Exp10 | site ∈ Top-10K (IG crawler, ≤500 links/site) [App. C] | 10,000 | 1 |
| ccanalzyer-ES11 | Exp11 | queue.size ∈ figure-axis set × workflow.cca.algo ∈ 15, all-CloudLab [§5.3] | Not specified × 15 | 5 traces per (queue, cca) [§5.3] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> "installed on Cloudlab servers in Wisconsin, USA" [§3.3.1]; bottleneck = "a
> custom switch with a deliberately slowed egress link … records when packets
> are enqueued/dequeued/dropped", implemented with the BESS software switch
> [§3.1]; client issues "pipelined HTTP requests via h2load" [§3.1]; AWS-
> Virginia = training (3 samples/CCA), Azure-East = testing (5 samples/CCA)
> [§3.3.1]; "the 15 built-in wide-area Linux CCAs", BBR = BBRv1 [§1; §3.3.1;
> fn 3]; training = iperf 120 s; testing = wget of a 100 MB Apache-hosted file
> for 60 s [§3.3.1]; queue "set to the power of 2 closest to 1 BDP"
> [§3.3.2 fn 4]; AQM discipline never named → Not specified; controlled
> cross-traffic: Not specified (background traffic appears only as a
> robustness discussion [§3.2]).


## Experiments

### ccanalzyer-ES1 — sawtooth motivation traces (Fig 1)

**(i) Raw text.** "queue occupancy of the bottleneck link from real TCP
connections" [§1]; CCAs New Reno, BBR, Cubic, BIC [Fig 1 caption]; "each have
their own patterns of rising and falling queue size" [§1]. Bandwidth, RTT,
queue size, duration, flow count, generating server: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow.cca.algo ∈ {newreno,
bbr, cubic, bic}) = 4⟩; Experiment = ⟨Workflow(bulk TCP; tool Not specified)
⊗ Regime⟨Static: capacity Not specified, queue Not specified; Dynamic: Not
specified (silence — no positive no-cross-traffic statement)⟩⟩ @
Roles⟨client, server: Not specified⟩; iterations Not specified; telemetry
{qtrace: true (queue-occupancy time series is the result), pcap: Not
specified, app_metrics: false}.

### ccanalzyer-ES2 — ED-vs-DTW illustration trace (Fig 3)

**(i) Raw text.** "a trace collected from usps.com to a Cubic training
sample" [§3.2; Fig 3 caption]; ED = 2.47, DTW = 0.76 [Fig 3a/3b]. Conditions
under which the usps.com trace was collected: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(HTTP
download from live site; params.url = usps.com) ⊗ Regime⟨Static: testbed
bottleneck, values Not specified; imposed at testbed egress [§3.1]⟩⟩ @
Roles⟨client: testbed node, server: real Internet endpoint (usps.com)⟩;
iterations Not specified; telemetry {qtrace: true}.

### ccanalzyer-ES3 — RTT distribution of the Top-10K (Fig 4)

**(i) Raw text.** Ping-time distribution to the Top-10K; "Most websites are
within a distance of 275ms" [Fig 4 caption; §3.3.2]; dataset = CrUX Top-10K,
Feb-2023 bucket [§5.1]. Repetitions per site: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow.params.target ∈
Top-10K) = 10,000⟩; Experiment = ⟨Workflow(ping; shell) ⊗ Regime⟨Static:
none imposed — inhabited (probe characterizes); Dynamic: none (no bottleneck
to impose; measurement of real path)⟩⟩ @ Roles⟨client: testbed node,
server: real endpoints⟩; iterations Not specified; telemetry {app_metrics:
true (RTT samples)}.

### ccanalzyer-ES4 — queue-size effect, Cubic (Fig 5)

**(i) Raw text.** Traces "from Azure-East" [Fig 5 caption]; CCA Cubic [Fig 5
caption]; bw 5 Mbps, RTT 275 ms [Fig 5 caption "5bw-275rtt"; §3.3.2]; queue
sizes swept (figure-axis only; "128 packets is ∼1 BPD in this setting"
[§3.3.2]); duration Not specified; repetitions Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(static.queue.size ∈ figure-axis
set [Fig 5]); count Not specified⟩; Experiment = ⟨Workflow(wget, 100 MB file
[§3.3.1]) @ cca: ⟨algo: cubic⟩ ⊗ Regime⟨Static: capacity_down 5 mbps [Fig 5
"5bw-275rtt"], queue: discipline Not specified, size swept (reference:
"128 packets is ∼1 BPD" [§3.3.2]); Dynamic: Not specified⟩⟩ @
Roles⟨client: testbed, server: Azure-East Apache (real cloud endpoint)⟩;
path.latency: 275 ms [Fig 5 caption]; iterations Not specified;
telemetry {qtrace: true}.

### ccanalzyer-ES5 — queue-size effect, BBR (Fig 6)

**(i) Raw text.** Traces "from Azure-East" [Fig 6 caption]; CCA BBR (BBRv1)
[Fig 6 caption]; bw 5 Mbps, RTT 275 ms [Fig 6 caption "5bw-275rtt"]; queue
sizes swept (figure-axis only, same axis as Fig 5); repetitions Not specified.

**(ii) Grammar.** INHERITED from ES4 (identical setup), delta:
workflow.cca.algo: bbr (BBRv1) [Fig 6 caption].
ExperimentSet⟨leaves: sweep(static.queue.size ∈ figure-axis set [Fig 6]);
count Not specified⟩; Experiment = ⟨Workflow(wget, 100 MB) @ cca: ⟨algo: bbr⟩
⊗ Regime⟨Static: capacity_down 5 mbps, queue swept; Dynamic: Not specified⟩⟩ @
Roles⟨client: testbed, server: Azure-East⟩; path.latency: 275 ms; iterations
Not specified; telemetry {qtrace: true}.

### ccanalzyer-ES6 — main 1NN-DTW collection (Figs 7–12, 14–17, 23; Table 2 shared)

**(i) Raw text.** Training: iperf at AWS-Virginia, 3 samples/CCA [§3.3.1];
testing: wget 100 MB at Azure-East, 5 samples/CCA [§3.3.1]. Sweeps:
bw ∈ {5, 10, 15} Mbps, RTT ∈ {85, 130, 275} ms — 9 settings; queue ≈ 1 BDP
per setting [§3.3.2]; 96% accuracy (649/675) [§3.3.2]. 15 CCAs [§3.3.1].
Testing traces 60 s, ~20 s used [§3.3.1, §3.3.3]. 4 accurate settings:
"bandwidth is 5 or 10 mbps, and RTT is 85 or 130 ms" [§3.3.2; §3.4; Table 2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(Regime.Static.capacity_down ∈
{5, 10, 15} mbps [§3.3.1] × path.latency ∈ {85, 130, 275} ms [§3.3.1] ×
workflow.cca.algo ∈ 15 CCAs [§3.3.1] × ⟨workflow, server⟩ ∈ {(iperf, AWS-Va),
(wget100MB, Azure-East)}) = 9 × 15 × 2 = 270 leaves, but train/test sub-campaigns
cross the workflow × server factor: treat 9 settings × 15 CCA × 2 sub-campaigns =
270⟩; Regime⟨Static: capacity_down ∈ {5,10,15} mbps, queue: discipline Not
specified, size ≈1 BDP per setting (4 named settings in Table 2 [§3.3.2]);
Dynamic: Not specified⟩; path.latency per-workflow: ∈ {85,130,275} ms [§3.3.1];
workflow.cca: ⟨algo: per-leaf 15 CCAs⟩; Roles⟨client: testbed, server:
per sub-campaign⟩; iterations: 3 (train leaves), 5 (test leaves) [§3.3.1];
telemetry {qtrace: true, pcap: true [§4.3: "We collect pcaps for all experiments"]}.

### ccanalzyer-ES7 — AWS-Ohio threshold-tuning collection (Table 2)

**(i) Raw text.** "run classification on a new testing set (we use a server
hosted in the AWS-Ohio region)" [§3.3.4]; 4 settings [Table 2]; leave-one-CCA-
out over 15 CCAs [§3.3.4]; repetitions/duration Not specified. Table 2 values:
10bw-130rtt-128q, 10bw-85rtt-128q, 5bw-130rtt-64q, 5bw-85rtt-64q [Table 2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(Regime.Static.capacity_down ×
path.latency ∈ 4 accurate settings [Table 2] × workflow.cca.algo ∈ 15) =
4 × 15 = 60; workflow wget 100 MB; server AWS-Ohio⟩; Regime: 4 accurate
settings from Table 2; Dynamic Not specified; iterations Not specified;
telemetry {qtrace: true}.

### ccanalzyer-ES8 — baseline tools collection: Gordon + IG (Fig 13; 14–17 shared)

**(i) Raw text.** Gordon and IG clients on CloudLab Utah download "the same
100 MB file from the Azure-East Apache web server" [§4.2]; each CCA
classified 5× (Gordon, CCAnalyzer), 20× (IG); Gordon = 75 CWND samples/CCA,
votes across 15 trials [§4.2]; IG-faithful used Azure for train+test [§4.2];
Gordon lacks CDG, Hybla, NV, Westwood [§4.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow ∈ {gordon_client,
ig_client} × workflow.cca.algo ∈ 15) = 2 × 15 = 30; IG-faithful Azure-
train+test sub-campaign leaf count Not specified [§4.2]⟩; Regime: conditions
the tools impose themselves — bottleneck parameters Not specified; Dynamic
Not specified; iterations: Gordon 75/CCA [§4.2], IG 20/CCA [§4.2]; telemetry
{pcap: true [§4.3]}.

### ccanalzyer-ES9 — Top-10K measurement + clustering (Fig 18–20, 24; Table 3)

**(i) Raw text.** h2load parallel HTTP requests targeting 5/10 Mbps
utilization [§5.1]; findcdn for CDN identity [§5.1]; 4 accurate settings,
one trace per setting, voting [§3.4]; 80% utilization validity threshold;
34% unresponsive, 13% RTT > 85 ms, 9% all-invalid [§5.1]; CrUX Top-10K [§5.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow.params.target ∈ Top-10K
× Regime.Static.capacity_down ∈ {5, 10} mbps [§5.1] × path.latency ∈ 4
accurate settings) = 10,000 × 4 = 40,000 attempted⟩; Regime: imposed bottleneck
at testbed (4 settings) over real path to each site; Dynamic Not specified;
iterations 1 [§3.4]; telemetry {qtrace: true, app_metrics: true (utilization)}.

### ccanalzyer-ES10 — IG on the Top-10K (Table 4)

**(i) Raw text.** Re-implemented IG crawler, "crawling up to 500 links per
website" seeking a ≥1.5 MB object [App. C]; 113 classified (~1%); 9533
"Not large enough object"; 354 "Trace collection fail" [Table 4]. Total:
113 + 9533 + 354 = 10,000 [Table 4].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow.params.target ∈
Top-10K) = 10,000; workflow ig_crawler (shell)⟩; Regime: Not specified
(no bottleneck described for the crawler); Dynamic Not specified;
iterations 1; telemetry {app_metrics: true (classification outcome)}.

### ccanalzyer-ES11 — low-bandwidth study, 0.3bw-275rtt on CloudLab (Fig 21, 22)

**(i) Raw text.** Training + testing "entirely on CloudLab", iperf-generated
[§5.3]; bw 0.3 Mbps (found by decreasing 0.1 Mbps at a time) [§5.3]; RTT 275 ms
[§5.3]; ~1 BDP = 16 packets [§5.3]; 5 traces per queue size [§5.3]; 3 training
+ 2 testing per CCA [§5.3]; queue-size and trace-length values figure-axis-only
→ Not specified; 100% accuracy at ≥20 s [§5.3; Fig 22 caption].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(static.queue.size ∈ figure-axis
set × workflow.cca.algo ∈ 15); count Not specified × 15; workflow iperf;
both roles on CloudLab (fully controlled)⟩; Regime⟨Static: capacity_down
0.3 mbps [§5.3], queue: discipline Not specified, size ≈16 pkts reference
[§5.3]; Dynamic: Not specified⟩; path.latency: 275 ms [§5.3]; iterations 5
[§5.3]; telemetry {qtrace: true}.
