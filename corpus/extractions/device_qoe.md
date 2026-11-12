# device_qoe — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| device_qoe-ES1 | Exp1 (Fig 1) | (no network experiment — dataset analysis) | n/a | n/a |
| device_qoe-ES2 | Exp2 (Fig 2) | device_type ∈ 7 smartphones [§2] × workflow ∈ {chrome, youtube, skype} [§2.1] | 7 × 3 = 21 | 20 [§2.1] |
| device_qoe-ES3 | Exp3 (Figs 3–5) | device_param ∈ {clock(12), memory(4), cores(4), governor(4)} × workflow ∈ {chrome, youtube, skype} [§3] | Not specified (4 params × multiple values × 3 apps; Nexus4 detail only) | 20 [§2.1] |
| device_qoe-ES4 | Exp4 (Fig 6) | clock_frequency ∈ {384,486,594,702,810,918,1026,1134,1242,1350,1458,1512} MHz [§4.1 / Fig 6] | 12 | 20 [§4.1] |
| device_qoe-ES5 | Exp5 (Fig 7) | (offline ePLT re-evaluation — no live network) | n/a | n/a |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> "video and pages hosted on a desktop on the authors' LAN, created using
> an Aruba Access Point with 72 Mbps link speed, 10 ms RTT, and 0% loss;
> mobile device connects to the server over the LAN" [§2.1]. "each workload
> repeated 20 times; average and standard deviation reported" [§2.1].
> Applications: Google Chrome 63.0.3239.111, YouTube, Skype [§2.1].
> Web workload: top 50 Web pages from Alexa; DNS + cache cleared [§2.1].
> Video workload: 5 min FullHD (1080p) video clip [§2.1].
> Cross traffic: Not specified. Congestion control: Not specified.
> Queue management: Not specified.


## Experiments

### device_qoe-ES1 — Fig 1 motivation trend dataset

**(i) Raw text.** "See Figure 1, which uses the page load history [4] and
device data mined from over 480 Android smartphone specifications over the
past 8 years" [§1]. "page load times (PLT) have increased by four ×" [§1].
Plotted quantities: PLT, Page Size, Clock, Cores, Memory, OS Version over
2011–2018 [Fig 1 axes]. Network: Not specified (dataset figure, no measurement
network). Hardware/testbed: Not specified. Repetitions: Not specified.

**(ii) Grammar.** Not applicable — this figure presents mined device
specification data (480+ Android smartphone specs [§1]) and an external dataset
(HTTP Archive PLT history [4]); no network Workflow or Regime exists. There is
no ExperimentSet in the Pramana sense: no packet flows are generated, no
bottleneck is imposed, and no application runs over an emulated path.

### device_qoe-ES2 — §2 cross-device QoE study

**(i) Raw text.** "we study the performance of the three Internet applications
(Web browsing, video streaming, and video telephony) across seven different
smartphones" [§2]; LAN: "72 Mbps link speed, 10 ms RTT, and 0% loss" [§2.1];
"each workload repeated 20 times" [§2.1]; devices: Intex Amaze+, Gionee F103,
Nexus4, SG S2-Tab, Pixel C-Tab, Pixel2, SG S6-edge [Table 1 / §2]; cost
"$60 to $880" [§2]; "maximum CPU clock frequencies range from 1.3 GHz to
2.4 GHz" [§2]. Applications: Google Chrome (top-50 Alexa pages), YouTube
(5 min FullHD), Skype video call [§2.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(device_type ∈ 7 smartphones [§2]
× workflow ∈ {chrome_pageload, youtube_stream, skype_call} [§2.1]) = 7 × 3 = 21;
ATTEMPTED⟩; Experiment = ⟨Workflow(per-leaf) ⊗ Regime⟨Static: capacity_down
72 mbps [§2.1], path.latency 10 ms [§2.1], path.loss 0% [§2.1]; queue Not
specified; Dynamic: Not specified (silence — controlled LAN, no cross-traffic
statement)⟩⟩ @ Roles⟨client: mobile phone on LAN, server: desktop on same
LAN⟩; iterations 20 [§2.1]; telemetry {app_metrics: true (PLT, start-up
latency, stall ratio, call setup delay, frame rate)}.

**Grammar gap (G2):** `device_type` is the primary sweep dimension; it has no
production in v2 grammar or A5 field vocabulary. NodeDescriptor `attrs` could
label the device model but cannot provision distinct phone hardware.

### device_qoe-ES3 — §3 device-parameter isolation study

**(i) Raw text.** "The experimental setup is the same as that of §2.1" [§3];
parameters swept: "CPU clock, memory, number of cores, and governors" [§3];
"from 1512 MHz to 384 MHz" [§3.1]; "reduced from 2GB to 512MB" [§3.1];
"reduced from four to one" [§3.1]; "four common frequency governors" [§3];
clock values: 384, 486, 594, 702, 810, 918, 1026, 1134, 1242, 1350, 1458,
1512 MHz [Fig 3a / §3.1]; memory values: 0.5, 1, 1.5, 2 GB [Fig 3b / §3.1];
cores: 1, 2, 3, 4 [Fig 3c / §3.1]; three devices: Pixel2, Intex Amaze+,
Nexus4 [§3]; results shown for Nexus4 [§3]. LAN: 72 Mbps, 10 ms RTT, 0% loss
[§2.1 inherited]. Repetitions: 20 [§2.1 inherited].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(device ∈ {Pixel2, IntelAmaze+,
Nexus4} [§3] × device_param ∈ {clock×12, memory×4, cores×4, governor×4} ×
workflow ∈ {chrome, youtube, skype} [§2.1]); count Not specified (full
factorial space not stated; 3 phones × (12+4+4+4) × 3 apps would give an upper
bound but one-factor-at-a-time design is used — other params at default while
one varies)⟩; Regime⟨Static: capacity_down 72 mbps [§2.1], path.latency 10 ms
[§2.1], path.loss 0% [§2.1]; Dynamic: Not specified⟩; iterations 20 per
workload [§2.1]; telemetry {app_metrics: true (PLT, start-up latency, stall
ratio, frame rate, call setup delay)}.

**Grammar gap (G2):** device hardware parameters (clock_mhz, mem_gb,
num_cores, cpu_governor) have no production in v2 grammar or A5 field
vocabulary. These are physical device tuning operations via ADB/root, not
network shaping parameters.

### device_qoe-ES4 — §4.1 iPerf clock-frequency vs. network throughput

**(i) Raw text.** "we conduct a study using the IPerf tool [16] from a server
that generates continuous traffic to the Nexus4 smartphone" [§4.1]; "Recall
(§2.1) that we host the content on our LAN" [§4.1] (LAN: 72 Mbps, 10 ms RTT,
0% loss [§2.1]); "experiment repeated 20 times for 12 clock frequencies"
[§4.1]; "average throughput measured over 5 minutes" [§4.1]; clock frequencies:
384–1512 MHz [Fig 6 / §3.1]; "average throughput drops from 48 Mbps to 32 Mbps
when clock is reduced from 1512 MHz to 384 MHz" [§4.1]; "TCP" [§4.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(clock_frequency ∈ {384, 486, 594,
702, 810, 918, 1026, 1134, 1242, 1350, 1458, 1512} MHz [§4.1 / Fig 6]) = 12⟩;
Experiment = ⟨Workflow(iperf3, continuous TCP bulk transfer, shell) ⊗
Regime⟨Static: capacity_down 72 mbps [§2.1], path.latency 10 ms [§2.1],
path.loss 0% [§2.1]; queue Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Nexus4 on LAN, server: desktop on LAN⟩; iterations 20 [§4.1];
telemetry {app_metrics: true (average TCP throughput Mbps over 5 min)}.

**Grammar gap (G2):** `clock_frequency` is the sweep dimension and has no
production in v2 grammar or A5. The experiment asks "how does CPU clock speed
affect TCP throughput?" — the network Regime is held fixed as a background;
the treatment is the device hardware setting.

### device_qoe-ES5 — §4.2 DSP offloading ePLT analysis

**(i) Raw text.** "we explore offloading Web computations to a DSP coprocessor"
[§4.2]; "ported the functions to the aDSP processor of the Google Pixel 2
phone" [§4.2]; "Node.js used to measure runtime performance of the offloaded
functions" [§4.2]; "page dependency graphs extracted with WProf" [§4.2];
"emulated page load time (ePLT), derived by re-evaluating the WProf dependency
graphs after replacing the execution time" [§4.2]; "top 20 sports Web pages"
[§4.2]; "18% improvement in page load time and 4× reduction in energy"
[abstract / §1]; "almost 4× reduction in median power consumption" [§4.2].
Network for ePLT computation: Not specified (ePLT re-evaluates offline
dependency graphs; no live traffic).

**(ii) Grammar.** Not applicable — this experiment performs an offline
re-evaluation of WProf page-load dependency graphs (captured previously),
substituting DSP runtimes in place of CPU runtimes. No live network Workflow
or Regime is imposed during the re-evaluation step. The experiment is an
analytical model evaluation, not a network data-generation experiment.
