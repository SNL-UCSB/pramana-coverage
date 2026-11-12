# cclinguist — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| cclinguist-ES1 | Exp1 | cca ∈ {Vegas, Veno, Reno} [§2.1] × profile ∈ {A, B, C} [§2.1; Fig 2 caption] (profile values Not specified in text) | 9 (= 3×3) | Not specified |
| cclinguist-ES2 | Exp2 | train: cca 12 × profile ∈ eligible grid (BJ→HK; count Not specified, ≤ 90); test: application.workflow ∈ {cclinguist, ccanalyzer, nebby} × cca 12 × profile (cclinguist adaptive: iterations=until(event(conf≥0.7),1,7); ccanalyzer 4 profiles; nebby 2 profiles) [§7.1] | train Not specified (≤ 12×90 = 1080); test Not specified (adaptive) | test: 10 tests/CCA (cclinguist) [§7.1]; training Not specified |
| cclinguist-ES3 | Exp3 | application.workflow ∈ {cclinguist, ccanalyzer, nebby} × cca 12 × profiles-visited (cclinguist adaptive from root 140ms_400Kbps [Table 3]; baselines TargetProp ∈ {140…200} ms grid values) | Not specified (adaptive) | Not specified |
| cclinguist-ES4 | Exp4 | test: server ∈ WS1–WS6 (PCC_Latency×2, Astraea×2, PCC-Loss×2) [§7.3.1] × profiles-visited (adaptive); upgrade rounds: profile ∈ full candidate grid from one server per round [§6.3]; +15-CCA accuracy runs; +application.workflow ∈ {ccanalyzer, nebby} [§7.3.1] | Not specified (test 6 servers × adaptive profiles; upgrades ≤ 90/server) | 10 CCprints/server (test) [§7.3.1]; else Not specified |
| cclinguist-ES5 | Exp5 | server ∈ {WS7 (PCC_Variant1), WS8 (PCC_Variant2)} [§7.3.2] × profiles-visited (Not specified) | Not specified | 10 CCprints/server [§7 shared] |
| cclinguist-ES6 | Exp6 | cca ∈ 15 (12 known + ECN-DCTCP, ECN-Cubic, ECN-BBR-v2) × ⟨train BJ, test TYO⟩; ECN-enabled Throttler [§7.3.3] | Not specified (adaptive; root 60ms_400Kbps [Table 4]) | Not specified |
| cclinguist-ES7 | Exp7 | application.params.url ∈ CrUX Top-10K [§8] × client-region ∈ {HK, TYO, SV} × profile (adaptive per site; eligibility from measured NetProp/NetBW) | Not specified (10,000 sites attempted; 7,930 identified is OUTCOME [§8], not leaf filter — §5b.1) | Not specified |
| cclinguist-ES8 | Exp8 | application.params.url = alibaba-cdn-site [§8] × profiles-visited (Not specified) | Not specified (≥1) | Not specified |
| cclinguist-ES9 | Exp9 | sweep(Static.queue ∈ {ECN-enabled (RED+XDP [§4]), ECN-disabled}) × application.params.url ∈ {facebook.com case study; census population — 6109 completed handshakes is OUTCOME [§8]} | Not specified | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> "we deployed web servers on Alibaba Cloud across three regions: Beijing (BJ),
> Tokyo (TYO), and Silicon Valley (SV)"; "a CClinguist-equipped client located
> in Hong Kong (HK) collected CCprints and identified the CCA deployed on the
> web server"; "the server during each transmission was configured to employ one
> of the specified CCAs"; "For each type of CCA on each web server, we collected
> 10 CCprints" [§7 Prototype Setup]. Throttler (client side): "BtlBW =
> TargetBW", "BtlProp = TargetProp − NetProp" — delta over measured path [§7];
> "Throttler sets the buffer size to the BDP"; "a 15-second flow duration" [§4].
> CCprint = BQDF from per-packet arrival times at both Throttler and client [§4].
> ECN mode: XDP ECT-reset → IFB → TC (delay by BtlProp, BtlBW limit) + RED
> CE-marking on queue [§4; Fig 4]. Queue discipline (default mode): Not
> specified (only buffer=BDP stated; RED appears only in ECN-mode). Cross
> traffic: never mentioned → Dynamic: Not specified (silence, §5b.2). D-profile
> Tree walk max T=7 iterations [§5.3], Th_high=0.7, Th_low=(1−0.7)/N [§5.1].
> Candidate grid: TargetProp ∈ [30,40,…,200] ms (18 values) × TargetBW ∈
> [200,400,…,1000] Kbps (5 values) = 18×5 = 90 profiles [§7].

---

### cclinguist-ES1 — DTW preliminary distinguishability (Fig 2)

**(i) Raw text.** "Through a preliminary experiment, we verify that the
feature curves of different CCAs exhibit varying degrees of distinguishability
when subjected to different network profiles" [§2.1]; CCAs {Vegas, Veno,
Reno}, profiles A, B, C [§2.1; Fig 2 caption]; "fixed DTW distance threshold
of 2" (illustrative only, fn 1) [§2.1]. Profile A/B/C parameter values,
testbed pair, trace duration, repetitions: Not specified in text.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(cca{algo: vegas|veno|reno} ×
Static ∈ {profile-A, profile-B, profile-C}) = 3×3 = 9⟩;
Experiment = ⟨Workflow(HTTP download from web server; browser or shell)
⊗ Regime⟨Static⟨capacity_down/up: profile values Not specified; latency: Not
specified; queue{discipline: Not specified, size: BDP [§4 shared]}⟩;
Dynamic⟨Not specified (silence)⟩⟩;
path⟨latency: Not specified; jitter: Not specified; loss: Not specified⟩⟩ @
Roles⟨client: Throttler-equipped node, server: web server node⟩;
cca{algo: per-leaf kernel CCA} applied at server workflow;
iterations: Not specified; telemetry{pcap: true (BQDF derives from per-packet
arrival times [§4])}.

**(iii) Requirements v2.** Per-leaf `cca{algo: vegas|veno|reno}` at the
serving server (v2 per-workflow cca field); 3-profile static sweep
(profile values default-with-echo at compile since text states none);
`telemetry.pcap` with BQDF derived result-side from per-packet timestamps
on both Throttler and client sides; a server workflow role.

**(iv) Capability match v2.**
- **Design: SATISFIED.** `cca{algo: vegas|veno|reno}` — all three are v2
  per-workflow cca fields; vegas/veno/reno are in the 15-entry capability
  enum (interface defs §8.2). The 3×3 factorial is a `sweeps:` expansion
  (spec §4). All unstated envelope values are default-with-echo (spec §4.1).
  Named condition: dual-point pcap capture (pre/post-bottleneck arrival times)
  is a realization detail of `telemetry.pcap`, not a declared telemetry kind
  — BQDF is result-side derivation.
  v2 delta vs gold: no verdict change (gold was SATISFIED); vocabulary update
  only (`cca{algo:…}` replaces `static.cca = …`).
  composable. GAP: no packaged HTTP-download/census client or web-server
  browser workflows @fb4d8b6).
  modules are declarative. Cap: the result is a per-packet queuing-delay time
  series; Mininet objectifies no such telemetry — dual tcpdump + timestamp
  subtraction is hand-built machinery (mininet-capability.md: telemetry =
  manual). Verdict = min across axes.

**confidence: high**

---

### cclinguist-ES2 — known-CCA identification campaign, BJ→HK train + TYO→HK test (Fig 8 "Known CCAs", Fig 9a, Table 2; Fig 13 shared)

**(i) Raw text.** "For the training of CClinguist, data was collected through
the server-client pairs from BJ to HK, including CCprints collected under all
candidate network profiles for 12 CCAs in Linux kernel 5.4.0" [§7.1]; client
in HK identifying CCAs on TYO server [§7.1]; "the NetProp was 23ms and the
NetBW was 25Mbps" (TYO-HK) [§7.1]; "top three optimal root profiles =
[80ms, 600kbps], [100ms, 400kbps], [90ms, 400kbps]" [§7.1]; "10 tests for
each CCA … voted by three D-profile Trees" [§7.1]; accuracy 97.33% [§7.1].
Baselines: CCAnalyzer 4 profiles, Nebby 2 profiles [§7.1]. Number of
training CCprints per (cca, profile): Not specified.

**(ii) Grammar v2.** ExperimentSet:
(train) sweep(cca{algo: ∈ 12 kernel CCAs} × Static ∈ eligible candidate
grid, count Not specified ≤ 90) — ordinary factorial;
(test) sweep(application.workflow ∈ {cclinguist, ccanalyzer, nebby} × cca{algo:
∈ 12} × Static ∈ profiles-visited);
**cclinguist test: iterations = until(event(classifier_confidence ≥ 0.7 [§5.1]),
min=1, max=7 [§5.3])** — D-profile-Tree walk expressed as event-triggered
iterations in v2 grammar;
ccanalyzer: 4 fixed profiles; nebby: 2 fixed profiles.
Experiment = ⟨Workflow(HTTP download, 15 s flow [§4]) ⊗
Regime⟨Static⟨capacity_down = TargetBW ∈ {0.2..1.0} mbps [§7]; latency =
TargetProp − 23 ms (NetProp stated [§7.1]); queue{size: BDP}⟩;
Dynamic⟨Not specified (silence)⟩⟩⟩;
cca{algo: per-leaf, version: kernel-5.4.0 [§7.1]} applied at server workflow;
Roles⟨client: HK node, server: BJ (train) / TYO (test) node⟩;
telemetry{pcap: true (BQDF); qtrace: true for ccanalyzer sub-family}.

**(iii) Requirements v2.** Factorial training sweep over cca × candidate
per-leaf `cca{algo, version: kernel-5.4.0}` at the server workflow; event-
triggered iterations for cclinguist test walk (`until(event(conf≥0.7),1,7)`);
imposed latency as TargetProp − NetProp (offline-computable for fixed testbed
pairs); `telemetry{pcap, qtrace}`.

**(iv) Capability match v2.**
- **Design: SATISFIED** (training grid SATISFIED; cclinguist adaptive test
  SATISFIED via event-triggered iterations; baselines have fixed profiles).
  v2 delta vs gold: gold was GAP-DESIGN (adaptive walk had no production in
  v1). In v2, `iterations = until(event(metric,target),min,max)` directly
  expresses the D-profile-Tree walk stopping condition.
  Named condition on cca placement: `cca` is per-workflow in v2; the server
  workflow carries `cca{algo: ∈ 12 kernel-enum}` — in-grammar; the §8.8b
  service-node restriction ("static block recorded, never applied") does NOT
  apply when the server is a pool Node running a per-leaf workflow.
  bic, cubic, highspeed, htcp, illinois, reno, scalable, vegas, veno,
  Gaps: (1) no result-conditioned dispatch in Core — scheduler is FIFO over
  pre-expanded leaves (spec §5.3); no classify→next-profile loop in
  §3: registry = 10 browser entries @fb4d8b6); (3) `/qtrace` queue-occupancy:
  (http_download + tool workflows), qtrace verification.
  (TCLink + shared-kernel cca); but the campaign is a classifier-driven walk
  — a hand-written driver embedding the trained model (machinery the platform
  does not objectify); BQDF/queue telemetry is hand-built; three real cloud
  regions reduce to emulated hosts (acceptable for the shape question, as
  ccanalzyer-ES4). Verdict = min across axes.

**confidence: high** — event-triggered iterations clearly cover the D-profile-
Tree stopping condition; implementation dispatch gap clearly remains.

---

### cclinguist-ES3 — new-scenario campaign, SV–HK (Fig 8 "New scenarios", Fig 9b, Table 3; Fig 13 shared)

**(i) Raw text.** "We migrated the CCA identification scenario from TYO-HK to
SV-HK, where the measured NetProp = 120∼140ms. At this latency, the
previously selected root profile was no longer eligible. CClinguist
automatically selected another profile as the root profile" [§7.2]; Fig 9(b)
root 140ms_400Kbps; CClinguist 91.67% [§7.2]; baselines: "CCAnalyzer:
42.5ms, 65ms, 137.5ms; Nebby: 50ms, 100ms were below NetProp, so we took the
average accuracy under profiles from 140 to 200 ms" — CCAnalyzer 84.3%,
Nebby 58.33% [§7.2]. NetBW at SV, tests per CCA: Not specified.

**(ii) Grammar v2.** As ES2 test campaign with one delta: Roles.server = SV;
NetProp ∈ [120, 140] ms measured (offline-computable TargetProp − NetProp
per run); cclinguist iteration walk same as ES2;
iterations = until(event(classifier_confidence ≥ 0.7 [§5.1]), min=1, max=7 [§5.3]);
Regime⟨Static⟨latency = TargetProp − NetProp; capacity_down = TargetBW⟩⟩.

**(iii) Requirements v2.** INHERITED from ES2's test campaign with one new
demand: root-profile eligibility re-selection against a newly measured NetProp.
For the fixed testbed pair (SV-HK), offline measurement of NetProp ∈ [120,140]
ms allows offline computation of TargetProp−NetProp before compile — the
workaround preserves in-grammar spelling (the automation is a compile-time
prelude, not a gap).

**(iv) Capability match v2.** Verdicts INHERITED from ES2, delta stated:
- **Design: SATISFIED** — inherited from ES2 (event-triggered iterations;
  TargetProp−NetProp offline-computable). Delta: the profile eligibility
  re-selection against SV-HK's measured NetProp is offline-computable for
  fixed testbed pairs → the compile gate asks one question (What is
  NetProp_SV-HK?), then fixes the latency offsets. Not a runtime dependency.
  dispatch; no census/http workflow; no delta-specific plumbing).
  (120–140 ms) reduces to a declarative TCLink delay; caps are ES2's
  (hand-built BQDF telemetry, closed-loop campaign machinery).

**confidence: high**

---

### cclinguist-ES4 — self-upgrading new-CCA campaign, WS1–WS6 (Fig 8 "New CCAs", Fig 10 a–d; Fig 13 shared)

**(i) Raw text.** "we introduced three new CCAs (PCC-Loss, PCC-Latency, and
Astraea) on top of the 12 known CCAs"; "WS1 and WS2 ran PCC_Latency, WS3 and
WS4 ran Astraea, and WS5 and WS6 ran PCC-Loss. Ten CCprints were collected
from each server for identification" [§7.3.1]; self-upgrade: collect CCprints
across all candidate profiles from WS1 → weak-label → incorporate into
training set [§6.3]; final "average identification accuracy of 88.33% across
all 15 CCAs" [§7.3.1]; baselines: CCAnalyzer 76.53%, Nebby 49.31% [§7.3.1].
Regions for WS1–WS6: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves:
(test) server ∈ {WS1…WS6} × profiles-visited
(iterations = until(event(conf ≥ 0.7 [§5.1]), min=1, max=7 [§5.3]));
(upgrade rounds) sweep(Static ∈ full candidate grid) from WS1, then WS3 (per
Fig 10 b/c; third round's source server Not specified [§7.3.1]);
(+15-CCA accuracy runs);
(baselines) application.workflow ∈ {ccanalyzer, nebby} × cca 15⟩;
Experiment = ⟨Workflow(HTTP download; server workflow embeds PCC/Astraea CCA
binary — treatment CCA rides Workflow(params), not cca{algo} enum) ⊗
Regime⟨Static as ES2 grid; Dynamic⟨Not specified⟩⟩⟩ @
Roles⟨client: HK testbed, server: WS1–WS6⟩;
iterations as above; telemetry{pcap: true; qtrace: true for ccanalyzer family}.

**(iii) Requirements v2.** Everything in ES2 plus: (1) treatment CCAs outside
the kernel enum (PCC-Loss/PCC-Latency/Astraea) — `cca{algo}` enum is host-
kernel CCAs; the treatment rides the server workflow artifact
(Workflow(params) whose image embeds the CCA binary, moving the treatment
from cca-field into workflow@sha in identity); (2) upgrade-round sequencing
conditioned on prior classification outcomes — each round is a compilable
factorial ExperimentSet; the decision to run it is the researcher's (out of
scope, not a gap); (3) the event-triggered iteration walk (as ES2).

**(iv) Capability match v2.**
- **Design: SATISFIED**, with two named conditions. (a) Treatment-CCA-as-
  workflow: Workflow = CLI(app, role) ▸ NFA covers arbitrary server programs
  (ccanalzyer-ES8 precedent); the cca enum field cannot name PCC/Astraea but
  the treatment expression moves into application.workflow — in-grammar. (b)
  Upgrade-round sequencing: each round is a separate compilable
  ExperimentSet; the decision to run it is the researcher's / agent's, above
  the waist — out of scope (not a gap). The event-triggered iteration walk
  (as ES2) is in-grammar. v2 delta vs gold: gold was GAP-DESIGN (adaptive
  walk). With v2 event-triggered iterations, the adaptive walk is SATISFIED;
  the treatment-CCA-as-workflow and sequencing conditions are named but
  in-grammar.
  cannot be modprobe-installed. GAP: authored server workflow images
  pins as ES2.
  (the workflow surface is "arbitrary process in host netns") — realizable by
  hand; but every distinguishing piece (Astraea RL runtime, PCC builds,
  closed-loop campaign, BQDF telemetry) is hand-authored machinery
  (mininet-capability.md: telemetry = manual; shared-kernel means kernel CCA
  install is global to all hosts).

**confidence: high** — event-triggered iterations resolve the adaptive walk;
PCC/Astraea-as-workflow is a named condition, not a gap.

---

### cclinguist-ES5 — CCA-variant classification standards, WS7/WS8 (Fig 11 a/b)

**(i) Raw text.** "two new PCC variants with modified parameters were deployed
in WS7 and WS8 (WS7: PCC_Variant1, WS8: PCC_Variant2)" [§7.3.2]; unified
training: 90% CCprints recognized as known PCC; separated training: 60%
WS7 / 70% WS8 detected as unknown [§7.3.2]. Two training regimes are re-
labelings of already-collected CCprints [§7.3.2]. Profiles, repetitions
(10 CCprints/server via §7 shared), regions: not restated.

**(ii) Grammar v2.** ExperimentSet⟨leaves: server ∈ {WS7, WS8} ×
profiles-visited (Not specified);
iterations = until(event(conf ≥ 0.7 [§5.1]), min=1, max=7 [§5.3])⟩;
Experiment = ⟨Workflow(HTTP download; server workflow carries variant-CCA
Workflow(params{variant: WS7|WS8}) — the variant is a params delta) ⊗
Regime⟨Static: profile values Not specified; queue size BDP [§4 shared];
Dynamic⟨Not specified⟩⟩⟩ @
Roles⟨client: HK testbed, server: WS7/WS8⟩;
iterations: 10 CCprints/server [§7 shared]; telemetry{pcap: true}.

**(iii) Requirements v2.** ES4's treatment-CCA-as-workflow for parameter-
tuned variants ("modified parameters" of a known CCA maps onto
Workflow(params) with params in the identity hash, spec §4.3 — cleaner
spelling than ES4's new-CCA images); event-triggered iteration walk.

**(iv) Capability match v2.** Verdicts INHERITED from ES4, delta stated:
- **Design: SATISFIED — INHERITED from ES4 (event-triggered iterations;
  treatment-CCA-as-workflow), delta:** the variant treatment is favorable to
  the grammar — "modified parameters" maps onto Workflow(params) directly,
  cleaner than ES4's new-CCA images; label-regime contrast (Fig 11a vs 11b)
  is analysis, zero collection delta (G1). v2 delta vs gold: gold was
  GAP-DESIGN; now SATISFIED.
  images + ES2 dispatch gaps; no new module named).
  CCA processes are hand-deployable on emulated hosts; caps unchanged
  (mininet-capability.md: shared-kernel CCA modules; closed-loop campaign +
  BQDF telemetry = hand-built machinery).

**confidence: high**

---

### cclinguist-ES6 — ECN-based CCA campaign, BJ train / TYO test (Fig 8 "New ECN CCAs", Fig 9c, Fig 12, Table 4; Fig 13 shared)

**(i) Raw text.** "we introduced three representative ECN-based CCAs:
ECN-based DCTCP, ECN-based Cubic, and ECN-based BBR-v2" [§7.3.3]; server in
BJ for training, TYO for testing; CCA library = {12 known, +3 ECN-based} = 15
[§7.3.3]; Throttler ECN-enabled: XDP ECT-reset → IFB → TC delay/bandwidth +
RED CE-marking on its own queue [§4; Fig 4]; Fig 9(c) root 60ms_400Kbps
[Table 4]; accuracy 89.33% overall [§7.3.3]. Tests/CCA: Not restated.

**(ii) Grammar v2.** ExperimentSet⟨leaves: cca{algo: ∈ 15 (12 kernel-enum +
3 ECN-based variants)} × ⟨train BJ (grid), test TYO (adaptive)⟩;
iterations = until(event(conf ≥ 0.7 [§5.1]), min=1, max=7 [§5.3])⟩;
Experiment = ⟨Workflow(HTTP download) ⊗
Regime⟨Static⟨capacity_down = TargetBW; latency = TargetProp − NetProp;
queue{discipline: red, size: BDP, ecn: true, mode: CE-marking [§4; Fig 4]}⟩;
Dynamic⟨Not specified⟩⟩;
path⟨…⟩⟩ @
Roles⟨client: HK (ECN-enabled Throttler), server: BJ/TYO⟩; telemetry{pcap: true}.

**(iii) Requirements v2.** ES2 vocabulary plus:
(1) `queue{discipline: red, ecn: true, mode: CE-marking}` — v2 queue{ecn, mode}
subfields are new, expressible (design-SAT for RED-with-ECN);
(2) **ECT-forcing packet mangling** — XDP reset-to-ECT + IFB redirection has
no v2 production; Static is ⟨capacity, latency, jitter, queue, path, cca⟩,
none of which is packet-codepoint rewriting;
(3) ECN-mode CCA naming — ECN-DCTCP / ECN-Cubic / ECN-BBR-v2 are cca{algo}
variants; `cca{algo, params, flags}` in v2 can potentially express these via
flags/params, but the implementation intentionally excludes ECN-dependent CCAs

**(iv) Capability match v2.**
- **Design: GAP-DESIGN**, two remaining gaps after v2 closes the adaptive-walk
  gap: (a) **XDP ECT-forcing** — no A5/v2 production for packet-codepoint
  rewriting (Static's queue{ecn: true} enables ECN negotiation on the queue;
  the XDP stage that RESETS arriving packets' codepoints before the queue is
  a distinct, unproduced operation); (b) `cca{algo}` codepoint qualifier for
  ECN-mode variants — `cca{flags}` could encode this but no closed-set
  validation rule exists for "ECN-mode flag" in the capability file at
  c788e98. RED-with-ECN on the queue is NOW design-SAT via v2
  `queue{ecn: true}` (named as resolved). The adaptive walk is SATISFIED via
  event-triggered iterations.
  v2 delta vs gold: gold was GAP-DESIGN (XDP-forcing + cca signal-mode +
  adaptive walk). v2 resolves adaptive walk + RED-ECN queue; XDP-forcing and
  ECN-mode CCA naming remain.
  intentionally excluded: they require in-network ECN/LEDBAT support" —
  (XDP/IFB) has no functional code at c788e98 (git grep xdp|ifb|ecn: only
  capability file enum change + ES2 gaps.
  on the veth qdisc; dctcp module, shared kernel) — no wide-area middlebox
  interference; the XDP stage is moot. qdisc is "whatever tc accepts", hand-
  configured (mininet-capability.md: qdisc = hand-configured). Campaign +
  telemetry caps are ES2's. Verdict = min across axes.

**confidence: high** — XDP-forcing gap is clear; RED-ECN queue resolution is
clear; event-triggered iterations resolution is clear.

---

### cclinguist-ES7 — CCA census of the CrUX Top-10K (Table 1)

**(i) Raw text.** "we conducted a census of the top 10,000 websites ranked in
the Google Chrome UX Report (CrUX) dataset in June 2024. With the clients
deployed across 3 regions (HK, TYO, and SV), CClinguist identified a total of
7,930 web servers. Some websites were excluded because they were
unresponsive" [§8]; "CClinguist initially measured NetProp and NetBW from the
server to a client via probe packets" [§7]; "each probing lasts 15 seconds, the
total measurement time for sequential probing across all websites amounts to
roughly 33 hours" [§9(b)]; Table 1 totals: BBR 3517 (44.35%), CUBIC 1347
(16.99%), total 7930 [Table 1; §8]. CCprints per site, per-region site
split: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.params.url ∈
CrUX-Top-10K) × client-region ∈ {HK, TYO, SV} (assignment Not specified) ×
Static ∈ profiles-visited (adaptive per site);
iterations = until(event(conf ≥ 0.7 [§5.1]), min=1, max=7 [§5.3]) per site⟩
= 10,000 sites ATTEMPTED (7,930 identified is OUTCOME, §5b.1);
Experiment = ⟨Workflow(census HTTP GET, 15 s [§9(b)]) ⊗
Regime⟨Static⟨capacity_down = TargetBW (per-site eligibility from measured
NetProp/NetBW); latency = TargetProp − NetProp; queue{size: BDP}⟩;
Dynamic⟨Not specified⟩⟩⟩ @
Roles⟨client: region node (mapping: multi-region client pool, A5 mapping),
server: None (real third-party site)⟩; telemetry{pcap: true}.

**(iii) Requirements v2.** Imposed envelope over real Internet paths to 10,000
third-party endpoints (dataset-as-allow-list, ccanalzyer-ES9 condition);
per-site runtime characterization feeding imposed TargetProp−NetProp values
(A5 statics hashed at compile, spec §4.3 — offline-computable for fixed pairs
but per-site at census scale it is a runtime-to-compile feedback, a gap);
event-triggered iteration walk per site; multi-region client mapping
(A5 mapping first-class); shell metric extraction.

**(iv) Capability match v2.**
- **Design: GAP-DESIGN**, with in-grammar remainder named. Imposed ×
  inhabited-tail quadrant, 10K endpoint sweep (allow-list-as-dataset), and
  multi-region mapping are in-grammar (spec §2; §6; A5 mapping). Event-
  triggered iterations (as ES2) SATISFIED. Remaining gaps: (a) per-site
  static values derived from a runtime measurement at census scale — A5
  statics compiled before dispatch (spec §4.3); offline workaround fails at
  10K-site scale (each site measured at collection time); (b) the adaptive
  eligibility per site (the "per-site runtime characterization feeding the
  imposed values" gap, spec §4.3). v2 delta vs gold: adaptive walk SATISFIED;
  per-site runtime-to-compile gap remains (related: spec-gap register #6,
  time-varying statics).
  gaps is absent at c788e98: no inhabited-path characterization → compile
  plumbing; no census client workflow; 10K-endpoint campaigns untested at
- **Mininet: M-UNSAT.** The measurand is the deployed Internet's CCA
  population (which algorithms real websites and CDNs run); no emulation
  contains it (mininet-capability.md M-UNSAT class: "CDN-side CCA
  deployment", real service endpoints).

**confidence: high**

---

### cclinguist-ES8 — Alibaba-CDN unknown-CCA case study (Fig 14)

**(i) Raw text.** "we conducted tests on a website hosted by Alibaba's CDN,
which officially confirmed in use of self-developed new CCAs. The CCprint from
this website is shown in Fig. 14. The representation distance (10.16) between
its CCprint and the closest known CCA is higher than the margin (2.45), leading
to the CCprint being correctly marked as unknown" [§8]. Profile(s), client
region, CCprint count: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: application.params.url =
alibaba-cdn-site [§8] × Static ∈ profiles-visited (Not specified);
iterations = until(event(conf ≥ 0.7 [§5.1]), min=1, max=7 [§5.3]) if D-profile
Tree walk used (the paper does not state for this site — conditional)⟩;
Experiment = ⟨Workflow(census HTTP GET, 15 s) ⊗
Regime⟨Static⟨imposed throttler profile, values Not specified⟩;
Dynamic⟨Not specified⟩⟩⟩ @
Roles⟨client: census node, server: None (real CDN endpoint)⟩;
telemetry{pcap: true}.

**(iii) Requirements v2.** One real third-party endpoint under an imposed
bottleneck (allow-list condition, ES7); collection is a fixed probe;
unknown-vs-known distance test is entirely result-side.

**(iv) Capability match v2.**
- **Design: SATISFIED with ES7 endpoint condition.** As a single-site probe
  under (unstated → default-with-echo) profiles, this is the imposed × none
  quadrant with an inhabited tail, fully in-grammar. IF the probe walked a
  D-profile Tree (shared method; paper does not confirm for this site),
  event-triggered iterations SATISFIED. v2 delta vs gold: no change
  (gold was SATISFIED with same conditional note).
  /capture) present, same pins as ES1.
- **Mininet: M-UNSAT.** The subject is a real CDN's proprietary CCA; an
  emulated host cannot instantiate it (mininet-capability.md: real external
  services outside the model).

**confidence: high**

---

### cclinguist-ES9 — ECN-support exploration on live servers, Facebook case study (Fig 15)

**(i) Raw text.** "We also attempted to identify CCAs in use with an
ECN-enabled CClinguist client. The results indicated that 6109 websites are
capable of successfully completing ECN handshakes between hosts" [§8]; "Taking
Facebook as a case study, for ECN-marked packets, we could see Congestion
Window Reduced (CWR) in response and there are significant differences in
CCprints between ECN-disabled and ECN-enabled modes, as shown in Fig. 15" [§8].
Profile parameters, CCprint counts: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(Static.queue ∈
{ECN-enabled (queue{discipline: red, ecn: true, mode: CE-marking} + XDP-ECT-
forcing [§4]), ECN-disabled (queue{discipline: red, ecn: false})}) ×
application.params.url ∈ {facebook.com case study; census population —
6109 completed handshakes is OUTCOME, attempted-site count Not specified [§8])⟩;
Experiment = ⟨Workflow(census HTTP GET) ⊗
Regime⟨Static⟨imposed profile Not specified; ECN queue as above⟩;
Dynamic⟨Not specified⟩⟩⟩ @
Roles⟨client: census node, server: None (real site)⟩; telemetry{pcap: true}.

**(iii) Requirements v2.** ES6's ECN-mode machinery (ECT-forcing + RED
CE-marking) pointed at real third-party endpoints (ES7 allow-list condition);
queue{ecn: true|false} as a leaf sweep dimension — expressible in v2 via
`sweep(Static.queue{ecn: true|false})`. The XDP ECT-forcing stage remains a
gap (no v2 production).

**(iv) Capability match v2.** Verdicts INHERITED from ES6 (ECN-mode) and ES7
(real endpoints), deltas stated:
- **Design: GAP-DESIGN** — ES6 verbatim: XDP ECT-forcing has no v2 production;
  the ECN-enabled vs disabled mode contrast is partially expressible via
  `queue{ecn: true|false}` sweep (v2 queue field resolves the queue dimension),
  but the XDP ECT-forcing is the distinguishing implementation that makes the
  mode semantically different from a simple RED+ECN toggle. Real-endpoint side
  carries ES7's in-grammar conditions.
- **Mininet: M-UNSAT.** The question is whether Facebook's real servers change
  congestion behavior under ECN signals — a property of a real service endpoint
  (mininet-capability.md M-UNSAT class).

**confidence: high**

---

