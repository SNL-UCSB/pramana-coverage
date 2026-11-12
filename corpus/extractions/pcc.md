# pcc — Experiment-Set Intent Corpus

**Version note (C9):** same as v1 gold — an earlier rendering used the NSDI
proceedings PDF (different figure numbering); gold matrix and this corpus follow
arXiv v3 figure numbers.

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| pcc-ES1 | E1 [OOS-as-published] | path-pair × transport ∈ {(510 pairs,CUBIC),(43,PCP),(85,SABUL)}, each also PCC [§4.1.1] | 1276 (= 1020+86+170; subset relation Not specified) | Not specified |
| pcc-ES2 | E2 | site-pair ∈ 9 × transport ∈ {PCC,SABUL,CUBIC,Illinois} [§4.1.2; Table 1] | 36 | Not specified |
| pcc-ES3 | E3 | static.queue.args ∈ (1.5 KB–1 MB, Not specified) × transport ∈ {PCC,Hybla,Illinois,CUBIC,Reno} [§4.1.3; Fig 6] | Not specified × 5 | Not specified |
| pcc-ES4 | E4 | static.impair.loss_pct ∈ (0–6%, Not specified) × transport ∈ {PCC,CUBIC,Illinois} [§4.1.4; Fig 7] | Not specified × 3 | Not specified |
| pcc-ES5 | E5 | per-workflow path.latency ∈ (20–100 ms long-path, figure-axis) × transport ∈ {PCC,CUBIC,Reno} [§4.1.5; Fig 8] | Not specified × 3 | Not specified |
| pcc-ES6 | E6 | static.queue.args ∈ (1.5–375 KB, Not specified) × transport ∈ {PCC,CUBIC,paced-Reno} [§4.1.6; Fig 9] | Not specified × 3 | Not specified |
| pcc-ES7 | E7 [OOS] | 3 transports × 1 time-varying scenario (bw/latency/loss re-drawn every 5 s for 500 s) [§4.1.7; Fig 11] | 3 | Not specified |
| pcc-ES8 | E8 | sender-count ∈ (5–35, Not specified) × params.data ∈ {64,128,256 KB} × transport ∈ {PCC,TCP} [§4.1.8; Fig 10] | Not specified × 3 × 2 | 15 [§4.1.8] |
| pcc-ES9 | E9 | flow-count ∈ {2,3,4} × transport ∈ {PCC,CUBIC,Reno} [§4.2.1; Fig 13] | 9 | Not specified |
| pcc-ES10 | E10 | PCC params (Tm sweep + εmin sweep) × {RCT,no-RCT} + static.cca ∈ 6 TCP variants [§4.2.2; Fig 16] | Not specified + 6 | 15 [§4.2.2] |
| pcc-ES11 | E11 | dynamic.load cardinality ∈ {1..8} × dynamic.load workflow-type ∈ {TCP-Selfish,PCC} × {capacity,latency} ∈ 4 pairs [§4.3.1; Fig 14] | 8 × 2 × 4 = 64 | Not specified |
| pcc-ES12 | E12 | application.params.load ∈ (5–75%, Not specified) × transport ∈ {PCC,TCP} [§4.3.2; Fig 15] | Not specified × 2 | Not specified |
| pcc-ES13 | E13 | static.queue ∈ {fq_codel,fq+deep-buffer} × transport ∈ {TCP,PCC-latency} [§4.4.1; Fig 17] | 4 | Not specified |

## Experiments

### pcc-ES1 — big data transfer in the wild (Fig 4, Fig 5) [OUT OF SCOPE — as-published]

**(i) Raw text.** "PCC's receiver on 85 globally distributed PlanetLab [14]
nodes and senders on 6 locations: five GENI [5] sites and our local server"
[§4.1.1]; "510 sending-receiving pairs"; BDP 14.3 KB–18 MB [§4.1.1]; "run TCP
iperf between them for 100 seconds, wait for 500 seconds and then run PCC for
100 seconds" [§4.1.1]; PCP 43 pairs, SABUL 85 pairs [§4.1.1]; PCC 5.52× median
vs CUBIC [§4.1.1]. Repetitions per pair, bottleneck buffer/AQM, whether 43/85
pairs subset the 510: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(⟨Roles/mapping path-pair⟩ ∈
{510,43,85 pair sets} × application.workflow ∈ {iperf_cubic, pcp_sender,
sabul_sender} ∪ {pcc_sender} per pair)⟩; Experiment = ⟨Workflow(bulk transfer;
iperf/pcc/pcp/sabul binaries; params.duration 100 s) ⊗ Regime⟨Static: none
imposed — inhabited real Internet paths; Dynamic: Not specified (silence)⟩⟩ @
Roles⟨client: GENI/local senders, server: PlanetLab receivers⟩; iterations Not
specified; telemetry {app_metrics: true (avg throughput; loss rate)}.

### pcc-ES2 — inter-data-center environment on GENI (Table 1)

**(i) Raw text.** "9 pairs of GENI sites … 800 Mbps end-to-end dedicated
bandwidth … PCC, SABUL, TCP CUBIC and TCP Illinois over 100-second runs" [§4.1.2];
per-pair RTTs 9.01–47.4 ms [Table 1]; PCC beats Illinois 5.2× average, 7.5× max
[§4.1.2]. Buffer size, AQM, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(⟨site-pair⟩ ∈ 9 ×
⟨application.workflow, static.cca⟩ ∈ {(pcc_sender,—),(sabul_sender,—),
(bulk-TCP,cubic),(bulk-TCP,illinois)}) = 36⟩; **Imposed/service-node form
(replication-equivalent):** Regime⟨Static: capacity_down 800 mbps [§4.1.2];
static.latency ∈ {9.01,12,21,35,36,38,38,47.4,47} ms (Table 1 RTT values,
sweep axis); queue: discipline Not specified, size Not specified (qualitative
"small buffer" [§4.1.2]); Dynamic: Not specified (silence)⟩;
Roles⟨client, server: service nodes⟩; params.duration 100 s; iterations Not
specified; telemetry {app_metrics: true (avg throughput)}.

### pcc-ES3 — emulated satellite links (Fig 6)

**(i) Raw text.** "emulated satellite links on Emulab parameterized with WINDS
satellite Internet system" [§4.1.3]; "800ms RTT, 42Mbps capacity and 0.74%
random loss" [§4.1.3]; "vary the bottleneck buffer from 1.5KB to 1MB" [§4.1.3];
baselines: TCP Hybla, Illinois, CUBIC, New Reno [§4.1.3; Fig 6 legend]; 100 s
trials. Swept buffer values beyond endpoints, AQM discipline, repetitions: Not
specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(static.queue.args ∈
figure-axis set (1.5 KB–1 MB), Not specified × ⟨application.workflow, static.cca⟩
∈ {(pcc_sender,—),(bulk-TCP,hybla),(bulk-TCP,illinois),(bulk-TCP,cubic),(bulk-TCP,reno)})
= Not specified × 5⟩; Regime⟨Static: capacity_down 42 mbps [§4.1.3],
static.latency 800 ms [§4.1.3] (note: paper states "800ms RTT", anchor
convention records as latency per static model), impair{loss_pct: 0.74 [§4.1.3]};
queue: discipline Not specified, size swept in BYTES; Dynamic: Not specified
(silence)⟩; Roles⟨client, server⟩; params.duration 100 s; iterations Not
specified; telemetry {pcap: true, app_metrics: true}.

### pcc-ES4 — unreliable lossy links (Fig 7)

**(i) Raw text.** "link on Emulab with 100Mbps bandwidth, 30ms RTT and varying
loss rate on both forward and backward paths" [§4.1.4]; loss axis 0–0.06 [Fig 7];
baselines TCP CUBIC, TCP Illinois [§4.1.4]. Duration, buffer, AQM, exact steps:
Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(static.impair.loss_pct ∈
figure-axis set (0–6), Not specified × ⟨application.workflow, static.cca⟩ ∈
{(pcc_sender,—),(bulk-TCP,cubic),(bulk-TCP,illinois)}) = Not specified × 3⟩;
Regime⟨Static: capacity_down 100 mbps [§4.1.4], latency 30 ms [§4.1.4],
queue Not specified, impair{loss_pct swept, applied on BOTH directions [§4.1.4]};
Dynamic: Not specified (silence)⟩; Roles⟨client, server⟩; iterations Not
specified; telemetry {pcap: true, app_metrics: true}.

### pcc-ES5 — mitigating RTT unfairness (Fig 8)

**(i) Raw text.** "one short-RTT (10ms) and one long-RTT (varying from 20ms to
100ms) network path sharing the same bottleneck link of 100Mbit/s bandwidth
and buffer equal to the BDP of the short-RTT flow. We run the long-RTT flow
first for 5s, letting it grab the bandwidth, and then let the short-RTT flow
join to compete with the long-RTT flow for 500s and calculate the ratio of the
two flows' throughput" [§4.1.5]; baselines TCP New Reno, TCP CUBIC [Fig 8 legend].
Swept long-RTT values beyond the range, AQM, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(Workflow_long.path.latency ∈
figure-axis set (20–100 ms) [§4.1.5] × ⟨application.workflow, static.cca⟩ ∈
{PCC, CUBIC, New Reno} forms) = Not specified × 3⟩; per leaf:
TWO flows on paths with DIFFERENT latencies (10 ms short-RTT [§4.1.5]; 20–100 ms
long-RTT [§4.1.5]) sharing one bottleneck;
- **Foreground:** Workflow_long @ client_long_RTT (the measured flow, 500 s);
- **Dynamic:** mode load — Workflow_short @ client_short_RTT enters at t=5s
  (staggered join = workflow-internal timing, §5b.10) — the short-RTT flow as a
  load entry whose path.latency is 10 ms [§4.1.5];
- Regime⟨Static: capacity_down 100 mbps [§4.1.5], queue = BDP of short-RTT
  path [§4.1.5]; Dynamic: mode load⟩; telemetry {pcap: true (both flows'
  throughput → ratio)}.
**v2 key point:** `Workflow_long.path.latency = 20–100 ms` (swept) vs
`Workflow_short.path.latency = 10 ms` (fixed). Per-workflow path is the v2
mechanism (CORPUS_PROMPT_v4 §1: "path = ⟨latency, jitter, loss, reorder, dup⟩
per workflow"). This resolves spec-gap #4 (per-flow latency, opened in v1 by
prudentia-ES1..8 and pcc-ES5).

### pcc-ES6 — small buffer on the bottleneck link (Fig 9)

**(i) Raw text.** "30ms RTT, 100Mbps bottleneck bandwidth and vary the network
buffer size from 1.5KB (one packet) to 375KB (1×BDP) … over 100s" [§4.1.6];
baselines TCP CUBIC and "paced TCP New Reno" [§4.1.6; Fig 9]. Swept buffer
values, AQM, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(static.queue.args ∈
figure-axis set (1.5–375 KB), Not specified × ⟨application.workflow, static.cca⟩
∈ {(pcc_sender,—),(bulk-TCP,cubic),(paced_reno_sender,—)}) = Not specified × 3⟩;
Regime⟨Static: capacity_down 100 mbps [§4.1.6], latency 30 ms [§4.1.6],
queue: discipline Not specified, size swept; Dynamic: Not specified (silence)⟩;
params.duration 100 s; iterations Not specified; telemetry {pcap: true,
app_metrics: true}.

### pcc-ES7 — rapidly changing network (Fig 11) [OUT OF SCOPE]

**(i) Raw text.** "a network path where available bandwidth, loss rate and RTT,
are all changing every 5 seconds … bandwidth ranging from 10Mbps to 100Mbps,
latency from 10ms to 100ms and loss rate from 0% to 1%" [§4.1.7]; "Over the
course of the experiment (500s), PCC's throughput is 44.9Mbps achieving 83% of
the optimal" [§4.1.7]. Buffer, AQM, flow count, repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: ⟨application.workflow, static.cca⟩
∈ {PCC, CUBIC, Illinois} forms = 3⟩; per leaf: the *intended* Regime is a 500 s
schedule of 100 redraws including **bandwidth changes** — bottleneck-capacity-over-
time → OUT-OF-SCOPE (CORPUS_PROMPT_v4 §2); latency and loss also vary
(latency ~U(10,100) ms, loss ~U(0,1) [§4.1.7]) but the capacity component is
sufficient to trigger OOS; Static at compile is fixed, hashed once.

### pcc-ES8 — incast in a data center (Fig 10)

**(i) Raw text.** "33 senders and 1 receiver" [§4.1.8]; sender counts 5–35 [Fig 10];
per-sender data ∈ {256,128,64 KB} [Fig 10 legend]; "each point is the average
of 15 trials" [§4.1.8]; "PCC achieves roughly 60-80% of the maximum possible
goodput, or 7-8× that of TCP" [§4.1.8]. Bandwidth, RTT, buffer, AQM, TCP
variant: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(dynamic.load composition ∈
sender-count set (5–35, Not specified) × application.params.data ∈ {64,128,256 KB}
× transport ∈ {PCC,TCP variant Not specified}) = Not specified × 3 × 2⟩;
Experiment = many-to-one: Roles⟨server: 1 receiver; senders = NodeDecl.count
pool running sender workflows via dynamic.load⟩; Regime⟨Static: Not specified
(bottleneck at receiver ingress); Dynamic: mode load, load = concurrent sender
workflows⟩; iterations 15; telemetry {pcap: true, app_metrics: true}.

### pcc-ES9 — convergence & fairness dumbbell (Fig 12, Fig 13)

**(i) Raw text.** "dumbbell topology on Emulab with four senders and four
receivers sharing a bottleneck link with 30ms RTT, 100Mbps bandwidth. Bottleneck
router buffer size is set to the BDP" [§4.2.1]; "initiates sequentially with a
500s interval … each pair transmits continuously for 2000s" [§4.2.1]; "under
FIFO queue" [Fig 12 caption]; 2/3/4 flows × PCC/CUBIC/Reno [Fig 13 legend].
Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(flow-count ∈ {2,3,4} ×
⟨application.workflow, static.cca⟩ ∈ {(pcc_sender,—),(bulk-TCP,cubic),
(bulk-TCP,reno)}) = 9⟩; Regime⟨Static: capacity_down 100 mbps [§4.2.1],
latency 30 ms [§4.2.1], queue{qdisc: fifo [Fig 12 caption], args: BDP≈375 KB};
Dynamic: mode load — flows 2..k as load entries, staggered 500 s starts as
workflow-internal timing (§5b.10), each flow 2000 s⟩; Roles⟨4 sender/receiver
pairs, pool nodes count 4⟩; iterations Not specified; telemetry {pcap: true}.

### pcc-ES10 — stability–reactiveness trade-off (Fig 16)

**(i) Raw text.** "two sending-receiving pairs sharing 100Mbps bottleneck, 30ms
RTT … first flow A for 20s then flow B" [§4.2.2]; convergence/stability metrics
[§4.2.2]; "results averaged over 15 trials" [§4.2.2]; Tm sweep 4.8×RTT→1×RTT,
then εmin sweep 0.01→0.05 [§4.2.2 fn 4]; RCT and no-RCT [Fig 16]; TCP points:
Bic, Cubic, Hybla, Reno, Westwood, Vegas [Fig 16]. Testbed NOT NAMED → Not
specified (gold deviation §1).

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.params ∈ {Tm
sweep @ εmin 0.01; εmin sweep @ Tm 1×RTT, step values Not specified} ×
application.params.rct ∈ {on,off}) ∪ sweep(static.cca ∈ {bic,cubic,hybla,reno,
westwood,vegas}) = Not specified + 6⟩; Regime⟨Static: capacity_down 100 mbps,
latency 30 ms, queue Not specified; Dynamic: mode load — flow B measured, flow A
a load entry joining 20 s earlier⟩; iterations 15; telemetry {pcap: true}.

### pcc-ES11 — TCP friendliness (Fig 14)

**(i) Raw text.** "one selfish flow as either a bundle of 10 parallel TCP flows
(TCP-Selfish) or a single PCC flow" [§4.3.1]; selfish-sender counts 1–8 [Fig 14
x-axis]; network conditions {10,30} Mbps × {10,20} ms and additional pairs [Fig
14 legend]: (10,10),(10,50?—see rendering),(30,10),(100,10) — 5 total conditions
per legend; "over 100 seconds, averaging over 5 runs" [§4.3.2 for the
friendliness table; rendering notes footnote 4 for Fig 14].

Wait — the gold ES11 corrects this. From v1 gold pcc.md: selfish-sender counts
1–8, network conditions {10,10},{30,20},{30,10},{100,10} mbps/ms [Fig 14 legend].
8 × 2 × 4 = 64 ✓. Repeated.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(dynamic.load[k selfish senders]
cardinality ∈ {1..8} [Fig 14 x-axis] — NOT a spec field (load cardinality; labels
the sweep over the load list) × dynamic.load[workflow-type] ∈ {TCP-Selfish
(10-parallel-flow bundle [§4.3.1]), PCC} — NOT a spec field (selfish workflow type)
× ⟨static.capacity_down, static.latency⟩ ∈ {(10,10),(30,20),(30,10),(100,10)}
mbps/ms [Fig 14 legend]) = 8 × 2 × 4 = 64⟩; Experiment = ⟨Workflow(one normal
TCP flow — the measurand; params.duration 100 s) ⊗ Regime⟨Static: per netcond
axis; Dynamic: mode load — k selfish entries⟩⟩; iterations Not specified;
telemetry {app_metrics: true (normal flow's avg throughput; ratio is analysis)}.

### pcc-ES12 — flow completion time for short flows (Fig 15)

**(i) Raw text.** "link on Emulab 15 Mbps bandwidth and 60ms RTT … short flows
of 100KB each … interval exponentially distributed … network load ranging from
5% to 75%" [§4.3.2]; FCT for PCC and TCP [Fig 15 legend]; "95th-percentile FCT
with 75% utilization is 20% longer than TCP" [§4.3.2]. TCP variant, buffer,
AQM, repetitions, step values: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.params.load ∈
figure-axis set (5–75%), Not specified × transport ∈ {PCC, TCP variant Not
specified}) = Not specified × 2⟩; Experiment = ⟨Workflow(open-loop short-flow
generator; params{flow_size: 100 KB [§4.3.2], interarrival: exponential(mean
per load)}) ⊗ Regime⟨Static: capacity_down 15 mbps [§4.3.2], latency 60 ms
[§4.3.2], queue Not specified; Dynamic: Not specified (the short flows ARE the
workload, not cross-traffic)⟩⟩; iterations Not specified; telemetry
{app_metrics: true (per-flow FCTs), pcap: true}.

### pcc-ES13 — alternate utility: power under AQM + FQ (Fig 17)

**(i) Raw text.** "40Mbps bandwidth and 20ms RTT link running a CoDel
implementation [1] with AQM parameters set as default … per-flow fair queueing
(FQ)" [§4.4.1]; "two simultaneous interactive flows" [§4.4.1]; power values
{TCP+CoDel+FQ 493.83, TCP+Bufferbloat+FQ 46.76, PCC+CoDel+FQ 772.80,
PCC+Bufferbloat+FQ 766.28} Mbit/s² [Fig 17]. Bufferbloat buffer, duration,
repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(static.queue ∈ {⟨qdisc:
fq_codel, args: default⟩ (CoDel+FQ), ⟨qdisc: fq, args: deep-buffer (Bufferbloat),
size Not specified⟩} × transport ∈ {(bulk-TCP,cubic),(pcc_sender,
params.utility=latency)}) = 4⟩; Regime⟨Static: capacity_down 40 mbps [§4.4.1],
latency 20 ms [§4.4.1]; Dynamic: mode load — second simultaneous interactive
flow⟩; iterations Not specified; telemetry {pcap: true (throughput + RTT
series → power, metrics.transport{throughput_mbps_ts,rtt_ms_ts} §8.11)}.

## Tier-1 gate (pipeline/corpus/gate_tier1.py)

**Result (initial):** 6 flags. Fixed G1 (1 real fix); remaining 5 are false positives.
**Result (after fix):** Re-run confirms G1 clean; C5 and G2 flags remain — all false positives.
