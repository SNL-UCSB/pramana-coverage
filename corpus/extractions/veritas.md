# veritas — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| veritas-ES1 | Exp1 (Fig 2(a)) | per FCC-trace ∈ 100 traces [§2.2] | 100 | 1 session per trace [§2.2] |
| veritas-ES2 | Exp2 (Fig 2(b)) | 1 trace ("a new trace with poor network conditions") [§2.2] | 1 | 1 [§2.2] |
| veritas-ES3 | Exp3 (Fig 2(c)) | payload_size ∈ [2KB, 4MB] [§2.2]; grid Not specified | Not specified | Not specified |
| veritas-ES4 | Exp4 (Fig 5) | GTBW ∈ [0.5, 10 Mbps] × delay ∈ [5, 40 ms] × payload_size ∈ [2KB, 4MB] × gap_time ∈ [0.12s, 8s] [§3.2]; grids Not specified | Not specified | Not specified |
| veritas-ES5 | Exp5 (Figs 7,8,9,10,11,13,14) | per FCC-trace (GTBW 3–8 Mbps [§4.1]) × counterfactual_query ∈ {MPC→BBA, buffer 5s→30s, higher qualities, MPC→Bola} [§4.3, Appendix A.1] | Not specified (trace count not stated; 4 query types; "5 by default" Veritas samples [§4.1]) | 5 Veritas samples per (trace, query) [§4.1] |
| veritas-ES6 | Exp6 (no figures; §4.4 training-only) | per FCC-trace ∈ 100 traces [§4.4] | 100 | 1 session per trace |
| veritas-ES7 | Exp7 (Fig 12) | per test trace ∈ 30 traces [§4.4] | 30 | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Testbed (in-scope ESes): mahimahi network emulator [§3.2, §4.1], client-server setup,
> TCP transport; for veritas-ES4: GTBW "kept constant for a particular experiment" and
> delay "kept constant for a particular experiment" [§3.2]; TCP socket stats via socket
> stats utility (Linux `ss`) [§3.2]; payloads of different sizes [2KB to 4MB] [§3.2];
> random wait intervals [0.12s to 8s] between successive payloads [§3.2].

---


## Experiments

### veritas-ES1 — Fugu-bias motivation: MPC training collection (100 FCC traces)

**(i) Raw text.** "we trained Fugu on 100 traces, 50 with poor network conditions
[0-0.3 Mbps] and 50 with good network condition [9-10 Mbps] with the MPC algorithm
in an emulation testbed" [§2.2]; dataset: FCC throughput traces [§2.2]; "Figure 2(a)
presents the download time of all chunks across all the video sessions" [§2.2]; base
latency, buffer size, video content: Not specified for this motivation run [§2.2,
"details in §4"].

**(ii) Grammar.** OUT-OF-SCOPE. The experiment uses FCC throughput traces as the
Mahimahi bandwidth schedule; the per-trace GTBW varies over time within each session
(each FCC trace encodes a time-series of available bandwidth slots). This is
time-varying bottleneck capacity: the 0-0.3 Mbps and 9-10 Mbps ranges describe the
AVERAGE GTBW of the traces, not a fixed static capacity. Per CORPUS_PROMPT_v4 §2:
time-varying bottleneck capacity → OUT-OF-SCOPE.

### veritas-ES2 — Fugu-bias motivation: causal-query test on a new trace

**(i) Raw text.** "We next test Fugu on a new trace with poor network conditions"
[§2.2]; procedure: Fugu answers what-if download times for high/low quality next
chunks; "the download times predicted by Fugu and the actual download times" [§2.2];
emulation testbed, "details in §4" [§2.2]; bandwidth: "poor network conditions"
(FCC trace; range not quantified for this specific trace); ABR algorithm during trace
collection: Not specified; base latency, buffer, transport: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE. Same rationale as veritas-ES1: uses an FCC
throughput trace (time-varying GTBW within the session) as the Mahimahi bandwidth
schedule. "Poor network conditions" describes an FCC trace with low average
throughput, not a static capacity setting. Time-varying bottleneck capacity →
OUT-OF-SCOPE.

### veritas-ES3 — Throughput-vs-chunk-size controlled experiment (fixed 18 Mbps)

**(i) Raw text.** "controlled experiments using TCP where we emulated a constant
network bandwidth of 18 Mbps in a client server setup" [§2.2]; "sent payloads of
varying sizes (2KB to 4MB)" [§2.2]; "the observed throughput itself is dependent on
the size of chunks owing to TCP slow start effects" [§2.2]; transport: TCP [§2.2];
key mechanism: "the gap between payloads impacts whether TCP enters a slow-start
restart phase" [§2.2]; emulator: Not specified for this experiment ("emulated" used
but no tool named [§2.2]); base latency: Not specified; queue: Not specified;
cross traffic: Not specified; duration/repetitions: Not specified; hardware: Not
specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(payload_size ∈ [2KB, 4MB] [§2.2]);
count Not specified (range only; per §5b.1)⟩; Experiment =
⟨Foreground = {Workflow(shell; cmd: "send_tcp_payloads --size <s>") @ node_client}
⊗ Regime⟨Static: capacity_down=18 Mbps [§2.2], capacity_up: Not specified (client
→ server direction; single direction stated implicitly); queue: Not specified;
Dynamic: none (no cross-traffic stated)⟩⟩ @
Roles⟨client: emulated host (sends payloads), server: emulated host (receives)⟩;
path.latency: Not specified; path.jitter: Not specified; path.loss: Not specified;
cca: Not specified (TCP, no CCA variant stated; compiles as default cubic);
iterations: Not specified; telemetry {throughput_per_payload: true (observed
throughput vs chunk size is the measured output [§2.2, Fig 2(c)])}.

### veritas-ES4 — Validation of throughput estimator f (Exp4)

**(i) Raw text.** "We test the performance of f in an emulation environment with a
server transmitting payloads of different sizes [2KB to 4 MB] to a client" [§3.2];
"random intervals of wait time [0.12s to 8s] between transmission of successive
payloads" [§3.2]; "The GTBW and delay is kept constant for a particular experiment"
[§3.2]; "GTBW varied from 0.5 to 10 Mbps" [§3.2]; "end-to-end delay varied from
5 to 40 ms" [§3.2]; emulator: mahimahi [§3.2, "using mahimahi [31]"]; "f derives
Wsn using the socket stats utility in Linux [4]" [§3.2]; metric: "a CDF of the
relative error between the actual throughput observed by a payload and the
throughput estimated by f across all GTBW and delays" [§3.2]; transport: TCP [§3.2,
"f models ... TCP congestion control with slow start, congestion avoidance and slow
start restart (TCP SSR)"]; queue: Not specified; cross traffic: Not specified;
exact swept grid values and repetitions per (GTBW, delay) point: Not specified
(only ranges stated); hardware: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(capacity_down ∈ [0.5, 10 Mbps] [§3.2]
× latency_ms ∈ [5, 40 ms] [§3.2] × payload_size ∈ [2KB, 4MB] [§3.2]
× gap_time ∈ [0.12s, 8s] [§3.2]); count Not specified (ranges only; per §5b.1)⟩;
Experiment = ⟨Foreground = {Workflow(shell;
cmd: "send_tcp_payloads --size <s> --gap <g> --collect-socket-stats") @ node_client}
⊗ Regime⟨Static: capacity_down ∈ [0.5, 10 Mbps] [§3.2] (fixed per experiment);
latency_ms ∈ [5, 40 ms] [§3.2] (one-way delay, fixed per experiment);
queue: Not specified; Dynamic: none⟩⟩ @
Roles⟨client: emulated host (sends payloads, collects socket stats),
server: emulated host (receives)⟩;
path.latency: INHERITED from Regime.Static.latency_ms (same link; capacity_down and
latency_ms are the Regime knobs, applied to the bottleneck link);
path.jitter: Not specified; path.loss: Not specified;
cca: Not specified (TCP; no CCA variant stated; compiles as default cubic);
iterations: Not specified (ranges state no per-point count); telemetry
{throughput_per_payload: true [§3.2, Fig 5]; socket_stats: true
(f uses socket stats utility [§3.2])}.

### veritas-ES5 — Counterfactual evaluation campaign (Setting A → Setting B replays)

**(i) Raw text.** "We emulate FCC throughput traces [1] using Mahimahi [31]" [§4.1];
"The GTBW of FCC traces varies from 3 Mbps to 8 Mbps" [§4.1]; "80 ms end to end
delay" [§4.1]; ABR (Setting A): MPC, buffer 5 seconds [§4.1]; "a 10 minute
pre-recorded video clip with bitrate ranging from 0.1 Mbps to 4 Mbps" [§4.1];
counterfactual queries: (i) MPC→BBA; (ii) buffer 5s→30s; (iii) higher qualities;
(iv) MPC→Bola [§4.3, Appendix A.1]; Veritas samples: "5 by default" [§4.1]; metrics:
SSIM, rebuffering ratio, average bitrate [§4.1, Fig 14 caption]; trace count: Not
specified in prose.

**(ii) Grammar.** OUT-OF-SCOPE. The experiment uses FCC throughput traces replayed
via Mahimahi as the GTBW profile: "FCC traces varies from 3 Mbps to 8 Mbps" [§4.1]
means the per-trace GTBW is a time series within [3, 8 Mbps], not a fixed static
value. Mahimahi replays each trace slot-by-slot, changing the available bandwidth
over time. This is time-varying bottleneck capacity → OUT-OF-SCOPE per
CORPUS_PROMPT_v4 §2 rule. (Contrast veritas-ES4, where "GTBW and delay is kept
constant for a particular experiment" [§3.2]: ES4 is static per leaf; ES5's GTBW
varies within each session.)

### veritas-ES6 — FuguNN training collection (training-only, §4.4)

**(i) Raw text.** "We train FuguNN using traces obtained by running the MPC algorithm
on 100 FCC traces sampled uniformly from all traces with average GTBW values ranging
from 0.5 to 10 Mbps" [§4.4]; ABR: MPC [§4.4]; dataset: FCC traces [§4.4]; emulator/
testbed: Not specified for this collection (assumed-shared context is §4.1's testbed,
but §4.4 does not restate — left unspecified per §5b.1 silence rule); model trained:
FuguNN [§4.4]; maps to no figure (training-only).

**(ii) Grammar.** OUT-OF-SCOPE. Uses FCC throughput traces as the bandwidth driving
signal. Same structural reason as veritas-ES1 and veritas-ES5: each FCC trace
encodes a time-varying GTBW profile (slots from 0.5 to 10 Mbps average but varying
per slot within the session). Time-varying bottleneck capacity → OUT-OF-SCOPE.
Additionally, this is a training-only experiment (no figures; model training data
only — the reference/training-data rule would render it to no ExperimentSets in any
case); listed here to document the collection setup.

### veritas-ES7 — Interventional evaluation: random-bitrate test collection

**(i) Raw text.** "a separate set of 30 traces drawn from the same range of GTBW
[0.5 to 10 Mbps], but where bit rates are selected randomly rather than use an ABR
algorithm" [§4.4]; "Each test trace gives us ground truth information for the size
and download time for several chunk sequences" [§4.4]; FuguNN and Veritas evaluated
offline for every chunk sequence [§4.4]; emulator/testbed: Not specified for this
collection [§4.4 does not restate §4.1 parameters — left Not specified per §5b.1].

**(ii) Grammar.** OUT-OF-SCOPE. Uses FCC throughput traces (GTBW 0.5–10 Mbps range
per trace, time-varying within sessions). "Drawn from the same range of GTBW [0.5
to 10 Mbps]" [§4.4] confirms these are the same FCC trace corpus (per-slot varying
bandwidth), not 30 distinct static-capacity conditions. Time-varying bottleneck
capacity → OUT-OF-SCOPE.
