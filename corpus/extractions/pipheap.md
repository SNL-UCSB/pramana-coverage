# pipheap — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering rows | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| pipheap-ES1 | Exp1–Exp6 | CPU accuracy evaluation; swept: algorithm set (varies per exp); W ∈ {1,2,4,8,16} (Exp1 [§5.2.1]); memory ∈ 30KB–360KB (Exp2–6 [§5.2.2; §5.3.2]); dataset ∈ {CAIDA, WebPage} [§5.1] | Exp1: 5 W values; Exp2: 4 algorithms × 2 datasets × grid; Exp3: 6 algorithms × 5 (memory × dataset) subfig points = 30 [Fig 6 subcaptions]; Exp4–6: 2 algorithms × 2 datasets × grid each | Not specified (trace replay; no per-leaf repetition count stated) |
| pipheap-ES2 | Exp7 | Tofino hardware resource measurement; algorithm configuration ∈ {PipHeap, +CM, +SuMax, +Coco, +Elastic, +Space Saving, +RHHH} = 7 [Table 3; §5.4] | 7 | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Algorithms (PipHeap and all competitors) implemented in P4 and C++ [§5.1]; source
> code open-source [§5.1]. Accuracy experiments run on a CPU platform: server with
> 36-core Intel i9-10980XE, 128GB DDR4, 25.4MB L3 cache; CPU frequency 4.2GHz, memory
> 3200MHz [§5.1]. Hash functions: CRC, Murmur, Farm (nearly identical results [§5.1]).
> Dataset (1) CAIDA: anonymous IP traces from CAIDA backbone monitors 2018; one-minute
> trace; ~27M packets, ~0.25M flows; flow ID = source IP 4 bytes [§5.1]. Dataset (2)
> WebPage: web page collection; each item 4 bytes = distinct item count per page; ~64M
> items, ~0.94M distinct items [§5.1]. Workload: insert each trace item into the data
> structure (trace replay) [§3.1; §5.1]. Metrics: ARE, AAE, PR, RR on most frequent k
> flows [§5.1]. Network bandwidth, RTT, queue management, topology, duration,
> repetitions: Not specified for all Exp1–6 (no network experiment present).


## Experiments

### pipheap-ES1 — Trace-driven CPU accuracy evaluation (Exp1–Exp6)

**(i) Raw text.** All 6 accuracy experiments replay CAIDA or WebPage traces on the CPU
platform, inserting items into in-memory data structures and measuring ARE/AAE/PR/RR on
the most frequent 3000 flows [§5.1; §5.2.1; §5.2.2]. No network traffic generated; no
topology; no congestion; no congestion control. Exp1: W swept 1–16, outcome W = 8 optimal
[§5.2.1]; dataset Not specified; memory Not specified. Exp2: PipHeap vs Space Saving vs
Elastic (vs Coco [Fig 5]); CAIDA and WebPage; memory 30KB–120KB [§5.2.2]; W = 8 for
PipHeap [§5.2.2]; Elastic 4 layers λ = 32 [§5.2.2]. Exp3: 6 algorithms (CM, Count, FCM,
Univmon, NitroCM, Elastic) original vs combined with PipHeap; CAIDA 120/240/360KB and
WebPage 120/240KB [Fig 6 subcaptions]; error reductions 33%, 92%, 85%, 97%, 72%, 80%
[§5.3.2]. Exp4: Elastic Sketch vs PipHeap+Elastic; CAIDA and WebPage; memory 10KB–100KB
[§5.3.1]; heavy hitter definition 3000 flows [§5.3.1]. Exp5: RHHH vs PipHeap-RHHH;
CAIDA 16-bit and 24-bit prefix [§5.3.3]; WebPage 24-bit prefix [§5.3.3]; memory 0–500KB
[Fig 8 x-axis]. Exp6: Coco vs PipHeap+Coco; CAIDA and WebPage; 16-bit prefix [§5.3.4];
memory 0–200KB [Fig 9 x-axis]; PipHeap reduces Coco error by 87% at 240KB on CAIDA
[§5.3.4].

**(ii) Grammar.** No grammar translation is possible. These experiments have no network
topology, no bottleneck link, no congestion control, no application workload, and no
traffic generation. The "workload" is trace-replay into in-memory sketch data structures
on a CPU server. There is no Regime, no Dynamic.pressure, no CCA, no path, and no
Foreground workflow in the v2 grammar sense.

### pipheap-ES2 — Tofino programmable switch resource measurement (Exp7)

**(i) Raw text.** PipHeap with 131071 nodes compiled to Tofino switch; capable of
tracking over 100K heavy flows [§5.4]. Combined with CM, SuMax, Coco, Elastic, Space
Saving, RHHH (7 configurations [Table 3; §5.4]). Resources measured: SRAM 10 (31.3%),
Map RAM 103 (26.82%), Hash Bits, TCAM, Stateful ALU 31.25%, Exact Match Xbar,
VLIW Instr [§5.4; Table 3]. Highest after combining: Stateful ALU 36.11%, Map RAM
31.48% [§5.4]. Measurement model: fixed window — timeline divided into consecutive
fixed windows; sketch data sent from data plane to control plane and reset when window
ends [§5.4]. Traffic/workload driven through the switch: Not specified. Window size:
Not specified. Duration: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 7 algorithm configurations [Table 3]⟩;
Experiment = ⟨Workflow(P4 compilation + switch resource measurement) on Tofino ASIC⟩;
Regime: Not applicable (no network traffic described); telemetry {app_metrics: true
(switch resource usage: SRAM/Map RAM/Hash Bits/TCAM/Stateful ALU/Xbar/VLIW [Table 3])}.
