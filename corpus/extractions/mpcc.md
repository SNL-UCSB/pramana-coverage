# mpcc — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| mpcc-ES1 | Exp1 (text-only, §6) | scheduler variant ∈ {default, new} on 2 parallel 100 Mbps links; BBR per subflow [§6] | 2 (one data point each) | Not specified |
| mpcc-ES2 | Exp2 | protocol ∈ 8 × Regime.Static[link1].buffer ∈ [3, 375] KB [§7.2.1]; link2.buffer=375 KB | Not specified (buffer grid Not stated) | 5 [§7.2.1] |
| mpcc-ES3 | Exp3 | protocol ∈ 8 × Regime.Static[link1].buffer ∈ [3, 375] KB [§7.2.1]; topology 3c | Not specified | 5 [§7.2.1] |
| mpcc-ES4 | Exp4 | protocol ∈ 8 × link1.loss_rate ∈ [0.001%, …] [§7.2.2]; topology 3b | Not specified (loss grid Not stated) | 5 [Fig 6 caption] |
| mpcc-ES5 | Exp5 | protocol ∈ 8 × link1.loss_rate ∈ [0.001%, …] [§7.2.2]; topology 3c | Not specified | 5 [Fig 6 caption] |
| mpcc-ES6 | Exp6 | protocol ∈ 6+ reference lines × one time series [§7.2.3]; topology 3c | Not specified | Not specified |
| mpcc-ES7 | Exp7 | protocol ∈ 8 × bottleneck_buffer > BDP (grid Not specified; Fig 9 axis 400–1000 KB [Fig 9]) | Not specified | 5 [§7.2.4] |
| mpcc-ES8 | Exp8 | protocol ∈ 8 × topology ∈ 5 [§7.2.5] = 40 | 40 | 10 [§7.2.5] |
| mpcc-ES9 | Exp9 | protocol ∈ {MPCC-latency, Balia} × topology 3c [§7.2.5] | 2 time series | Not specified |
| mpcc-ES10 | Exp10 | protocol ∈ 6 × link1.buffer ∈ [3, 375] KB [§7.2.6] | Not specified | 5 [inherited §7.2.1] |
| mpcc-ES11 | Exp11 | protocol ∈ 6 × link1.loss_rate [§7.2.6] | Not specified | Not specified |
| mpcc-ES12 | Exp12 | protocol ∈ {MPCC-latency, LIA, OLIA} × 576 configs [§7.2.7] = 3 × 576 = 1728 | 1728 | 5 [§7.2.7] |
| mpcc-ES13 | Exp13 | protocol ∈ {MPCC-latency, LIA, OLIA} × 576 configs [§7.2.7] = 3 × 576 = 1728 | 1728 | 5 [§7.2.7] |
| mpcc-ES14 | Exp14 | protocol ∈ 8 × server_loc ∈ 6 × home_net ∈ 3 = 8 × 6 × 3 = 144 | 144 | 3 [§7.3] |
| mpcc-ES15 | Exp15 | protocol ∈ 7 [Fig 19 legend] | 7 | 10 [§7.4] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> MPTCP kernel version 0.95 on all sending/receiving nodes [§7.1]. MPCC implementation extends the PCC
> Vivace kernel module; sender-side only, receiver uses legacy MPTCP with SACK feedback [§6]. MPCC
> utility params: α = 0.9, β = 11.35; γ = 0 (MPCC-loss) / γ = 1 (MPCC-latency) [§7.1]. Schedulers:
> paper's rate-based scheduler (10% queued-packet threshold) for rate-based protocols; default MPTCP
> scheduler for window-based schemes [§7.1]. OS: sender/receiver buffers 300 MB; MPTCP checksum
> disabled [§7.1]. Emulab emulator [§7.1]; Ubuntu 16.04 on d710/d430 machines; bridge nodes with ipfw
> [§7.1]. Default per-link params (block B): bandwidth 100 Mbps, latency 30 ms, buffer 375 KB (BDP)
> [§7.2]. Queue management: Not specified. Cross-traffic beyond described flows: Not specified.


## Experiments

### mpcc-ES1 — Scheduler validation (text-only, §6)

**(i) Raw text.** Two parallel 100 Mbps links; single-path BBR per subflow; default MPTCP scheduler
goodput 148.2 Mbps vs new scheduler 179.4 Mbps [§6]. Run on Emulab [§6]. Application/duration/
latency/buffer/repetitions: Not specified for this §6 experiment (described before the §7.1 framework).

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scheduler.variant ∈ {default, new}) = 2⟩;
Experiment = ⟨Workflow(iperf3 multipath sender) @ [GAP-DESIGN: two independent bottleneck links;
grammar v2 single-Regime cannot express]:
MULTIPATH⟨link1: Regime.Static⟨capacity 100 Mbps [§6]⟩;
link2: Regime.Static⟨capacity 100 Mbps [§6]⟩⟩;
cca: ⟨algo: bbr [§6], stack: mptcp, version: 0.95 [§7.1]⟩⟩;
iterations: Not specified; telemetry {app_metrics: true (goodput)}.

### mpcc-ES2 — Shallow-buffer sweep, network 3b (one multipath connection)

**(i) Raw text.** One multipath connection over two links (network 3b) [Fig 3b; Fig 5a subcaption].
Buffer of link 1 varied within [3, 375] KB; link 2 buffer = BDP = 375 KB [§7.2.1]. 5 runs of 200 s
each, first 30 s omitted [§7.2.1]. 8 protocols compared: balia, bbr, lia, olia, MPCC-latency, MPCC-loss,
reno, wvegas [Fig 5a legend]. Metric: average goodput of the multipath connection.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cca.algo ∈ {balia, bbr, lia, olia, MPCC-latency,
MPCC-loss, reno, wvegas} × Regime.Static[link1].buffer ∈ [3, 375] KB [§7.2.1]); count Not specified
(buffer grid Not stated)⟩;
Experiment = ⟨Workflow(iperf3 multipath sender → receiver; 200 s, first 30 s omitted [§7.2.1]) @
[GAP-DESIGN: two independent link bottlenecks]:
MULTIPATH⟨link1: Regime.Static⟨capacity 100 Mbps [§7.2], latency 30 ms [§7.2],
  buffer ∈ [3, 375] KB [§7.2.1]⟩;
link2: Regime.Static⟨capacity 100 Mbps [§7.2], latency 30 ms [§7.2], buffer 375 KB [§7.2.1]⟩;
Dynamic: none⟩;
cca: ⟨algo: swept, stack: mptcp, version: 0.95 [§7.1]⟩⟩;
iterations: 5 [§7.2.1]; telemetry {app_metrics: true (average goodput, min/max bars)}.

### mpcc-ES3 — Shallow-buffer sweep, network 3c (multipath vs. single-path)

**(i) Raw text.** Network 3c: multipath connection on two links competing with a single-path sender on
link 2 [§7.2.1; Fig 3c]. Single-path competitor: PCC Vivace when multipath is MPCC; TCP Reno when MPTCP
[§7.2.1]. Settings repeat Exp2: iperf3, 5 runs × 200 s (first 30 s omitted), link-1 buffer swept
[3, 375] KB, link-2 buffer 375 KB. Metric: goodput of the single-path connection on link 2.

**(ii) Grammar.** ExperimentSet⟨leaves: same as ES2 (protocol × buffer_link1) on topology 3c⟩;
Experiment = ⟨Workflow(iperf3 multipath sender) ⊗ Workflow(PCC Vivace or TCP Reno; single-path on link
2) @ [GAP-DESIGN: two independent links; link 2 has Dynamic.pressure from competitor]:
MULTIPATH⟨link1: Regime.Static as ES2; link2: Regime.Static⟨capacity 100 Mbps, latency 30 ms,
  buffer 375 KB⟩ ⊗ Dynamic⟨pressure = load(competitor_workflow ↦ link2 only)⟩⟩;
cca: ⟨algo: swept, stack: mptcp/single-path, version: 0.95 [§7.1]⟩;
iterations: 5; telemetry {app_metrics: true (single-path goodput)}.

### mpcc-ES4 — Random-loss sweep, network 3b

**(i) Raw text.** Similar to Exp2, varying random loss on link 1 instead of buffer [§7.2.2]. Network 3b
[Fig 6a subcaption]. Loss rate from "as low as 0.001%" [§7.2.2]; Fig 6a x-axis: log scale 10⁻³–10¹ %
[Fig 6a axis]. Buffers/bandwidth/latency defaults (block B): 375 KB / 100 Mbps / 30 ms. 5 runs [Fig 6
caption]. 8 protocols [Fig 6a legend].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cca.algo ∈ 8 protocols × Regime.Static[link1].loss_rate
∈ [0.001%, ~10%] log-scale [§7.2.2]; grid Not specified)⟩;
Experiment = ⟨Workflow(iperf3 multipath; 200 s, first 30 s omitted [§7.2.1 procedure]) @
[GAP-DESIGN: two independent links + loss on link 1]:
MULTIPATH⟨link1: Regime.Static⟨capacity 100 Mbps [§7.2], latency 30 ms [§7.2],
  buffer 375 KB [§7.2], path.loss: swept [§7.2.2]⟩;
link2: Regime.Static⟨capacity 100 Mbps, latency 30 ms, buffer 375 KB [§7.2]⟩; Dynamic: none⟩;
cca: ⟨algo: swept, stack: mptcp, version: 0.95⟩; iterations: 5.

### mpcc-ES5 — Random-loss sweep, network 3c (multipath vs. single-path)

**(i) Raw text.** Similar to Exp3, varying random loss on link 1 [§7.2.2]. Network 3c [Fig 6b]. Single-
path competitor on link 2 as Exp3. 5 runs, 200 s, first 30 s omitted (inherited §7.2.1 procedure).
Metric: single-path connection goodput.

**(ii) Grammar.** INHERITED from ES4 (loss sweep on link 1) with topology change to 3c + single-path
competitor on link 2 (per ES3 delta).

### mpcc-ES6 — Changing network conditions (network 3c, time-varying)

**(i) Raw text.** Network 3c; link 1's bandwidth, latency, and loss rate assigned random values every
30 seconds from ranges 10–100 Mbps, 10–100 ms, 0.01%–0.1% [§7.2.3]. Buffer 375 KB [§7.2.3].
Duration: Fig 7/8 x-axis labeled "Time (Sec)" to 1400 s. Application/repetitions: Not specified.
Protocols compared: MPCC-latency, reno, lia, olia, balia, wvegas + OPT reference [Fig 7 legend]; Fig 8
shows single-path PCC competitor's throughput.

**(ii) Grammar.** [OUT-OF-SCOPE — time-varying bottleneck capacity; see design verdict.] For reference:
the conditions would require Regime with time-varying capacity (10–100 Mbps every 30 s),
time-varying latency, and time-varying loss — plus multipath topology — none of which are supported
by grammar v2 or the substrate worker.

### mpcc-ES7 — Self-induced latency vs. buffer size (network 3e)

**(i) Raw text.** Network 3e: two multipath connections [Fig 3e, §7.2.4]. iperf3, average latency over 5
runs; ss utility samples smoothed RTT every 0.1 s for 200 s [§7.2.4]. Bottleneck buffer swept exceeding
BDP; Fig 9 x-axis: "Bottleneck Buffer (KB)" 400–1000 [Fig 9 axis]. Bandwidth/latency: defaults 100 Mbps
/ 30 ms (block B). 8 protocols [Fig 9 legend].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cca.algo ∈ 8 × Regime.Static.buffer > 375 KB (grid Not
specified, Fig 9 axis range 400–1000 KB [Fig 9]))⟩;
Experiment = ⟨Workflow(iperf3 multipath sender × 2) @
[GAP-DESIGN: two multipath connections, two links]:
MULTIPATH⟨link: Regime.Static⟨capacity 100 Mbps [§7.2], latency 30 ms [§7.2],
  buffer ∈ [400, 1000] KB [Fig 9 axis, above BDP]⟩⟩;
cca: ⟨algo: swept, stack: mptcp, version: 0.95⟩; iterations: 5 [§7.2.4];
telemetry {app_metrics: true (smoothed RTT via ss every 0.1 s [§7.2.4])}.

### mpcc-ES8 — Convergence campaign across topologies

**(i) Raw text.** 5 topologies from Figs 3/4: Two-links MP-SP-SP (3d), Two-links MP-SP (3c), OLIA
topology (Fig 4a), LIA topology (Fig 4b), Single-link MP-SP (3a) [Fig 10 x-axis; §7.2.5]. 10 iperf3
200 s runs (first 30 s omitted) [§7.2.5]. Buffer = BDP = 375 KB on all links [§7.2.5]. 8 protocols
[Fig 10 legend]. Metrics: Jain's fairness index + average total-goodput/capacity ratio [§7.2.5].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cca.algo ∈ 8 × topology ∈ 5) = 8 × 5 = 40⟩;
Experiment = ⟨Workflow(iperf3 multipath sender + competitors per topology) @
[GAP-DESIGN: multi-link topologies, each with independent bottleneck links]:
MULTIPATH⟨topology: one of 5 [§7.2.5]; link: Regime.Static⟨capacity 100 Mbps, latency 30 ms,
  buffer 375 KB [§7.2.5]⟩; Dynamic: none⟩;
cca: ⟨algo: swept, stack: mptcp, version: 0.95⟩; iterations: 10 [§7.2.5];
telemetry {app_metrics: true (Jain's fairness, goodput ratio)}.

**[G1 arithmetic check: 8 × 5 = 40. ✓]**

### mpcc-ES9 — Illustrative convergence example (network 3c)

**(i) Raw text.** MPCC-latency and Balia each vs. single-path flow on topology 3c [§7.2.5; Fig 11].
Fig 11 x-axis: "Time (Sec)" 0–300 [Fig 11 axis]. Buffer BDP 375 KB on all links [§7.2.5]. Duration
not stated (300 s from figure axis vs 200 s from Exp8 campaign). Application/repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 2 (one per protocol: MPCC-latency, Balia)⟩;
Experiment = ⟨Workflow(iperf3 multipath) ⊗ Workflow(single-path flow on link 2) @
[GAP-DESIGN: two independent links, topology 3c]:
MULTIPATH⟨link1, link2: Regime.Static⟨capacity 100 Mbps, latency 30 ms, buffer 375 KB⟩⟩;
cca: ⟨algo: {MPCC-latency|Balia}, stack: mptcp, version: 0.95⟩; iterations: Not specified;
telemetry {app_metrics: true (per-flow throughput time series [Fig 11])}.

### mpcc-ES10 — TCP friendliness, buffer sweep vs. TCP Cubic (topology 3c)

**(i) Raw text.** Repeat of Exp2 (buffer sweep, §7.2.1 procedure) with single-path competitor TCP Cubic
[§7.2.6]. Topology 3c [Fig 12 caption]. 6 protocols: balia, lia, olia, MPCC-latency, reno, wvegas
[Fig 12 legend] (MPCC-loss excluded as not friendly to legacy TCP [§7.2.6]). Metric: multipath
goodput (Fig 12a) + single-path Cubic goodput (Fig 12b).

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cca.algo ∈ 6 × link1.buffer ∈ [3, 375] KB [§7.2.1
inherited]); Not specified (buffer grid Not stated)⟩;
Experiment = ⟨Workflow(iperf3 multipath) ⊗ Workflow(iperf3 cubic; single-path) @
[GAP-DESIGN: topology 3c, two links]:
MULTIPATH⟨link1: Regime.Static⟨capacity 100 Mbps, latency 30 ms, buffer swept⟩;
link2: Regime.Static⟨capacity 100 Mbps, latency 30 ms, buffer 375 KB⟩;
Dynamic⟨link2: pressure = load(cubic_flow ↦ link2)⟩⟩;
cca: ⟨algo: swept ∪ {cubic for competitor}, stack: mptcp, version: 0.95⟩;
iterations: 5 [§7.2.1 inherited]; telemetry {app_metrics: true (goodput)}.

### mpcc-ES11 — TCP friendliness, loss sweep vs. TCP Cubic (topology 3c)

**(i) Raw text.** Repeat of Exp4 (loss sweep, §7.2.2 procedure) with single-path competitor TCP Cubic
[§7.2.6]. Topology 3c [Fig 13 caption]. 6 protocols [Fig 13 legend]. Repetitions/duration: Not
specified for this repeat (Fig 13 caption unlike Figs 5/6 does not restate run count [rendering §7.2.6]).

**(ii) Grammar.** INHERITED from ES5 (loss sweep, topology 3c, single-path competitor), delta:
competitor = cubic; 6 protocols (MPCC-loss excluded).

### mpcc-ES12 — Varying-network-configuration campaign (topology 3c, 576 configs)

**(i) Raw text.** Two-link MP-SP network (topology 3c) [§7.2.7]. Per-link swept parameters per Table 1:
bandwidth ∈ {50, 500} Mbps; latency ∈ {10, 100} ms; loss ∈ {0%, 0.1%, 0.001%}; buffer ∈ {50, 700} KB.
24 options per link → 24² = 576 configurations [§7.2.7]. Protocols: MPCC-latency vs. LIA, MPCC-latency
vs. OLIA [§7.2.7]. 5 runs per configuration [§7.2.7]. Application/duration: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(protocol ∈ {MPCC-latency, LIA, OLIA} × config ∈ 576)
= 3 × 576 = 1728 [§7.2.7]⟩;
Experiment = ⟨Workflow(iperf3 multipath) ⊗ Workflow(iperf3 single-path; topology 3c) @
[GAP-DESIGN: two independent links, per-link capacity/latency/loss/buffer swept]:
MULTIPATH⟨link1: Regime.Static⟨capacity ∈ {50, 500} Mbps [Tab 1], latency ∈ {10, 100} ms [Tab 1],
  buffer ∈ {50, 700} KB [Tab 1], loss ∈ {0%, 0.1%, 0.001%} [Tab 1]⟩;
link2: Regime.Static⟨same parameter space [Tab 1]⟩⟩;
cca: ⟨algo: swept, stack: mptcp, version: 0.95⟩; iterations: 5 [§7.2.7].

**[G1: 3 × 576 = 1728. ✓]**

### mpcc-ES13 — Varying-network-configuration campaign (topology 3d, 576 configs)

**(i) Raw text.** Same 576-configuration sweep as ES12, on topology 3d (two links MP-SP-SP: multipath
competes with a single-path connection on **each** link) [§7.2.7; Fig 3d subcaption "two links MP-SP-SP"].

**(ii) Grammar.** INHERITED from ES12 (576-config sweep, 3 protocols, 5 runs), delta: topology 3d
(two links, each with an independent single-path competitor).

### mpcc-ES14 — Live Internet AWS-to-residential experiments

**(i) Raw text.** Download 75 MB file from 6 AWS server locations (Ohio, Sao Paulo, London, Tokyo,
Frankfurt, North California [Fig 16 x-axis]) to 3 residential home networks (Israel, Boston, Illinois)
with WiFi + cellular (USB tethering to PC) [§7.3]. 8 protocols [Fig 16 legend]. 3 runs per server-home
pair, round-robin [§7.3]. Metric: download time (Fig 16) + normalized ratio (Fig 17 re-analysis of
same data). Duration per download / network conditions: Not specified.

**(ii) Grammar.** [OUT-OF-SCOPE — live Internet paths; see design verdict.]

### mpcc-ES15 — Data center testbed (FCT)

**(i) Raw text.** 6 switches + 6 hosts; 2-layer Clos network (Fig 18); 25 Gbps DAC cables; ECMP
routing between shortest paths [§7.4]. Hosts: 4 dual-homed Xeon Silver processors, 128 GB RAM [§7.4].
Workload: 15 10 GB flows + 35 10 MB flows per host (simultaneously) + 10 KB flows at each second of
first minute per host [§7.4]. 7 protocols [Fig 19 legend]. 10 repetitions [§7.4].
Metric: FCT (mean, 1st/5th/median/95th/99th percentile [§7.4]).

**(ii) Grammar.** [OUT-OF-SCOPE — physical datacenter testbed; see design verdict.]
