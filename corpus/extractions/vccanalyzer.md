# vccanalyzer — Experiment-Set Intent Corpus (v4 re-render, grammar v2)

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| vccanalyzer-ES1 | E1 | (single: bulk transfer, reno, 5 Mbps) [Fig 1a caption] | 1 | Not specified |
| vccanalyzer-ES2 | E2 | (single: video streaming, reno, 10 Mbps) [Fig 1b caption] | 1 | Not specified |
| vccanalyzer-ES3 | E3 | (single: video initial phases, reno, 5 Mbps) [Fig 1c caption; §2] | 1 | Not specified |
| vccanalyzer-ES4 | E4 | capacity_down ∈ (100 Kbps → 30 Mbps sweep) × cca ∈ 15 × abr ∈ 3 [§3.1] | Not specified | Not specified |
| vccanalyzer-ES5 | E5 | (single trace, 5 Mbps; cca and abr Not specified) [§3.2; Fig 3 caption] | 1 | Not specified |
| vccanalyzer-ES6 | E6 | capacity_down ∈ {1,2,3,4,5} mbps × cca ∈ 16 × abr ∈ 3 [§4; §5.1; §3.3] | 5×16×3 = 240 | Not specified |
| vccanalyzer-ES7 | E7 | workflow ∈ {ccanalyzer_tool, nebby_tool} × cca (Fig 6 eval set) × per-tool settings [§5.1] | Not specified | Not specified |
| vccanalyzer-ES8 | E8 | service ∈ 10 [Table 1] × capacity_down ∈ {1,2,3,4,5} mbps [§3.3] | 10×5 = 50 attempted | 1 (majority vote across 5 capacity settings [§3.3]) |

## Experiments

### vccanalyzer-ES1 — bulk-transfer motivation trace (Fig 1a)

**(i) Raw text.** "Bulk transfer flow using TCP Reno on 5 Mbps link, 85ms RTT,
and 64 packet queue" [Fig 1a caption]; "compare the classic sawtooth of Reno
(Figure 1a) versus the steadier, lower queue preferred by BBR" [§2]; Fig 1
traces "captured at a controlled bottleneck by CCAnalyzer" [Fig 1 caption].
Duration, flow count, repetitions: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: 1⟩;
Experiment = ⟨Workflow(bulk TCP transfer; tool Not specified; engine shell) ⊗
Regime⟨Static: capacity_down 5 mbps [Fig 1a caption], capacity_up Not specified,
queue⟨discipline: Not specified (size-only per §5b.3), size: 64 pkts [Fig 1a
caption], params: Not specified, ecn: Not specified, mode: Not specified⟩;
Dynamic: Not specified (silence, §5b.2)⟩⟩;
path⟨latency: 85 ms [Fig 1a caption], jitter: Not specified, loss: Not
specified, reorder: Not specified, dup: Not specified⟩;
cca⟨algo: reno, stack: kernel, version: Not specified, params: Not specified,
flags: Not specified, build: Not specified⟩;
@ Roles⟨client: testbed node, server: testbed node⟩;
iterations: Not specified;
telemetry {qtrace: true (queue occupancy IS the result), pcap: Not specified,
app_metrics: false}.
confidence: high.

### vccanalyzer-ES2 — video-Reno distortion trace at 10 Mbps (Fig 1b)

**(i) Raw text.** "Video streaming flow using TCP Reno on 10 Mbps link, 85ms
RTT, and 64 packet queue" [Fig 1b caption]; "The off-periods and sudden rate
changes common in video mask or distort the CCA's queue signature" [§2]. ABR,
video content, duration, repetitions: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: 1⟩;
Experiment = ⟨Workflow(video streaming client; engine browser; params.abr: Not
specified) ⊗ Regime⟨Static: capacity_down 10 mbps [Fig 1b caption],
capacity_up Not specified, queue⟨discipline: Not specified, size: 64 pkts
[Fig 1b caption], params: Not specified, ecn: Not specified, mode: Not
specified⟩; Dynamic: Not specified (silence)⟩⟩;
path⟨latency: 85 ms [Fig 1b caption], jitter: Not specified, loss: Not
specified, reorder: Not specified, dup: Not specified⟩;
cca⟨algo: reno, stack: kernel, version: Not specified, params: Not specified,
flags: Not specified, build: Not specified⟩;
@ Roles⟨client: testbed node, server: testbed node (video origin)⟩;
iterations: Not specified;
telemetry {qtrace: true}.
confidence: high.

### vccanalyzer-ES3 — video-Reno initial-phase trace (Fig 1c)

**(i) Raw text.** "HTTP responses overlayed on queue occupancy at 5 Mbps link,
85ms RTT, and 64 packet queue" [Fig 1c caption]; "these early connection phases
do not provide enough data points for reliable classification" [§2]; CCA = "the
same CCA (TCP Reno)" [§2]. ABR, duration, repetitions: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: 1⟩;
Experiment = ⟨Workflow(video streaming client; params.abr: Not specified) ⊗
Regime⟨Static: capacity_down 5 mbps [Fig 1c caption], capacity_up Not
specified, queue⟨discipline: Not specified, size: 64 pkts [Fig 1c caption],
params: Not specified, ecn: Not specified, mode: Not specified⟩; Dynamic: Not
specified (silence)⟩⟩;
path⟨latency: 85 ms [Fig 1c caption], jitter: Not specified, loss: Not
specified, reorder: Not specified, dup: Not specified⟩;
cca⟨algo: reno, stack: kernel, version: Not specified, params: Not specified,
flags: Not specified, build: Not specified⟩;
@ Roles⟨client: testbed node, server: testbed node⟩;
iterations: Not specified;
telemetry {qtrace: true, pcap: Not specified, app_metrics: false}.
The "initial phases" framing [§2] is the analysis window over the captured
trace, not a distinct workflow.
confidence: high.

### vccanalyzer-ES4 — optimal link-rate sweep (Fig 2)

**(i) Raw text.** "we emulate a client watching a specific video stream governed
by an ABR algorithm (e.g., BOLA) and a server using a particular CCA. We then
sweep through a range of bottleneck link capacities configured on our intermediate
switch, from 100 Kbps up to 30 Mbps." [§3.1]; "Plotting the curves for 15 Linux
CCAs with the BOLA ABR (Figure 2)" [§3.1]; "the entire analysis was repeated
using different ABR algorithms: BOLA (buffer-based), a Throughput-based algorithm,
and a Dynamic algorithm" [§3.1]; band "between 1-5 Mbps" [§3.1]. Discrete sweep
points, video used, repetitions per point: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(capacity_down ∈ (100 Kbps →
30 Mbps, points Not specified) × cca ∈ 15 × application.params.abr ∈ {bola,
throughput, dynamic}) = Not specified⟩;
Experiment = ⟨Workflow(video streaming client; params.abr per leaf) ⊗
Regime⟨Static: capacity_down swept [§3.1], capacity_up Not specified,
queue⟨discipline: Not specified, size: 64 pkts [§4], params: Not specified,
ecn: Not specified, mode: Not specified⟩; Dynamic: Not specified (silence)⟩⟩;
path⟨latency: 85 ms [§4 testbed default], jitter: Not specified, loss: Not
specified, reorder: Not specified, dup: Not specified⟩;
cca⟨algo: per-leaf ∈ 15-CCA-enum [§3.1], stack: kernel, version: Not specified,
params: Not specified, flags: Not specified, build: Not specified⟩;
@ Roles⟨client: testbed node, server: testbed node⟩;
iterations: Not specified;
telemetry {app_metrics: true (average requested-chunk bitrate per 60-second
interval [§3.1] — the result), qtrace: Not specified}.
confidence: high.

### vccanalyzer-ES5 — trace-processing pipeline demo trace (Fig 3)

**(i) Raw text.** "Using the link bandwidth of 5 Mbps (85 ms RTT, 64 packet
queue) gives us more usable traces like shown in Figure 3a" [§3.2]; Fig 3
caption: "Queue occupancy trace captured on 5 Mbps link, 85ms RTT and 64 packet
queue after pre-processing stages" [Fig 3 caption]; valley threshold swept
"50ms - 1000ms", EWMA α swept "0.1 to 0.9", "α=0.5 for all captured traces"
[§3.2]. CCA, ABR, duration, repetitions: Not specified. Fig 3b/3c are the same
capture re-processed.

**(ii) Grammar v2.** ExperimentSet⟨leaves: 1⟩;
Experiment = ⟨Workflow(video streaming client; params: Not specified) ⊗
Regime⟨Static: capacity_down 5 mbps [§3.2], capacity_up Not specified,
queue⟨discipline: Not specified, size: 64 pkts [Fig 3 caption], params: Not
specified, ecn: Not specified, mode: Not specified⟩; Dynamic: Not specified
(silence)⟩⟩;
path⟨latency: 85 ms [§3.2], jitter: Not specified, loss: Not specified, reorder:
Not specified, dup: Not specified⟩;
cca: Not specified (unstated → default-with-echo at compile);
@ Roles⟨client: testbed node, server: testbed node⟩;
iterations: Not specified;
telemetry {qtrace: true}.
The interpolation/EWMA pipeline and per-trace threshold sweep are result-side
processing of one collected qtrace — out of collection scope.
confidence: high.

### vccanalyzer-ES6 — known-CCA classification collection (Figs 4, 5, 6 VCCAnalyzer part, 7)

**(i) Raw text.** Training: "we stream a 10-minute video clip (Big Buck Bunny
[1]) encoded at multiple quality levels (from 144p up to 4K) from a server which
is in a different cloudlab region than the switch and client" [§4]; "All training
samples are collected using the same link rate band (1–5 Mbps, using discrete
bandwidths of 1, 2, 3, 4, and 5 Mbps)" [§4]; ABRs "BOLA (buffer-based), a
throughput-based ABR, and a dynamic ABR" [§4]. Testing: "server which cycled
through all 16 CCAs in the Linux kernel (which includes some of the following:
Cubic, Reno, BBR, BBRv3, and others from the standard kernel set)" [§4; §5.1].
Accuracy "100%" processed and "90.6%" raw [§5.1; Fig 6]. Note: the gold records
a 15-vs-16 CCA discrepancy (Fig 2 states 15 [§3.1]; this set states 16 [§5.1]);
unreconciled in the prose — this file follows the gold.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(capacity_down ∈ {1,2,3,4,5}
mbps [§4] × cca ∈ 16 × application.params.abr ∈ {bola, throughput, dynamic}
[§4]) = 5×16×3 = 240⟩;
Experiment = ⟨Workflow(video streaming client, Big Buck Bunny 144p–4K; params.abr
per leaf) ⊗ Regime⟨Static: capacity_down per leaf, capacity_up Not specified,
queue⟨discipline: Not specified, size: 64 pkts [§4], params: Not specified,
ecn: Not specified, mode: Not specified⟩; Dynamic: Not specified (silence)⟩⟩;
path⟨latency: 85 ms [§4], jitter: Not specified, loss: Not specified, reorder:
Not specified, dup: Not specified⟩;
cca⟨algo: per-leaf ∈ 16 CCAs [§5.1] (15 stock + bbrv3), stack: kernel, version:
Not specified, params: Not specified, flags: Not specified, build: Not
specified⟩;
@ Roles⟨client: testbed node, server: service node in a different CloudLab
region [§4]⟩;
iterations: Not specified;
telemetry {qtrace: true [§4]}.
confidence: high.
interpreted: "16 CCAs" per §5.1 which includes BBRv3; §3.1 says 15; unreconciled
in the paper — using 16 for this set per the gold.

### vccanalyzer-ES7 — baseline-tools video collection: CCAnalyzer + Nebby (Fig 6, baseline part)

**(i) Raw text.** "We tested two previous approaches, CCAnalyzer and Nebby
(Figure 6), by collecting traces at their recommended link rates. We modified
Nebby to assign a dedicated bottleneck link to each flow" [§5.1]; "CCAnalyzer
achieved 82.3% accuracy and Nebby's shape-based classifier achieved 60.41%
accuracy on video traffic" [§5.1; Fig 6 caption]. Per-tool link rates, CCA
coverage counts, sample counts, durations: Not specified. Workload = known-CCA
video streams.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.workflow ∈
{ccanalyzer_tool, nebby_tool} × cca (Fig 6 evaluation set) × per-tool
recommended settings, values Not specified) = Not specified⟩;
Experiment = ⟨Workflow(third-party measurement tool; engine shell/mixed) ⊗
Regime⟨Static: per-tool recommended link rates Not specified, capacity_up Not
specified, queue⟨discipline: Not specified, size: 64 pkts [§4], params: Not
specified, ecn: Not specified, mode: Not specified⟩; Dynamic: Not specified
(silence)⟩⟩;
path⟨latency: 85 ms [§4], jitter: Not specified, loss: Not specified, reorder:
Not specified, dup: Not specified⟩;
cca⟨algo: per-tool evaluation set (Fig 6 axis), stack: kernel, version: Not
specified, params: Not specified, flags: Not specified, build: Not specified⟩;
@ Roles⟨client: testbed node, server: testbed node⟩;
iterations: Not specified;
telemetry {pcap: Not specified, qtrace: Not specified, app_metrics: Not
specified} (each tool carries its own capture, outside the A5 telemetry
switches).
confidence: high.

### vccanalyzer-ES8 — third-party services measurement study (Table 1; Fig 8)

**(i) Raw text.** "we deployed it against popular Over-The-Top (OTT) video
streaming services and popular websites that serve video content. For each video
service, we initiated a video playback on our client (using the Selenium tool)
and routed traffic through our controlled bottleneck" [§5.2]; "5 different network
settings within the band identified earlier: 1,2,3,4,5 Mbps link, 85ms RTT and
64 packet queue" [§3.3]; majority vote "across the 5 traces collected for that
service" [§3.3]. Services (10) with predicted labels from Table 1: Hulu bbr;
CNN bbr; Dailymotion bbr; YouTube bbrv3; NYT cubic; Disney+ bbr; Tiktok bbrv3;
Twitch bbrv3; Vimeo unknown; HBO Max bbrv3. Fig 8 = example traces "captured on
5 Mbps link, 85ms RTT, and 64 packet queue" for NYT, Max (HBO), Vimeo
[Fig 8 caption]. Per-service durations, flow counts, repetitions: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.params.service ∈
Table-1 set (10) × capacity_down ∈ {1,2,3,4,5} mbps [§3.3]) = 10×5 = 50
attempted⟩;
Experiment = ⟨Workflow(service video playback; engine browser — Selenium in the
paper ≙ the browser-automation engine class) ⊗ Regime⟨Static: capacity_down per
leaf [§3.3], capacity_up Not specified, queue⟨discipline: Not specified, size:
64 pkts [§3.3], params: Not specified, ecn: Not specified, mode: Not specified⟩;
Dynamic: Not specified (silence; the real WAN tail beyond the imposed bottleneck
is uncontrolled)⟩⟩;
path⟨latency: 85 ms [§3.3] (imposed bottleneck path; real WAN beyond is
inhabited/uncontrolled), jitter: Not specified, loss: Not specified, reorder:
Not specified, dup: Not specified⟩;
cca: Not specified (server-side CCA is the measurand, not a spec field);
@ Roles⟨client: testbed node, server: real third-party service (no Pramana-
controlled server role)⟩;
iterations: 1 per leaf ("majority vote across the 5 traces collected for that
service" [§3.3] = 1 trace per (service, setting), voting across settings);
telemetry {qtrace: true}.
The server-side CCA is the measurand, not a spec field. Classification against
ES6's training library is analysis-side.
confidence: high.
