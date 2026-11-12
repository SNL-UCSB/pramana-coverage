# converge — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| converge-ES1 | Exp1 | 1 (single motivation call pair) | 1 | Not specified |
| converge-ES2 | Exp2 | scheme ∈ {WebRTC,M-TPUT,SRTT,M-RTP,Converge} × camera_streams ∈ {1,2,3} [Tab 1; Fig 3] | 5 × 3 = 15 | Not specified |
| converge-ES3 | Exp3 | camera_streams ∈ {1,2,3} [Tab 3 Walking] | 3 | Not specified |
| converge-ES4 | Exp4 | camera_streams ∈ {1,2,3} [Tab 3 Driving] | 3 | Not specified |
| converge-ES5 | Exp5 | scenario ∈ 12 iperf3 scenarios [§6.2] | 12 | Not specified |
| converge-ES6 | Exp6 | feedback ∈ {with,without} [§6.2; Tab 4] | 2 | Not specified |
| converge-ES7 | Exp7 | path.loss ∈ {1,2,3,4,5,6,7,8,9,10} % [§6.2; Tab 5] | 10 | Not specified |
| converge-ES8 | Exp8 | scheme ∈ {WebRTC-V,WebRTC-T,WebRTC-CM,M-RTP,M-TPUT,SRTT,Converge} [Fig 14; §6.2] | 7 | Not specified |
| converge-ES9 | Exp9 | camera_streams ∈ {1,2,3} [Tab 6; Appendix A] | 3 | Not specified |

## Shared methodology (raw text, §6 experiments ES3,ES4,ES6,ES7,ES8,ES9) (quoted from the paper)


> "All experiments are conducted using a sample conference call lasting 3 minutes"
> [§6 preamble]; "with a video resolution of 1280x720" [§6 preamble];
> "a maximum encoding rate of 10 Mbps per stream" [§6 preamble]; "using the
> same video source [3]" = Big Buck Bunny [§6 preamble, ref [3]]; QoE metrics:
> received throughput, PSNR, video stall duration, quantization parameter (QP),
> E2E latency [§6 preamble]; normalization: throughput ÷ 10 Mbps, FPS ÷ 24,
> QP ÷ 60 [§6 preamble]; FEC overhead = % extra FEC packets; FEC utilization =
> fraction of generated FEC packets used for recovery [§6 preamble].
> Transport: WebRTC (RTP/RTCP); GCC congestion control per path, uncoupled [§4.1].
> Implementation: Converge built as part of the Chromium browser [§1; §5].
> Cross traffic: Not specified. Queue management: Not specified.


## Experiments

### converge-ES1 — Motivation: real-world WebRTC calls over live cellular (Fig 1)

**(i) Raw text.** "We conducted two video calls with WebRTC … using four devices
simultaneously. One call was made over T-Mobile and the other over Verizon"
[§1]; "with Full-HD resolution" [§1]; "a maximum encoding rate of 10 Mbps"
[§1]; "variations in cellular bandwidth (BW) with mobility" [Fig 1 caption].
Duration: x-axis 0–160 s implied by Fig 1 [Fig 1 x-axis "Time(s)"]; not stated
in text. Bandwidth/latency/queue/loss/CCA: Not specified. Number of repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(WebRTC
video call over live cellular) ⊗ Regime: no controlled bottleneck — real cellular
networks (T-Mobile, Verizon); conditions exogenous⟩ @ Roles⟨client: 4 mobile
devices, server: WebRTC endpoints over live cellular⟩; iterations: Not specified;
telemetry {app_metrics: true (BW, FPS, E2E latency [Fig 1 axes])}.

### converge-ES2 — §2.3 emulated multipath-variant study (Fig 3, Tab 1)

**(i) Raw text.** "These experiments were performed in an emulated network using
traces collected from two cellular carriers (T-Mobile and Verizon) while
driving along the highway" [§2.3]; "involving up to three camera streams" [§2.3];
"The maximum encoding rate of each camera stream is 10 Mbps" [§2.3]; "with Full
HD resolution" [§2.3]; schemes: WebRTC, M-TPUT (Musher), SRTT (minRTT), M-RTP
(MPRTP), Converge [§2.2; Fig 3 legend]; "all multipath WebRTC variants dropped a
significant number of frames and requested more keyframes" [§2.3]; FEC overhead
"reaching or exceeding 60%" [§2.3]; E2E latency ">500 ms" [§2.3].
Emulation tool: Not specified. Link parameters (bandwidth/latency/loss/queue): Not specified (determined by T-Mobile/Verizon driving traces). Repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scheme ∈ {WebRTC,M-TPUT,SRTT,
M-RTP,Converge} × camera_streams ∈ {1,2,3}) = 5 × 3 = 15⟩; Experiment =
⟨Workflow(WebRTC multipath video call; transport=WebRTC/RTP; browser=Chromium)
⊗ Regime⟨Static: Not specified — link parameters determined by cellular trace
replay; Dynamic: time-varying capacity from real T-Mobile+Verizon driving traces
[§2.3] — no CTP replay production; capacity varies with the trace, inexpressible
in A5 Regime.Static⟩⟩ @ Roles⟨client: emulated endpoint,
server: emulated endpoint⟩; iterations: Not specified; telemetry {app_metrics:
true (FPS/stream, freeze duration/stream, E2E latency, FEC overhead [Fig 3;
Tab 1])}.

### converge-ES3 — Real-world walking scenario (Fig 9a, Fig 10a, Tab 3 Walking)

**(i) Raw text.** "In the walking scenario, Converge utilized two networks, WiFi
and T-Mobile" [§6.1]; "as the laptops move in and out of network coverage" [§6.1];
"around 19-24 FPS" [§6.1]; "average FPS rates of 25 and 24, respectively,
representing 41% and 31% improvement over WebRTC" [§6.1]; FEC overhead improved
"68% … with 2.8× better utilization" [§6.1]; latency improvement "approximately
42% in latency compared to WebRTC over WiFi" [§6.1]. Swept: camera_streams ∈ {1,2,3} [Tab 3].
Shared-methodology block applies (3-min, 1280×720, 10 Mbps, Big Buck Bunny).
Repetitions: Not specified. Hardware: laptops [§6.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(camera_streams ∈ {1,2,3}) = 3⟩;
Experiment = ⟨Workflow(Converge WebRTC multipath call; Chromium) ⊗ Regime: real-world WiFi + T-Mobile cellular, no controlled bottleneck⟩ @ Roles⟨client:
laptops, server: WebRTC endpoints over live networks⟩; iterations: Not specified;
telemetry {app_metrics: true (throughput, FPS, stall, QP, E2E latency [Tab 3])}.

### converge-ES4 — Real-world driving scenario (Fig 9b, Fig 10b, Tab 3 Driving)

**(i) Raw text.** "in the driving scenario, it used Verizon and T-Mobile"
[§6.1]; "The driving scenario … utilizes two 4G/5G networks" [§6.1]; FEC
overhead improved "51% with 1.3× better utilization" [§6.1]; latency improvement
"approximately 20% compared to WebRTC over Verizon (WebRTC-V)" [§6.1]. Swept:
camera_streams ∈ {1,2,3} [Tab 3]. Shared-methodology block applies.
Repetitions: Not specified.

**(ii) Grammar.** INHERITED from ES3, delta: networks = Verizon + T-Mobile [§6.1].
ExperimentSet⟨leaves: sweep(camera_streams ∈ {1,2,3}) = 3⟩; Regime: real-world
4G/5G Verizon + T-Mobile, no controlled bottleneck.

### converge-ES5 — iperf3 network-trace collection campaign (Figs 11a, 20, 21, 22)

**(i) Raw text.** "The network environments used in this analysis were collected
at various times of the day using iperf3" [§6.2]; "resulting in 12 scenarios"
[§6.2]; "three representative scenarios: stationary, walking, and driving"
[Appendix D]; traces cover T-Mobile, Wi-Fi/Verizon [Fig 20/21/22 subcaptions];
trace duration: 0–200 s [Fig 20–22 x-axis "Time (S)"]. Path 1 ≈ 25 Mbps;
Path 2 drops to 0.5–2.5 Mbps from 30 to 90 seconds [§6.2].

**(ii) Grammar.** ExperimentSet⟨leaves: 12 scenarios [§6.2]⟩; Experiment =
⟨Workflow(iperf3 throughput measurement; shell) ⊗ Regime: real-world WiFi/cellular
capacity characterization — no imposed bottleneck; inhabited mode (probe
characterizes)⟩ @ Roles⟨client: measurement device, server: real network
endpoints⟩; iterations: Not specified; telemetry {app_metrics: true
(bandwidth time-series [Figs 20–22])}.

### converge-ES6 — QoE-feedback ablation in controlled environment (Fig 11b-d, Tab 4)

**(i) Raw text.** "we created a controlled network environment" [§6.2]; "The
network environments used in this analysis were collected at various times of
the day using iperf3" [§6.2]; Path 1 "maintains a consistent capacity of
approximately 25 Mbps" [§6.2]; Path 2 "drop to around 0.5-2.5 Mbps from 30
to 90 seconds" [§6.2]; compared: "baseline system utilizes the video-aware
scheduler from §4.1 … without QoE feedback" vs. "system that incorporates QoE
feedback as described in §4.2" [§6.2]; "the IFD value exceeds the expected
value of 33ms (1/30 of the frame rate)" [§6.2]; "the overall received rate
falls below the maximum encoding rate of 10 Mbps when feedback is not utilized"
[§6.2]; run length: 0–120 s shown [Fig 11 axes]. Emulation tool: Not specified.
Queue/congestion control: Not specified. Repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(feedback ∈ {with, without}) = 2⟩;
Experiment = ⟨Workflow(Converge WebRTC multipath call; Chromium) ⊗ Regime⟨
Static: path1.capacity ≈ 25 Mbps [§6.2]; path2 time-varying 0.5–2.5 Mbps
(30–90 s trace-driven [§6.2]); two independent paths — multipath regime;
no single-bottleneck A5 production; Dynamic: Not specified⟩⟩ @ Roles⟨client,
server: controlled-environment endpoints⟩; iterations: Not specified; telemetry
{app_metrics: true (video throughput, IFD, FCD [Fig 11]; frame drops, freeze
duration, keyframe requests [Tab 4])}.

### converge-ES7 — FEC trade-off controlled experiment (Figs 12, 13, Tab 5)

**(i) Raw text.** "we create a controlled environment with two paths of 15 Mbps
capacities, 100ms propagation delay, and varying loss levels from 0-10%" [§6.2];
Tab 5 "Loss rate (%)" columns: 1,2,3,4,5,6,7,8,9,10 [Tab 5]; compared:
"path-specific loss-based FEC controller" (Converge) vs. "default WebRTC
mechanism" (table-based FEC) [§6.2]; at 1% loss, WebRTC overhead ~40 extra FEC
packets per 100 media (~40% overhead) [§6.2]; "at a 10% packet loss rate … the
Converge method reduces frame drops by 97% … 67% reduction in freeze duration
and 66% fewer keyframe requests" [§6.2]. Emulation tool: Not specified.
Number of camera streams: Not specified. Duration: Not specified. Repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(path.loss ∈ {1,2,3,4,5,6,7,8,9,10} % [§6.2; Tab 5]) = 10⟩; Experiment = ⟨Workflow(WebRTC video call;
Chromium; scheme ∈ {Converge-FEC, WebRTC-table-FEC}) ⊗ Regime⟨Static: two
paths, capacity_down 15 Mbps each [§6.2], path.latency 100 ms [§6.2]; loss
∈ {1,…,10} % per path [§6.2; Tab 5]; two-path topology — multipath regime;
no dual-path A5 production; Dynamic: Not specified⟩⟩ @ Roles⟨client, server:
controlled endpoints⟩; iterations: Not specified; telemetry {app_metrics: true
(FEC overhead %, FEC utilization %, frame drops, freeze duration, keyframe
requests [Figs 12,13; Tab 5])}.

### converge-ES8 — Comparison with existing solutions, controlled driving scenario (Figs 14, 15)

**(i) Raw text.** "We compared the performance of Converge in both the 'walking'
and 'driving' scenarios, but we present only the results for the 'driving'
scenario" [§6.2]; "The network environments used in this analysis were collected
at various times of the day using iperf3" [§6.2]; schemes: WebRTC-V, WebRTC-T,
WebRTC-CM, M-RTP, M-TPUT, SRTT, Converge [Fig 14 caption; §6 preamble];
"an average delivered throughput of 38% of the encoding rate at the sender"
[§6.2]; "Its FEC overhead is 10% during driving" [§6.2]; Verizon path latency
"0.3 to .6 seconds" [§6.2]; "the Verizon path has video conferencing latency
between 0.3 to .6 seconds" [§6.2]. Emulation tool: Not specified. Static
link parameters: Not specified (driven by iperf3 driving trace). Repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scheme ∈ {WebRTC-V,WebRTC-T,
WebRTC-CM,M-RTP,M-TPUT,SRTT,Converge}) = 7⟩; Experiment = ⟨Workflow(multipath
WebRTC call; Chromium; scheme per leaf) ⊗ Regime⟨Static: Not specified — link
parameters driven by iperf3-collected driving-scenario trace; two paths,
time-varying capacity, multipath regime; no A5 production⟩⟩ @ Roles⟨client,
server: controlled-environment endpoints⟩; iterations: Not specified; telemetry
{app_metrics: true (normalized QoE, FEC overhead/utilization, E2E latency CDF,
PSNR [Figs 14,15])}.

### converge-ES9 — Real-world stationary scenario (Figs 16, 17, Tab 6)

**(i) Raw text.** "we also evaluated the performance of Converge in the
stationary case without mobility" [Appendix A]; "Converge utilizes two networks,
WiFi and T-Mobile" [Appendix A]; "maintain a consistent video throughput of
around 10 Mbps, achieve a frame rate of approximately 30 FPS" [Appendix A];
"outperforms WebRTC-W by approximately 41% in terms of throughput and surpasses
WebRTC-T by a factor of 2.67" [Appendix A]; "approximately 7% higher than
that of WebRTC-W" [Appendix A] for E2E latency. Swept: camera_streams ∈ {1,2,3}
[Tab 6]. Shared-methodology block applies.
Repetitions: Not specified.

**(ii) Grammar.** INHERITED from ES3, delta: no mobility (stationary); networks =
WiFi + T-Mobile [Appendix A]. ExperimentSet⟨leaves: sweep(camera_streams ∈
{1,2,3}) = 3⟩; Regime: real-world WiFi + T-Mobile cellular, no controlled
bottleneck.
