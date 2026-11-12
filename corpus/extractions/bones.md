# bones — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| bones-ES1 | Exp1 (Fig 3) | enhancement_option ∈ 5 levels × download_res ∈ {240p,360p,480p,720p} [§4.3; Fig 3] | 5 × 4 = 20 | Not specified |
| bones-ES2 | Exp2 (Tab4, Fig4, Fig5) | enhancement_setting ∈ 6 × trace_dataset ∈ 4 [§5.1] | 6 × 4 = 24 | Not specified |
| bones-ES3 | Exp3 (Tab 5) | variant ∈ {Basic, Monitor, AutoTune, Monitor+AutoTune} [§5.3] | 4 | Not specified |
| bones-ES4 | Exp4 (Fig 6) | gamma_p ∈ {10,20,30,40,50,60,70,80,90,100} × beta ∈ {0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0} [Fig 6 axis ticks; §5.4] | 10 × 8 = 80 | Not specified |
| bones-ES5 | Exp5 (text-only) | network_condition = synthetic (avg bw 200–5000 Kbps, variance 500–5000 Kbps, latency 20–100 ms [§5.3]); grid step: Not specified | Not specified | Not specified |
| bones-ES6 | Exp6 (Fig7, Tab6) | model_pool_config ∈ {low, low+medium, low+medium+high, 240p, 240p+360p, full-content-aware} × gpu ∈ {GTX 2080ti, GTX 3060ti} [§5.5; Fig 7 legend] | 6 × 2 = 12 (plus reused endpoints from ES2) | Not specified |
| bones-ES7 | Exp7 (Fig 9) | 1 (illustrative prototype rendering) [§6.1] | 1 | Not specified |
| bones-ES8 | Exp8 (Tab7, Fig10) | algorithm ∈ {BONES, BOLA*, Dynamic*, Buffer*, Throughput*, NAS} × enhancement ∈ {IMDN-agnostic+QuickStart, IMDN-aware+QuickStart} [§6.2] | Not specified (results averaged over 10 traces [§6.2]; 6 algorithms, 2 enhancement settings) | Not specified |

## Shared methodology A — simulation (applies to ES2, ES3, ES4, ES6) (quoted from the paper)


> Simulation environment extending Sabre [38] [§4.2, "Our simulator extends Sabre [38]"];
> Python, PyTorch [§4.2]; video: Big Buck Bunny, 636-second 30-fps [§4.2]; segments:
> 4-second chunks [§4.2]; bitrate ladder: 240p/360p/480p/720p/1080p at
> 400/800/1200/2400/4800 Kbps [§4.2]; network traces: 3G (mean 1184 Kbps, std 818 Kbps,
> 86 traces), 4G (mean 31431 Kbps, std 14058 Kbps, 40 traces), FCC-SD (mean 6081 Kbps,
> std 11615 Kbps, 1000 traces), FCC-HD (mean 17127 Kbps, std 4018 Kbps, 1000 traces)
> [Tab 2; §4.2]; exclude 3G traces with average bandwidth < 400 Kbps [§4.2]; QoE:
> α1 = 1, α2 = 0.1 [§4.1]; hardware: Not specified; repetitions: Not specified.

---


## Experiments

### bones-ES1 — NAS-MDSR enhancement profiling (Fig 3)

**(i) Raw text.** "the visual quality and computation speed of each enhancement option
are illustrated in Fig. 3" [§4.3]; NAS-MDSR enhancement setting [§4.3]; five quality
levels (no enhancement, low, medium, high, ultra) × four download resolutions (240p,
360p, 480p, 720p) [§4.3]; hardware: "an Nvidia GTX 1080ti GPU card" [§4.3]; metrics:
VMAF quality and computation speed (fps) [Fig 3 sub-captions]; "zero computation speed
implies the enhancement is not applicable" [§4.3].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(quality_level ∈ {none,low,medium,high,
ultra}[§4.3] × download_res ∈ {240p,360p,480p,720p}[§4.3]) = 5 × 4 = 20⟩; Experiment
= ⟨Workflow(ML inference; NAS-MDSR model; params.resolution, params.quality_level) ⊗
Regime: Not applicable (no network bottleneck; pure computation benchmark)⟩; hardware:
GTX 1080ti [§4.3]; iterations: Not specified; telemetry {app_metrics: true (VMAF,
fps [Fig 3])}.

### bones-ES2 — main simulation comparison campaign (Tab 4, Fig 4, Fig 5)

**(i) Raw text.** "We present the simulation results of BONES and other benchmark methods
averaged across all network trace datasets in Tab. 4 and Fig. 4" [§5.1]; six enhancement
settings: one no-enhancement plus NAS-MDSR on GTX 1080ti, IMDN content-agnostic/
content-aware on GTX 2080ti or GTX 3060ti [§5.1; Tab 4 headers]; algorithms: BOLA,
Dynamic, FastMPC, Buffer-based, Throughput-based, Pensieve (+ * greedy variants), NAS,
PreSR, BONES [§4.4]; "break down the results under the NAS-MDSR enhancement setting
across four different network traces" [§5.2; Fig 5]; Pensieve trained on 10,000 FCC
traces [§4.4]; video: Big Buck Bunny 636 s [§4.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(enhancement_setting ∈ 6[§5.1] ×
trace_dataset ∈ {3G,4G,FCC-SD,FCC-HD}[§4.2]) = 6 × 4 = 24; algorithm is the
comparison treatment (not a sweep dim)⟩; Experiment = ⟨Workflow(simulated video
streaming; DASH; 4 s segments; ABR: per-algorithm) ⊗ Regime⟨Static: Not imposed
(trace-driven simulation, not real testbed); Dynamic: pressure = replay(network_trace
∈ 4 datasets [§4.2])⟩⟩ @ Roles⟨client: simulation node, server: simulated origin⟩;
path.latency: Not specified (embedded in trace); cca: Not specified; iterations: Not
specified; telemetry {app_metrics: true (VMAF quality, QoE, rebuffering, quality
oscillation [§4.1; Tab 4])}.

### bones-ES3 — ablation for practical improvements (Tab 5)

**(i) Raw text.** "We conduct an ablation study for practical improvement techniques
and present the results under the NAS-MDSR enhancement setting in Tab. 5" [§5.3];
variants: Basic (γ_p=10, β=1), Monitor (Download Process Monitoring), AutoTune
(Automatic Hyper-Parameter Tuning), Monitor+AutoTune [§5.3]; Monitor+AutoTune row
89.23/3.07/2.52/76.05 = Tab 4 BONES NAS-MDSR row (assumed reuse of ES2).

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(variant ∈ {Basic, Monitor, AutoTune,
Monitor+AutoTune}[§5.3]) = 4; enhancement_setting = NAS-MDSR [§5.3]; otherwise
INHERITED from ES2 simulation setup⟩; iterations: Not specified; telemetry {app_metrics:
true (VMAF, rebuffering, QoE [Tab 5])}.

### bones-ES4 — hyperparameter sweep (Fig 6)

**(i) Raw text.** "comprehensively investigate the effect of hyper-parameters" [§5.4];
enhancement setting: NAS-MDSR [§5.4]; γ_p ∈ {10,20,30,40,50,60,70,80,90,100} [Fig 6
axis ticks], β ∈ {0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0} [Fig 6 axis ticks]; metrics:
Visual Quality (VMAF), Quality Oscillation, Rebuffering Ratio, QoE [Fig 6 panel titles].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(gamma_p ∈ {10,20,...,100}[Fig 6] ×
beta ∈ {0.3,...,1.0}[Fig 6]) = 10 × 8 = 80; enhancement_setting = NAS-MDSR [§5.4];
otherwise INHERITED from ES2⟩; telemetry {app_metrics: true (VMAF, rebuffering, QoE)}.

### bones-ES5 — AutoTune offline synthetic-trace tuning (text-only, §5.3)

**(i) Raw text.** "In the offline phase, we generate synthetic network traces with
different average bandwidths (from 200 to 5000 Kbps), different bandwidth variances
(500 to 5000 Kbps), and different latency (20 to 100 ms)" [§5.3]; "search for the
optimal hyper-parameter β (from 0.1 to 1) and γ_p (from 10 to 100) under each network
condition" [§5.3]; results: offline hyperparameter mapping table (not plotted); emulator:
Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(avg_bandwidth ∈ 200–5000 Kbps[§5.3]
× bandwidth_variance ∈ 500–5000 Kbps[§5.3] × latency ∈ 20–100 ms[§5.3] × gamma_p
∈ 0.1–1[§5.3] × beta ∈ 10–100[§5.3]); grid step Not specified → count Not specified⟩;
Experiment: offline computation campaign producing a hyperparameter lookup table; no
live network traffic.

### bones-ES6 — model-pool trade-off runs (Fig 7, Tab 6)

**(i) Raw text.** "study the trade-off between performance and extra download size in
Fig. 7" [§5.5]; IMDN enhancer, hardware GTX 2080ti and GTX 3060ti [Fig 7 panel titles];
model-pool configs: low, low+medium, low+medium+high, 240p, 240p+360p, full content-aware
[Fig 7 legend]; download overheads: content-agnostic 0 MB [§5.5], low 89 KB [§5.5],
first two quality levels 310 KB [§5.5], first three quality levels 2215 KB [§5.5];
Tab 6 uses IMDN with low+medium on GTX 3060ti [§5.5]; startup latency: Aware 0.68 s
with QuickStart 0 s [Tab 6]; QuickStart threshold: 2 segments (8 seconds) [§5.5].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(model_pool ∈ {low, low+medium,
low+medium+high, 240p, 240p+360p, full}[Fig 7 legend] × gpu ∈ {GTX 2080ti, GTX 3060ti}
[Fig 7 panel titles]) = 6 × 2 = 12; plus reused ES2 content-agnostic endpoints;
enhancement_method = IMDN [§5.5]; otherwise INHERITED from ES2 simulation setup⟩;
telemetry {app_metrics: true (QoE, download overhead, startup latency [Tab 6])}.

### bones-ES7 — prototype illustrative rendering (Fig 9)

**(i) Raw text.** "we illustrate sample frames rendered by the prototype system" [§6.1];
prototype built on iStream framework [5] [§6.1]; "approximately 3000 lines of code"
[§6.1]; deep-learning in PyTorch, decoder VPF [33], renderer OpenGL; video/enhancement/
network conditions: Not specified; hardware: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1 (illustrative run)⟩; Experiment = ⟨Workflow(
browser/shell: iStream prototype player; enhancement: Not specified) ⊗ Regime⟨Static:
Not specified; Dynamic: Not specified⟩⟩ @ Roles⟨client: prototype machine, server:
Not specified⟩; path.latency: Not specified; cca: Not specified; iterations: Not
specified; telemetry {app_metrics: true (frame quality visual comparison [Fig 9])}.

### bones-ES8 — prototype evaluation campaign (Tab 7, Fig 10)

**(i) Raw text.** "10 pre-recorded network traces sampled from the low-bandwidth 3G
network trace dataset and the high-bandwidth FCC-HD dataset" [§6.2]; algorithms: BOLA*,
Dynamic*, Buffer*, Throughput*, NAS, BONES [§6.2]; enhancement: "two variants of IMDN
enhancer, one content-agnostic and one content-aware with the QuickStart heuristic"
[§6.2]; prototype: iStream, Python/PyTorch/VPF/OpenGL [§6.1]; video: Not specified;
hardware (GPU/CPU): Not specified; repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(algorithm ∈ 6[§6.2] × enhancement ∈ 2
[§6.2]); count not fully factorial (Tab 7 shows all algorithms × both enhancement
settings, 6 × 2 = 12 treatment combinations); plus 10 traces = 12 × 10 = 120 leaf
attempts; exact reported count Not specified (Tab 7 averages across traces)⟩;
Experiment = ⟨Workflow(iStream prototype player) ⊗ Regime⟨Static: Not imposed
(trace-driven prototype, not controlled Regime); Dynamic: pressure = replay(network_trace
∈ 10 3G+FCC-HD traces [§6.2])⟩⟩ @ Roles⟨client: prototype machine⟩; path.latency:
embedded in trace; cca: Not specified; iterations: Not specified; telemetry {app_metrics:
true (QoE: VMAF, rebuffering, quality oscillation [Tab 7; Fig 10])}.
