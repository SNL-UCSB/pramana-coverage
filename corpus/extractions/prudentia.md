# prudentia — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| prudentia-ES1 | Exp1 | pair ∈ Fig-2 throughput-competition pairs × static.capacity_down ∈ {8, 50} mbps [§3.1, L187-193] | Not specified ("almost 80" pairs × 2 [L129]) | until(event(ci_width_of_median, ≤0.5 mbps @8 Mbps | ≤1.5 mbps @50 Mbps), min=10, max=30) [§3.3, L332-373] |
| prudentia-ES2 | Exp2 | incumbent ∈ {meet, teams} × contender ∈ throughput services (grid Not specified) × static.capacity_down ∈ {8, 50} | Not specified | Not specified |
| prudentia-ES3 | Exp3 | page ∈ {youtube.com, news.google.com, wikipedia.org} × contender ∈ {mega, netflix, cubic-iperf, bbr-iperf} + solo family (Dynamic: none) × static.capacity_down ∈ {8, 50} | 3 × 4 × 2 = 24, plus solo: 3 × 1 × 2 = 6; total 30 | ≥5 trials (10 page loads are workflow-internal NFA states per §5b.10) [§5.2, L536-544] |
| prudentia-ES4 | Exp4 | incumbent ∈ {dropbox, newreno-iperf, cubic-iperf} vs 5×iperf-bbr, 50 Mbps only [§4, L506-509] | 3 | Not specified |
| prudentia-ES5 | Exp5 | pair (YouTube-vs-Dropbox highlighted; others Not specified) × static.capacity_down ∈ 8–100 mbps range (grid Not specified; axis ticks 20/40/60/80/100 only [Fig 7]) | Not specified | Not specified |
| prudentia-ES6 | Exp6 | pair ∈ grounded set (newreno-vs-mega, cubic-vs-mega @50 [Fig 8b, L690]; newreno-vs-cubic @8 [§6, L699-712]) at queue 8×BDP (2048 pkt) | Not specified (3 pairs grounded in prose) | Not specified |
| prudentia-ES7 | Exp7 | incumbent ∈ {youtube, gdrive} vs iperf-bbr (Linux 4.15), 2022 [§6, L731] | 2 (bw Not specified) | Not specified |
| prudentia-ES8 | Exp8 | incumbent ∈ {youtube, dropbox, gdrive} × workflow.cca.build ∈ {linux-4.15, linux-5.15} iperf-bbr [Fig 9b, L735-748] | 3 × 2 = 6 (bw Not specified) | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Dumbbell topology; two clients simultaneously receive from two live,
> deployed Internet services; BESS software switch as the controlled
> bottleneck (access-link speed, queue size, ingress/egress delay; logs queue
> occupancy + packet loss) [§3.1, L170-175]. Wired links; loss only from queue
> overflow [§3.1]. Clients: Mac Mini desktops, desktop-marketed GPU, connected
> 4K monitor (needed for real 4K bitrate selection) [§3.3, L309-318]; Chrome
> driven by Selenium [§3.3, L299-300]; Netflix on Safari due to DRM [Table 1
> fn, L235]; cookies and cache wiped between experiments [§3.3]. Bandwidth
> {8, 50} Mbps [§3.1, L187-193]. RTT normalized to 50 ms per service (BESS
> adds delay; can only add; highest recorded native service RTT 40 ms;
> multi-flow services normalized on the first flow) [§3.1, L249-256]. Queue:
> drop-tail FIFO ≈ 4×BDP, rounded to nearest power of two = 1024 pkt @50 Mbps
> [§3.1, L258-280; Fig 8a, L665]. Workloads: 10 GB random file (file transfer);
> Big Buck Bunny (video, RTC) [§3.2, L287-289]. 10-min runs, first and last
> 2 min ignored [§3.4, L327-328]. Metric: Max-Min-Fair share [§2/§3].
> AQM never named beyond drop-tail FIFO; pcap capture: Not specified.


## Experiments

### prudentia-ES1 — 2023 all-pairs throughput/MmF competition (Figs 2,3,4p,8a,9a-2023,10–13, Table 3)

**(i) Raw text.** "12 services translates to almost 80 pairs to test, with
10 trials each" [L129]; trials ≥10 up to 30 until the 95% CI of the median is
within ±0.5 Mbps (highly) / ±1.5 Mbps (moderately) [§3.3, L332-373]; full
all-pairs trial ≈ 20 h [§3.2, L287]; period June–Sept 2023 [§3.2, L291-293].
Per-service CCA from Table 1 [§3.2, L214-232]; RTT normalized to 50 ms per
service [§3.1, L249-256]. Queue: drop-tail FIFO ≈ 4×BDP = 1024 pkt @50 Mbps
[§3.1, L258-280].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(pair ∈ Fig-2 throughput-
competition pairs × Regime.Static.capacity_down ∈ {8, 50} mbps [§3.1]);
count Not specified⟩; Experiment = ⟨Workflow(incumbent service; browser or
transfer client) @ path.latency: 50 ms per service [§3.1, L249-256] ⊗
Regime⟨Static: capacity_down ∈ {8, 50} mbps, queue: drop-tail FIFO 1024 pkt
@50 Mbps [L258-280]; Dynamic: pressure = load(contender_workflow ↦ second
client node)⟩⟩ @ Roles⟨client: 4K/GPU desktop node, server: real service
endpoints⟩; iterations = until(event(ci_width_of_median, ≤0.5 mbps @8 Mbps
| ≤1.5 mbps @50 Mbps), min=10, max=30) [§3.3, L332-373]; telemetry
{qtrace: true (queue occupancy + loss at bottleneck [§3.1, L170-175]),
app_metrics: true (per-service throughput shares), pcap: Not specified}.

### prudentia-ES2 — RTC QoE competition (Fig 5)

**(i) Raw text.** Incumbents Google Meet (GCC, WebRTC, ≤1.5 Mbps, 1 flow)
and Microsoft Teams (CCA unknown, WebRTC, ≤2.6 Mbps, 1 flow) [Table 1;
§5.1]; metrics per Table 2: resolution (px), average FPS, freezes/min
(inter-arrival > max(3δ, δ+150 ms)), fraction of packets with RTT > 190 ms
[§5.1, L499-512]; period Jan 2024 [§3.2, L293]; Big Buck Bunny [§3.2].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(incumbent.workflow ∈ {meet,
teams} × contender_workflow ∈ throughput services (grid Not specified) ×
Regime.Static.capacity_down ∈ {8, 50} mbps)⟩; Experiment as ES1 with
Workflow(RTC session; params: resolution, fps, freeze, delay targets) @
path.latency: 50 ms [§3.1, L249-256]; iterations Not specified; telemetry
{app_metrics: true (WebRTC stats: resolution, FPS, freeze events, per-packet
delay [§5.1, L499-512]), qtrace: true}.

### prudentia-ES3 — web page-load-time competition (Fig 6)

**(i) Raw text.** PLT = time for 95% of the above-the-fold region to load
via Google SpeedIndex, on a 4K display [§5.2, L534, L593-594]; protocol:
start contender, wait 30 s, load page in fresh Chrome, 10 loads with 45 s
gaps, ≥5 trials ⇒ ≥50 points per pair [§5.2, L536-544]; pages and contenders
per Fig 6.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(page ∈ {youtube.com,
news.google.com, wikipedia.org} × contender ∈ {mega, netflix, cubic-iperf,
bbr-iperf} × Regime.Static.capacity_down ∈ {8, 50} mbps) = 3 × 4 × 2 = 24,
plus a solo leaf family (Dynamic: none — a stated baseline, not silence
[Fig 6]) = 3 × 1 × 2 = 6; total 30⟩; Experiment = ⟨Workflow(page load;
params.url) @ path.latency: 50 ms [§3.1, L249-256] ⊗ Regime as ES1⟩;
iterations = ≥5 trials [§5.2, L536] (the 10 timed page loads are NFA-internal
workflow states per §5b.10 — profile reset within each load, not a
between-iteration operation); telemetry {app_metrics: true (SpeedIndex /
paint-timeline inputs [§5.2, L534]), qtrace: true}.

### prudentia-ES4 — five-flow iPerf-BBR competition (Fig 4-partial)

**(i) Raw text.** "in separate experiments in the moderately-constrained
setting", Dropbox / NewReno / Cubic each vs five concurrent iPerf BBR flows
[§4, L506-509]; results: Dropbox 33% MmF [§4, L510]; NewReno/Cubic 80–90%
MmF [§4, L510-516]; 50 Mbps, 50 ms, 4×BDP = 1024 pkt inherited from §3.1.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(incumbent.workflow ∈ {dropbox,
newreno-iperf, cubic-iperf}) = 3, Regime.Static.capacity_down = 50 mbps
only [§4, L506-509]⟩; Experiment = ⟨Workflow(incumbent) @
path.latency: 50 ms [§3.1, L249-256] ⊗ Regime⟨Static: capacity_down 50 mbps,
queue: drop-tail FIFO 1024 pkt; Dynamic: pressure = load(iperf × 5,
cca: ⟨algo: bbr⟩ ↦ contender node)⟩⟩; iterations Not specified; telemetry
{app_metrics: true (throughput), qtrace: Not specified}.

### prudentia-ES5 — bandwidth sweep 8–100 Mbps, 2022 (Fig 7)

**(i) Raw text.** All-pairs experiments at a range of bottleneck bandwidths
between 8 and 100 Mbps [§6, L758-760]; axis ticks 20/40/60/80/100 Mbps [Fig 7,
L640]; highlighted pair YouTube (incumbent) vs Dropbox [Fig 7 caption,
L644-647]; period 2022 [§6 fn 8, L798]; fairness non-monotonic, fair only
beyond 70 Mbps [§6, L768-774; Fig 7 caption].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(pair (extent Not specified;
YouTube-vs-Dropbox grounded) × Regime.Static.capacity_down ∈ 8–100 mbps,
grid Not specified)⟩; Experiment as ES1 (except collection period 2022);
path.latency: 50 ms per-workflow [§3.1]; iterations Not specified; telemetry
{app_metrics: true}.

### prudentia-ES6 — buffer-doubling 8×BDP (Fig 8b)

**(i) Raw text.** Queue 8×BDP = 2048 pkt vs baseline 4×BDP = 1024 pkt
[Fig 8b, L690]; iPerf NewReno and Cubic vs Mega, queue-occupancy time series,
moderately-constrained 50 Mbps [Fig 8b]; NewReno-vs-Cubic share change @8 Mbps
also reported [§6, L699-712]; full pair coverage Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: Not specified (grounded pairs:
newreno-vs-mega and cubic-vs-mega @50 Mbps [Fig 8b, L690]; newreno-vs-cubic
@8 Mbps [§6, L699-712]); Regime.Static.queue: drop-tail, size 2048 pkt
[L690]⟩; Experiment as ES1 with queue override; path.latency: 50 ms
per-workflow [§3.1]; telemetry {qtrace: true (occupancy time series is the
result), app_metrics: true}.

### prudentia-ES7 — 2022 longitudinal collection (Fig 9a, 2022 bars)

**(i) Raw text.** YouTube and Google Drive vs iPerf-BBR built on Linux 4.15,
measured in 2022, compared to 2023 in Fig 9a [§6, L731; Fig 9a, L714];
throughput deltas +46% / +172% attributed to service-side deployment changes
[§6, L790-794]; bandwidth setting Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(incumbent.workflow ∈ {youtube,
gdrive}) = 2⟩; Experiment as ES1 (period 2022) with contender =
iperf-bbr @ workflow.cca: ⟨algo: bbr, build: linux-4.15⟩ [§6, L731];
path.latency: 50 ms per-workflow [§3.1]; iterations Not specified; telemetry
{app_metrics: true}.

### prudentia-ES8 — kernel 4.15 vs 5.15 BBR comparison (Fig 9b)

**(i) Raw text.** YouTube, Dropbox, Google Drive vs iPerf BBR on Linux 4.15
vs 5.15 [Fig 9b, L735-748]; 5.15 less contentious vs Dropbox/Drive, more vs
YouTube [§6, L731-748]; bandwidth setting Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(incumbent.workflow ∈ {youtube,
dropbox, gdrive} × workflow.cca.build ∈ {linux-4.15, linux-5.15}) = 3 × 2 = 6;
contender = iperf-bbr; otherwise as ES7⟩; path.latency: 50 ms per-workflow
[§3.1]; iterations Not specified; telemetry {app_metrics: true}.
