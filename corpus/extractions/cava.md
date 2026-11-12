# cava — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| cava-ES1 | Exp1 (Fig 2) | codec ∈ {H.264, H.265} × video ∈ {ED, BBB, ToS, Sintel} [§2] | 2 × 4 = 8 | Not specified |
| cava-ES2 | Exp2 (Fig 1, Fig 3) | video ∈ {ED, BBB, ToS, Sintel} + 4 additional YouTube videos [§2] | 8 (4 uploaded + 4 downloaded) | Not specified |
| cava-ES3 | Exp3 (text-only, §6.1) | 1 coast-to-coast LTE drive = 200 traces [§6.1] | 200 traces (each ≥18 min [§6.1]) | 1 per trace |
| cava-ES4 | Exp4 (Fig4, Fig7–10, Tab1) | video ∈ 16 × scheme ∈ 7 × trace_set ∈ {LTE 200, FCC 200} × sweep_dim (W, W', codec, cap, err) [§6.1–6.7] | Not specified (compound: 16 videos × 400+ traces × 7 schemes; per-sub-analysis leaf count Not specified) | 1 per (video, trace, scheme) [§6.2 implied] |
| cava-ES5 | Exp5 (Fig11, Tab2) | video ∈ {BBB, ED, Sports, ToS}[Tab2] × scheme ∈ {CAVA, BOLA-E-peak, BOLA-E-avg, BOLA-E-seg}[§6.8] × trace ∈ LTE [§6.8; Fig11 caption] | Not specified (200 LTE traces per video-scheme pair; run count not restated in §6.8) | Not specified |

## Shared methodology — testbed (Exp5 only) (quoted from the paper)


> Two computers (Ubuntu 12.04 LTS, CPU Intel Core 2 Duo, memory 4 GB) with a 100 Mbps
> direct connection [§6.8]; Apache httpd server [§6.8]; Google Chrome via Selenium [32]
> [§6.8]; tc for LTE trace replay [§6.8, "replaying the network traces of §6.1"]; dash.js
> version v2.7.0 with CAVA as CAVARule.js (520 LoC) [§5.5]; BOLA-E baselines in same
> dash.js version [§6.8]; 5-chunk harmonic mean bandwidth estimator [§5.5]; startup
> latency / max buffer: Not specified (§6.1 values 10 s / 100 s assumed); 4 YouTube
> videos: BBB, ED, Sports, ToS [Tab 2]; chunk duration ~5 s [§2]; runtime overhead
> ~56 ms for 10-minute video [§6.8].

---


## Experiments

### cava-ES1 — FFmpeg VBR encoding characterization (Fig 2)

**(i) Raw text.** "FFmpeg [13]" encoder [§2]; 4 raw Xiph videos (Elephant Dream, Big Buck
Bunny, Tears of Steel, Sintel) [§2]; "4 H.264 and 4 H.265 videos (8 encoded videos in
total)" [§2]; "six tracks/levels, resolutions 144p, 240p, 360p, 480p, 720p, and 1080p"
[§2]; "CRF value of 25" [§2]; "Each video is around 10 minutes" [§2]; "segmented into
2-sec chunks after encoding" [§2]; "2× capped (peak limited to 200% of average)" [§2];
coefficient of variation 0.3 to 0.6 [§2]; max bitrate 1.4× to 2.4× the average [§2];
H.264: 78% of Q4 chunks have SI/TI > 25/7 vs 11% of Q1 [§3.1.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(codec ∈ {H.264, H.265}[§2] × video ∈
{ED, BBB, ToS, Sintel}[§2]) = 2 × 4 = 8⟩; Experiment = ⟨Workflow(offline FFmpeg
encoding; params: CRF 25, 2× cap, 6 tracks) ⊗ Regime: Not applicable (no network;
offline processing)⟩; iterations: Not specified; telemetry {app_metrics: true
(chunk size, VMAF, SI/TI per quartile [§3.1])}.

### cava-ES2 — YouTube VBR encoding characterization (Fig 1, Fig 3)

**(i) Raw text.** Uploaded 4 raw videos to YouTube and "downloaded the encoded videos
using youtube-dl [48]"; additionally downloaded 4 more YouTube videos [§2]; "All YouTube
videos are encoded using H.264 codec" [§2]; bottom six tracks between 144p and 1080p
[§2]; chunk duration "around 5 seconds" [§2]; each video "around 10 minutes" [§2];
reference: top track (2160p) at average bitrate 14–18 Mbps [§2]; quality metrics:
PSNR, SSIM, VMAF TV and phone models [§3.1.2]; max bitrate 1.1× to 2.3× the average
[§2]; coefficient of variation 0.3 to 0.6 [§2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(video ∈ {ED, BBB, ToS, Sintel, plus 4
YouTube videos}[§2]) = 8 (4 uploaded + 4 downloaded); codec = H.264 [§2]⟩;
Experiment = ⟨Workflow(offline: YouTube upload/download via youtube-dl) ⊗ Regime: Not
applicable (no network experiment; passive download of encoded content)⟩; iterations:
Not specified; telemetry {app_metrics: true (PSNR, SSIM, VMAF [§3.1.2])}.

### cava-ES3 — LTE trace collection campaign (text-only, §6.1)

**(i) Raw text.** "The first set, LTE, contains 200 cellular network traces we captured in
commercial LTE networks with a collaborator driving coast-to-coast across the US" [§6.1];
"downloading a large file from a well-provisioned server to a mobile phone" [§6.1]; per-
second throughput recorded; "each trace contains at least 18 minutes of bandwidth
measurements" [§6.1]; application/tool used, phone model, server location, operator:
Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 200 (one trace = one drive segment) [§6.1]⟩;
Experiment = ⟨Workflow(shell: large-file download; params.server: well-provisioned
[§6.1]) ⊗ Regime⟨Static: Not imposed (inhabited; real LTE network [§6.1]); Dynamic:
Not specified⟩⟩ @ Roles⟨client: mobile phone, server: well-provisioned server⟩;
path.latency: embedded in real LTE path; cca: Not specified; iterations: 1 per trace;
telemetry {app_metrics: true (per-second throughput time series [§6.1])}.

### cava-ES4 — trace-driven simulation evaluation (Figs 4, 7–10, Tab 1)

**(i) Raw text.** "we use real-world network trace-driven replay experiments" [§6.1];
LTE: 200 traces (Exp3) [§6.1]; FCC: 200 broadband traces per-5-second throughput
[§6.1]; "16 video clips" (Exp1+Exp2 encodings: 4 FFmpeg + 4 YouTube × 2 formats,
animation/sci-fi/sports/animal/nature/action) [§6.1; §2]; ABR schemes: CAVA, MPC,
RobustMPC, PANDA/CQ (max-sum, max-min), BBA-1, RBA, CAVA ablation variants [§6.1];
CAVA parameters: W = 40 s (20/8 chunks for 2/5 s durations) [§6.2], W′ = 200 s
(100/40 chunks) [§6.2], startup 10 s [§6.1], max buffer 100 s [§6.1]; bandwidth error
sweep: 0 to 50% in steps of 25% [§6.7]; simulator name: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(video ∈ 16[§2; §6.1] × trace_set ∈
{LTE 200, FCC 200}[§6.1] × scheme ∈ 7+[§6.1]); exact leaf count Not specified
(compound; one replay per trace implied, scheme comparison within runs)⟩; Experiment =
⟨Workflow(simulated ABR streaming; DASH/HLS; params.scheme: CAVA/MPC/…) ⊗ Regime⟨Static:
Not imposed; Dynamic: pressure = replay(network_trace from LTE/FCC sets [§6.1])⟩⟩ @
Roles⟨client: simulation node, server: simulated origin⟩; path.latency: embedded in
trace; cca: Not specified; iterations: 1 per (video, trace) [§6.2 implied]; telemetry
{app_metrics: true (Q4 chunk quality, low-quality %, rebuffering, quality change, data
usage [§6.1])}.

### cava-ES5 — dash.js prototype testbed evaluation (Fig 11, Tab 2)

**(i) Raw text.** "we set up a HTTP server as the origin server" [§3.1]; two computers,
Ubuntu 12.04 LTS, CPU Intel Core 2 Duo, memory 4 GB, 100 Mbps direct connection [§6.8];
Apache httpd [§6.8]; Google Chrome via Selenium [§6.8]; tc for LTE trace replay [§6.8];
dash.js v2.7.0, CAVA as CAVARule.js (520 LoC) [§5.5]; baselines: BOLA-E peak/avg/seg
[§6.8]; 4 YouTube videos: BBB, ED, Sports, ToS [Tab 2]; Fig 11: Big Buck Bunny, YouTube
encoded, H.264, LTE traces [Fig 11 caption]; runtime overhead ~56 ms [§6.8]; metrics:
Q4 quality, low-quality %, rebuffering, quality change, data usage [§6.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(video ∈ {BBB, ED, Sports, ToS}[Tab2] ×
scheme ∈ {CAVA, BOLA-E-peak, BOLA-E-avg, BOLA-E-seg}[§6.8]); trace set = LTE 200
traces [§6.8; Fig 11 caption]; exact count Not specified in §6.8 (200 LTE traces
replayed per video/scheme pair, implied)⟩; Experiment = ⟨Workflow(browser; Google
Chrome via Selenium; dash.js v2.7.0; DASH; params.scheme ∈ {CAVA, BOLA-E variants})
⊗ Regime⟨Static: Not imposed (tc trace replay); Dynamic: pressure = replay(ctp,
LTE traces [§6.8])⟩⟩ @ Roles⟨client: testbed Chrome node, server: Apache httpd
on local testbed⟩; path.latency: Not specified (embedded in LTE traces); cca: Not
specified; iterations: Not specified; telemetry {app_metrics: true (Q4 quality,
rebuffering, data usage [Fig 11 panels; §6.1])}.
