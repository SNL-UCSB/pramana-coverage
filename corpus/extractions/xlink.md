# xlink — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Upstream row | Scope verdict | Primary reason |
| --- | --- | --- | --- |
| xlink-ES1 | Exp1 — Campus-walk trace replay of vanilla-MP (Mahimahi) [§3.1; Fig 1a/1b] | OUT-OF-SCOPE | Mahimahi network emulator (simulator class) |
| xlink-ES2 | Exp2 — Production A/B test: vanilla-MP vs. SP, one week [§3.3; Fig 1c, Tab 1] | OUT-OF-SCOPE | Production deployment, real users (exogenous) |
| xlink-ES3 | Exp3 — Path-delay measurement study [§3.2; Tab 4] | OUT-OF-SCOPE | Passive measurement; no controlled network |
| xlink-ES4 | Exp4 — Trace-replay: re-injection variants (Mahimahi/mpshell) [§5.2.2; Fig 6] | OUT-OF-SCOPE | Mahimahi/mpshell multi-path simulator |
| xlink-ES5 | Exp5 — First-frame delivery on 5G SA testbed + enterprise Wi-Fi [§5.3; Fig 7] | OUT-OF-SCOPE | Physical-layer radio testbed; no tc/netem bottleneck |
| xlink-ES6 | Exp6 — ACK_MP path selection with Mahimahi, Cubic, swept RTT ratio [§5.3; Fig 8] | OUT-OF-SCOPE | Mahimahi network emulator (simulator class) |
| xlink-ES7 | Exp7 — Online double-threshold study, real Taobao users [§7.1; Fig 10, Tab 2] | OUT-OF-SCOPE | Real users, online deployment (exogenous) |
| xlink-ES8 | Exp8 — Large-scale A/B test: XLINK vs. SP, >100K participants [§7.2; Fig 11, Tab 3, Fig 12] | OUT-OF-SCOPE | Production A/B test, real users (exogenous) |
| xlink-ES9 | Exp9 — Extreme-mobility trace-driven evaluation (Mahimahi/mpshell) [§7.3; Fig 13, Fig 15] | OUT-OF-SCOPE | Mahimahi/mpshell multi-path simulator |
| xlink-ES10 | Exp10 — Energy consumption on Android phones [§7.4; Fig 14] | OUT-OF-SCOPE | Physical device energy measurement; no network bottleneck control |

## Shared methodology (raw text, for context) (quoted from the paper)


> XLINK is a multi-path QUIC transport system for short video services, deployed in
> Taobao (Alibaba). XLINK's client is implemented in XQUIC (Alibaba's IETF QUIC
> implementation) in C, integrated into the Taobao Android app [§6]. Congestion
> control: Cubic ("decoupled" for multi-path) throughout the §7 evaluation [§7 preamble].
> Emulation uses Mahimahi with the multi-path extension (mpshell) [Appx B]. Production
> A/B tests involve >100K participants and >3-million video plays [§7 intro].

---


## Experiments

### xlink-ES1 — Campus-walk trace replay of vanilla-MP (Fig 1a/1b)

**(i) Raw text.** "we plot the dynamics of its in-flight packets replayed with a pair
of Wi-Fi & LTE traces collected when walking on our campus shown in Fig. 1a and 1b
with the Mahimahi emulation tool" [§3.1]; multi-path extension of Mahimahi used [§3.1
footnote 5]. Signals: link capacity, in-flight packets, CWND [Fig 1a/1b legends].
Duration and CCA: Not specified (§7 Cubic preamble not applied backward to §3).

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES2 — Production A/B test: vanilla-MP vs. SP (Fig 1c, Tab 1)

**(i) Raw text.** "we verified the effectiveness of vanilla-MP by conducting a
large-scale A/B test against single-path QUIC (SP) in our short video services" [§3.3];
"throughout one week" [§3.3]; "The largest median RCT degradation was 16%" [§3.3];
"99th percentile RCT could be even 28% worse than SP" [§3.3]; rebuffer rate "increased
more than 34%, largest increase up to 96%" [§3.3].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES3 — Path-delay measurement study (Tab 4; text-only in §3.2)

**(i) Raw text.** "We measured RTTs when accessing our video services via different
wireless technologies" [§3.2]; authors' 5G SA testbed deployed [§3.2]; Table 4 shows
cross-ISP LTE delay increases: A→B 21%, A→C 17%, B→A 42%, B→C 54%, C→A 39%,
C→B 34% [Tab 4]; text results: median LTE path delay 2.7 times that of Wi-Fi and 5.5
times that of 5G SA [§3.2]; 90th percentile LTE 3.3 times that of Wi-Fi [§3.2].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES4 — Trace-replay: re-injection variants (Fig 6)

**(i) Raw text.** "We test vanilla-MP (Fig. 6b), re-injection without QoE control
(Fig. 6c) and re-injection with QoE control (Fig. 6d)" [§5.2.2]; "replayed with the
same network traces shown in Fig. 6a" [§5.2.2]; Mahimahi multi-path extension (mpshell)
inferred from Appx B general methods statement.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES5 — First-frame delivery: 5G SA testbed + enterprise Wi-Fi (Fig 7)

**(i) Raw text.** "We measured the first-frame delivery time vs. different frame sizes
when starting a multi-path connection from different wireless interfaces in Fig. 7.
The measurement was conducted with our 5G SA test-bed and enterprise Wi-Fi" [§5.3];
swept factor: first frame size ∈ {128K, 256K, 512K, 1M, 2M} bytes [Fig 7 x-axis];
compared: WiFi primary vs. 5G primary [Fig 7 legend].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES6 — ACK_MP path selection strategies (Fig 8)

**(i) Raw text.** "We show the effect of the two ACK path selection strategies with
Cubic congestion control in Fig. 8. We measured the request completion time of a 4MB
load by changing the path RTT ratio between two paths of equal bandwidth with Mahimahi"
[§5.3]; RTT ratio swept: {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1} [Fig 8 x-axis];
strategies: ACK_MP on min-RTT path vs. ACK_MP on original path [Fig 8 legend].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES7 — Online double-threshold study (Fig 10, Tab 2)

**(i) Raw text.** "we report data from real users who upgraded to Taobao Android app
with XLINK" [§7 intro]; thresholds tested: off, (95,80), (90,80), (90,60), (60,50),
(60,1), (1,1) [Fig 10 x-axis; Table 2]; most cost-efficient: (95,80) at 66% improvement
in re-buffering probability with 2.1% overhead [§7.1].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES8 — Production A/B test: XLINK vs. SP (Fig 11, Tab 3, Fig 12)

**(i) Raw text.** "The total number of participants was over 100K and our measurements
consisted of over 3-million video plays" [§7 intro]; RCT over two weeks [§7.2];
rebuffer rate over one week [§7.2]; first-video-frame latency feature toggled [§7.2];
2.3% to 8.9% (median) / 9.4% to 34% (95th) / 19 to 50% (99th) day-to-day RCT
improvements [§7.2]; rebuffer rate reduction 23.8% to 67.6% [§7.2].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES9 — Extreme-mobility trace-driven evaluation (Fig 13, Fig 15)

**(i) Raw text.** "We collected LTE and onboard Wi-Fi traces in subways and high-speed
rails" [§7.3]; "conducted trace-driven evaluation with Mahimahi emulation tools" [§7.3];
mpshell multi-path extension [Appx B]; schemes: SP, vanilla-MP, MPTCP, CM, XLINK
[§7.3]; 10 traces [Fig 13 x-axis "Trace #ID" 1–10]; simple C video player, constant
bit-rate, sequential chunk requests [Appx B]; Cubic/decoupled [§7 preamble].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xlink-ES10 — Energy consumption on Android phones (Fig 14)

**(i) Raw text.** "three popular 5G-NSA-capable Android smartphone models" [§7.4];
chipsets Snapdragon 765G and Kirin 990 [§7.4]; downloaded "different sized loads
(10MB-50MB)" [§7.4]; link speed capped to 30Mbps [§7.4]; link configurations: WiFi,
LTE, NR, WiFi-LTE, WiFi-NR [Fig 14 legend]; in-house Android energy monitoring tool
[§7.4].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.
