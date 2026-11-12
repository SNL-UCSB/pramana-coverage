# gmm_video_quality — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| gmm_video_quality-ES1 | Exp1 | production sessions ∈ Viasat geosynchronous satellite network, Oct 1–12, 2023 [§2] | 1,885 unique playback sessions (raw); 1,557 after cleaning [§2; Table 1] | 1 (one collection period) |

## Shared methodology (raw text) (quoted from the paper)


> Passive Speed Measurement (PSM) — "performed for each service class every few
> milliseconds and aggregated into 5-second averages" [§2]; CDN-side playback-bitrate
> labels from ISP collaboration with "a major long-form video streaming provider" [§2];
> "642,617 raw PSM measurements for 1,885 unique playback sessions from October 1-12,
> 2023" [§2]; one streaming provider, long-form content only [§2]; all data anonymized
> [§1]; network bandwidth, latency, queue, cross traffic: Not specified (production
> network, no emulation described).


## Experiments

### gmm_video_quality-ES1 — Passive PSM + bitrate collection on Viasat satellite network

**(i) Raw text.** "leading geosynchronous satellite internet provider, Viasat" [§1];
passive PSM telemetry "every few milliseconds and aggregated into 5-second averages"
[§2]; "642,617 raw PSM measurements for 1,885 unique playback sessions from October
1-12, 2023" [§2]; session "median of 780 seconds" [§2]; label: "Satisfactory" if
video bitrate ≥ 1.8 Mbps (target ≈ 720p), else "Unsatisfactory" [§2]; "real-world
production data" [§1]; network parameters (bandwidth, latency, queue, cross traffic,
CCA): Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: production sessions on Viasat geostationary
satellite network, Oct 1–12, 2023 [§2]; count: 1,885 sessions ATTEMPTED
(1,557 after cleaning) [§2; Table 1]⟩; Experiment = ⟨Workflow(video playback from
live streaming provider, residential/inflight satellite subscribers) ⊗
Regime⟨Static: Not specified (production network; no controlled bottleneck);
Dynamic: Not specified⟩⟩ @ Roles⟨client: Viasat residential/in-flight subscribers,
server: third-party CDN endpoints (major streaming provider)⟩; iterations Not
specified; telemetry {app_metrics: true (PSM scheduling weights, 5-second averages;
CDN-side playback bitrate labels [§2])}.
