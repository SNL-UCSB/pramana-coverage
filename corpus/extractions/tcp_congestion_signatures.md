# tcp_congestion_signatures — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| tcp_congestion_signatures-ES1 | E1 | dynamic ∈ {load(TGtrans), load(TGtrans+TGcong)} [§2.3; Fig 1 caption] | 2 | Not specified |
| tcp_congestion_signatures-ES2 | E2 | static.capacity_down ∈ {10,20,50} mbps × path.loss ∈ {0.02,0.05} × static.latency ∈ {20,40} ms × static.queue{size: buffer_ms ∈ {≈20,50,100} ms} × dynamic ∈ {load(TGtrans), load(TGtrans+TGcong)} [§3.1] | 3×2×2×3×2 = 72 | 50 per ⟨capacity, latency, loss⟩ triple [§3.1]; allocation across buffer and pressure dims Not specified |
| tcp_congestion_signatures-ES3 | E3 | dynamic.load[tgcong].params.concurrency ∈ {100,50,20,10} [§3.3] | 4 | Not specified |
| tcp_congestion_signatures-ES4 | E4 | access-link cross-flow count → dynamic.load[tgaccess].params.concurrency ∈ {1,2,5} [§3.3] | 3 | Not specified |
| tcp_congestion_signatures-ES5 | E5 | exogenous corpus: M-Lab NDT Jan–Apr 2014 | Not specified (crowdsourced) | n/a |
| tcp_congestion_signatures-ES6 | E6 | two sub-campaigns, one collection: (a) ndt_client @ Ark↦TATA, (b) tslp_probe (continuous) [§4.2] | 2 | (a) 2593 realized tests [§4.2]; (b) continuous, Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Dual-bottleneck testbed [Fig 2; §3.1]: 2× Raspberry Pi 2, 2× Linksys
> WRT1900AC, "physically located at the San Diego Supercomputing Center in
> San Diego, CA" [§3.1]. AccessLink emulation: "we use tc with a token-bucket
> with a 5 KByte burst filter" [§3.1]. InterConnectLink "emulates an
> interdomain link at 950 Mbps with a 50 ms buffer (we shape it to 950 Mbps,
> slightly less than its 1 Gbps capacity …)" [§3.1]; no added latency or loss
> on it [§3.1]. Workload: "We use netperf to run 10-second downstream
> throughput tests" [§3.1]; "capturing packet traces using tcpdump for each
> test" [§3.1]; "We extract the RTT features from the Server 1 packet traces"
> [§3.2] — result pcap captured at the SERVER. Cross traffic: TGtrans (Go,
> Pi 2) fetches HTTP objects {10 KB…100 MB} from Server 2 (ICSI Berkeley,
> 20 ms) and Server 3 (Georgia Tech, 60 ms); "we run TGtrans during all our
> experiments" [§3.1]. TGcong (bash, Router 2) fetches a 100 MB file from
> Server 4 (< 2 ms) "using 100 concurrent curl processes", saturating
> InterConnectLink; "we run TGcong for experiments that require external
> congestion" [§3.1]. CCA of the test flow: Not specified.

---

### tcp_congestion_signatures-ES1 — illustrative self-vs-external runs (Fig 1)

**(i) Raw text.** "We run two simple experiments over an emulated 20 Mbps
'access link'" [§2.3]; "one set of experiments using a 20 Mbps emulated
access link with a 100 ms buffer, served by a 1 Gbps link with a 50 ms
buffer. The access link has zero loss and 20 ms added latency" [Fig 1
caption]; one self-induced run family and one external run family (TGcong
added) [§2.3; Fig 1].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(dynamic ∈ {load(tgtrans ↦
cross-node), load(tgtrans, tgcong ↦ cross-nodes)}) = 2⟩;
Experiment = ⟨Workflow(netperf, 10 s downstream; shell) ⊗
Regime⟨Static⟨capacity_down: 20 mbps [Fig 1 caption], latency: 20 ms [Fig 1 caption],
queue{discipline: tbf, size: 100 ms buffer [Fig 1 caption], params: burst 5 KByte [§3.1]};
second envelope (interconnect, cascaded): 950 mbps shaped / 50 ms buffer [Fig 1 caption;
§3.1] — no v2 production (see (iv));
Dynamic⟨pressure: load({tgtrans: http-fetch-workflow ↦ Router2-node},
{tgcong: curl-saturation ↦ Router2-node} for the second leaf)⟩⟩⟩ @
Roles⟨client: Pi1, server: Server1 (real Internet host)⟩;
path⟨latency: not added (0, stated [Fig 1 caption "zero loss"]), loss: 0,
jitter: Not specified⟩;
iterations: Not specified; telemetry{pcap: true (tcpdump at server [§3.1–3.2]),
app_metrics: true (netperf throughput stdout_summary)}.

**(iii) Requirements v2.** `Static.capacity_down: 20 mbps` ∈ [0.1 mbps, 10 gbps];
`Static.latency: 20 ms` ∈ [0, 2000 ms]; `path.loss: 0` (stated zero); `queue{discipline: tbf,
size: 100 ms buffer, params: burst 5 KByte}` — tbf ∉ closed qdisc set (§8.1
interface defs), a minor named gap; second Static envelope (950 mbps / 50 ms
buffer) cascaded behind the first — no v2 production; `dynamic.mode: load`
with two LoadEntry workflows (tgtrans, tgcong) whose endpoints attach BETWEEN
the two bottlenecks (bypass AccessLink topology [§3.1]); server role for netperf
sink + three cross-traffic server roles; telemetry.pcap captured at server role
(§8.8b: service deployments produce no ResultEnvelopes).

**(iv) Capability match v2.**
- **Design: GAP-DESIGN.** Three missing productions (same as gold, v2 does not
  resolve them): (1) A second Regime.Static cascaded envelope — v2 Static is
  still one bottleneck block (spec §2: `Regime = Static⟨capacity↓↑, latency,
  queue⟩ ⊗ Dynamic⟨pressure⟩`); (2) load-endpoint topology attachment point
  (load(Workflow* ↦ Node*) does not specify WHERE on the path a node attaches —
  TGtrans/TGcong must bypass AccessLink); (3) server-side pcap via §8.8b
  production (service node produces no ResultEnvelopes). `tbf` ∉ qdisc closed
  set remains a named minor gap (enum extension, not structural).
  v2 delta: `path.loss: 0` is now v2-vocabulary (the stated zero is `path.loss`
  not a v1 `impair.loss_pct` field), vocabulary correct; but the topology gaps
  mean overall GAP-DESIGN.
  (server-side capture path).
  element (Topology = arbitrary graphs; two TCLinks with bw/delay/max_queue_size,
  use_tbf) — envelope axis is Mininet's best case. Caps (min across axes,
  §5b.5): cross traffic (TGtrans random-fetch, TGcong 100-curl saturation) is
  hand-run processes (mininet-capability.md: Regime = Static-only, no
  Dynamic⟨pressure⟩ production); telemetry = manual (tcpdump by hand);
  server is a real Internet host (M-UNSAT class — but the shape question only
  needs the emulation topology; so the experiment reduces to emulated hosts

**confidence: high** — dual-bottleneck gap well-established; v2 path.loss
vocabulary adds nothing structural here.

---

### tcp_congestion_signatures-ES2 — main controlled sweep (Figs 3, 4)

**(i) Raw text.** "set [AccessLink] to 10 Mbps, 20 Mbps, and 50 Mbps, loss
to 0.02% and 0.05%, and latencies to 20 ms and 40 ms, with jitter set to
2 ms" [§3.1]; "three buffer sizes for AccessLink: approximately 20 ms, 50 ms,
and 100 ms" [§3.1]; "For each throughput, latency, and loss combination, we
run 50 download throughput tests" [§3.1]. Jitter 2 ms [§3.1]. Bandwidth,
latency values above; loss values above; all with locators.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  Static.capacity_down ∈ {10,20,50} mbps [§3.1] ×
  Static.latency ∈ {20,40} ms [§3.1] ×
  path.loss ∈ {0.02,0.05} [§3.1] ×
  Static.queue{size: buffer_ms ∈ {≈20,50,100} ms} [§3.1] ×
  Dynamic.pressure ∈ {load(tgtrans), load(tgtrans+tgcong)}) = 3×2×2×3×2 = 72⟩;
path.jitter: 2 ms fixed [§3.1] across all leaves; second envelope (interconnect):
950 mbps / 50 ms buffer fixed [§3.1];
Experiment = ⟨Workflow(netperf 10 s; shell) ⊗ Regime as ES1 with swept values⟩ @
Roles as ES1; iterations: 50 per ⟨capacity, latency, loss⟩ triple [§3.1] —
per-leaf allocation across buffer and pressure dims Not specified;
telemetry{pcap: true, app_metrics: true}.

**(iii) Requirements v2.** ES1's vocabulary plus: `path.loss ∈ {0.02, 0.05}` [§3.1]
(v2 per-workflow path field); `path.jitter: 2 ms` [§3.1] (v2 per-workflow path field;
expansion to 72 leaves; per-leaf iterations ≈ 50.

**(iv) Capability match v2.**
- **Design: GAP-DESIGN — INHERITED from ES1** (dual-bottleneck envelope,
  load-endpoint attachment, server-side capture; stated there).
  v2 delta: `path.loss` and `path.jitter` are now first-class v2 vocabulary
  (per-workflow path fields); the swept values {0.02%, 0.05% loss; 2 ms jitter}
  are in-range. The single-bottleneck projection of this set is fully
  in-grammar v2; only the topology carries the gap.
  `path.jitter` are design-valid v2 fields but NOT wired at the
  `loss_pct` and `jitter` as first-class parameters (mininet-capability.md:
  `Link = TCLink⟨bw, delay, jitter, loss_pct, max_queue_size⟩`) — the loss/
  jitter axes are declaratively expressible in Mininet. However the campaign
  (72 leaves × 50 iterations), cross-traffic drivers, and hand-built telemetry

**confidence: high** — v2 adds path.loss/path.jitter vocabulary; topology gap
unchanged.

---

### tcp_congestion_signatures-ES3 — interdomain multiplexing sweep (§3.3, text-only)

**(i) Raw text.** "we fix the access link to 50 Mbps, and reduce the number
of cross-traffic processes generated by TGcong" [§3.3]; classification
decreases "from 93% when there are 100 concurrent flows, to 84% when there
are 50, to 74% with 20, and 50% with 10" [§3.3]. Latency/loss/buffer Not
specified (not restated). Repetitions Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  dynamic.load[tgcong].params.concurrency ∈ {100,50,20,10}) = 4⟩;
Experiment = ⟨Workflow(netperf; shell) ⊗
Regime⟨Static⟨capacity_down: 50 mbps [§3.3], latency: Not specified, queue: Not specified⟩;
dual-bottleneck base inherited [§3.1];
Dynamic⟨pressure: load(tgtrans + tgcong, tgcong.params.concurrency swept)⟩⟩⟩ @
Roles as ES1; iterations Not specified; telemetry{pcap: true, app_metrics: true}.

**(iii) Requirements v2.** ES1's vocabulary; the treatment rides
`LoadEntry.params.concurrency` (a declared param, interface defs §8.1 LoadEntry)
swept as a dim — dynamic.load participates in identity (§8.11b), so the four
leaves are distinct identity-hashed Experiments.

**(iv) Capability match v2.**
- **Design: GAP-DESIGN — INHERITED from ES1** (topology productions). Delta:
  sweeping a load-workflow parameter is in-grammar (sweep is generic, spec §2;
  dynamic.load is in the identity payload); the concurrency treatment is
  exactly what `load()` exists for.
  count, trivially scriptable, but this is hand-run cross-traffic machinery

**confidence: high**

---

### tcp_congestion_signatures-ES4 — access-link multiplexing sweep (§3.3, text-only)

**(i) Raw text.** "we introduce cross traffic in the access link … with 1, 2
and 5 concurrent flows" [§3.3]; "Even with 1 cross-flow, our test [flow] …
the classifier still classifies 86% of flows as self-limited. With 5 flows,
this number is 70%" [§3.3]. AccessLink bandwidth for THIS sweep: Not
specified (only interdomain sweep states 50 Mbps [§3.3]). Repetitions: Not
specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(
  dynamic.load[tgaccess].params.concurrency ∈ {1,2,5}) = 3⟩;
Experiment = ⟨Workflow(netperf; shell) ⊗
Regime⟨Static⟨capacity_down: Not specified, latency: Not specified, queue: Not specified⟩;
dual-bottleneck base inherited;
Dynamic⟨pressure: load(tgtrans ↦ interconnect-side) +
load(tgaccess.params.concurrency N ↦ access-link-side)⟩⟩⟩ @
Roles as ES1; iterations Not specified; telemetry{pcap: true, app_metrics: true}.

**(iii) Requirements v2.** ES1's vocabulary; access-link cross-flows are
LoadEntry workflows whose path SHARES the client's shaped bottleneck (closed-
loop cross-traffic through the access-link regime); swept over flow count via
`LoadEntry.params.concurrency`.

**(iv) Capability match v2.**
- **Design: GAP-DESIGN — INHERITED from ES1** (dual-bottleneck base and
  TGtrans attachment remain). Delta: the treatment itself — N concurrent
  cross-flows through the SAME bottleneck as the foreground — is the one
  pressure pattern `load()` expresses without residue in v2; if run against
  a single-bottleneck regime it would be fully in-grammar v2.
  half is closest to shipped mechanics but the load-workflow path is not
  packaged (registry gap, as ES1).
  hand-run cross-traffic, manual telemetry, hand-scripted campaign).

**confidence: high**

---

### tcp_congestion_signatures-ES5 — Dispute2014 M-Lab NDT collection (Figs 5, 7, 8, 9)

**(i) Raw text.** M-Lab NDT measurements, January–April 2014 [§1; §4.1];
server-side "Web100 statistics that … provide TCP performance over 5 ms
intervals" + raw traces "in pcap format", obtained "through Google's Big
Query and Big Store" [§4.1]. Transit: Cogent (LAX, LGA), Level3 (ATL);
access ISPs Comcast, TimeWarner, Verizon, Cox [§4.1]. Labels: peak
(4 PM–12 AM) Jan–Feb = external; off-peak (1 AM–8 AM) Mar–Apr = self-induced
[§4.1]. Total flow count: Not specified.

**(ii) Grammar v2.** Not compilable as a collection: the dataset query
(BigQuery/BigStore [§4.1]) is not `collect = deploy ; prepare ; verify ;
run ; publish` (spec §2). The treatment (2013/14 Cogent–Netflix peering
dispute and its late-Feb 2014 resolution [§4.1]) is a historical world event
outside any backend's actuation. Leaf space: Not specified (crowdsourced).

**(iii) Requirements v2.** None realizable in v2 vocabulary — exogenous-data
acquisition. All post-collection filters (9 s duration, 90%-congestion-limited,
≥10-RTT-sample) are post-hoc outcomes (§5b.1), not collection parameters.

**(iv) Capability match v2.**
- **Design: OUT-OF-SCOPE.** Exogenous data, per CALIBRATION.md §3.4a: the
  collection is a third-party historical corpus whose treatment (a real
  peering dispute) is outside any backend's actuation; `collect()` generates
  new measurements (spec §2) and no production fetches an external archive.
- **Implementation: n/a** (CORPUS_PROMPT_v4 §1 rule 4: OUT-OF-SCOPE design ⇒
- **Mininet: M-UNSAT.** The measurand is deployed Internet interconnect
  congestion during a real peering dispute, observed through a crowdsourced
  user population — phenomena of the real Internet path
  (mininet-capability.md M-UNSAT class).

**confidence: high** — exogenous historical corpus, unambiguously OUT-OF-SCOPE.

---

### tcp_congestion_signatures-ES6 — TSLP2017 targeted campaign (Fig 6; §5.4 text results)

**(i) Raw text.** "We run periodic, automated NDT measurements between this
Ark node and the TATA server" [§4.2]; Ark node in Comcast's network, Bedford,
Massachusetts; M-Lab server hosted by TATA in New York [§4.2]; "We run
throughput tests every 1 hour during off-peak hours and every 15 minutes
during peak hours between February 15 and April 30, 2017" [§4.2]; "We
collected 2593 NDT tests in the 10[-week period]" [§4.2]. Client plan
25 Mbps downlink [§4.2]; baseline latency ≈18 ms rising above 30 ms when
congested [§4.2]; corresponding buffer size not stated (omitted per C5).
Labels (§5.4): external if throughput < 15 Mbps and min latency ≥ 30 ms;
self-induced if exceeding 20 Mbps and minimum latency less than 20 ms [§5.4].

**(ii) Grammar v2.** ExperimentSet⟨leaves: 2 sub-campaign leaf families, one
collection [gold E6]: (a) ⟨Workflow(ndt_client; shell) ⊗
Regime⟨Static⟨none imposed — inhabited (probe characterizes); the 25 mbps
plan and ≈18 ms baseline are MEASURED properties of the real path [§4.2]⟩;
Dynamic⟨Not specified (treatment is real diurnal interconnect congestion —
nothing generated)⟩⟩ @ Roles⟨client: Ark node (Comcast, Bedford MA),
server: TATA-hosted M-Lab server (real third-party endpoint)⟩;
path⟨latency: inhabited (not imposed)⟩⟩;
(b) ⟨Workflow(tslp_probe; shell, out-of-band far/near-router latency probes [§4.2]) ⊗
same inhabited Regime⟩ @ same Roles⟩.
iterations: (a) 2593 realized tests on a time-of-day-conditional schedule
(15 min peak / 1 h off-peak, Feb 15–Apr 30 2017) — `iterations = int` cannot
express calendar cadence; (b) continuous, Not specified.
telemetry{pcap: true (server-side M-Lab), app_metrics: true (Web100 stats +
NDT throughput [§4.1–4.2])}.

**(iii) Requirements v2.** Inhabited-mode Regime (spec §2: "inhabited (probe
characterizes)"); shell `ndt_client` and `tslp_probe` workflows; a vantage node
inside a third-party residential network (Ark) — a connector beyond
local_docker | aws | ssh (A5 `mapping:`, spec §4; Tier-3 connectors deferred,
spec §5.4 M9); a time-triggered, peak/off-peak-conditional iteration schedule
sustained for 10 weeks (no v2 production — `iterations = int | until(event(...))`;
calendar cadence is outside both forms); the M-Lab endpoint via endpoints:

**(iv) Capability match v2.**
- **Design: GAP-DESIGN.** Two missing productions (same as gold, v2 does not
  resolve them): (1) calendar-triggered collection schedule — v2 `iterations
  = int | until(event(metric,target),min,max)` covers adaptive stopping but
  NOT wall-clock cadence ("every 1 hour off-peak, every 15 minutes peak"
  [§4.2]); this is the same family as spec-gap register #3 but distinct
  (calendar cadence vs CI-driven stopping). (2) Third-party vantage connector
  (Ark node in Comcast's network) — T3 connectors are declared future work
  in spec (spec §5.4 M9). Inhabited mode itself is a declared Regime mode
  (in-grammar, explicitly unevaluated).
  workflows); no time-triggered scheduler (orchestration engine is FIFO
  sequential, no cron logic); no T3/Ark connector (`connectivity.py:754-771`
  (calendar cadence), connectors (T3).
- **Mininet: M-UNSAT.** The measurand is real, periodic Comcast–TATA
  interdomain congestion and its diurnal structure — phenomena of the real
  Internet path and real service endpoints (mininet-capability.md M-UNSAT
  class).

**confidence: high** — calendar-schedule gap and T3 vantage gap unchanged in v2.

---

