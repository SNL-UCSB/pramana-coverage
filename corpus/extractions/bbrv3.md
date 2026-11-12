# bbrv3 — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| bbrv3-ES1 | E1 | cca{build} ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0} × queue{size: ×BDP} ∈ {1/4,1/2,1,2,4,8,16}×BDP [§4.1; Fig 4b axis] | 3×7 = 21 | 3 [§3] |
| bbrv3-ES2 | E2 | cca{build} 3 × queue{size} 7 (as ES1) [§4.2 "repeat the earlier evaluation"] | 21 | 3 [§3] |
| bbrv3-ES3 | E3 | cca{build} ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0, cubic} × queue{size} ∈ {8,16,32}×BDP [Fig 8/9a axes] | 4×3 = 12 | 3 [§3] |
| bbrv3-ES4 | E4 | cca{build} 4 × path.latency ∈ {10,20,40,80} ms (second flow) [§4.4] × queue{size} ∈ {1/4,1/2,1,2,4}×BDP | 4×4×5 = 80 | 3 [§3] |
| bbrv3-ES5 | E5 | same dims as ES4, reversed arrival order [§4.4 second scenario] | 80 | 3 [§3] |
| bbrv3-ES6 | E6 | CCA pair (foreground cca{build} × load cca{build}) ∈ 6 unordered pairs of {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0, cubic} × queue{size} 7 [Fig 17 axis] | 6×7 = 42 | 3 [§3] |
| bbrv3-ES7 | E7 | cca{build} ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0} × n_BBR ∈ {1..5} × n_Cubic ∈ {1..5} [§4.5] | 3×5×5 = 75 | 3 [§4.5] |
| bbrv3-ES8 | E8 | cca{build} ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0, cubic} [§4.6] | 4 | 3 [§3] |
| bbrv3-ES9 | E9 | pairing ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0} × cubic (50/50 Harpoon split) [§4.6] | 3 | 3 [§3] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Testbed: "six Dell R6515 blade servers, each with 16 cores and 128 GiB of
> RAM"; "25 Gbps DACs"; "four APS Networks BF6064X-T switches"; single-
> bottleneck topology [§3; Fig 2]. "Servers … run Linux kernel v5.4 (Debian
> 10)"; "two VMs … one ran BBRv2 with Linux kernel v5.13.12 … the other ran
> BBRv3 with Linux kernel v6.4.0" [§3]. "We did not enable ECN support in
> our testbed" [§3]. "netem [47] … to avoid issues with TCP small queues";
> "tc-tbf [1] … to configure the bottleneck bandwidth and buffer size"; "half
> of the configured delay before the bottleneck and half after"; base RTT
> "without any added delay, was 1.5 ms on average" [§3]. AQM never named [§5].
> Cross traffic beyond contending flows: Not specified (silence). Workload
> tool (§4.1–4.5): Not specified. Real-world workload (§4.6): "Harpoon [44]
> to generate traffic" using MAWI-derived Pareto flow-sizes / Lognormal inter-
> arrivals, "scaled up the inter-arrival times by a factor of 5" [§3]; "fixed
> the random seed" [§4.6]. "Unless otherwise stated, we repeated each
> experiment three times" [§3].

**Modeling note (v2-specific).**
(1) *BBR versions as cca{build}:* BBRv1/v2/v3 all name the kernel CCA `bbr`;
version is selected by which kernel build the endpoint runs (host v5.4 /
VM v5.13.12 / VM v6.4.0) [§3]. In v2: `cca{algo: bbr, build: v5.4|
v5.13.12|v6.4.0}` — the `build` field carries the qualifier. spec-gap #5
is resolved at design level.
(2) *Per-flow contention as Dynamic.load:* flow 1 is the application Workflow;
contending flows = `Dynamic.pressure = load(Workflow* ↦ Node*)` (spec §2),
with start offsets as workflow params / NFA timing states — in-grammar.
(3) *Bottleneck:* `Static.capacity_down/up` (HTB) + `Static.queue{size:
×BDP, params: tbf-configured [§3]}`. tbf ∉ closed qdisc set (§8.1) — named
minor gap (enum extension, not structural; size is the swept treatment).
(4) *Per-flow latency:* two flows see different RTTs (ES4/5/6/7). In v2:
each workflow's `path.latency` carries its one-way delay contribution.
spec-gap #4 resolved.
(5) *BDP-relative buffers:* ×BDP queue sizes without stated capacity remain
compile-time questions (ES1/2/4/5 capacity Not specified) — `queue{size:
N×BDP}` with a batched compile question, never a silent default.

---

### bbrv3-ES1 — similar & synchronous two-flow fairness (Fig 3, Fig 4)

**(i) Raw text.** "two similar flows, i.e., using the same CCA and
experiencing the same RTT (of 100 ms), contend for bandwidth on a
bottleneck"; "start both flows at the same time and let them run for a
duration of 300 s" [§4.1]. "We repeated this experiment by varying the
bottleneck queue size from one-fourth to 16 times the BDP, doubling the
queue size once for each experiment" [§4.1]. CCAs BBRv1/BBRv2/BBRv3
[Fig 3a–c; Fig 4 x-axes]. Bandwidth: Not specified. RTT 100 ms [§4.1].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  cca{algo: bbr, build: ∈ {v5.4=BBRv1, v5.13.12=BBRv2, v6.4.0=BBRv3} [§3]} ×
  Static.queue{size: ∈ {1/4,1/2,1,2,4,8,16}×BDP [§4.1]}) = 3×7 = 21⟩;
Experiment = ⟨Workflow(long-lived bulk TCP; tool Not specified; duration 300 s [§4.1]) ⊗
Regime⟨Static⟨capacity_down: Not specified; latency: such that RTT=100 ms [§4.1],
queue{size: swept ×BDP, params: tbf-configured [§3]}⟩;
Dynamic⟨pressure: load(second identical bulk flow with same cca{build} ↦
second sender node, synchronous start)⟩⟩⟩;
path⟨latency: shared (100 ms RTT symmetric, both flows)⟩;
Roles⟨client: sender S1, server: receiver R1 [Fig 2]⟩;
iterations 3 [§3]; telemetry{pcap: true (per-flow throughput timelines +
retransmission %, capture-derived metrics.transport)}.

**(iii) Requirements v2.** `cca{algo: bbr, build: v5.4|v5.13.12|v6.4.0}`
per-workflow (v2 build qualifier); imposed envelope {path.latency → 100 ms
RTT ∈ [0, 2000 ms]; queue{size: ×BDP}}; `Dynamic.pressure = load(identical
(Roles client + server); `iterations: 3`; `telemetry.pcap` with
`metrics.transport{throughput_mbps_ts, retransmits}` (§8.11);
capacity Not specified → compile question for literal ×BDP resolution.

**(iv) Capability match v2.**
- **Design: SATISFIED.** v2 `cca{build}` resolves spec-gap #5 (the BBR-
  version-as-kernel-build qualifier is now a first-class field). Two-flow
  contention is `load(Workflow* ↦ Node*)` ⊗ imposed Static (spec §2);
  queue-size sweep is a `sweeps:` axis; both roles self-hosted. The
  unresolved capacity (compile question for ×BDP values) is a compile-gate
  question, not a grammar gap (spec §4.1: compile asks if a required field
  is absent; it does not block the spec production).
  v2 delta vs gold: gold was GAP-DESIGN (spec-gap #5). Now SATISFIED.
  Named minor: tbf ∉ qdisc closed set (§8.1) — enum extension, not
  structural; queue size (the swept treatment) is in-grammar.
  entries @fb4d8b6; `iperf` exists only as a test artifact
  `test_iperf_workflow.json`). Modules: kernel-variant node pool (BBRv2/v3
  builds), load co-scheduling (2nd workflow driver), bulk-TCP registry entry.
  names tbf as first-class (mininet-capability.md Link production); two iperf-
  like processes on emulated hosts are the declarative surface. Caps (min
  across axes, §5b.5): BBR-version dimension needs three host-kernel builds —
  all hosts share one kernel, version sweep = host reprovisioning between runs,
  machinery the platform does not objectify (mininet-capability.md: cca =
  shared-kernel host modules); telemetry = manual (hand-built per-flow
  throughput + retx %); 21×3 campaign hand-scripted (no sweep/identity
  production).

**confidence: high** — v2 `cca{build}` unambiguously resolves #5; load()
co-scheduling gap clearly IMPL-level only.

---

### bbrv3-ES2 — similar but staggered two-flow fairness (Fig 5, Fig 6)

**(i) Raw text.** "We now repeat the earlier evaluation, but with one change:
We stagger the flows so that the second flow starts 15 s after the first"
[§4.2]. Same CCA set, buffer axis 1/4…16×BDP [Fig 6b axis]; RTT 100 ms
inherited from §4.1 setup [§4.2 "repeat the earlier evaluation"].

**(ii) Grammar v2.** As ES1 with one delta: `Dynamic.pressure = load(second
identical bulk flow, start-offset: 15 s [§4.2] ↦ second node)`. Leaves 21;
iterations 3 [§3].

**(iii) Requirements v2.** INHERITED from ES1, delta: a 15 s start offset on
the LoadEntry — in-grammar as workflow-internal timing (a `LoadEntry.params`
start-offset value or NFA timing state; §5b.10: protocol-internal schedule
≠ iterations).

**(iv) Capability match v2.**
- **Design: SATISFIED — INHERITED from ES1 (cca{build} resolves #5), delta
  SATISFIED:** 15 s stagger is NFA-internal timing / `LoadEntry.params` —
  in-grammar.
  load co-scheduling; bulk-TCP registry entry). No new module beyond ES1.
  routine scripting; same kernel-sweep + manual-telemetry caps).

**confidence: high**

---

### bbrv3-ES3 — five-flow staggered arrivals/departures, deep buffers (Fig 7, 8, 9)

**(i) Raw text.** "a staggered-flow experiment … we add a new flow to the
testbed every 100 s until we reach five concurrent flows, and then remove one
flow every 100 s until we have only one left" [§4.3]; "converge to the fair
share of the bottleneck (100 Mbps)" [§4.3]; buffer ∈ {8,16,32}×BDP [Fig 8/9a
axes]; timelines at 32×BDP [Fig 7 caption]; CCAs BBRv1/v2/v3 [Fig 7/8] +
Cubic [Fig 9a]. RTT: Not specified [§4.3]. Duration: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  cca{algo: bbr, build: ∈ {v5.4, v5.13.12, v6.4.0}} ∪ cca{algo: cubic} ×
  Static.queue{size: ∈ {8,16,32}×BDP [Fig 8/9a axes]}) = 4×3 = 12⟩;
Experiment = ⟨Workflow(bulk flow; tool Not specified) ⊗
Regime⟨Static⟨capacity_down: 100 mbps [§4.3], latency: Not specified,
queue{size: swept}⟩;
Dynamic⟨pressure: load(4 additional identical-cca flows ↦ sender nodes,
arrival on +100 s/−100 s schedule [§4.3] — NFA timing states)⟩⟩⟩;
path⟨latency: Not specified⟩;
Roles⟨client: sender, server: receiver⟩;
iterations 3 [§3; §4.3]; telemetry{pcap: true (timelines + JFI capture-derived)}.

**(iii) Requirements v2.** INHERITED from ES1, deltas: `capacity_down:
100 mbps` [§4.3] (∈ [0.1 mbps, 10 gbps]; and BDP now resolves to
100 mbps × RTT for queue.args); four LoadEntries with scheduled start/stop
offsets (NFA-internal timing, in-grammar); the competing-flow count on Fig 8
x-axis is an analysis window over one run, no collection requirement.

**(iv) Capability match v2.**
- **Design: SATISFIED — INHERITED from ES1 (cca{build}), delta SATISFIED:**
  arrival/departure schedule = NFA-internal timing; 100 mbps and 8–32×BDP
  queue sizes are ordinary A5 fields. Cubic + bbr@v5.4 leaves are gap-free
  at design AND impl level for the CCA axis (kernel-build gap only affects
  BBRv2/v3 at implementation, not design in v2).
  five-flow scheduled workflow is one more registry entry).
  are routine scripting; kernel-sweep and manual-telemetry caps unchanged.

**confidence: high**

---

### bbrv3-ES4 — RTT fairness, long-RTT (160 ms) starts first (Fig 10, 11, 12)

**(i) Raw text.** "two flows using the same CCA, where the first flow is our
base flow with a fixed RTT of 160 ms and the second flow experiences a
different RTT—one of 10, 20, 40, 80 ms, each constituting a different
experiment. In the first experiment scenario, the base flow, 160 ms, starts
first and the second flow joins after 15 seconds" [§4.4]. Buffer axis
{1/4,1/2,1,2,4}×BDP [Fig 10/11 axes]. CCAs BBRv1/v2/v3/Cubic [Fig 10; Fig 11].
Bandwidth, duration: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  cca{build: ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0, cubic}} ×
  path.latency_second_flow ∈ {10,20,40,80} ms [§4.4] ×
  Static.queue{size: ∈ {1/4,1/2,1,2,4}×BDP}) = 4×4×5 = 80⟩;
Experiment = ⟨Workflow(bulk base flow; path⟨latency: 80 ms one-way →
RTT=160 ms [§4.4]; tool Not specified⟩; duration 300 s; starts first) ⊗
Regime⟨Static⟨capacity_down: Not specified; latency: Not specified (both flows
use per-workflow path.latency; no shared Static.latency needed when both paths
differ); queue{size: swept}⟩;
Dynamic⟨pressure: load(second bulk flow;
path⟨latency: ∈ {5,10,20,40} ms one-way → RTT ∈ {10,20,40,80} ms [§4.4]⟩;
cca{same as foreground, per-leaf}; start +15 s offset [§4.4])⟩⟩⟩;
Roles⟨client: sender, server: receiver⟩;
iterations 3 [§3]; telemetry{pcap: true (per-flow throughput → TD/JFI)}.

**(iii) Requirements v2.** INHERITED from ES1 (cca{build}; load; bulk
workflow), deltas: **per-flow latency** — v2 `path.latency` per-workflow
expresses the two different RTTs (foreground 160 ms round-trip, load flow
swept 10–80 ms round-trip) through one shared bottleneck — spec-gap #4
RESOLVED at design level. The swept second-flow `path.latency` is a
`sweeps:` axis on a v2 first-class field.

**(iv) Capability match v2.**
- **Design: SATISFIED.** v2 per-workflow `path.latency` resolves spec-gap #4
  (per-flow latency; spec-gap register as of gold). Each workflow carries its
  own `path.latency`; the bottleneck `Static.latency` can be left unset (or
  set to a base value) with per-flow additions realized via separate netem
  instances on per-host access links. The `cca{build}` field resolves spec-gap
  #5. EVERY leaf of this set is now gap-free at design level.
  v2 delta vs gold: gold was GAP-DESIGN (spec-gaps #4 + #5). Now SATISFIED.
  would need per-flow tc filter classes (HTB or netem per-source-IP, or
  (per-flow netem classes or per-host access-link separate shape calls);
  BBRv2/v3 builds and load co-scheduling inherited from ES1.
  Per-flow RTT is declarative in Mininet: each sender's access TCLink carries
  its own `delay`, so 160 ms vs 10–80 ms paths over one bottleneck are plain
  topology (Link = TCLink⟨delay⟩ per link) — Mininet expresses declaratively
  what A5 historically could not (now resolved in v2, but the IMPL gap remains).
  Caps: kernel-build sweep = host reprovisioning; telemetry manual; 80×3
  campaign hand-scripted.

**confidence: high** — per-workflow path.latency unambiguously resolves #4;
per-flow netem impl gap clearly remains.

---

### bbrv3-ES5 — RTT fairness, short-RTT starts first (Fig 13, 14, 15)

**(i) Raw text.** "In the second scenario, the base flow joins 15 seconds
after the flow with the shorter RTT (Fig. 13, Fig. 14 and Fig. 15)" [§4.4].
Same RTT set {10,20,40,80} ms, same buffer axis {1/4…4}×BDP, same CCAs.
Bandwidth, duration: Not specified.

**(ii) Grammar v2.** As ES4 with arrival order reversed: Workflow = short-RTT
flow starts first; load = 160 ms base flow, +15 s offset. Leaves 80;
iterations 3 [§3].

**(iii) Requirements v2.** INHERITED from ES4 (per-workflow path.latency;
cca{build}; load); the arrival-order flip is a `LoadEntry.params` start-offset
swap, in-grammar.

**(iv) Capability match v2.** Verdicts INHERITED from ES4, delta: arrival
order only (a params start-offset swap, in-grammar at every level) —
ES4's stated reasons.

**confidence: high**

---

### bbrv3-ES6 — inter-CCA two-flow fairness, buffer sweep (Fig 16, 17, 18)

**(i) Raw text.** "we run two (co-existing) long-lived flows, each using a
different CCA; we start these flows at the same time. We set the RTT to
100 ms and the bandwidth to 100 Mbps, and we vary the bottleneck buffer size
as a function of BDP" [§4.5]. Buffer axis 1/4…16×BDP [Fig 17 axes]. Pairs:
each BBR version vs the others and Cubic [Fig 17a–c]. Duration: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  foreground.cca{build: ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0, cubic}} ×
  load.cca{build: ∈ {bbr@v5.4, bbr@v5.13.12, bbr@v6.4.0, cubic}}
  → 6 unordered CCA pairs [§4.5] ×
  Static.queue{size: ∈ {1/4,1/2,1,2,4,8,16}×BDP}) = 6×7 = 42⟩;
Experiment = ⟨Workflow(bulk flow, cca{build: A}; tool Not specified) ⊗
Regime⟨Static⟨capacity_down: 100 mbps [§4.5], latency: →RTT 100 ms [§4.5],
queue{size: swept, params: tbf}⟩;
Dynamic⟨pressure: load(bulk flow, cca{build: B} ↦ second sender,
synchronous)⟩⟩⟩;
path⟨latency: shared 100 ms symmetric⟩;
Roles⟨client: sender, server: receiver⟩;
iterations 3 [§3]; telemetry{pcap: true (timelines, JFI, retx %)}.

**(iii) Requirements v2.** INHERITED from ES1, delta: **per-flow CCA** —
v2 per-workflow `cca` carries each flow's own `cca{build}` (foreground
workflow and load workflow each have a `cca` field). The per-flow-cca tension
identified in gold (A5 `static.cca` had only one value; `LoadEntry` had no
static override) is resolved: in v2 cca is per-workflow, and both the
foreground and load workflows carry their own `cca{algo, build}`.

**(iv) Capability match v2.**
- **Design: SATISFIED.** Per-workflow `cca` in v2 resolves the per-flow-cca
  tension from gold. Each of the 6 CCA pairs (foreground cca{build: A} +
  load cca{build: B}) is expressible. `cca{build}` resolves spec-gap #5 for
  all pairs including the three inter-BBR-version pairs. The pairwise campaign
  shape is in-grammar (load ⊗ imposed Static, sweeps axis).
  v2 delta vs gold: gold was GAP-DESIGN (#5; per-flow-cca tension). Now SATISFIED.
  Named minor: tbf ∉ qdisc closed set (§8.1) — enum extension, not structural.
  dispatch exists but is per-request/single-valued (`_REQUEST_TCP_CCA`
  two-CCA-in-one-experiment path; BBRv2/v3 kernel-variant nodes and load
  dispatch path in one experiment), plus ES1 gaps.
  BBRvX-vs-Cubic pair families (21/42 leaves) are realizable per kernel build:
  per-host `cca` selection is declarative (host kernel module, per-socket
  selection) and cubic coexists with whichever bbr the booted kernel provides.
  The three inter-BBR-version pair families (21/42 leaves) are structurally
  outside the model: all hosts share one kernel, and no kernel ships two BBR
  builds side by side (mininet-capability.md: cca = shared kernel).
  Manual-telemetry and hand-scripted campaign caps apply to the realizable half.

**confidence: high** — per-workflow cca in v2 cleanly resolves the
per-flow-cca tension; the impl two-CCA-path gap clearly remains.

---

### bbrv3-ES7 — inter-CCA at scale: 1–5 BBR vs 1–5 Cubic flows (Fig 19)

**(i) Raw text.** "we vary the number of BBR flows as well as competing Cubic
flows from 1 through 5"; "link bandwidth to 100 Mbps, the RTT to 100 ms, and
the buffer size to 1×BDP (i.e., 1250 KB). We start all the flows at the same
time and run them for 360 s" [§4.5]; "concatenated over three experiment runs"
[§4.5]. Versions v1/v2/v3 each vs Cubic [Fig 19a–c].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  BBR cca{build: ∈ {v5.4, v5.13.12, v6.4.0}} ×
  n_BBR ∈ {1..5} × n_Cubic ∈ {1..5}) = 3×5×5 = 75⟩;
Experiment = ⟨Workflow(bulk flow-group, cca{build: bbr@vX, algo: bbr},
  count n_BBR as workflow param) ⊗
Regime⟨Static⟨capacity_down: 100 mbps [§4.5], latency: →RTT 100 ms [§4.5],
queue{size: 1×BDP = 1250 KB [§4.5], params: {limit-in-bytes: 1250000}}⟩;
Dynamic⟨pressure: load(n_Cubic cubic flows, cca{algo: cubic} ↦ second sender,
synchronous)⟩⟩⟩;
duration 360 s [§4.5]; iterations 3 [§4.5]; telemetry{pcap: true}.

**(iii) Requirements v2.** INHERITED from ES6 (per-workflow cca{build};
load with per-side cca), deltas: flow-count parameters on both the workflow
and the LoadEntry (plain `params` ints, in-grammar); a byte-denominated
queue size (`queue{params: {limit-bytes: 1250000 [§4.5]}}` — verbatim tc
args, interface defs §8.1).

**(iv) Capability match v2.**
- **Design: SATISFIED — INHERITED from ES6 (per-workflow cca{build}; load),
  delta SATISFIED:** flow counts are ordinary params; 1250 KB is a literal
  `queue.params`; the 2-D count grid is client-side sweep expansion.
  v2 delta vs gold: gold was GAP-DESIGN (inherited ES6 #5 + per-flow-cca).
  Now SATISFIED.
  BBRv2/v3 kernel builds; load co-scheduling; N-flow bulk workflow entry).
  pair), so per kernel build every leaf is realizable: N processes per host,
  per-socket cca (shared-kernel), TCLink 100 Mbps/delay/queue. Caps: version
  dimension = three host kernels (reprovisioning between run families),
  telemetry manual (per-flow JFI + shares), 75×3 campaign hand-scripted.

**confidence: high**

---

### bbrv3-ES8 — real-world workload, all flows same CCA (Fig 20)

**(i) Raw text.** "a distribution of flows comprising both short-lived (i.e.,
mouse) and long-lived (i.e., elephant) flows … We use the Harpoon [44]
traffic generator to sample the flow sizes and connection times from this
trace data. We fixed the random seed used in the sampling" [§4.6]; "all
flows to use the same CCA" [§4.6]; "bottleneck bandwidth set to 100 Mbps,
RTT to 100 ms, and the buffer size to BDP" [§4.6]. CCAs BBRv1/v2/v3/Cubic
[Fig 20b/c legends]. FCT buckets 5K/300K/20M/1.5G bytes [Fig 20b/c axes].
Flow count, duration: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(cca{algo: bbr|cubic,
build: ∈ {v5.4, v5.13.12, v6.4.0, n/a}}) = 4⟩;
Experiment = ⟨Workflow(harpoon generator; params{seed: fixed [§4.6],
distributions: MAWI-derived Pareto/Lognormal [§3], inter-arrival-scale: ×5 [§3]}) ⊗
Regime⟨Static⟨capacity_down: 100 mbps [§4.6], latency: →RTT 100 ms [§4.6],
queue{size: 1×BDP}⟩;
Dynamic⟨Not specified (the workload IS the flow mix; no additional pressure;
silence §5b.2)⟩⟩⟩;
Roles⟨client: sender, server: receiver⟩;
iterations 3 [§3]; telemetry{pcap: true (per-flow FCTs capture-derived),
app_metrics: true (generator flow log → stdout_summary, §8.11)}.

**(iii) Requirements v2.** INHERITED from ES1 (cca{build} for BBRv2/v3
leaves), deltas: a seeded distribution-driven generator workflow (seed ∈
`application.params` → inside `identity(e)` — reproducible sampling, spec
§4.3); MAWI trace download + Zeek extraction are offline workload-authoring
inputs (exogenous data preparation, not collection); FCT extraction needs
per-flow records (pcap + generator logs as `app_metrics.stdout_summary`).

**(iv) Capability match v2.**
- **Design: SATISFIED — INHERITED from ES1 (cca{build}), delta SATISFIED:**
  seeded generator is Workflow(params) — the seed in params lands in identity;
  trace-derived distribution files are workflow artifacts via offline authoring
  gate (spec P-SYS 3). Cubic and bbr@v5.4 leaves gap-free at design AND impl
  CCA axis (BBRv2/v3 impl-only gap). v2 delta vs gold: gold was GAP-DESIGN
  (inherited #5). Now SATISFIED.
  any distributional traffic-generator) workflow anywhere in the registry or
  worker tools = iperf3/tcpreplay-class); authoring item: `harpoon_client`/
  `harpoon_server` entries + distribution artifact files.
  (the tool was built for testbeds); envelope declarative. Caps: BBRv2/v3
  kernel builds, FCT telemetry hand-built, campaign scripted.

**confidence: high**

---

### bbrv3-ES9 — real-world workload, flows split BBR/Cubic (Fig 21)

**(i) Raw text.** "in the second, we configure half of the flows to use one
of the BBR versions and the other half to use Cubic" [§4.6]; same seeded
MAWI/Harpoon workload, same 100 Mbps / 100 ms / BDP buffer [§4.6]. Pairings
v1/v2/v3 each vs Cubic [Fig 21a–f]. Flow count, duration: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(pairing ∈
{bbr@v5.4-vs-cubic, bbr@v5.13.12-vs-cubic, bbr@v6.4.0-vs-cubic}) = 3⟩;
Experiment = ⟨Workflow(harpoon half-population, cca{algo: bbr, build: vX};
params as ES8 ↦ sender S1) ⊗
Regime⟨Static as ES8; Dynamic⟨pressure: load(harpoon half-population,
cca{algo: cubic} ↦ sender S2, same fixed seed across pairings)⟩⟩⟩;
Roles⟨client, server⟩; iterations 3 [§3]; telemetry as ES8.

**(iii) Requirements v2.** INHERITED from ES8 (Harpoon; seed-in-identity) and
ES6 (per-workflow cca{build}): the 50/50 CCA split is two half-rate generator
instances — foreground workflow with `cca{algo: bbr, build: vX}` and load
workflow with `cca{algo: cubic}`. Per-workflow cca in v2 resolves the split
— in-grammar.

**(iv) Capability match v2.**
- **Design: SATISFIED — INHERITED from ES8 (cca{build}) + ES6 (per-workflow
  cca), delta:** the 50/50 split is expressible as two half-rate generator
  workflows (workflow + LoadEntry) with per-workflow cca. v2 per-workflow cca
  resolves the per-flow-cca tension from gold. v2 delta vs gold: gold was
  GAP-DESIGN (inherited #5 + per-flow-cca tension). Now SATISFIED.
  two-CCA dispatch path; BBRv2/v3 kernel-variant nodes; load co-scheduling).
  Cubic (realizable per kernel build); kernel reprovisioning across the three
  pairings, manual FCT telemetry, scripted campaign.

**confidence: high**

---

