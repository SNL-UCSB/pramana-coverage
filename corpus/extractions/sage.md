# sage — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| sage-ES1 | E1 | scheme ∈ 7 [Fig 1] × env ∈ Set I ∪ Set II | Not specified (7 × "more than 1000" [§5]; per-set sampling unstated) | Not specified |
| sage-ES2 | E2 | checkpoint ∈ daily snapshots over one week × env ∈ all Set I+II [§5.2] | Not specified (≈7 × env family) | Not specified |
| sage-ES3 | E3 **[OOS]** | scheme ∈ Fig 8a/b legends × src-dst pair ∈ 16-US-city GENI ∪ 13-server AWS [§6.1; App G] | Not specified | 5 [App G] |
| sage-ES4 | E4 | trace ∈ 23 cellular [§6.1] × scheme ∈ Fig 8c legend | Not specified (23 × legend set) | 5 [§6.1] |
| sage-ES5 | E5 | scheme ∈ 14 (Sage + 13 ML-based [§6.2]) × env ∈ Set I+II | Not specified | Not specified |
| sage-ES6 | E6 | scheme ∈ 7 (Sage + 6 delay-based [§6.3]) × env ∈ Set I+II | Not specified | Not specified |
| sage-ES7 | E7 | scheme ∈ {Sage, Vegas, BC} [§7.1] × env = 1 (step 24→96 Mbps) | 3 | Not specified |
| sage-ES8 | E8 | model ∈ 6 ablated variants [§7.3] × env ∈ Set I+II | Not specified | Not specified |
| sage-ES9 | E9 | env ∈ 8 [§7.2] × scheme ∈ 14 (Sage + 13 pool [Fig 13]) | 8 × 14 = 112 | Not specified |
| sage-ES10 | E10 | model ∈ {Sage-s, Sage-m, Sage-l} [§7.4] × env ∈ Set I+II | Not specified | Not specified |
| sage-ES11 | E11 | model ∈ {Sage-Top, Sage-Top4} [§7.5] × env ∈ Set I+II | Not specified | Not specified |
| sage-ES12 | E12 | scenario ∈ 3 (step up, step down, +Cubic) [§7.6] | 3 | Not specified |
| sage-ES13 | E13 **[OOS]** | scheme ∈ 10 × 1 random GENI path [§7.7] | 10 | 3 [§7.7] |
| sage-ES14 | E14 | scheme ∈ 5 × competitor-count ∈ {3,7} [§7.7] | 5 × 2 = 10 | Not specified |
| sage-ES15 | E15 | scheme ∈ 14 × env ∈ 2 (shallow/deep buffer) [App E.1] | 14 × 2 = 28 | Not specified |
| sage-ES16 | E16 | queue.qdisc ∈ 5 AQMs [App E.2] × scheme ∈ Fig 23 legend | Not specified | 5 [App E.2] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Emulator: "We use an improved/debugged version of Mahimahi" [§5 fn 5];
> "no other parts are simulated or emulated … generating, sending, and
> receiving real packets" via Kernel code and APIs [§4.1]. Controlled knobs:
> "link capacity, minimum end-to-end delay, bottleneck link buffer size, and
> the existence/non-existence of competing Cubic flows" [§4.1]. Deployment:
> TCP Pure kernel module + user-space policy [§3]. Pool CCAs: "13 available
> Internet CC schemes: Westwood, Cubic, Vegas, YeAH, BBR2, NewReno, Illinois,
> Veno, HighSpeed, CDG, HTCP, BIC, and Hybla" [§5]. Scale: "more than 1000
> different environments" [§5].
>
> Set I flat: BW/minRTT/qs ∈ [12,192] Mbps, [10,160] ms, [½,16]×BDP [App C.1].
> Set I step: BW changes to m×BW1, m ∈ {0.25,0.5,2,4} "under 200Mbps" [App C.1].
> Set II: qs ∈ [1,16]×BDP; one competing Cubic flow enters earlier; 120 s
> [App C.2]; BW/minRTT similar to Set I [App C.2]. Scoring: winner ∈
> [0.9,1]×top-score, α=2 default [§5.1]. AQM: Not specified everywhere except
> ES16. Repetitions: stated for §6.1 (5 ×), §7.7 fairness (3 ×), App E.2 AQM
> (5 ×); elsewhere Not specified.

**Shared grammar template ("Set I+II campaign") — v2 update — argued once,
inherited by ES1/ES2/ES5/ES6/ES8/ES10/ES11.**

**Grammar shorthands (NOT A5 fields; defined once for all inheriting blocks):**
- "scheme" abbreviates ⟨static.cca ∈ kernel-enum | application.workflow = CLI(app, role)▸NFA⟩
- "env" abbreviates the three leaf families' ⟨static.capacity_down, static.latency, static.queue.args, dynamic.mode⟩ block

**v2 three leaf families per campaign:**
- **Set I flat leaves:** Static⟨capacity_down ∈ [12,192] mbps, latency ∈
  [10,160] ms, queue: size ∈ [½,16]×BDP (discipline Not specified =
  default-with-echo)⟩; Dynamic: none (single-flow positive statement [App C.1]).
  v2 verdict: **SATISFIED** (all dims are A5; queue from queue.args; dynamic
  silence from [App C.1] §5b.9 precedent).
- **Set I step leaves:** Static capacity CHANGES mid-experiment (BW1 → m×BW1
  [App C.1]). v2 verdict: **OUT-OF-SCOPE** (CORPUS_PROMPT_v4 §2: time-varying
  bottleneck capacity → OOS; impl → n/a for these leaves).
- **Set II leaves:** Static (qs ∈ [1,16]×BDP); Dynamic: mode load, one Cubic
  flow entering earlier (Cubic-first is workflow-internal timing, §5b.10);
  120 s [App C.2]. v2 verdict: **SATISFIED** (static flat + load-mode in
  grammar; Cubic-first timing is workflow staging, not a grammar hole).

**v2 shared design analysis (replaces v1 "step = GAP-DESIGN" paragraph):**
Flat + Set II leaf families: SATISFIED. Step leaf family: OUT-OF-SCOPE.
BBR2: Design SATISFIED in v2 via `cca⟨algo:bbr,version:v2alpha,build:non-mainline⟩`
Sets with BOTH families → design verdict is SPLIT: "SATISFIED (flat+Set II) +
OUT-OF-SCOPE (step)". Sets that are ALL step → "OUT-OF-SCOPE".

**v2 shared implementation analysis (unchanged from v1 grounding, venue
GAPS (unchanged): (a) no time-varying-envelope mode (step family OOS →
impl n/a for those leaves; flat/Set II leaves — step driver not needed);
(c) no Sage/non-kernel-scheme runtimes packaged; (d) bbr2 kernel-build absent.

Step leaves need hand-scripted mid-run tc changes (TCLink is static per
mininet-capability.md); BBR2 needs custom shared kernel; telemetry manual;
campaign driver hand-scripted. Flat envelope is declarative (M-SAT axis), but

in that pin.

---


## Experiments

### sage-ES1 — motivation: winning rates of heuristics (Fig 1)

**(i) Raw text.** "Fig. 1 shows the percentage of times that a scheme's
performance is either the best or at most 10% less than the best-performing
scheme" [§1]; "following the setup described in more detail in section 5" [§1];
schemes: Vegas, YeAH, Copa, BBR2, Cubic, HTCP, BIC (Set I panel) and Cubic,
HTCP, BIC, BBR2, Copa, YeAH, Vegas (Set II panel) [Fig 1]. Per-scenario
BW/RTT/queue values, run counts: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scheme ∈ 7 × env ∈ Set I ∪
Set II) = Not specified⟩; per the §2 template — all three leaf families:
flat (SATISFIED), step (OUT-OF-SCOPE), Set II (SATISFIED). BBR2 as structured
cca (v2: design-SAT); Copa as program workflow (CLI, spec §2).

### sage-ES2 — 7-day checkpoint rollouts (Fig 7)

**(i) Raw text.** "after every roughly 24 hours of training, we record the
gained model and collect its performance over all network environments used in
Set I and Set II" [§5.2]; Fig 7 shows checkpoint progression [§5.2]. Training
is analysis-side (boundary note). Repetitions, per-env duration: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈
{sage_day1@sha … sage_day7@sha}, count Not specified (≈7) × env ∈ all Set I+II)
= Not specified⟩ per the §2 template; each checkpoint is a distinct workflow
pin (model sweep = pin sweep, spec §4.3 identity includes workflow_sha); all
three leaf families.

### sage-ES3 — intra-/inter-continental live-Internet (Fig 8a,b; Fig 26 a–f) [OUT OF SCOPE]

**(i) Raw text.** "employed different servers around the US continent (16
different cities) and 13 different servers around the globe" [§6.1]; "sent
traffic over the Internet among these servers"; GENI + AWS + own servers [App G];
10-second flows; five trials per pair [App G]; RTTs 7–237 ms [§6.1]. Fig 26
(a–f) = sample views of the same collection [App H].

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scheme × src-dst pair ∈
GENI-16-city ∪ AWS-13)⟩; Regime: inhabited (real Internet paths); Roles: client
AND server on remote T3 infrastructure; iterations 5 [App G].

### sage-ES4 — highly-variable emulated cellular links (Fig 8c; Fig 26 g–i)

**(i) Raw text.** "emulated 23 cellular traces … and sent traffic using different
schemes" [§6.1]; "repeat the tests five times" [§6.1]; sample links: "Walking in
Times Square", "Riding Bus on 6th Avenue", "Stationary Pos. in Times Sq." [Fig
26 g–i]; metrics: normalized delay + throughput [§6.1]. Per-trace
BW/RTT/queue: governed by traces (Not specified).

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(trace ∈ 23 [§6.1] × scheme ∈
Fig 8c legend, Not specified)⟩; Experiment = ⟨Workflow(bulk sender per scheme) ⊗
Regime⟨Static: capacity = TRACE-DRIVEN time-varying capacity schedule (Mahimahi
cellular trace replay) → OUT-OF-SCOPE; latency/queue Not specified⟩⟩;
iterations 5.

### sage-ES5 — league of ML-based schemes (Fig 9; reuses: Fig 20, Fig 24, Table 3)

**(i) Raw text.** "compare sage with a league of ML-based CC schemes including
13 ML-based counterparts" [§6.2]; Sage, Orca, Indigo, DeepCC, Genet, Indigov2,
Vivace, BC-top3, Orcav2, BCv2, Aurora, OnlineRL, BC-top, BC [Fig 9]. Models
built from analysis (BC/OnlineRL/Orcav2/Indigov2 training is analysis-side,
boundary note). Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈ 14
(all non-kernel CLI programs per §2 workflow note) × env ∈ Set I+II) = Not
specified⟩ per the §2 template; all three leaf families.

### sage-ES6 — league of delay-based schemes (Fig 10; reuses: Fig 21, Fig 25, Table 2)

**(i) Raw text.** "compare performance of Sage with the league of delay-based
schemes: BBR2, Copa, C2TCP, LEDBAT, Vegas, and Sprout" [§6.3]; reuses of the
same Set I+II campaign. Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scheme ∈ 7 × env ∈ Set I+II) =
Not specified⟩ per the §2 template; scheme axis: Sage (program workflow) + Vegas
(static.cca) + BBR2 (structured cca: `cca⟨algo:bbr,version:v2alpha⟩`) + Copa,
C2TCP, LEDBAT, Sprout (program workflows).

### sage-ES7 — distributional-shift rollouts (Fig 11)

**(i) Raw text.** "an arbitrary environment from the pool (a step scenario where
the BW changes from 24Mbps to 96Mbps)" [§7.1]; "rollout Sage … for 30 seconds"
[§7.1]; Vegas and BC also run "under the same setting" [§7.1]. minRTT, queue,
repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scheme ∈ {Sage, Vegas, BC}) = 3⟩;
all 3 leaves: Regime⟨Static: capacity STEP 24→96 mbps [§7.1]; → OUT-OF-SCOPE⟩.
Dynamic: none (single-flow rollout, positive statement [§7.1]).

### sage-ES8 — ablation-model evaluation (Fig 12)

**(i) Raw text.** "retrain 6 more models under the same 7-day training regime and
report their performance" [§7.3]; ablations: no-Min/Max, no-rrtVar, no-Loss/Inf
(input ablations) + no-GRU, no-Encoder, no-GMM (architecture ablations) [§7.3];
metric = winning rates, Set I + Set II [Fig 12]. Retraining is analysis-side;
collection = 6 variants' evaluation rollouts. Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈ 6
ablated-model pins@sha × env ∈ Set I+II) = Not specified⟩ per the §2 template;
all three leaf families; each variant is a distinct workflow pin (§2 workflow note).

### sage-ES9 — (dis)similarity trajectory collection (Fig 13)

**(i) Raw text.** "choose eight different environments and send traffic using
different CC schemes and gather trajectories … (st, at, st+1) vectors" [§7.2];
"eight random env. (each row represents an env.)" [Fig 13]; the 13 pool schemes
as columns [Fig 13]; Similarity Index = averaged cosine similarity [§7.2] —
similarity computation is analysis. Environment parameters, duration, repetitions:
Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(env ∈ 8 × scheme ∈ 14 (Sage +
13 pool)) = 8 × 14 = 112⟩; Experiment = ⟨Workflow(bulk sender, GR-instrumented)
⊗ Regime⟨Static: 8 unstated environments, values Not specified; Dynamic: Not
specified (silence — no stated Set I/II classification)⟩⟩; iterations Not
specified; telemetry {app_metrics: true (trajectory vectors)}.

### sage-ES10 — input-granularity models Sage-s/m/l (Fig 14; reuse: Fig 16)

**(i) Raw text.** "vary the granularity of calculating input statistics and
reconstruct three pools … Sage-s, Sage-m, Sage-l" [§7.4]; compared with Sage
by winning rate in Set I + Set II [Fig 14]; t-SNE view in Fig 16 [§7.4] (gold
merge, same study). Pool reconstruction = re-processing per gold. Repetitions:
Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈
{sage_s, sage_m, sage_l}@sha × env ∈ Set I+II) = Not specified⟩ per the §2
template; all three leaf families.

### sage-ES11 — pool-diversity models Sage-Top/Sage-Top4 (Fig 15)

**(i) Raw text.** "retrain Sage with a couple of alternative pools: Sage-Top
(Vegas + Cubic only) and Sage-Top4 ({Vegas,BBR2,YeAH,Illinois} + {Cubic,HTCP,
BIC,Highspeed})" [§7.5]; metric = winning rates vs Sage [Fig 15]; Set I + Set II
[§7.5]. Pool sub-selection is analysis-side. Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(application.workflow ∈
{sage_top, sage_top4}@sha × env ∈ Set I+II) = Not specified⟩ per the §2 template.

### sage-ES12 — three sample scenarios, dynamics deep-dive (Fig 17)

**(i) Raw text.** Scenarios: 1) "link capacity suddenly doubles (24Mbps to 48Mbps)"
[§7.6]; 2) "link capacity suddenly halves (48Mbps to 24Mbps)" [§7.6]; 3) "in the
presence of a Cubic flow (24Mbps link)" [§7.6]; "minimum delay of 20ms and
bottleneck buffer size of 450KBytes (=300pkts)" [§7.6]; plotted: Sage's rate,
one-way delay, cwnd, and (scenarios 3–4) the Cubic flow's throughput [Fig 17].
Duration: Not specified (time axes ≈55 s / ≈100 s from Fig 17). Repetitions:
Not specified.

**(ii) Grammar (v2).**
- Leaf 1: Static step 24→48 mbps [§7.6]; latency 20 ms; queue 450 KB (300 pkts);
  Dynamic: none; → OUT-OF-SCOPE (capacity-change).
- Leaf 2: Static step 48→24 mbps [§7.6]; latency 20 ms; queue 450 KB;
  Dynamic: none; → OUT-OF-SCOPE.
- Leaf 3: Static flat 24 mbps [§7.6]; latency 20 ms; queue 450 KB; Dynamic:
  mode load — one Cubic flow (Foreground = {Workflow_sage @ client_0,
  Workflow_cubic @ client_1}, both Foreground because BOTH are measured [§7.6,
  Fig 17 row 3/4 plots both flows' throughputs]). → SATISFIED in v2 (n-party
  Foreground resolves spec-gap #7).

### sage-ES13 — GENI fairness (Fig 18; reuse: Fig 27) [OUT OF SCOPE]

**(i) Raw text.** "send traffic from our server to a randomly selected remote
server on GENI. Then, every 25 seconds, we add another flow … measure the
throughput of each flow over a 2-minute period. We repeat all the runs three
times" [§7.7]; Fig 27 extends the fairness campaign to other schemes [App I].
Bandwidth/RTT/queue: real path, Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scheme ∈ 10) = 10⟩; Regime:
inhabited (real GENI path); Roles: client = authors' server, server = random
remote GENI node (T3); iterations 3 [§7.7]; staged-arrival multi-flow = workflow-
internal states (§5b.10).

### sage-ES14 — many-Cubic TCP-friendliness, emulated (Fig 19; reuse: Fig 28)

**(i) Raw text.** "emulate a 48Mbps, 40ms mRTT, and BDP buffer size bottleneck,
share it between a Sage flow and three (and in another case, seven) more Cubic
flows, and measure the throughput of *each individual flow* over a 2-minute
period" [§7.7]; Fig 28 extends to {Aurora, Indigo, Sage, BBR2, Cubic} × {7
Cubic, 3 Cubic} [Fig 28 caption]. Repetitions: Not specified.

**(ii) Grammar (v2).**
**v2 key re-classification:** In v1, the N Cubic flows were classified as
`dynamic.mode load` (pressure flows). But in v2, the measurand explicitly
includes each Cubic flow's individual throughput [§7.7 "each individual flow"].
Flows whose outcomes ARE the result are not "load" — they are Foreground entries.
Per v2 grammar: Foreground = {scheme_flow@client_0, cubic_flow_1@client_1, ...,
cubic_flow_N@client_N} (n-party).

ExperimentSet⟨leaves: sweep(scheme ∈ 5 [Fig 28 caption: Aurora, Indigo, Sage,
BBR2, Cubic] × competitor-count ∈ {3,7} [§7.7]) = 5 × 2 = 10⟩; Experiment =
⟨Foreground = {Workflow_scheme @ client_0, Workflow_cubic_bulk × N @ client_1..N}
⊗ Regime⟨Static: capacity_down 48 mbps [§7.7], latency 40 ms [§7.7],
queue size 1×BDP [§7.7], discipline Not specified; Dynamic: Not specified
(no external load beyond the Foreground flows themselves)⟩⟩; params.duration
2 min [§7.7]; Roles⟨N+1 clients, server⟩; iterations Not specified; telemetry
{app_metrics: true (per-Foreground-flow throughput time series)}.

### sage-ES15 — performance frontier vs 13 heuristics (Fig 22)

**(i) Raw text.** "compare Sage to thirteen heuristics … in two network
environments where the link capacities are *constant*, one with a shallow buffer
and the other with a deep buffer" [App E.1]; throughput-vs-delay scatter [Fig 22].
Exact BW/RTT/buffer values: Not specified. Repetitions: Not specified.

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(scheme ∈ 14 (Sage + 13 pool
[App E.1; §5]) × env ∈ 2) = 28⟩; Regime⟨Static: capacity constant [App E.1],
values Not specified; queue: shallow vs deep, values Not specified, discipline
Not specified; Dynamic: Not specified (silence)⟩; iterations Not specified;
telemetry {app_metrics: true (avg throughput + delay)}.

### sage-ES16 — AQM-impact study (Fig 23)

**(i) Raw text.** "48Mbps, 20ms minimum RTT, and 240KB buffer … HDrop, TDrop,
PIE, BoDe, and CoDel as AQM schemes … different CC schemes … run for a minute.
Five times. Average throughput and delay." [App E.2]. Scheme legend: figure data
(count Not specified).

**(ii) Grammar (v2).** ExperimentSet⟨leaves: sweep(static.queue.qdisc ∈ {HDrop,
TDrop, PIE, BoDe, CoDel} × scheme ∈ Not specified)⟩; Regime⟨Static: capacity
48 mbps [App E.2], latency 20 ms [App E.2], queue size 240 KB [App E.2], qdisc
swept; Dynamic: Not specified (silence)⟩; duration 60 s [App E.2]; iterations 5;
telemetry {app_metrics: true (avg throughput + delay)}.

## Tier-1 gate (pipeline/corpus/gate_tier1.py)

**Result:** 2 flags → route to Tier-2. Both are false positives.
