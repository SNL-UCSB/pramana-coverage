# webrtc_live_streaming — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Rendering row | Description | Leaves |
| --- | --- | --- | --- |
| webrtc_live_streaming-ES1 | Exp1 | HTTP-FLV pre-buffer 6s→3s A/B, production Douyin [§2.2] | n/a |
| webrtc_live_streaming-ES2 | Exp2 | Vanilla-RTM vs HTTP-FLV 1-week A/B, 450M sessions/arm [§2.3.2] | n/a |
| webrtc_live_streaming-ES3 | Exp3 | Illustrative online viewer session: AV drift [§4.2.1] | n/a |
| webrtc_live_streaming-ES4 | Exp4 | Startup-pacing parameter-tuning A/B tests (text-only) [§4.3.2] | n/a |
| webrtc_live_streaming-ES5 | Exp5 | Light-weight SDP rollout observation (text-only) [§5.1] | n/a |
| webrtc_live_streaming-ES6 | Exp6 | Integrated-pipeline sensitivity A/B, 1 week [§5.1.1] | n/a |
| webrtc_live_streaming-ES7 | Exp7 | Audio-calibrated-sync sensitivity A/B, 1 week [§5.1.2] | n/a |
| webrtc_live_streaming-ES8 | Exp8 | Bitrate-limited-startup sensitivity A/B, 1 week [§5.1.3] | n/a |
| webrtc_live_streaming-ES9 | Exp9 | RTM vs HTTP-FLV 2-week A/B, 2024Q4 [§5.2] | n/a |
| webrtc_live_streaming-ES10 | Exp10 | Competitor case study: FIFA World Cup 2022 [§5.3] | n/a |
| webrtc_live_streaming-ES11 | Exp11 | Competitor case study: Asian Games 2023 [§5.3] | n/a |

## Experiments

### webrtc_live_streaming-ES1 — HTTP-FLV pre-buffer A/B test

**(i) Raw text.** "an online A/B test conducted in the initial phase of
optimizing HTTP-FLV" [§2.2]. Pre-buffering duration changed from 6 seconds to
3 seconds; "we only changed the configured pre-buffering duration" [§2.2].
Results: end-to-end delay −39.3%, video stall duration +71.6%, video stall
count +82.0%, stall session ratio +69.7% [Table 1; §2.2]. Platform: Douyin
production [§1]. Duration, session counts: Not specified beyond "billions" [§5.1].
No network Regime controlled.

**(ii) Grammar.** OUT-OF-SCOPE. Production A/B test on deployed Douyin
infrastructure. The experiment variable is a software configuration parameter
(pre-buffering duration), not a network Regime setting. No Regime expression
possible.

### webrtc_live_streaming-ES2 — Vanilla-RTM vs HTTP-FLV 1-week A/B

**(i) Raw text.** "a one-week A/B test" [§2.3.2]. "450 million viewer sessions
for each" arm [§2.3.2]. Vanilla-RTM: RTP-based streaming, ICE, customized SDP,
BBR-based CC with random-loss detection [§2.3.1]. Transport: Vanilla-RTM = RTP
(WebRTC stack) vs HTTP-FLV = TCP [§4.3.1]. Results (Fig 2): e2e latency −49.6%,
audio stall −41.6%, video stall −9.5%, first-frame delay +7.4%, viewer
penetration −0.70%, daily viewing time −1.28% [§2.3.2]. Platform: Douyin
production. No network Regime controlled.

**(ii) Grammar.** OUT-OF-SCOPE. Production A/B test on deployed infrastructure
comparing two streaming protocols. No controlled Regime.

### webrtc_live_streaming-ES3 — Illustrative AV-drift viewer session

**(i) Raw text.** "Figure 5 showcases an online viewer session. Due to the
bursty losses and fluctuating RTTs, it suffers from over 300 ms AV drift for
nearly 30 seconds" [§4.2.1]. WebRTC sync adjustment: once per second by
default, each bounded by 80 ms [§4.2.1]. Single production session; no
described collection campaign; provenance: "an online viewer session" [§4.2.1].

**(ii) Grammar.** OUT-OF-SCOPE. A single production viewer session selected
for illustration; bursty losses and fluctuating RTTs are exogenous real-network
events, not controlled parameters. No Regime expression possible.

### webrtc_live_streaming-ES4 — Startup-pacing parameter-tuning A/B tests (text-only)

**(i) Raw text.** "find the best configurations for each tier through multiple
rounds of large-scale A/B tests" [§4.3.2]. "typical setup for viewers with an
ideal access link adopts D_s = 600 Kbit and G_m = 1.1" [§4.3.2]. Viewer
link-quality tier determined from short viewing history [§4.3.2]. Platform:
Douyin production. Number of rounds, session counts, tier definitions: Not
specified.

**(ii) Grammar.** OUT-OF-SCOPE. Multiple rounds of production A/B tests tuning
algorithm parameters (D_s, G_m) for bitrate-limited startup pacing. No
controlled network Regime.

### webrtc_live_streaming-ES5 — SDP rollout observation (text-only)

**(i) Raw text.** "there is no separate A/B test for that" [§5.1]. "lowers the
first-frame delay of RTM by around 10% after being rolled out in the live
streaming scenario" [§5.1]. Rollout: "initially developed as a general
WebRTC-stack enhancement and first verified in our RTC services (e.g., Lark)"
[§4.4]. Platform: Douyin production rollout.

**(ii) Grammar.** OUT-OF-SCOPE. Observational rollout — explicitly not an A/B
test. No controlled Regime; no described collection campaign.

### webrtc_live_streaming-ES6 — Integrated-pipeline sensitivity A/B

**(i) Raw text.** "one of 'multiple one-week online A/B tests specific to each
optimization mechanism'" [§5.1]. Compared: with vs without integrated media
pipeline [Fig 8 legend]. Results: CPU −1.48%, first-frame delay −5.4%, startup
rebuffering −7.2%/−4.9%, viewer penetration +0.22%, daily viewing time +1.0%
[§5.1.1, Fig 8]. Platform: Douyin production.

**(ii) Grammar.** OUT-OF-SCOPE. Production A/B test; controlled variable is
a software architecture change (shared codec object, jitter buffer routing), not
a network Regime parameter. No Regime expression possible.

### webrtc_live_streaming-ES7 — Audio-calibrated-sync sensitivity A/B

**(i) Raw text.** "one of 'multiple one-week online A/B tests'" [§5.1].
Mechanism: two-stage AV sync with threshold th_a = 25 ms [§4.2.2]; target delay
aligned to 95th-percentile inter-packet jitter [§4.2.2]. Drift definition:
audio ahead by > 90 ms or lagging by > 185 ms [§5.1.2]. Results: drift duration
−90.2%, drifted session ratio −87.4%; video rebuffering +10.2%/+8.4%; daily
viewing time +1.61% [§5.1.2, Fig 9]. Platform: Douyin production.

**(ii) Grammar.** OUT-OF-SCOPE. Production A/B test; controlled variable is
an AV synchronization algorithm, not a network Regime parameter.

### webrtc_live_streaming-ES8 — Bitrate-limited-startup sensitivity A/B

**(i) Raw text.** "one of 'multiple one-week online A/B tests'" [§5.1].
Compared: with vs without bitrate-limited startup [Fig 10 legend]. Metric window:
first 4 seconds of each viewer session [§5.1.3]. Results: startup rebuffering
instances −8.3%, duration −12.2%; whole-session rebuffering −10.0%/−12.0%;
viewer penetration +0.48% [§5.1.3, Fig 10]. Platform: Douyin production.

**(ii) Grammar.** OUT-OF-SCOPE. Production A/B; controlled variable is a
startup pacing algorithm, not a network Regime parameter.

### webrtc_live_streaming-ES9 — RTM vs HTTP-FLV 2-week A/B (2024Q4)

**(i) Raw text.** "a recent 2-week A/B test conducted in 2024Q4" [§5.2].
Compared: RTM (optimized WebRTC stack, §4 improvements) vs HTTP-FLV (years of
optimization) [§5.2]. Results (Fig 11, Fig 12): e2e latency −54.5%, first-frame
delay −10.6%, startup rebuffering count −71.8%, CPU +0.15%, AV drift duration
similar, drifted sessions +8.1%; viewer penetration +0.03%, daily viewing time
+0.39%, paid orders +0.8% [§5.2]. Platform: Douyin production.

**(ii) Grammar.** OUT-OF-SCOPE. Production A/B; controlled variable is the
streaming protocol stack (RTM vs HTTP-FLV), not a network Regime parameter.

### webrtc_live_streaming-ES10 — Competitor case study: FIFA World Cup 2022

**(i) Raw text.** "two smartphones of identical device brand and identical
operating system version, connected to the same WiFi network, placed on the
same desk; open Douyin and one competitor, click the same match, compare time
difference of seeing the same video frame" [§5.3, "Test methodology"]. "10 data
points per trial spanning at least 10 minutes" [§5.3]. "repeatedly iterated
among the four competitors in multiple trials on multiple days" [§5.3]. Latency
differences: Douyin −31 s vs Competitor A, −3.5 s vs Competitor B [Table 2].
All competitors broadcast from same exclusive rights holder [§5.3, footnote 5].
Network: real WiFi shared by both devices. Competitors C, D marked × (non-rights
holders for this event) [Table 2].

**(ii) Grammar.** OUT-OF-SCOPE. Field measurement over a real WiFi access link
with real production streaming apps (Douyin and uncontrolled competitors). WiFi
physical layer is the access medium — OUT-OF-SCOPE per CORPUS_PROMPT_v4
("WiFi-PHY → OUT-OF-SCOPE"). Additionally, no network Regime is configured:
the WiFi network is shared and uncontrolled.

### webrtc_live_streaming-ES11 — Competitor case study: Asian Games 2023

**(i) Raw text.** "19th Asian Games in 2023" [§5.3; Table 2]. Methodology,
repetitions, content-source conditions: identical to ES10 [§5.3, "Test
methodology" covers both events]. Latency differences: Douyin −14 s vs
Competitor A, −4.3 s vs Competitor C, −5.8 s vs Competitor D [Table 2].
Competitor B marked × (non-rights holder for this event) [Table 2].
"competitor A approximately halved its end-to-end latency" between the two
events [§5.3]. Competitor identities, smartphone model, OS, WiFi bandwidth:
Not specified.

**(ii) Grammar.** OUT-OF-SCOPE. INHERITED from ES10 (WiFi PHY + exogenous
production apps). The Asian Games is a separately collected campaign (different
event date, different year, different competitor availability), confirming ES10
and ES11 as two distinct ExperimentSets, but both are OUT-OF-SCOPE.
