# tladder — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Figures | OUT-OF-SCOPE class | Leaves |
| --- | --- | --- | --- | --- |
| tladder-ES1 | Exp1 | Fig 2 | passive/exogenous | 4 network-speed groups × 1 collection (passive; not controlled) [§2.1] |
| tladder-ES2 | Exp2 | Fig 3 | offline-encoding | 2 videos × 3 resolutions × (CRF ∈ [20,36], step Not specified) [§2.2; Fig 3] |
| tladder-ES3 | Exp3 | Fig 4 | offline-encoding | 25,000 videos × (bitrate bucket count Not specified) [Fig 4 caption; §2.2] |
| tladder-ES4 | Exp4 | text-only | offline-algorithmic | 1 (single benchmark run) [§3.4.1] |
| tladder-ES5 | Exp5 | text-only | offline-ML | ~20 (codec, resolution, prediction-target) model tuples × 50k-video training corpus [§4] |
| tladder-ES6 | Exp6 | Tab 2 (partial) | exogenous | "several" pilot A/B runs; count Not specified [§5.1] |
| tladder-ES7 | Exp7 | Fig 7 | exogenous | 1 (TLadder vs VLadder, developed region, 0.11B DAU) [§5.1–5.2; Fig 7 caption] |
| tladder-ES8 | Exp8 | Fig 8 | exogenous | 1 (TLadder vs VLadder, developing region, 0.13B DAU) [§5.1–5.2; Fig 8 caption] |
| tladder-ES9 | Exp9 | Fig 9 | simulator | 20,000 videos × 5 systems (TLadder + 4 baselines), developed region [§5.2; Fig 9 caption] |
| tladder-ES10 | Exp10 | Fig 10 | simulator | 20,000 videos × 5 systems, developing region [§5.2; Fig 10 caption] |
| tladder-ES11 | Exp11 | Fig 11, Tab 2 | simulator | 5 systems × (parameter grid Not specified) × developed region [§5.1–5.2; Fig 11] |
| tladder-ES12 | Exp12 | Fig 12, Tab 2 | simulator | 5 systems × (parameter grid Not specified) × developing region [§5.1–5.2; Fig 12] |
| tladder-ES13 | Exp13 | Tab 3 | offline-algorithmic | 5 systems × 3 input sizes = 5 × 3 = 15 [§5.3; Tab 3] |
| tladder-ES14 | Exp14 | Fig 13 | passive/exogenous | 1 (CDF over production transcoding logs; population Not specified) [§5.3; Fig 13] |
| tladder-ES15 | Exp15 | Fig 14 | simulator | 3 variants × (parameter points swept, Not specified) [§5.4; Fig 14] |
| tladder-ES16 | Exp16 | Fig 15 | simulator | 2 rebuffering scenarios × 1 video (illustrative; provenance Not specified) [§5.5; Fig 15] |
| tladder-ES17 | Exp17 | Fig 16 | simulator | 2 ABR modes × 5 systems = 2 × 5 = 10 (assumed simulation per §5.1) [§5.4; Fig 16] |
| tladder-ES18 | Exp18 | Fig 17 | simulator | 4 noise types × (noise level axis ticks Not specified as discrete count) [§5.4; Fig 17] |

## Experiments

### tladder-ES1 — Production rebuffering-vs-bitrate measurement (Fig 2)

**(i) Raw text.** "We collected and analyzed 26 billion play sessions over a six-month period,
sampling those with average network speeds between 5–40 Mbps." [§2.1]; network-speed groups
plotted: 5, 10, 20, 40 Mbps [Fig 2 legend, "Net. Speed 5 Mbps 10 Mbps 20 Mbps 40 Mbps"];
metric: average rebuffer ratio as a function of video bitrate [Fig 2 caption]; "a rebuffering
ratio as low as 0.1% causes 1% reduction in users watch time, as observed from our metric data"
[§2.1]. Period dates, device mix, region mix: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — passive production telemetry log analysis. No Regime, Workflow,
or Roles under experimenter control; network speeds are observed user properties, not imposed
bottleneck knobs.

### tladder-ES2 — RD-curve encoding of two example videos (Fig 3)

**(i) Raw text.** Two videos: "relatively 'easy' content (video 1, an animation) ... 'hard'
content (video 2, sports footage)" [§2.2]; "Each mark in the RD curve corresponds to a CRF value
(ranging from 20 to 36 in our experiment)" [§2.2]; resolutions 540p, 720p, 1080p [Fig 3 legend:
"video1 1080p / video1 540p / video1 720p / video2 1080p / video2 540p / video2 720p"]; quality
metric VMAF [§2.2, "the Video Multi-Method Assessment Fusion (VMAF) score"]. Codec, encoder,
CRF step, hardware: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — offline video encoding study; no network, no transport, no
congestion control.

### tladder-ES3 — VMAF distribution across 25,000 videos (Fig 4)

**(i) Raw text.** Fig 4 caption: "VMAF distribution at different video bitrate bucket across a
25,000 video datasets"; §2.2: "the VMAF variance across 25,000 videos at similar bitrates is
considerable"; "the VMAF score is capped at 100" [§2.2]. Video selection method, encoding
settings per bucket: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — offline encoding corpus analysis.

### tladder-ES4 — Matrix-optimization offline performance test (text-only, §3.4.1)

**(i) Raw text.** "the overall computation can speed up by 10.3× based on our offline performance
test" [§3.4.1]; comparing naive vs matrix-form computation (Eq. 4–6 vs Eq. 8–10) [§3.4.1].
Hardware, workload, input sizes, repetitions: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — offline algorithmic benchmark; no network.

### tladder-ES5 — RD-curve prediction model training / cross-validation (text-only, §4)

**(i) Raw text.** "We construct a dataset of 50k diverse videos for training and cross validation"
[§4]; "train a gradient boosting regressor. The two prediction targets, bitrate and VMAF, are
trained in separate models" [§4]; "yielding ∼20 models" for (codec, resolution, prediction
target) tuples [§4]; input vector "encompassing a dimension of around 100" [§4]; results:
MAE "∼5% for bitrate prediction" and "a MAE of 0.75 for VMAF prediction" [§4]; "The training
occurs offline" [§4]. Training hardware, cross-validation protocol, per-codec breakdown:
Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — offline ML training / evaluation; no network.

### tladder-ES6 — Pilot A/B experiments for QoE parameter finalization (Tab 2 partial)

**(i) Raw text.** "we empirically use several pilot A/B experiments to finalize the parameter
selection to be used in Eq. 1" [§5.1]; outcome reported in Table 2: Developed Country α=2375,
β=0; Developing Country α=6000, β=0.0065 [Table 2]. Number of pilots, duration, user
populations per pilot: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — production A/B experiment on real user traffic; no
experimenter-controlled network conditions.

### tladder-ES7 — Production A/B experiment, developed region (Fig 7)

**(i) Raw text.** "two-week A/B experiments conducted in both the developed region ... and the
developing region" [§5.2]; "The developed region includes all developed countries with a daily
active users (DAU) of 0.11 billion" [§5.1; Fig 7 caption "A/B experiment on developed region
(with 0.11 billions DAU)"]; compared TLadder vs VLadder; "videos randomly and equally split
using our A/B experimentation platform" [§5.1]; cost "approximately 50,000 dollars per group per
experiment" [§5.1]; results: average QoE 85.3 → 88.3; VMAF 89.5 → 92.2; rebuffering −6.2%;
CDN cost −4% [§5.2]; "under the same ABR algorithm" [§1].

**(ii) Grammar.** OUT-OF-SCOPE — production A/B on 0.11B real users; exogenous deployment.

### tladder-ES8 — Production A/B experiment, developing region (Fig 8)

**(i) Raw text.** "all developing countries" with 0.13 billion DAU [§5.1; Fig 8 caption
"A/B experiment on developing region (with 0.13 billions DAU)"]; same two-week duration [§5.2];
QoE parameters α=6000, β=0.0065 [Table 2]; results: QoE 73.9 → 79.4 (+over 5.5 units); VMAF
87.6 → 91.1 (+3.5 units); rebuffering cut by nearly 20%; CDN cost −1% [§5.2]. All other
fields: per ES7 shared A/B methodology [§5.1].

**(ii) Grammar.** OUT-OF-SCOPE — production A/B, developing region; exogenous.

### tladder-ES9 — Trace-driven simulation, developed region (Fig 9)

**(i) Raw text.** "We utilize the simulator described in §3.3 for trace-driven simulation"
[§5.1]; "In each region, we randomly sample 20,000 videos in production and transcode the
videos with the bitrate ladders from TLadder and the four baselines" [§5.2]; "we generate the
ladders with the data on day T and then evaluate the results with the data from day T+1" [§5.1];
5 systems compared: TLadder, VLadder, ARTEMIS, Google, Brightcove [§5.1]; developed region,
0.11 billion DAU population [Fig 9 caption "Simulated experiment on developed region (with 0.11
billions DAU)"]; results: TLadder highest QoE (85.3 on average, 2.0–4.3 units gain over
baselines); VMAF 93.1 [§5.2]. QoE parameters: per Table 2 [§5.1].

**(ii) Grammar.** OUT-OF-SCOPE — trace-driven simulation using ByteDance's custom in-house
digital twin simulator fed by Apache Hive playback databases; not a controllable network
emulator.

### tladder-ES10 — Trace-driven simulation, developing region (Fig 10)

**(i) Raw text.** Developing region, 0.13 billion DAU population [Fig 10 caption "Simulated
experiment on developing region (with 0.13 billions DAU)"]; same 20,000-video sample and
day-T/T+1 protocol as ES9 [§5.2]; results: VMAF improvement over VLadder/ARTEMIS/Google ∼0.3
units; QoE boost 1.3–7.7 units [§5.2]. All other fields: per ES9.

**(ii) Grammar.** OUT-OF-SCOPE — simulator (same class as ES9; developing region).

### tladder-ES11 — Parameter-space exploration simulation, developed region (Fig 11, Tab 2)

**(i) Raw text.** "We first use offline simulation to explore the tradeoffs incurred by the
parameters as illustrated in Fig. 11 and Fig. 12" [§5.1]; "each dot is generated by a unique
parameter set for a given algorithm" [§5.2]; 5 systems: Brightcove, Google, ARTEMIS, VLadder,
TLadder [Fig 11 legend]; metrics: average VMAF (x-axis) vs normalized average rebuffer rate
(y-axis) [§5.2]; developed region [Fig 11 caption "Selection space for different algorithms in
the developed region"]. Parameter grid size, video sample, day range: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — offline parameter-space sweep via the same custom simulator.

### tladder-ES12 — Parameter-space exploration simulation, developing region (Fig 12, Tab 2)

**(i) Raw text.** Developing region [Fig 12 caption "Selection space for different algorithms in
the developing region"]; all other fields as ES11 [§5.1–5.2 covers both figures simultaneously].

**(ii) Grammar.** OUT-OF-SCOPE — offline simulation, developing region.

### tladder-ES13 — Offline computation-time benchmark (Tab 3)

**(i) Raw text.** Tab 3 caption: "Average computation time (in seconds) for a single video
laddering decision on a single-core Intel i7-13700K CPU"; 5 systems: Brightcove, ARTEMIS, Google,
VLadder, TLadder [Tab 3]; 3 input sizes: 19, 85, 405 candidate quality levels [§5.3]; timeout:
algorithms failing in 3,600 s marked '-' [Tab 3 caption]; results: TLadder 0.163 / 0.728 / 2.044
s; Brightcove 0.0158 (all sizes); VLadder 0.0023 (all sizes); ARTEMIS 2.164 (19) then '-';
Google 14.973 (19) / 148.691 (85) then '-' [Tab 3]. Repetitions, videos averaged over, OS:
Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — offline CPU benchmark; no network.

### tladder-ES14 — Online resource-usage measurement from production logs (Fig 13)

**(i) Raw text.** "based on our online transcoding logging" [§5.3]; "the x-axis represents the
ratio of TLadder's processing cost to the full transcoding cost; the y-axis indicates the
percentage of videos" [§5.3]; result: "most cases (80th percentile) fall below 0.2% of the
transcoding cost" [§5.3]. Video population size, logging period: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — passive production logging analysis; no controllable network
or workload.

### tladder-ES15 — Rebuffer/bitrate penalty ablation simulation (Fig 14)

**(i) Raw text.** "To isolate each penalty's effect, we examine two alternatives that exclude
one penalty at a time" [§5.4]; 3 variants: TLadder; "No rebuffer" (ignores rebuffering costs);
"No bitrate" (ignores bitrate penalties) [§5.4]; "Fig. 14 plots the resulting QoE values against
the simulated average playback bitrate for each approach; different points on each curve are
generated by varying parameters" [§5.4]. Region, video sample, parameter grid: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — ablation via the same custom digital twin simulator.

### tladder-ES16 — Case study: ladders under high vs low rebuffering (Fig 15)

**(i) Raw text.** "Fig. 15 presents a case study illustrating how rebuffering influences
TLadder's decisions. ... We plot TLadder-produced ladders in both high (TLadder-high) and low
(TLadder-low) rebuffering scenarios, alongside the reference ladder from VLadder" [§5.5];
x-axis bitrate per quality level, y-axis VMAF; each curve is a distinct bitrate ladder [§5.5].
Video identity, region, scenario construction, provenance (simulation vs other): Not specified
(flagged in rendering as ambiguous).

**(ii) Grammar.** OUT-OF-SCOPE — illustrative case study (no controlled network, regardless of
whether generated by the simulator or by offline ladder optimization).

### tladder-ES17 — ABR-mode adaptation comparison (Fig 16)

**(i) Raw text.** "Fig. 16 compares multiple approaches under two ABR modes: Conservative and
Aggressive" [§5.4]; 5 systems: Brightcove, Google, ARTEMIS, VLadder, TLadder [Fig 16 legend];
metrics: QoE, VMAF, Rebuffer, Normalized CDN Cost [Fig 16 panels]; finding: "TLadder achieves
the highest QoE in both settings" [§5.4]. Evaluation method not explicitly stated for this
figure; rendering flags assumption: trace-driven simulation per §5.1 two-method constraint
(A/B or simulation; non-deployed baselines exist only as authors' own implementations compared
via simulation) [§5.1].

**(ii) Grammar.** OUT-OF-SCOPE — assumed trace-driven simulation (custom digital twin); exogenous
if A/B.

### tladder-ES18 — Robustness to prediction noise (Fig 17)

**(i) Raw text.** "we inject noises into four ground-truth metrics: bitrate, VMAF, network speed,
and rebuffering. Fig. 17 shows the impact of each error type" [§5.4]; Fig 17 subfigures a–d;
noise axes: Bitrate Noise Variance 0–20% [Fig 17(a)]; VMAF Noise Variance 0–4 [Fig 17(b)];
Network Noise Variance 0–2% [Fig 17(c)]; Rebuffer Noise Variance 0–6% [Fig 17(d)]; "The dashed
lines mark typical online error levels" [Fig 17 caption]; baseline: VLadder [§5.4]; results:
average QoE lost 0.065 / 0.178 / 0.038 / 0.0008 [§5.4]. Region, video sample, noise
distribution family, repetitions: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — noise injection into the simulator's input data; not a network
experiment (noise is added to the simulator's ground-truth data tables, not to packet-level
network conditions).
