# cake — Experiment-Set Intent Corpus (v4 re-render, grammar v2)

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| cake-ES1 | E1 | qdisc ∈ {cake, fq_codel} [Fig 2 labels] | 2 | Not specified |
| cake-ES2 | E2 | qdisc/mode ∈ {cake, cake_dst, cake_src, cake_triple, fq_codel} [Fig 3 labels] | 5 | Not specified |
| cake-ES3 | E3 | mode ∈ {No DiffServ, DiffServ4} [Fig 4 labels] | 2 | Not specified |
| cake-ES4 | E4 | mode ∈ {Cake, Cake DiffServ, FQ-CoDel} [Fig 5 legend] | 3 | Not specified |
| cake-ES5 | E5 | filter ∈ {No filtering, Conservative, Aggressive} [Fig 6 labels] | 3 | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> "All tests are performed on a testbed that emulates a pair of hosts
> communicating through a low-bandwidth link" [§IV]. "We use the Flent
> testing tool [23] to run the tests" [§IV]. "Unless otherwise stated below,
> all tests are run on a symmetrical 10 Mbps link with 50 ms baseline
> latency" [§IV]. RRUL basic test: "four TCP flows in each traffic
> direction, along with three different latency measurement flows" [§IV].
> Baseline comparator FQ-CoDel [§III intro]. CCA, queue size, duration
> (except ES4), repetitions, hardware: Not specified throughout.


## Experiments

### cake-ES1 — baseline RRUL, CAKE vs FQ-CoDel (Fig 2)

**(i) Raw text.** "the baseline performance of CAKE is comparable to that of
FQ-CoDel: both achieve low latency and high throughput in the baseline test"
[§IV]; "on a 10 Mbps link" [Fig 2 caption]; metrics: "Mean TCP goodput
(Mbit/s)" down/up + "Mean induced latency (ms)" [Fig 2 axis labels].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(queue.discipline ∈ {cake,
fq_codel}) = 2⟩; Experiment = ⟨Workflow(RRUL: 4 TCP flows each direction +
3 latency-measurement flows; shell tool Flent) ⊗ Regime⟨Static:
capacity_down 10 mbps [§IV], capacity_up 10 mbps [§IV],
queue⟨discipline: {cake, fq_codel} (swept), size: Not specified, params:
Not specified, ecn: Not specified, mode: Not specified⟩; Dynamic: Not
specified (silence, §5b.2)⟩⟩; path⟨latency: 50 ms [§IV], jitter: Not
specified, loss: Not specified, reorder: Not specified, dup: Not specified⟩;
cca: Not specified (standard TCP, not varied); @ Roles⟨client: Node,
server: Node⟩; iterations: Not specified; telemetry {app_metrics: true
(Flent goodput/latency series), pcap: Not specified}.
confidence: high.

### cake-ES2 — host isolation, 2 sources × 4 destinations (Fig 3)

**(i) Raw text.** "Source host A runs one flow to each of destination hosts
A and B, and two flows to destination host C, while source host B runs one
flow to each of destination hosts C and D" [§IV-A]; modes "cake cake_dst
cake_src cake_triple fq_codel" [Fig 3 labels]; metric "average flow goodput"
[Fig 3 caption]; link inherits 10 Mbps / 50 ms [§IV "Unless otherwise
stated"].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(queue ∈ {⟨discipline:
fq_codel⟩, ⟨discipline: cake, mode: unset⟩, ⟨discipline: cake, mode: dst⟩,
⟨discipline: cake, mode: src⟩, ⟨discipline: cake, mode: triple⟩}) = 5;
CAKE isolation modes ride queue.mode (A5 structured queue field; design-SAT
in v2); concrete tc-CLI argument strings are a compile concern, not
extraction⟩; Experiment = ⟨Workflow(6 TCP flows across 2 source hosts × 4
destination hosts) ⊗ Regime⟨Static: capacity_down 10 mbps [§IV],
capacity_up 10 mbps [§IV], queue⟨discipline: {cake, fq_codel} (swept), size:
Not specified, params: Not specified, ecn: Not specified, mode: {unset, dst,
src, triple} for cake leaves (swept), Not specified for fq_codel⟩;
Dynamic: Not specified⟩⟩; path⟨latency: 50 ms [§IV], jitter: Not specified,
loss: Not specified, reorder: Not specified, dup: Not specified⟩; cca: Not
specified; @ Roles: DEMANDS 2 client + 4 server nodes — see (iv); iterations:
Not specified; telemetry {app_metrics: true (per-flow goodput)}.
confidence: high.

### cake-ES3 — DiffServ RRUL by code point (Fig 4)

**(i) Raw text.** "An RRUL test with each flow marked with a different
DiffServ priority" [§IV-B]; code points "BE BK CS5 EF" [Fig 4 labels];
modes "No DiffServ" / "DiffServ4" [Fig 4 labels]; "a 4-tier mode matching
the 802.11e precedence rules" [§III-C]; link inherits 10/50 [§IV].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(queue.mode ∈ {no_diffserv,
diffserv4} [Fig 4 labels]) = 2; CAKE DiffServ modes ride queue.mode (design-SAT
in v2); concrete tc-argument realization a compile concern⟩; Experiment =
⟨Workflow(RRUL with per-flow DSCP marks BE/BK/CS5/EF as Flent workflow params)
⊗ Regime⟨Static: capacity_down 10 mbps [§IV], capacity_up 10 mbps [§IV],
queue⟨discipline: cake, size: Not specified, params: Not specified, ecn: Not
specified, mode: {no_diffserv, diffserv4} (swept)⟩; Dynamic: Not
specified⟩⟩; path⟨latency: 50 ms [§IV], jitter: Not specified, loss: Not
specified, reorder: Not specified, dup: Not specified⟩; cca: Not specified;
@ Roles⟨client: Node, server: Node⟩; iterations: Not specified; telemetry
{app_metrics: true (per-class throughput)}.
confidence: high.

### cake-ES4 — DiffServ EF flow vs 32 bulk flows (Fig 5)

**(i) Raw text.** "a fixed-rate 2 Mbps flow, which marks its packets with
the high-priority EF DiffServ marking ... the flow competes with 32 bulk
TCP flows" [§IV-B]; "The bulk flows start after 5 seconds" [Fig 5 caption];
modes "Cake  Cake DiffServ  FQ-CoDel" [Fig 5 legend]; "on a 10 Mbps link"
[Fig 5 caption]; "additional latency above the base latency of 50 ms"
[Fig 5 caption]; duration ~140 s [Fig 5 time axis, axis-grounded]; metric
"Induced one-way delay (ms)" [Fig 5 y-axis].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(queue ∈ {⟨discipline:
cake, mode: no_diffserv⟩, ⟨discipline: cake, mode: diffserv4⟩,
⟨discipline: fq_codel⟩} [Fig 5 legend]) = 3; realization rides
queue.discipline / queue.mode⟩; Experiment = ⟨Workflow(one 2 Mbps
fixed-rate EF-marked flow + 32 bulk TCP flows, bulk offset +5 s as
NFA-internal staging, §5b.10; one client/server pair) ⊗ Regime⟨Static:
capacity_down 10 mbps [Fig 5 caption], capacity_up 10 mbps [§IV],
queue⟨discipline: {cake, fq_codel} (swept), size: Not specified, params:
Not specified, ecn: Not specified, mode: {no_diffserv, diffserv4} for cake
leaves, Not specified for fq_codel⟩; Dynamic: Not specified⟩⟩;
path⟨latency: 50 ms [Fig 5 caption], jitter: Not specified, loss: Not
specified, reorder: Not specified, dup: Not specified⟩; cca: Not specified;
@ Roles⟨client: Node, server: Node⟩; telemetry {app_metrics: true
(one-way delay series)}.
confidence: high.

### cake-ES5 — ACK filtering on 30/1 Mbps asymmetric link (Fig 6)

**(i) Raw text.** "a highly asymmetrical link with 30 Mbps download
capacity and only 1 Mbps upload capacity" [§IV-C]; "four simultaneous TCP
uploads and four simultaneous TCP downloads ... along with the added
latency of a separate measurement flow" [§IV-C]; filter modes "No
filtering / Conservative / Aggressive" [Fig 6 labels]; ranges "24.5-27.5
Mbps and 0.45-0.7 Mbps ... 2.6-7.5 ms" [Fig 6 caption]; latency inherits
50 ms [§IV].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(queue.params.ack_filter ∈
{off, conservative, aggressive} [Fig 6 labels]) = 3; CAKE ACK-filter
settings ride queue.params (design-SAT in v2); concrete tc-argument
realization a compile concern⟩; Experiment = ⟨Workflow(4 TCP up + 4 TCP
down + 1 measurement flow) ⊗ Regime⟨Static: capacity_down 30 mbps [§IV-C],
capacity_up 1 mbps [§IV-C], queue⟨discipline: cake, size: Not specified,
params: {ack_filter: {off, conservative, aggressive}} (swept), ecn: Not
specified, mode: Not specified⟩; Dynamic: Not specified⟩⟩;
path⟨latency: 50 ms [§IV], jitter: Not specified, loss: Not specified,
reorder: Not specified, dup: Not specified⟩; cca: Not specified;
@ Roles⟨client: Node, server: Node⟩; telemetry {app_metrics: true}.
confidence: high.
