# content_aware_retransmission — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Description | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| content_aware_retransmission-ES1 | Exp1 | Single manual packet-loss decoding demo | 1 | 1 |
| content_aware_retransmission-ES2 | Exp2 | Per-packet SSIM sweep over relative packet index | Not specified | Not specified |
| content_aware_retransmission-ES3 | Exp3 | Monte Carlo Q_i metric estimation per frame | Not specified | Not specified |
| content_aware_retransmission-ES4 | Exp4 | libx264 simulator: content-aware vs. baselines | Not specified (p × π × λ × burst-length combinations) | Not specified |

## Experiments

### content_aware_retransmission-ES1 — Single-loss decoding demonstration (Fig 1)

**(i) Raw text.** "We manually create a packet loss when transmitting Fig. 1a,
pad the missing bits with zero, and decode it into Fig. 1b. We enable the
error concealment in libx264 at the decoder." [§1]; "One lost packet
(index=0.75)" [Fig 1b caption]; SSIM = 0.97 [Fig 1 caption]; dataset:
"We present two decoded images from [11] in Fig. 1" [§1] (YT-UGC [11]).
Network bandwidth: Not specified. Base latency / RTT: Not specified.
Queue / CCA / cross traffic / topology / testbed / duration /
repetitions: Not specified.

**(ii) Grammar.** No network Regime; no live Workflow. This is an offline
software operation: manually corrupt one encoded video frame at relative
index 0.75, run libx264 decoder with error concealment enabled, measure
SSIM.
ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(offline libx264 decode,
error concealment) ⊗ Regime: none — no link, no Regime⟩ @
Roles: not applicable; iterations: 1; telemetry: {app_metrics: true
(SSIM)}.

### content_aware_retransmission-ES2 — Per-packet SSIM sweep (Fig 2)

**(i) Raw text.** "Then we conduct an experiment to further explore the
significance of each packet in a frame." [§1]; swept factor: relative
index of lost packet within a frame [Fig 2 x-axis "Relative index of lost
packet"]; "40% of packet losses in our preliminary experiments are not
necessary to recover with the degradation on SSIM of less than 0.05,
only 20% can lead to video quality degradation of more than 0.1" [§1];
result metric: SSIM loss per index [Fig 2 y-axis "SSIM loss"]. Codec:
Not specified. Dataset: Not specified. Loss-injection method: Not
specified. Network bandwidth / RTT / queue / cross traffic / CCA /
transport / topology / testbed / duration / repetitions: Not specified.

**(ii) Grammar.** No network Regime; no live Workflow. Experiment is an
offline per-packet SSIM measurement sweeping loss position within a frame.
ExperimentSet⟨leaves: sweep(packet_index within frame — axis-only, Not
specified count)⟩; Experiment = ⟨Workflow(offline SSIM measurement at
varying packet positions) ⊗ Regime: none⟩; iterations: Not specified;
telemetry: {app_metrics: true (SSIM loss per index)}.

### content_aware_retransmission-ES3 — Monte Carlo importance-metric estimation (Fig 3)

**(i) Raw text.** "we perform an experiment to demonstrate the variability
of Q_i among different frames and its effectiveness in differentiating
them." [§3]; "We estimate E[S_i|r] using the Monte Carlo method" [§3];
"In Fig. 3, red line represents Q_a" [§3]; Q_i = E[S_i|r]/f_i [§2].
Loss rate r: Not specified. Dataset / video: Not specified. Monte Carlo
sample count / repetitions: Not specified. Network bandwidth / RTT /
queue / cross traffic / CCA / transport / topology / testbed / duration:
Not specified.

**(ii) Grammar.** No network Regime; no live Workflow. Experiment is an
offline Monte Carlo estimation of per-frame importance Q_i across frames.
ExperimentSet⟨leaves: sweep(frame index across a video — count Not
specified)⟩; Experiment = ⟨Workflow(offline Monte Carlo SSIM-loss
estimation) ⊗ Regime: none⟩; iterations: Not specified; telemetry:
{app_metrics: true (Q_i per frame, Q_a average)}.

### content_aware_retransmission-ES4 — Simulator comparison campaign (Figs 4–5)

**(i) Raw text.** "We implement a simple simulator using libx264." [§3];
"we suppose RTT is 15 ms, bandwidth is 40 Mbps ... the loss rate is 10%
... the frame rate of the video is 30fps ... taking from the typical
network conditions [9]" [§3]; "We suppose only one burst happens during
the whole video" [§3]; "bursts occur every 20 seconds" [§4]; burst length
= 8 frames for Fig 4 [Fig 4 caption; §3]; swept "from 1 frame to 16
frames" for Fig 5 [§3]; p = {0, 0.1, 0.2, …, 0.9}; π = {0, 1, 2}; λ =
{0, 1, 2, …, 8}; plus retransmit-all case [§3]; dataset: "YT-UGC
Dataset [11] … each with a duration of 20 seconds" [§3]; analysis
constraint: "limit the load time to 40ms" [§3]; headline: SSIM loss
0.025 / 0.075 / 0.14 for content-aware / deadline-aware / probabilistic
at 40 ms load-time limit [§3]. Congestion control: Not specified.
Transport: Not specified. Queue size / management: Not specified. Cross
traffic: Not specified. Number of flows / topology: Not specified.
Emulator/testbed: Not specified (software simulator only). Repetitions:
Not specified.

**(ii) Grammar.** RTT=15 ms, BW=40 Mbps, and loss_rate=10% are scalar
INPUTS to the libx264 retransmission simulator — they parameterise the
mathematical model, not an actual emulated network link. No packets flow
through any bottleneck. No network Regime is imposed.
ExperimentSet⟨leaves: sweep(p, π, λ, burst_length — simulator knobs;
combined leaf count Not specified)⟩; Experiment = ⟨Workflow(libx264
simulator, retransmission policy) ⊗ Regime: none — no emulated link⟩;
iterations: Not specified; telemetry: {app_metrics: true (SSIM loss,
load time)}.
