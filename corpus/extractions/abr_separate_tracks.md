# abr_separate_tracks — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| abr_sep-ES1 | Exp1 (Fig 2a) | 1 (ExoPlayer DASH, 900 Kbps, low-audio B-set) [§3.2] | 1 | 1 |
| abr_sep-ES2 | Exp2 (Fig 2b) | 1 (ExoPlayer DASH, high-audio C-set) [§3.2] | 1 | 1 |
| abr_sep-ES3 | Exp3 (Fig 3) | 1 (ExoPlayer HLS, Hsub, avg 600 Kbps time-varying) [§3.2] | 1 | 1 |
| abr_sep-ES4 | Exp4 (text-only) | 1 (ExoPlayer HLS, A1-first manifest, 5 Mbps fixed) [§3.2] | 1 | 1 |
| abr_sep-ES5 | Exp5 (Fig 4a) | 1 (Shaka Player HLS, Hall, 1 Mbps constant) [§3.3] | 1 | 1 |
| abr_sep-ES6 | Exp6 (Fig 4b) | 1 (Shaka Player HLS, Hall, avg 600 Kbps dynamic) [§3.3] | 1 | 1 |
| abr_sep-ES7 | Exp7 (Fig 5) | 1 (dash.js DASH, 700 Kbps fixed) [§3.4] | 1 | 1 |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> HTTP server as origin; single server–client path; tc at the server for bandwidth
> control [§3.1, "The network bandwidths from the server to client are controlled by
> using tc [15] at the server"]; content: drama show ~5 minutes, 6 video tracks + 3
> audio tracks from YouTube (youtube-dl) [§3.1]; tracks in Table 1; Bento4 for
> DASH/HLS manifests [§3.1]; players: ExoPlayer v2.10.2, Shaka Player v2.5.1,
> dash.js v2.9.3 [§2.4]; transport/RTT/queue/loss/CCA/cross-traffic: Not specified;
> client hardware/OS: Not specified; run duration: Not specified (content ~5 min [§3.1],
> figure x-axes labeled to 300 s).

---


## Experiments

### abr_sep-ES1 — ExoPlayer DASH, low-bitrate audio B-set (Fig 2a)

**(i) Raw text.** "The network bandwidth is fixed at 900 Kbps" [§3.2]; ExoPlayer
v2.10.2, DASH [Fig 2 caption "ExoPlayer results (DASH)"]; audio tracks B1, B2, B3 at
32, 64, 128 Kbps [§3.2]; video tracks per Table 1; ExoPlayer "conservatively assumes
that the actual network bandwidth is 75% of the estimated bandwidth" [§3.2]; result:
V3+B2 selected despite V3+B3 being better [§3.2].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(browser-like
ABR client; ExoPlayer v2.10.2; DASH; params.manifest: audio B-set, video Table-1)
⊗ Regime⟨Static: capacity_down 900 Kbps [§3.2], queue: Not specified; Dynamic: Not
specified⟩⟩ @ Roles⟨client: testbed node (ExoPlayer), server: local HTTP origin⟩;
path.latency: Not specified; cca: Not specified; iterations: 1; telemetry {app_metrics:
true (bitrate selection time series [Fig 2a])}.

### abr_sep-ES2 — ExoPlayer DASH, high-bitrate audio C-set (Fig 2b)

**(i) Raw text.** ExoPlayer v2.10.2, DASH [§3.2]; audio tracks C1, C2, C3 at 196, 384,
768 Kbps [§3.2]; video tracks per Table 1; network bandwidth: Not specified for Exp2
[§3.2 states 900 Kbps for Exp1 only; Fig 2(b) curve not stated in text]; result: V2+C2
selected [§3.2].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; INHERITED from ES1, delta: audio adaptation
set = C1/C2/C3 at 196/384/768 Kbps [§3.2]; capacity_down: Not specified (Exp2 bandwidth
not stated in text per §5b C5 rule); iterations: 1; telemetry {app_metrics: true
(bitrate selection time series [Fig 2b])}.

### abr_sep-ES3 — ExoPlayer HLS, Hsub, time-varying 600 Kbps average (Fig 3)

**(i) Raw text.** ExoPlayer v2.10.2, HLS [Fig 3 caption "ExoPlayer results (HLS)"];
manifest Hsub (6 combinations); "set to be time-varying, with the average as 600 Kbps"
[§3.2]; A3 (highest-bitrate audio) first in Hsub manifest; result: A3 selected
throughout, 5 stall events, "36.9 seconds of rebuffering" [§3.2].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(browser-like;
ExoPlayer v2.10.2; HLS; params.manifest = Hsub) ⊗ Regime⟨Static: capacity_down
Not specified (average 600 Kbps [§3.2] but the time-varying profile is not a single
static value); Dynamic: pressure = replay(ctp, time-varying bandwidth profile with
average 600 Kbps [§3.2]) — the bandwidth varies in time⟩⟩ @ Roles⟨client: testbed,
server: local HTTP origin⟩; path.latency: Not specified; cca: Not specified;
iterations: 1; telemetry {app_metrics: true (bitrate, buffer [Fig 3 panels],
rebuffering 36.9s [§3.2])}.

### abr_sep-ES4 — ExoPlayer HLS, A1-first manifest, 5 Mbps (text-only)

**(i) Raw text.** "we modify the manifest file so that A1 (the lowest quality audio
track) is listed as the first audio track" [§3.2]; "fix the network bandwidth to 5
Mbps" [§3.2]; ExoPlayer selects A1 throughout despite "plenty of available network
bandwidth" [§3.2]; figures omitted [§3.2].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(ExoPlayer v2.10.2;
HLS; params.manifest = modified HLS with A1 first) ⊗ Regime⟨Static: capacity_down
5 Mbps [§3.2], queue: Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨client: testbed,
server: local HTTP origin⟩; path.latency: Not specified; cca: Not specified;
iterations: 1; telemetry {app_metrics: true (bitrate selection outcome, text-only)}.

### abr_sep-ES5 — Shaka Player HLS, Hall, 1 Mbps constant (Fig 4a)

**(i) Raw text.** Shaka Player v2.5.1 [§2.4], HLS [Fig 4 caption "Shaka Player results
(HLS)"]; manifest Hall (all 18 combinations) [§3.3, "two experiments with the HLS
manifest file Hall"]; "the network bandwidth is set to a constant 1 Mbps" [§3.3]; Shaka
estimated constant 500 Kbps; V2+A2 (460 Kbps aggregate peak) selected [§3.3].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(browser ABR;
Shaka v2.5.1; HLS; params.manifest = Hall) ⊗ Regime⟨Static: capacity_down 1 Mbps
[§3.3], queue: Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨client: testbed,
server: local HTTP origin⟩; path.latency: Not specified; cca: Not specified;
iterations: 1; telemetry {app_metrics: true (bitrate selection, bandwidth estimate
500 Kbps [§3.3])}.

### abr_sep-ES6 — Shaka Player HLS, Hall, dynamic 600 Kbps average (Fig 4b)

**(i) Raw text.** Shaka Player v2.5.1, HLS, Hall manifest [§3.3]; "the specified
network bandwidth is dynamic (with the average as 600 Kbps, see Fig. 4(b))" [§3.3];
result: initial underestimation, then overestimation "starting around 50 s"; tracks
V2+A2 then V3+A3; "leading to a total rebuffering of 39 s" [§3.3].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; INHERITED from ES5, delta: capacity_down:
Not specified (time-varying; average 600 Kbps [§3.3]); Dynamic: pressure = replay(ctp,
time-varying profile avg 600 Kbps [§3.3]) [same dynamic model as ES3]; telemetry
{app_metrics: true (rebuffering 39 s [§3.3], bitrate time series [Fig 4b])}.

### abr_sep-ES7 — dash.js DASH, 700 Kbps fixed (Fig 5)

**(i) Raw text.** dash.js v2.9.3 [§2.4], DASH [Fig 5 caption "dash.js results (DASH)"];
"a fixed network bandwidth of 700 Kbps" [§3.4]; DASH manifest (6 video + 3 audio
in two Adaptation Sets) [§3.1]; DYNAMIC ABR algorithm (THROUGHPUT/BOLA switching at
12s/6s buffer thresholds) [§3.4]; result: V2+A3, V2+A2, V2+A3, V3+A3 selected;
buffer levels unbalanced [§3.4; Fig 5b].

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(browser ABR;
dash.js v2.9.3; DASH; params.manifest: main DASH manifest) ⊗ Regime⟨Static:
capacity_down 700 Kbps [§3.4], queue: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: testbed (dash.js), server: local HTTP origin⟩; path.latency: Not
specified; cca: Not specified; iterations: 1; telemetry {app_metrics: true (bitrate
selection, buffer levels [Fig 5 panels])}.
