# cgsynth — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| cgsynth-ES1 | Exp1 (text-only, §2) | game ∈ {Forza, Fortnite, Mortal Kombat} [§2]; other dims Not specified | Not specified (no reported results; prospective demo) | Not specified |

## Shared methodology (quoted from the paper)


> CGReplay for real CG traffic capture [§2]; GRU trained on IPG data from captured PCAPs
> [§2(C), "trains a GRU model on IPG data extracted from game replays (e.g., Fortnite)"];
> frame interpolation: RIFE (AI-based) or addWeighted (OpenCV) [§2(B)]; Mininet for
> synthetic trace replay [§3, "Synthetic video traces are replayed in an emulated network
> (via Mininet)"]; transport: RTP/UDP [Fig 1 annotation "Current implementation uses
> RTP/UDP"]; QoE metrics: PSNR, SSIM, LPIPS, VMAF [§2(B)], MOS [abstract]; network
> parameters: Not specified (configurable via YAML [§2(A)]).

---


## Experiments

### cgsynth-ES1 — CG traffic capture, synthesis, and QoE validation (text-only, §2)

**(i) Raw text.** "We compare synthetic and real downlink video streams" [§1]; "validate
synthetic traffic's video quality and responsiveness against real streams" [abstract];
games: Forza, Fortnite, Mortal Kombat [§2, "prerecorded PCAPs and video frames from
Forza, Fortnite, and Mortal Kombat"]; capture tool: CGReplay [§2, "CGReplay focuses on
capturing and replaying real-world CG traffic (uplink/downlink)"]; GRU trained on "IPG
data extracted from game replays (e.g., Fortnite)" [§2(C)]; Mininet for replay [§3];
Mininet-WiFi and P4/Tofino as hardware alternative [§2(A)]; QoE: PSNR, SSIM, LPIPS
[10], VMAF [7] and subjective MOS [abstract]; network bandwidth/delay/loss/queue:
"Network settings such as bandwidth, delay, loss rates, and queue management can be
configured" [§2(A)] but no values stated; repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: Not specified; game ∈ {Forza, Fortnite,
Mortal Kombat}[§2] is the primary varying factor; network conditions Not specified
(configurable [§2(A)])⟩; Experiment = ⟨Workflow(cloud gaming: uplink player commands
via CGReplay + downlink synthetic video via CGSynth; params.game ∈ {Forza, Fortnite,
Mortal Kombat}[§2]) ⊗ Regime⟨Static: capacity Not specified [§2(A)], queue: Not
specified [§2(A)], latency Not specified [§2(A)]; Dynamic: pressure = replay(ctp,
real CG PCAPs from CGReplay [§2])⟩⟩ @ Roles⟨client: gaming host, server: CG service
endpoint⟩; path.latency: Not specified; cca: Not specified (RTP/UDP, not TCP [Fig 1]);
iterations: Not specified; telemetry {app_metrics: true (PSNR, SSIM, LPIPS [§2(B)],
VMAF [§2(B)], MOS [abstract])}.
