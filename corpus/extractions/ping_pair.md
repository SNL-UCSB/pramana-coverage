# ping_pair — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering rows | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| ping_pair-ES1 | Exp1, Exp4, Exp8, Exp10, Exp11 | Wi-Fi AP testbed; Exp8: TCP flow count ∈ {0…7} × band ∈ {2.4 GHz, 5 GHz} [§8.1; Table 1]; Exp11: contenders ∈ {0,1,2,3,4} [Fig 6 x-axis]; others: single-scenario | Not specified aggregate; Exp8: 8 flow-count steps × 2 bands; Exp11: 5 contender levels; Exp1/Exp4/Exp10: 1 each | Exp8: 30 Ping-Pair measurements per step [§8.1]; Exp11: ~1500 estimates per contender level [§8.2]; others Not specified |
| ping_pair-ES2 | Exp2, Exp5, Exp6, Exp7, Exp9 | Text-only; no parameterized sweep described | Not specified | Not specified |
| ping_pair-ES3 | Exp12, Exp13, Exp14 | Kwikr-enabled vs unmodified Skype on Wi-Fi; Exp12: 40 runs (20 Kwikr, 20 control) [§8.3]; Exp13: Not specified; Exp14: 30 runs across 3 co-existence conditions [§8.3] | Exp12: 1 (one Wi-Fi congestion setting); Exp13: 1 (token-bucket throttle); Exp14: 3 co-existence configurations [Table 2] | Exp12: 40 total runs [§8.3]; Exp14: 30 total runs [§8.3]; Exp13 Not specified |
| ping_pair-ES4 | Exp3, Exp15 | Exp3: 171 unique Wi-Fi APs from 166 users across 14 countries [§5.5]; Exp15: 119,789 production video calls Dec 9–16, 2016 [§8.4] | Not specified (exogenous) | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Wi-Fi access point downlink queue as the bottleneck; Ping-Pair technique sends
> back-to-back ICMP packets differentiated by 802.11e WMM priority; response-order
> reversal indicates whether the AP downlink queue is congested [§5.1–§5.4]. All
> controlled testbed experiments use real 802.11 Wi-Fi hardware (Netgear WNDR3800
> OpenWRT Chaos Calmer 15.05 for Exp8 [§8.1]; APs from LinkSys, TP-Link, Cisco, D-Link
> for Exp9; unspecified AP model elsewhere). Client hardware: Android phones for Exp12–14
> [§8.3], Windows laptops for Exp1 [§8.3], Linux workstation for Exp11. Cross-traffic when
> present: TCP bulk transfers from other Wi-Fi clients (Exp8: 0–7 flows; Exp12/Exp10:
> parallel TCP downloads) or token-bucket filter on AP (Exp13). Probing: Ping-Pair twice
> per second [§6]; congestion threshold 5 ms on Ping-Pair delay estimate for both
> bands [§8.1]. Backbone wired link bandwidth, RTT, queue management: Not specified
> throughout.


## Experiments

### ping_pair-ES1 — Controlled Wi-Fi testbed characterization (Exp1, Exp4, Exp8, Exp10, Exp11)

**(i) Raw text.** Exp1: Skype, FaceTime, and Hangouts AV streams vs TCP bulk (6 devices
[§3]) on Wi-Fi; congestion introduced/withdrawn [§3; Fig 1 caption]. Exp4: dual-Ping-Pair
mobility experiment; client moved close/far from AP; link-layer retransmissions up to 6
observed; EWMA-filtered estimates [§5.6; Fig 4 caption]. Exp8: OpenWRT Netgear WNDR3800
(Chaos Calmer 15.05) instrumented with frame-queue logging [§8.1]; TCP flows 0–7 to other
Wi-Fi clients; 30 Ping-Pair measurements per step [§8.1]; 10-fold cross-validation decision
tree; 5 ms threshold derived [§8.1]. Exp10: two APs on same channel; UDP client on first AP;
6 clients running 20 parallel TCP bulk transfers each on second AP, congested for 30 seconds
[§8.1; Fig 5]. Exp11: channel access delay estimator (~600 LOC C; raw Linux sockets
[§7.2]); contenders upload UDP at one-packet-per-1 ms [§8.2]; ~1500 estimates per level
[§8.2]; 95% CI error bars [Fig 6 caption].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(Wi-Fi AP scenario × cross-traffic load ×
band (Exp8: 8 load-steps × 2 bands); Exp11: 5 contender levels; Exp1/4/10: 1 each)⟩;
Experiment = ⟨Workflow(Ping-Pair probing; AV/bulk app traffic) ⊗ Regime⟨Bottleneck: 802.11
Wi-Fi link at AP; capacity Not specified; queue: AP downlink buffer, depth Not specified;
Dynamic: TCP bulk flows (Exp1/8/10) | mobility/retransmission (Exp4) | UDP contenders
(Exp11)⟩⟩; path: 802.11 wireless channel characteristics (no v2 grammar production);
iterations per §8.1/§8.2 above; telemetry {app_metrics: true (Ping-Pair delay estimates,
WMM reversal, OWD [Exp10]), qtrace: true (Exp8: AP frame-queue log [§8.1])}.

### ping_pair-ES2 — Text-only Wi-Fi field validation (Exp2, Exp5, Exp6, Exp7, Exp9)

**(i) Raw text.** Exp2: Ping-triplet technique for WMM detection; 6 Wi-Fi networks from
various manufacturers; reversal in at least 3 of 5 runs leads to accurate detection
[§5.5]. Exp5: enterprise thin-AP settings (Aruba, Cisco); accurate WMM detection because
TOS bits preserved [§5.7]. Exp6: TP-Link range-extender; WMM and TOS bits preserved;
accurate detection [§5.7]. Exp7: Android raw-socket vs ping-based implementation; 1 ms vs
0 ms uncongested; 180 ms vs 183 ms congested [§7.3]. Exp9: qualitative Ping-Pair
detection on LinkSys/TP-Link/Cisco/D-Link APs; TCP bulk cross-traffic introduced [§8.1].
No figures or tables for any of these experiments.

**(ii) Grammar.** ExperimentSet⟨leaves: Not specified (no parameterized sweep in
text)⟩; Experiment = ⟨Workflow(Ping-Pair probing) ⊗ Regime⟨Bottleneck: 802.11 Wi-Fi
link; all parameters Not specified⟩⟩; iterations Not specified; no quantitative
telemetry reported.

### ping_pair-ES3 — Kwikr application evaluation on Wi-Fi (Exp12, Exp13, Exp14)

**(i) Raw text.** Exp12: 40 experiments; Skype for Android (version 7.23.0.245 onwards
[§8.3]); half Kwikr-enabled; three-minute calls; TCP cross-traffic during middle minute
(2 clients × 20 parallel threads downloading from wired server) [§8.3; Fig 8 caption].
Exp13: three-minute calls, bandwidth throttled mid-stream via token-bucket filter on
regular AP [§8.3]; both regular and Kwikr-enabled Skype. Exp14: 30 experiments; two
simultaneous two-minute calls; 10 both-Kwikr, 10 one-Kwikr, 10 neither [§8.3; Table 2].
All on Android phones [§8.3]. Kwikr config: β = 4 [§6]; probing twice per second [§6];
channel access delay 0.125 ms fixed [§7.3]; congestion threshold 5 ms [§8.1].

**(ii) Grammar.** ExperimentSet⟨leaves: Exp12: 2 conditions (Kwikr / no-Kwikr) × 20 runs
each = 40; Exp13: 2 conditions (Kwikr / no-Kwikr), run count Not specified; Exp14:
3 × 10 runs = 30⟩; Experiment = ⟨Workflow(Skype for Android, Kwikr-enabled or baseline)
⊗ Regime⟨Bottleneck: 802.11 Wi-Fi link at AP; Dynamic: TCP bulk cross-traffic (Exp12) |
token-bucket filter on AP (Exp13) | no additional cross-traffic (Exp14)⟩⟩; iterations:
Exp12 40 total [§8.3]; Exp14 30 total [§8.3]; Exp13 Not specified; telemetry
{app_metrics: true (per-call average data rate, RTT percentiles, loss percentiles)}.

### ping_pair-ES4 — Exogenous/passive measurements (Exp3, Exp15)

**(i) Raw text.** Exp3: Mechanical Turk study; 171 unique Wi-Fi APs from 166 users across
14 countries; IRB approved [§5.5 fn3]; WMM prevalence outcome: 77% of APs [§5.5].
Exp15: production A/B deployment of Kwikr in Skype for Android v7.23.0.245+; 119,789
video calls from Dec 9–16, 2016 [§8.4]; average call duration 967 seconds [§8.4];
~8.5% gain in median bandwidth [§1]; existing telemetry reports bandwidth over entire
calls only [§8.4].

**(ii) Grammar.** ExperimentSet⟨leaves: Exp3: 171 unique APs (user-provided,
uncontrolled); Exp15: 119,789 calls (production logs, uncontrolled)⟩; sweep: exogenous
(user-provided home/office Wi-Fi networks); all network parameters Not specified (user
hardware and environment); telemetry {app_metrics: true (WMM prevalence for Exp3;
call bandwidth/RTT/loss for Exp15)}.
