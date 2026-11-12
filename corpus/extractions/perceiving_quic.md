# perceiving_quic — Experiment-Set Intent Corpus

## Shared methodology (ES1 raw text) (quoted from the paper)


> Mahimahi-based testbed modified to incorporate the Google QUIC (gQUIC) Web
> stack [§3, "we reuse our Mahimahi-based testbed from [24]"; §1, "we modified
> the Mahimahi [15] framework and incorporated the Google QUIC Web stack"].
> 36 websites from Alexa Top 50 + Moz Top 50, filtered to 36 for accurate
> replay ("We had to exclude four sites since we were unable to replay them
> accurately, and one was a private project site" [§3 "Websites Selection"]).
> Server: NGINX + gQUIC Web stack embedded in Mahimahi [§3, "we embedded the
> gQUIC Web stack as well as an NGINX Web server in Mahimahi"]. Client:
> Chromium browser automated via Browsertime, each visit "using a fresh
> Chromium browser with an empty cache" [§3]. Metrics: FVC (First Visual
> Change), LVC (Last Visual Change), PLT (Page Load Time), SI (Speed Index),
> VC85 (Visual Completeness 85%) [§3, "derive technical and visual metrics
> (FVC, LVC, PLT, SI, VC85)"]. No cross-traffic stated (Dynamic: none).

---


## Experiments

### perceiving_quic-ES1 — Testbed website-load / video-production campaign (Fig.6)

**(i) Raw text.**
"We repeatedly requested a set of previously recorded websites using the Chromium
browser, which we automated using Browsertime" [§3]; each website visited "at
least 31 times while recording the browser window" [§3 "Producing Videos"].
Protocol configurations (Table 1): TCP = "Stock TCP (Linux): IW10, Cubic";
TCP+ = "IW 32, Pacing, Cubic, tuned buffers, no slow start after idle";
TCP+BBR = "TCP+, but with BBRv1 as congestion control"; QUIC = "Stock Google
QUIC: IW 32, Pacing, Cubic"; QUIC+BBR = "QUIC, but with BBRv1 as congestion
control" [Tab.1]. TCP+ parameterization: "initial congestion window of 32
segments matching gQUIC's default, using pacing … and not falling back to the
initial window after idle"; send/receive buffers enlarged "according to the
bandwidth-delay product" [§3 "Protocol Parametrization"]. "BBRv2 was not yet
available at the time of testing" [§3, footnote 2]. Network settings (Table 2
[Tab.2]): DSL — 5 Mbps up / 25 Mbps down, min. RTT 24 ms, Loss 0.0 %;
LTE — 2.8 / 10.5 Mbps, 74 ms, 0.0 %; DA2GC — .468 / .468 Mbps, 262 ms,
3.3 %; MSS — 1.89 / 1.89 Mbps, 760 ms, 6.0 %. Queue size: "Queue size is
set to 200 ms except for DSL with 12 ms" [Tab.2 caption]; DSL queue "adds
further jitter (up to 12 ms)" [§3]. DSL/LTE loss set to 0.0 % ("we set no
artificial loss as the link-layer would recover it" [§3]).

**(ii) Grammar-v2 translation.**
ExperimentSet⟨leaves: sweep(
  website ∈ 36-site corpus [§3 "Websites Selection"]
  × cca-config ∈ {TCP, TCP+, TCP+BBR, QUIC, QUIC+BBR} [Tab.1]
  × net-setting ∈ {DSL, LTE, DA2GC, MSS} [Tab.2]
) = 36 × 5 × 4 = 720⟩;

Experiment = ⟨
  Foreground: Workflow(browser-page-load; params.url = website; engine = Chromium;
    cache = empty-per-visit [§3]) @ client-node;
  Regime⟨
    Static:
      capacity_down ∈ {25, 10.5, 0.468, 1.89} Mbps [Tab.2],
      capacity_up   ∈ {5,  2.8,  0.468, 1.89} Mbps [Tab.2],
      queue: size ∈ {12 ms (DSL), 200 ms (LTE/DA2GC/MSS)} [Tab.2 caption]
             (time-based, not buffer_packets; discipline Not specified);
    Dynamic: none (no cross-traffic stated)
  ⟩;
  path (per-workflow, varies by net-setting):
    latency ∈ {12, 37, 131, 380} ms one-way (half of min. RTT [Tab.2]);
    jitter: "up to 12 ms" for DSL [§3]; Not specified for LTE/DA2GC/MSS;
    loss_pct ∈ {0.0, 0.0, 3.3, 6.0} % [Tab.2];
  cca per protocol config:
    TCP:      cca = ⟨algo: cubic, stack: tcp-linux, params: {IW: 10}⟩ [Tab.1]
    TCP+:     cca = ⟨algo: cubic, stack: tcp-linux,
                     params: {IW: 32, pacing: true, no-slow-start-after-idle: true},
                     flags:  {tuned-send-recv-buffers}⟩ [Tab.1; §3 "Protocol Parametrization"]
    TCP+BBR:  cca = ⟨algo: bbr,   stack: tcp-linux, version: v1,
                     params: {IW: 32, pacing: true}⟩ [Tab.1; §3 fn.2]
    QUIC:     cca = ⟨algo: cubic, stack: quic-gquic,
                     params: {IW: 32, pacing: true}⟩ [Tab.1]
    QUIC+BBR: cca = ⟨algo: bbr,   stack: quic-gquic, version: v1,
                     params: {IW: 32, pacing: true}⟩ [Tab.1; §3 fn.2]
⟩;
iterations = ≥31 visits [§3 "at least 31 times"];
telemetry {app_metrics: true (FVC, LVC, PLT, SI, VC85 [§3]);
           video-recording: true (browser window captured for stimulus production [§3])};
Roles ⟨client: Chromium/Browsertime node;
       server: NGINX + gQUIC embedded in Mahimahi [§3]⟩.

### perceiving_quic-ES3–ES8 — Human-subjects user studies (OUT-OF-SCOPE)

**(i) Raw text (shared for all six).**
Lab A/B (Exp3, 35 participants [Tab.3]), Lab Rating (Exp4, 35 [Tab.3]), µWorker A/B
(Exp5, 233 final [Tab.3]), µWorker Rating (Exp6, 614 final [Tab.3]), Internet A/B
(Exp7, 155 final [Tab.3]), Internet Rating (Exp8, 138 final [Tab.3]). Participants
watch pre-recorded videos of website-loading processes from ES1's testbed campaign and
provide pairwise preferences (A/B: "if the left or right video was the faster one or
if they cannot decide" [§4 "Study 1 (A/B)"]) or scalar quality ratings (Rating:
"seven-point linear scale … ranging from extremely bad over … ideal" [§4 "Study 2
(Rating)"]) via TheFragebogen platform hosted on their infrastructure [§4]. No network
traffic is generated in these studies; stimuli are static pre-recorded video files
from ES1 [§3 "Producing Videos"].

**(ii–iv) Grammar / requirements / match.**
**Design: OUT-OF-SCOPE.**
These are human-subjects perception / user-experience studies. No network traffic is
generated; no controlled network Regime is varied. Pramana models network data
generation (controlled bottleneck + foreground workflows + telemetry); rating of
pre-recorded video stimuli by human participants is structurally outside this model.

**Implementation: n/a** (design is OUT-OF-SCOPE).
**Mininet: n/a.**

**confidence: high**
