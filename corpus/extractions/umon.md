# umon — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Upstream row | Nature | OUT-OF-SCOPE reason |
| --- | --- | --- | --- |
| umon-ES1 | Exp1 | Motivational RDMA testbed monitoring run (Fig 1) | Passive monitoring: observes RDMA flow-rate curves at µs granularity; no controlled conditions generated |
| umon-ES2 | Exp2 | Counter-increase-factor workload analysis (Fig 3) | Passive analysis: counts per-window packets from external published flow distributions; no network experiment |
| umon-ES3 | Exp3 | Testbed RDMA flow collection (Figs 9b, 13) | Passive monitoring + physical-layer: 40 Gbps DCQCN testbed, Tofino2 all-packet mirroring at line rate |
| umon-ES4 | Exp4 | Testbed TCP flow illustrative run (Fig 9a) | Passive monitoring: single low-throughput TCP flow captured by WaveSketch on an unspecified testbed |
| umon-ES5 | Exp5 | NS-3 network-wide simulation campaign (Figs 10–18, Tab 2) | Pure simulator: NS-3 fat-tree (k=4, 100 Gbps, 1 µs hops) — simulator exclusion |
| umon-ES6 | Exp6 | WaveSketch-HW hardware resource measurement (Tab 1) | Physical-layer: P4 compilation + Tofino2 ASIC resource measurement |

## Shared methodology (raw text) (quoted from the paper)


> RDMA testbed: Arista DCS-7060CX, Tofino2 switch, two Intel Xeon E5-2650
> servers, 40 Gbps links; perftest-generated RDMA flows, default DCQCN; on-off
> background flow to induce rate changes; ground truth via Lumina-style Tofino
> timestamping + mirroring of all packets [§7 Setup, App. D]. NS-3 simulation:
> fat-tree (k=4), 100 Gbps links, 1 µs per-hop latency, 16 hosts; WebSearch
> and Facebook Hadoop flow-size distributions; link loads 15/25/35%; 20 ms runs;
> RoCEv2 + DCQCN, KMin=20 KiB, KMax=200 KiB, p=0.01 [§7 Setup, §7 Workloads,
> App. D]. Measurement window: 8.192 µs (evaluation) [§7.1]; 10 µs
> (motivational/illustrative figures) [Figs 1, 9, 10c].


## Experiments

### umon-ES1 — Motivational RDMA-testbed monitoring run (Fig 1)

**(i) Raw text.** "Figure 1 showcases a flow rate curve gathered from our RDMA
testbed, where we execute the WebSearch workload [8] and induce traffic
contention within a single bottleneck topology" [§2.1]. Observation windows: 10
µs and 10 ms [§2.1; Fig 1 axis "Time Window (10 us)"]. Hardware / bandwidth /
CCA / duration: Not specified.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### umon-ES2 — Counter-increase-factor workload analysis (Fig 3)

**(i) Raw text.** "We evaluate the counter increase factor N(10µs)/N(10ms) …
under two popular workloads" [§2.3]; Facebook Hadoop 34.4x, DCTCP WebSearch
387x when link load > 35% [§2.3]; link load axis: 5–45% [Fig 3 x-axis "Link
Load (%)"]; extrapolated bandwidth 6.34 Gbps at 10 µs for WebSearch > 35% load
[§2.3]. Environment / topology / hardware: Not specified.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### umon-ES3 — Testbed RDMA flow collection (Figs 9b, 13)

**(i) Raw text.** Hardware: Arista DCS-7060CX, Tofino2 switch, two Intel Xeon
E5-2650 servers; 40 Gbps links [§7 Setup]. Flows: perftest RDMA [5], default
DCQCN [§7 Workloads]. Cross traffic: on-off background flow [App. D].
Ground truth: Tofino timestamping + mirroring of all packets [App. D]. WaveSketch
K=32 vs. OmniWindow-Avg [§7.1]; 8.192 µs window (Fig 13) [§7.1]; 10 µs window
(Fig 9b) [Fig 9b axis]. Topology / duration / flow count / sizes: Not specified.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### umon-ES4 — Testbed TCP flow illustrative run (Fig 9a)

**(i) Raw text.** "Figure 9a presents a low-throughput TCP flow captured in our
testbed using WaveSketch" [§6.2]; transport: TCP [§6.2; Fig 9a "(a) TCP flow"];
measurement window: 10 µs [Fig 9a axis "Time Window (10 us)"]. Hardware /
bandwidth / CCA / cross traffic / duration: Not specified.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### umon-ES5 — NS-3 network-wide simulation campaign (Figs 10–18, Tab 2)

**(i) Raw text.** NS-3 fat-tree (k=4), 100 Gbps, 1 µs per-hop latency, 16 hosts
[§7 Setup]; WebSearch and Facebook Hadoop distributions [App. D]; link loads 15%,
25%, 35% [§7 Workloads]; 20 ms runs [§7 Workloads, App. D]; RoCEv2 + DCQCN,
KMin=20 KiB, KMax=200 KiB, p=0.01 [§7.2]; flows 356–11773 (Table 2: WebSearch
367/625/815; Facebook Hadoop 4966/8366/11773 at 15/25/35% [Tab 2]); 8.192 µs
window [§7.1]; sampling-ratio sweep p ∈ {1, 1/4, 1/16, 1/64, 1/128, 1/256}
[Fig 14]; memory sweep 500–1500 KB [Fig 11/12 axes].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### umon-ES6 — WaveSketch-HW hardware resource measurement (Tab 1)

**(i) Raw text.** WaveSketch-HW implemented in P4 on Tofino2 chip; Table 1: full
version WaveSketch heavy (h=256, L=8, K=64) + light (w=256, L=8, K=64, D=1)
[Tab 1 caption]; Stateful ALU 76.56% (most consumed resource) [§7.1; Tab 1];
line-rate feasibility verified [§7.1].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.
