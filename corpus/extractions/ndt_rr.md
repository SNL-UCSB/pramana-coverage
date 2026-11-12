# ndt_rr — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| ndt_rr-ES1 | E1 | vca ∈ {Meet, Teams, Webex} [§4] × condition-trace ∈ NDT tcp-info subset, avg < 10 Mbps [§4.2] | Not specified (volumes "around 11k seconds, 15k seconds, and 13k seconds" per VCA [§4.2]) | Not specified |
| ndt_rr-ES2 | E2 | vca ∈ {Meet, Teams, Webex} [§4.2] | 3 | 320 (Meet) / 178 (Teams) / 417 (Webex) calls [§4.2] |
| ndt_rr-ES3 | E3 | impairment condition ∈ 33 distinct one-at-a-time settings [Table A.6, deduped per G1]; vca multiplicity Not specified | 33 distinct (34 rows in Table A.6; throughput-σ=0 and latency-μ=50 both equal the all-defaults leaf — deduped per spec §4.3) | 4 calls per condition [§5.4] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> "three prevalent VCAs running over WebRTC: Google Meet, Microsoft Teams,
> and Cisco Webex" [§1]; "We conduct 2-person calls, each lasting for a
> variable duration" [§4]; "we use a virtual web camera at one of the
> endpoints streaming a predefined short video on loop and log the QoE
> metrics on the other endpoint" [§4]; "At the end of the call, we collect
> both network traces and WebRTC logs" [§4]; ground truth = "webrtc-internals
> API provided by Google Chrome" [§4; §4.1]; "The framework uses PyAutoGUI,
> a UI automation framework" [§4]; QoE metrics = video bitrate, frame rate,
> frame jitter, resolution [§2.1]. CCA, queue size/discipline, AQM, emulation
> tool, host hardware: Not specified throughout. Cross traffic: Not specified
> for ES1/ES3 (silence, §5b.2); ES2 runs on real uncontrolled access networks.

---

### ndt_rr-ES1 — in-lab NDT-trace-emulated collection (Figs 1–9, 12, A.1, A.3–A.10; Tables 2–4, A.1, A.2; train side of Tables 5/A.4/A.5)

**(i) Raw text.** "The data is collected by conducting calls between two
machines in the lab under emulated network conditions" [§4.2]. Condition
source: "the tcp-info stats dataset from the Measurement Lab's Network
Diagnostic Test (NDT)" [§4.2]; "we emulate the same sequence of RTT and
packet loss values as observed in a single test, while the throughput values
are sampled from a normal distribution with the same mean and variance as the
test throughput" [§4.2]; "We did not use the throughput samples directly as
they include throughput observed during the TCP slow-start period" [§4.2];
"Each throughput, delay, and loss value is emulated for a period of 1 second"
[§4.2]; "We only use traces with average speeds below 10 Mbps" [§4.2];
"around 11k seconds, 15k seconds, and 13k seconds of Meet, Teams, and Webex
data" [§4.2]. Emulation tool, number of calls, per-call duration, queue,
CCA: Not specified.

**(ii) Grammar v2 (informational only — set is OUT-OF-SCOPE).** The intent
would require: per-second tc schedule changes over `Static.capacity_down/up`,
`Static.latency`, and `path.loss` — driven from an exogenous NDT dataset.
v2 grammar `Regime = Static⟨capacity↓↑, latency, queue⟩` is fixed per
experiment and hashed once (spec §4.3); no scheduler changes `Static` within
a run. The throughput (= capacity) variation is a TIME-VARYING BOTTLENECK
CAPACITY sourced from exogenous NDT data → OUT-OF-SCOPE per CORPUS_PROMPT_v4
§2 rule 3. No production exists for the remainder (stochastic throughput
sample from a normal distribution, dataset-sourced Static, per-second tc
reschedule).

**(iii) Requirements v2.** None realizable in v2 vocabulary for the
regime-half: the bottleneck capacity must be constant per leaf (Regime.Static
is fixed per experiment). The workflow-half (VCA browser calls, two roles,
telemetry) would be expressible, but the load-bearing regime demand is
OUT-OF-SCOPE.

**(iv) Capability match v2.**
- **Design: OUT-OF-SCOPE.** The per-second capacity variation is a
  time-varying bottleneck capacity schedule driven from an exogenous NDT
  dataset. v2 Regime.Static is one fixed block per experiment; "the model
  does not schedule the bottleneck" (CORPUS_PROMPT_v4 §2 rule 3).
  The companion latency/loss time-variation is secondary — the bottleneck-
  capacity scheduling alone places this OUT-OF-SCOPE.
  v2 delta vs gold: gold classified this as GAP-DESIGN (spec-gap #6 time-
  varying static envelope). Under v4's explicit OUT-OF-SCOPE rule for
  time-varying bottleneck capacity, the verdict upgrades to OUT-OF-SCOPE.
- **Implementation: n/a** (CORPUS_PROMPT_v4 §1 rule 4: OUT-OF-SCOPE design
- **Mininet: M-UNSAT.** The 2-person Meet/Teams/Webex call transits the real
  VCA cloud service; emulated hosts cannot stand in for it
  (mininet-capability.md: Roles = emulated hosts only; real external services
  outside the model). The M-UNSAT verdict applies even setting aside the
  capacity-schedule issue.

**confidence: low** — the OUT-OF-SCOPE reclassification is a v4-rule
interpretation (time-varying bottleneck capacity). The workflow-half is
fully in-grammar v2; only the regime-half is out-of-scope. If the team
rules that the throughput variation is better characterized as CTP-like
`Dynamic.pressure` (replay at varying rates), this set could re-enter as
GAP-DESIGN for the schedule production. Route to Tier-2.
**interpreted:** throughput-emulation-from-NDT-trace = time-varying bottleneck
capacity (tc rate changes per second from exogenous data) → OUT-OF-SCOPE per
v4 §2 rule 3.

---

### ndt_rr-ES2 — real-world 15-household RPi collection (Fig 10a/b/c, A.2; Table A.3; test side of Tables 5/A.4/A.5)

**(i) Raw text.** "we deploy Raspberry Pi (RPi) devices in 15 households,
directly connected to the home router" [§4.2]; households "are located in a
major city, spanning different neighborhoods, ISPs, and speed tiers" [§4.2];
"The RPi collects VCA data by initiating a 15-25s call every 30 minutes to
an end point located inside a cloud network" [§4.2]; "The VCA is selected
randomly from the three VCAs" [§4.2]; "the video on the RPi is kept off
while the cloud-network end point streams a predefined video over a virtual
camera interface" [§4.2]; "Data collection spanned over a period of two weeks
and includes 320 Meet calls, 178 Teams calls, and 417 Webex calls" [§4.2].
Per-household ISP/speed tier, cloud provider/location, RPi model: Not
specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.workflow ∈
{meet, teams, webex}) = 3; 15 household vantages ride nodes/mapping, outside
identity (spec §4.3)⟩;
Experiment = ⟨Workflow(VCA call, 15–25 s [§4.2]; client role video-off, server
role streams via virtual camera [§4.2]) ⊗
Regime⟨Static⟨none imposed — inhabited (probe characterizes, spec §2)⟩;
Dynamic⟨Not specified (real household traffic on the access path; nothing
generated — inhabited collection by construction; §5b.2)⟩⟩⟩ @
Roles⟨client: household RPi node (mapping: {<connector_id>}, interface defs §8.12),
server: cloud service node (kind: service, §8.8b)⟩;
path⟨latency: inhabited (not imposed); jitter: Not specified; loss: Not specified⟩;
iterations: 320/178/417 per VCA leaf (attempted counts [§4.2]);
recurring cadence — "one call every 30 minutes" over "two weeks" [§4.2] —
no v2 production (see (iv));
telemetry{pcap: true, app_metrics: true (webrtc-internals [§4; §4.1])}.

**(iii) Requirements v2.** Inhabited-mode Regime (spec §2); 15 client nodes
with residential attrs (Nodes = Pool(attrs), spec §2) reached through a
connector (`mapping: {<node>: <connector_id>}`, interface defs §8.12); one cloud
service node with virtual-camera + browser requirements; per-VCA workflows with
`$secrets.*` prerequisites; hundreds of iterations per leaf; wall-clock launch
cadence (30-min spacing, two-week span) — v2 `iterations = int |
until(event(metric,target),min,max)` covers adaptive stopping but NOT
calendar cadence; telemetry{pcap, app_metrics}; per-call export = publish step.

**(iv) Capability match v2.**
- **Design: GAP-DESIGN (per-call experiment in-grammar; temporal cadence has
  no production).** In-grammar: inhabited is a declared Regime mode (spec §2);
  residential vantages use `mapping: {<connector_id>}` — custom connector tokens
  are first-class in v2 (interface defs §8.12); the random per-call VCA choice
  reduces to three leaves × iteration counts. Gap: "every 30 minutes for two
  weeks" has no v2 production. `iterations = int` is a bare count;
  `until(event(...))` covers adaptive stopping not wall-clock cadence.
  This gap is the same as in gold (spec-gap register: launch cadence /
  longitudinal collection).
  v2 delta vs gold: no change to verdict — cadence gap is NOT resolved by v2's
  event-triggered iterations.
  `connectivity.py:754-771` raises NotImplementedError for `remote`). Meet/Teams
  `run_teams_workflow.json` @fb4d8b6); webex has only a generation script, no
  compiled workflow artifact. No webrtc-internals channel. No cadence
  scheduler. Modules: connectors (ssh/edge-device), Core scheduler (launch
- **Mininet: M-UNSAT.** The measurand is 15 real households' access networks
  plus real VCA cloud services (mininet-capability.md M-UNSAT classes:
  "phenomena of the real Internet path", "real service endpoints",
  multi-machine physical vantage).

**confidence: high** — cadence gap and RPi-connector gap unchanged in v2.

---

### ndt_rr-ES3 — synthetic single-impairment sensitivity collection (Fig 11; Table A.6 = its configuration)

**(i) Raw text.** "we collect data under synthetic network conditions by
varying one of the following five network parameters: throughput (1500
kbps), throughput jitter (0 kbps), latency (50 ms), latency jitter (0 ms),
and packet loss (0%). The numbers in parentheses represent the default
values" [§5.4]; "loss is varied from 0% to 20% following a Bernoulli loss
model" [§5.4]; "Each combination of network conditions is repeated for four
calls" [§5.4]. Swept values [Table A.6]: throughput μ ∈ {100, 200, 500,
1000, 2000, 4000} kbps (σ=0); throughput σ ∈ {0, 100, 200, 500, 1000, 1500}
kbps (μ=1500); latency μ ∈ {50, 100, 200, 300, 400, 500} ms (σ=0); latency
σ ∈ {10, 20, 30, 40, 50, 60, 70, 80, 90, 100} ms (μ=50); loss ∈ {1, 2, 5,
10, 15, 20}% (six values). Call duration, shaped direction, emulation tool,
vca multiplicity per condition: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(one-at-a-time impairment
∈ 33 distinct conditions [Table A.6, deduped: throughput-σ=0 and
latency-μ=50 both equal all-defaults identity ⟨capacity=1500 kbps, latency=50 ms,
loss=0%⟩, spec §4.3]);
vca multiplicity Not specified⟩.

In-grammar leaves (28): conditions with fixed capacity_down/up [§5.4],
fixed latency [§5.4], path.jitter [§5.4], path.loss [§5.4], and the shared
all-defaults point:
Experiment = ⟨Workflow(VCA call; browser; shared methodology) ⊗
Regime⟨Static⟨capacity_down/up: 1.5 mbps default [§5.4] / mean-throughput axis
0.1–4 mbps (direction Not specified); latency: 50 ms default [§5.4] / mean-
latency axis 50–500 ms [Table A.6]⟩;
Dynamic⟨Not specified (silence, §5b.2)⟩⟩;
path⟨jitter: latency-σ axis 10–100 ms [Table A.6] (v2 per-workflow path field);
loss: loss axis 1–20% [§5.4] (v2 per-workflow path field, Bernoulli model)⟩⟩ @
Roles⟨client: lab node, server: lab node (streamer) — real VCA cloud on-path⟩;
iterations 4 per condition [§5.4].

OUT-OF-SCOPE leaves (5): throughput-σ ∈ {100, 200, 500, 1000, 1500} kbps
— stochastic capacity variation during a call = time-varying bottleneck
capacity (see disposition note 2). These 5 leaves not expressible in v2.

**(iii) Requirements v2.**
In-grammar leaves (28):
`Static.capacity_down/up` 0.1–4 mbps (direction Not specified) ∈ [0.1 mbps, 10 gbps]
(the 100 kbps point sits exactly at the floor) [§5.4; Table A.6];
`Static.latency` 50–500 ms ∈ [0, 2000 ms] [Table A.6];
knob range interface defs §8.2) [Table A.6];
`path.loss` 1–20% (v2 per-workflow path field; Bernoulli = netem-style random
loss, interface defs §8.1) [§5.4; Table A.6].
One-axis-at-a-time sweeps = client-side `sweeps:` expansion (spec §4).
Per-leaf iterations 4 [§5.4].

OUT-OF-SCOPE leaves (5): stochastic capacity per-call from a distribution —
no v2 production (time-varying bottleneck capacity).

**(iv) Capability match v2.**
- **Design: mixed — 28 leaves SATISFIED, 5 leaves OUT-OF-SCOPE.**
  Dedup: Table A.6 rows throughput-σ=0 and latency-μ=50 both encode the
  all-defaults identity ⟨capacity=1500 kbps, latency=50 ms, loss=0%⟩; they
  form one leaf, giving 33 unique leaves (G1 dedup, spec §4.3).
  In-grammar (28): mean-throughput (6), non-default mean-latency (5),
  shared all-defaults (1), latency-σ (10), loss (6) — all v2 path vocabulary.
  v2 delta vs gold: gold verdict was GAP-DESIGN (28/33 in-grammar, 5 throughput-σ
  leaves lacked stochastic-capacity production). Under v4's OUT-OF-SCOPE rule
  for time-varying capacity: the 5 throughput-σ leaves are OUT-OF-SCOPE
  (stochastic capacity variation = time-varying bottleneck capacity, same
  rule as ES1). The in-grammar 28 leaves are now SATISFIED in v2 (path.jitter,
  path.loss are v2 vocabulary). Set-level design verdict: SATISFIED for 28/33
  leaves, OUT-OF-SCOPE for 5/33 leaves (split named per §5b.8).
  no compiled workflow artifact at fb4d8b6; no webrtc-internals/getStats
  internals channel).
- **Mininet: M-UNSAT.** Both lab endpoints are platform machines, yet the VCA
  cloud (Meet/Teams/Webex) is on-path for every call; emulated hosts cannot
  stand in for it (mininet-capability.md M-UNSAT class: real external services
  outside the model). The envelope alone (capacity/latency/jitter/loss) would
  be declarative in Mininet via TCLink, but the real-service dependency
  settles M-UNSAT (min across axes, §5b.5).

**confidence: low** — the 5 throughput-σ leaves' reclassification from
GAP-DESIGN to OUT-OF-SCOPE rests on the same v4 interpretation as ES1.
If team rules stochastic-capacity is GAP-DESIGN (not OUT-OF-SCOPE), the
split becomes 28/33 SATISFIED + 5/33 GAP-DESIGN. Route to Tier-2 for those 5.
**interpreted:** throughput-σ = stochastic bottleneck capacity variation
during a call = time-varying bottleneck capacity → OUT-OF-SCOPE per v4 §2 rule 3.

---

