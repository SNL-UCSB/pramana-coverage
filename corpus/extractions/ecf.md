# ecf — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| ecf-ES1 | Exp1 (Netflix trace, May 2014) | 1 (single trace) | 1 | Not specified |
| ecf-ES2 | Exp2 (fixed-bw DASH streaming lab) | WiFi_bw ∈ {0.3,0.7,1.1,1.7,4.2,8.6} Mbps × LTE_bw ∈ {0.3,0.7,1.1,1.7,4.2,8.6} Mbps × scheduler ∈ {Default,ECF,DAPS,BLEST} [§3.1; §5.2.1] | 6 × 6 × 4 = 144 | 5 [§5.2.1] |
| ecf-ES3 | Exp3 (CWND reset disabled) | bandwidth_pairs ∈ Exp2 grid; scheduler = Default, CWND reset disabled [§3.2] | Not specified (bandwidth pairs not fully enumerated for this sub-campaign) | Not specified |
| ecf-ES4 | Exp4 (four-subflow streaming) | WiFi_bw ∈ {0.3} Mbps × LTE_bw ∈ {0.3,0.7,1.1,1.7,4.2,8.6} Mbps × scheduler ∈ {Default,ECF} [§5.2.5] | 1 × 6 × 2 = 12 | Not specified |
| ecf-ES5 | Exp5 (variable-bw streaming) | scenario ∈ 10 × scheduler ∈ {Default,ECF,DAPS,BLEST} [§5.3] | 10 × 4 = 40 ATTEMPTED | 5 [§5.3] |
| ecf-ES6 | Exp6 (wget downloads) | file_size ∈ {64KB,128KB,256KB,512KB,1MB,2MB} × scheduler ∈ {Default,ECF,DAPS,BLEST} × WiFi/LTE bw ∈ [1,10] Mbps (Not enumerated) [§5.4] | Not specified | 30 [§5.4] |
| ecf-ES7 | Exp7 (web browsing, lab) | scheduler ∈ {Default,ECF,DAPS,BLEST} × WiFi/LTE bw ∈ [1,10] Mbps (Not enumerated) [§5.5] | Not specified | 10 [§5.5] |
| ecf-ES8 | Exp8 (wild streaming) | run ∈ 9 [§6.2] | 9 | 1 |
| ecf-ES9 | Exp9 (wild web browsing) | run ∈ 30 [§6.3] | 30 | 1 |

## Shared methodology (raw text, ES2–ES7) (quoted from the paper)


> Android mobile device, Google Nexus 5 [§5.1]; WiFi access point (IEEE 802.11g) and
> AT&T LTE cellular interface [§5.1]; server: desktop Ubuntu Linux 12.04, MPTCP 0.89
> [§5.1]; Apache 2.2.22, HTTP persistent connections, Keep Alive Timeout 5 sec [§5.1];
> server-side bandwidth regulation via Linux tc [§3.1]; schedulers: Default, ECF, DAPS,
> BLEST [§5.1]; ECF hysteresis β = 0.25 [§5.1]; DASH content: 4K gaming montage, 1332
> seconds, encoded at 50 Mbps, H.264/MPEG-4 AVC, original resolution 2160p [§5.1];
> six representations 144p–1080p (5-second chunks) [§5.1]; ABR algorithm: buffer-based
> approach of Huang et al. [ref 12] [§3.1]; CCA: Not specified (MPTCP coupled CC;
> algorithm name not stated in paper). MPTCP opportunistic retransmission and
> penalization enabled [§5.1]; queue management: Not specified; cross traffic:
> Not specified.


## Experiments

### ecf-ES1 — Illustrative Netflix trace (Fig 1)

**(i) Raw text.** "This trace was collected using an Android mobile handset (Samsung
Galaxy S3) while watching Netflix through WiFi on May 2014" [§2.2]; standalone
motivation trace, ON-OFF DASH download pattern illustrated [§2.2]; network bandwidth,
RTT, duration, scheduler: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment =
⟨Workflow(Netflix streaming on Samsung Galaxy S3, WiFi) ⊗
Regime⟨Static: Not specified (WiFi path, uncontrolled); Dynamic: Not specified⟩⟩ @
Roles⟨client: Samsung Galaxy S3, server: real Netflix CDN endpoints⟩;
iterations Not specified; telemetry {app_metrics: true (download rate trace [§2.2])}.

### ecf-ES2 — Fixed-bandwidth DASH streaming campaign (lab, Figs 2,3,5,6,7,9–14; Tables 2,3)

**(i) Raw text.** WiFi and LTE each regulated to {0.3, 0.7, 1.1, 1.7, 4.2, 8.6} Mbps
[§3.1]; all WiFi×LTE combinations [Fig 2/Fig 9 axes]; schedulers Default, ECF, DAPS,
BLEST [§5.2.1]; "five runs per experiment; a run consists of the playout of the 20
minute video" [§5.2.1]; "values averaged over the five runs" [§3.1]; server-side tc
regulation [§3.1]; Android Nexus 5 client [§5.1]; measured average RTTs at each
bandwidth setting from Table 2 (e.g. WiFi 969 ms / LTE 858 ms at 0.3 Mbps; WiFi 40
ms / LTE 105 ms at 8.6 Mbps [Table 2]); RTTs are measured results, NOT imposed
conditions; DASH encoding at 50 Mbps [§5.1]; MPTCP 0.89 [§5.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(Regime.Static.WiFi_capacity ∈
{0.3,0.7,1.1,1.7,4.2,8.6} Mbps [§3.1] × Regime.Static.LTE_capacity ∈
{0.3,0.7,1.1,1.7,4.2,8.6} Mbps [§3.1] × mptcp_scheduler ∈ {Default,ECF,DAPS,BLEST}
[§5.2.1]) = 6 × 6 × 4 = 144; workflow: DASH streaming (ExoPlayer)⟩;
Experiment = ⟨Workflow(DASH adaptive streaming; ExoPlayer on Android Nexus 5;
MPTCP over WiFi+LTE) @ cca: Not specified (MPTCP coupled congestion controller,
not named) ⊗ Regime⟨Static: two separately-regulated paths: WiFi capped at
selected Mbps, LTE capped at selected Mbps via server-side tc [§3.1]; queue:
Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Android Nexus 5 (WiFi + LTE), server: Ubuntu desktop Apache 2.2.22⟩;
iterations: 5 [§5.2.1]; telemetry {app_metrics: true (average video bit rate,
fraction of ideal [§3.1]), pcap: Not specified}.

### ecf-ES3 — Streaming with CWND reset disabled (Fig 6 "w/o reset" series)

**(i) Raw text.** "we perform streaming experiments with the default scheduler
disabling the CWND reset" [§3.2]; bandwidth pairs "according to bandwidth regulation
pairs" as in the streaming campaign [§3.2]; Fig 6 x-axis labels match Exp2's pairs
(e.g. 0.3-0.3, 0.3-8.6 Mbps); scheduler: Default [§3.2]; repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(bandwidth_pair ∈ Exp2 grid; scheduler
= Default; kernel_mptcp_cwnd_reset = disabled); count Not specified⟩;
Experiment = ⟨Workflow(DASH streaming; ExoPlayer on Android; MPTCP; kernel
mechanism modified: CWND reset disabled) ⊗ Regime⟨Static: two-path tc-regulated
bandwidth pairs (WiFi + LTE) [§3.2]; Dynamic: Not specified⟩⟩ @
Roles⟨client: Android Nexus 5, server: Ubuntu desktop Apache⟩; iterations Not
specified; telemetry {app_metrics: true (average throughput [§3.2])}.

### ecf-ES4 — Four-subflow streaming (Fig 15)

**(i) Raw text.** "using four subflows (two over WiFi and two over LTE)" [§5.2.5];
WiFi: 0.3 Mbps (two subflows, each 0.15 Mbps [§5.2.5]); LTE: {0.3,0.7,1.1,1.7,
4.2,8.6} Mbps [§5.2.5]; schedulers Default and ECF [§5.2.5]; repetitions: Not
specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(WiFi_bw = 0.3 Mbps × LTE_bw ∈
{0.3,0.7,1.1,1.7,4.2,8.6} Mbps × scheduler ∈ {Default,ECF}) = 1 × 6 × 2 = 12⟩;
Experiment = ⟨Workflow(DASH streaming; ExoPlayer; MPTCP with 4 subflows) @
cca: Not specified ⊗ Regime⟨Static: WiFi capped at 0.3 Mbps (0.15 Mbps per
subflow [§5.2.5]), LTE capped at selected Mbps; Dynamic: Not specified⟩⟩ @
Roles⟨client: Android Nexus 5, server: Ubuntu desktop Apache⟩; iterations Not
specified; telemetry {app_metrics: true (ratio of measured vs ideal bit rate
[§5.2.5])}.

### ecf-ES5 — Variable-bandwidth streaming (Figs 16, 17)

**(i) Raw text.** WiFi and LTE bandwidths "changed randomly at exponentially
distributed intervals with an average of 40 seconds" [§5.3]; values "selected from
{0.3, 1.1, 1.7, 4.2, 8.6} Mbps, chosen uniformly at random" [§5.3]; "ten" scenarios
each with a "different unique random seed" [§5.3]; "5 runs per scenario" [§5.3];
schedulers Default, ECF, BLEST plotted; DAPS run but omitted [§5.3].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scenario ∈ 10 × scheduler ∈
{Default,ECF,DAPS,BLEST} = 10 × 4 = 40 ATTEMPTED [§5.3]; bandwidth changes at
mean 40 s exponential intervals from {0.3,1.1,1.7,4.2,8.6} Mbps)⟩;
Experiment = ⟨Workflow(DASH streaming; ExoPlayer) ⊗ Regime⟨Static: time-varying
capacity via random bandwidth changes at exponentially-distributed intervals
[§5.3]; Dynamic: Not specified⟩⟩; iterations: 5 [§5.3].

### ecf-ES6 — wget download campaign (Figs 18, 19)

**(i) Raw text.** "simple file downloads using wget" [§5.4]; file sizes "64 KB to
2 MB, in powers of two" [§5.4]; WiFi and LTE bandwidth "regulated between [1,10]
Mbps, 'in a manner similar to Section 3.1'" [§5.4]; averaged over "thirty runs"
[§5.4]; schedulers Default, DAPS, BLEST, ECF [§5.4]; server-side tc regulation
[§3.1, shared methodology]; MPTCP [shared methodology].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(file_size ∈ {64KB,128KB,256KB,
512KB,1MB,2MB} × scheduler ∈ {Default,ECF,DAPS,BLEST} × bandwidth_pair ∈ [1,10]
Mbps (Not enumerated)); count Not specified (file_size × scheduler = 6 × 4 = 24
known basis; bandwidth grid not stated as discrete steps)⟩;
Experiment = ⟨Workflow(wget file download; shell) @ cca: Not specified (MPTCP) ⊗
Regime⟨Static: two-path tc-regulated WiFi + LTE bandwidth ∈ [1,10] Mbps [§5.4];
queue: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Android Nexus 5, server: Ubuntu desktop Apache (same lab setup)⟩;
iterations: 30 [§5.4]; telemetry {app_metrics: true (download completion time [§5.4])}.

### ecf-ES7 — Web browsing, lab (Figs 20, 21)

**(i) Raw text.** "a copy of CNN's home page (as of 9/11/2014) consisting of 107
Web objects deployed on the MPTCP server" [§5.5]; "Android Web browser, six parallel
(MP)TCP connections to the server (12 subflows for MPTCP)" [§5.5]; bandwidth "between
[1,10] Mbps as in Section 5.4" [§5.5]; "traces collected from 10 runs" [§5.5];
schedulers Default, DAPS, BLEST, ECF [§5.5]; Fig 20 shows 3 configurations:
5.0/5.0 Mbps, 1.0/5.0 Mbps, 1.0/10.0 Mbps (WiFi/LTE).

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(scheduler ∈ {Default,ECF,DAPS,BLEST}
× bandwidth_pair ∈ [1,10] Mbps (Not enumerated; 3 specific configs in figures)); count
Not specified⟩; Experiment =
⟨Workflow(web browsing; Android browser; CNN home page with 107 objects; 6 parallel
connections / 12 subflows) @ cca: Not specified (MPTCP) ⊗ Regime⟨Static: two-path
tc-regulated WiFi + LTE ∈ [1,10] Mbps [§5.5]; Dynamic: Not specified⟩⟩ @
Roles⟨client: Android Nexus 5, server: Ubuntu desktop Apache (CNN copy)⟩;
iterations: 10 [§5.5]; telemetry {app_metrics: true (per-object completion time,
out-of-order delay [§5.5])}.

### ecf-ES8 — In-the-wild streaming (Fig 22)

**(i) Raw text.** "WDC cloud server" deployed in Washington D.C. [§6.1]; "local town
public WiFi" + AT&T LTE [§6.1]; "the device uses each network as-is without any
additional bandwidth regulation" [§6.1]; "nine runs over two days" [§6.2]; schedulers
Default and ECF only [§6].

**(ii) Grammar.** ExperimentSet⟨leaves: 9 runs [§6.2]⟩; Experiment =
⟨Workflow(DASH streaming; ExoPlayer; MPTCP; real WiFi + LTE paths) ⊗
Regime⟨Static: Not specified (unregulated public WiFi + AT&T LTE, no bandwidth
control [§6.1]); Dynamic: Not specified⟩⟩ @
Roles⟨client: Android device, server: WDC commercial cloud (real Internet)⟩;
iterations: 1; telemetry {app_metrics: true (average throughput, ECF 7.79 Mbps vs
Default 6.72 Mbps [§6.2])}.

### ecf-ES9 — In-the-wild web browsing (Fig 23, Table 4)

**(i) Raw text.** Same in-the-wild setup as ES8 (WDC server, unregulated public WiFi
+ AT&T LTE [§6.1]); "the device retrieves a copy of CNN's home page at the WDC
server" [§6.3]; "measured over thirty runs" [§6.3]; schedulers Default and ECF [§6.3].
Average object download completion: ECF 0.650 s vs Default 0.882 s [§6.3; Table 4].

**(ii) Grammar.** ExperimentSet⟨leaves: 30 runs [§6.3]⟩; Experiment =
⟨Workflow(web browsing; Android browser; CNN copy at WDC server; real unregulated
paths) ⊗ Regime⟨Static: Not specified (unregulated [§6.1]); Dynamic: Not
specified⟩⟩ @ Roles⟨client: Android device, server: WDC cloud⟩; iterations: 1;
telemetry {app_metrics: true (object completion time, out-of-order delay [§6.3; Table 4])}.
