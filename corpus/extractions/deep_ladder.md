# deep_ladder — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Description | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| deep_ladder-ES1 | Exp1 | DeepLadder-CBR vs. baselines, HSDPA and FCC traces | Not specified | Not specified |
| deep_ladder-ES2 | Exp2 | DeepLadder-VBR vs. baselines, Oboe and HDFS traces | Not specified | Not specified |
| deep_ladder-ES3 | Exp3 | Practical deployment: per-process timing on CPU/GPU | 2 (CPU, GPU) | Not specified |

## Experiments

### deep_ladder-ES1 — DeepLadder-CBR trace-driven evaluation (Fig 2)

**(i) Raw text.** "Using trace-driven experiments" [§1]; "we test the
performance of each scheme by the video under the HSDPA and FCC network
environment" [§3]; "we collect over 3,000 network traces, totally almost
50 hours, from public datasets for training and testing" [§3]; video
quality metric: "VMAF" [§2]; schemes: DeepLadder-CBR, Nf-Greedy (Netflix),
Pen-Set ({300, 750, 1200, 1850, 2850, 4300} kbps [§3]), RMPC-Set ({300,
700, 1000, 1500, 2000, 3000} kbps [§3]); results: "average video quality
improved 8.49%-12.94% (HSDPA) and 8.78%-14.25% (FCC); bandwidth
utilization improved 3.66%-11.68% (HSDPA); storage overhead reduced
39.77%-54.84% vs. baselines" [§3]. Network topology / testbed / live
traffic / CCA / queue / cross traffic / transport: Not specified (no live
network; trace-driven).

**(ii) Grammar.** No network Regime; no live Workflow. Experiment replays
pre-collected bandwidth-trace datasets (HSDPA, FCC) through a DRL bitrate-
ladder algorithm and its baseline comparators. The "network environment"
is a trace, not an imposed link.
ExperimentSet⟨leaves: sweep(trace × scheme — count Not specified)⟩;
Experiment = ⟨Workflow(offline trace-driven ABR algorithm evaluation) ⊗
Regime: none — no emulated or physical link⟩; iterations: Not specified;
telemetry: {app_metrics: true (VMAF, bandwidth utilization, storage
overhead)}.

### deep_ladder-ES2 — DeepLadder-VBR trace-driven evaluation (Fig 3)

**(i) Raw text.** "Figure 3 illustrates the results for the Oboe and HDFS
network conditions" [§3]; schemes: DeepLadder-VBR (w=0, w=1), Fixed-25,
X265 (default CRF=28 [§3]); action size 20, CRF=20−39 [§2]; results:
"DeepLadder-VBR (w=0) bandwidth utilization within 8.37%-15.03% compared
with fixed encoding ladder schemes; DeepLadder-VBR (w=1) reduces storage
cost by 29.8% on the Oboe traces and 21.26%-44.88% on the HDFS network"
[§3]; quality metric: VQAlog [Fig 3 axis]; "3,000 network traces, totally
almost 50 hours" [§3]. Network topology / testbed / live traffic / CCA /
queue / cross traffic / transport: Not specified.

**(ii) Grammar.** No network Regime; no live Workflow. Trace-driven replay
of Oboe/HDFS bandwidth traces through VBR bitrate-ladder algorithm and
fixed-CRF baselines.
ExperimentSet⟨leaves: sweep(trace × scheme × w — count Not specified)⟩;
Experiment = ⟨Workflow(offline trace-driven ABR algorithm evaluation) ⊗
Regime: none⟩; iterations: Not specified; telemetry: {app_metrics: true
(VQAlog, bandwidth utilization, storage overhead)}.

### deep_ladder-ES3 — Practical implementation timing (Table 1)

**(i) Raw text.** "We deploy the proposed scheme as a service into the
transcoding frameworks and list the time consumption for each process in
Table 1, tested on an Intel Core i7 CPU2.2GHz and an Nvidia 1080Ti GPU"
[§3]; CPU results: Video Content Extraction 439 ms; Inference Timespan
3 ms; Transcoding Time 12060 ms; Extra Cost 3.67% [Table 1]; GPU results:
Video Content Extraction 94 ms; Inference Timespan 12 ms; Transcoding
Time 3407 ms; Extra Cost 3.11% [Table 1]; "DeepLadder consumes only
3.11%-3.67% extra cost compared with the original system" [§3]. Workload
(videos transcoded for timing): Not specified. Repetitions: Not specified.
Network setup: Not specified (offline transcoding measurement).

**(ii) Grammar.** No network Regime; no live Workflow. Offline
hardware-timing measurement of a deployed transcoding service on two
hardware configurations (CPU, GPU).
ExperimentSet⟨leaves: 2 (CPU; GPU)⟩; Experiment = ⟨Workflow(offline
transcoding timing, DeepLadder service) ⊗ Regime: none⟩;
iterations: Not specified; telemetry: {app_metrics: true (per-process
latency ms, extra cost %)}.
