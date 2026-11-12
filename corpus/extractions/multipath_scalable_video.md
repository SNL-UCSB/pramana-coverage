# multipath_scalable_video — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| multipath_scalable_video-ES1 | Exp1 (CH profiling) | path ∈ {SCION production paths to Switzerland} [§3, "816 end-to-end paths"] | 816 | Not specified |
| multipath_scalable_video-ES2 | Exp2 (KR profiling) | path ∈ {SCION SCIERA paths to South Korea} [§3, "160 paths"] | 160 | Not specified |
| multipath_scalable_video-ES3 | Exp3 (encoding) | single encoding campaign (no network sweep) | 1 | Not specified |
| multipath_scalable_video-ES4 | Exp4 (CH streaming) | path_count ∈ {1, 2, 3, 4} [Fig 4 x-axis] | 4 | Not specified |
| multipath_scalable_video-ES5 | Exp5 (KR streaming) | single result (no path-count sweep stated) | 1 | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Server at ETH Zurich; Switzerland receiver via SCION production network;
> South Korea receiver via SCIERA (SCION Education, Research and Academic
> Infrastructure) [§3 Testbed]. Video pipeline: ingest with FFmpeg → encode
> into OBUs with AV1 codec → segment and encapsulate into SCION UDP packets →
> transmit over selected SCION paths → reassemble → playback [§2]. Path
> selection procedure: Offline Profiling (measure latency and bandwidth per
> path; select candidate set) followed by Online Probing (continuously monitor
> candidates and update path policies periodically) [§3 Network Profiling].
> Measured bandwidths account for payload only and exclude headers [§3,
> "Measured bandwidths account for payload only and exclude headers"].
> Hardware: Not specified. Test duration and repetitions: Not specified.


## Experiments

### multipath_scalable_video-ES1 — Offline network profiling, Switzerland receiver (Fig 2)

**(i) Raw text.** "We discovered 816 end-to-end paths to the Switzerland
receiver" [§3]; candidate filter: "measured bandwidth >80 Mbps and latency
<5 ms, then select a subset that maximizes path disjointness" [§3]; highest
observed goodput 85 Mbps on a path with three AS hops [§3]; receiver access
link 100 Mbps Ethernet [§3, "the 100 Mbps Ethernet access link at the
receiver"]; period and measurement tool: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE experiment — passive latency-and-bandwidth
profiling of 816 existing SCION production-network paths. No controllable
bottleneck; no Pramana Regime knobs exercised. Grammar translation is not
applicable.

### multipath_scalable_video-ES2 — Offline network profiling, South Korea receiver (Fig 3)

**(i) Raw text.** "160 paths to the South Korea receiver" [§3]; path structure:
vertical latency bands — "Paths that pass through Singapore (blue) exhibit
significantly lower latency than those traversing Chicago (green)" [§3];
candidate selection: "We select the top two paths within each latency band to
form the candidate set" [§3]; networks exceeding 300 Mbps offered far more
bandwidth than the stream could utilize [§3 Streaming Bitrate]. Period and
measurement tool: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — same passive profiling structure as ES1,
applied to SCIERA paths to South Korea.

### multipath_scalable_video-ES3 — Video-encoding measurement (Tab 2, Tab 3)

**(i) Raw text.** "we used a 4K@60 fps camera source (≈ 200 Mbps)" [§3 Video
Encoding]; codec: AV1 [§3]; SVC configuration: three spatial × three temporal
layers (nine total) [§3]; per-layer bitrates measured (Table 2); per-OP VMAF
scores measured (Table 3) [§3, "the per-layer bitrates and per-OP VMAF scores
are measured and reported in Table 2 and Table 3"]; encoder: FFmpeg [§2].
Network: none (offline encoding; no transmission involved) [§3 Note in
rendering].

**(ii) Grammar.** OUT-OF-SCOPE — offline encoding quality measurement with no
network transmission. No Regime, no Workflow network traffic, no CCA.

### multipath_scalable_video-ES4 — Video-streaming test, Switzerland receiver (Fig 4)

**(i) Raw text.** "We encoded the live source in real time and transmitted the
base and enhancement layers concurrently over multiple SCION paths" [§3 Video-
Streaming Test]; streaming bitrate: 88 Mbps [§3 Streaming Bitrate, "We set the
streaming bitrate to 88 Mbps"]; swept factor: number of SCION paths ∈ {1, 2,
3, 4} [Fig 4 x-axis, labeled "Number of SCION Paths"]; OBU receiving rate (%):
91.5% (1 path), 95.9% (2), 96.4% (3), 96.8% (4) [Fig 4 data labels]; access
link: "all flows eventually converged on the same 100 Mbps downlink" [§3];
receiver: 100 Mbps Ethernet access link [§3, "the 100 Mbps Ethernet access link
at the receiver"]; baseline: Traditional Network path (IP/UDP, delivered without
loss per §3); transport: SCION UDP packets [§2]; paths from Exp1's candidate set
(>80 Mbps, <5 ms, maximizing disjointness) [§3]; duration / repetitions:
Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(path_count ∈ {1, 2, 3, 4}
[Fig 4]) = 4⟩; Experiment = ⟨Workflow(svc-video-streaming; codec: AV1;
bitrate: 88 Mbps [§3]; layers: SVC 3-spatial × 3-temporal; transport:
SCION UDP) @ Regime⟨Static: capacity_down: 100 Mbps [§3] (shared access
link at receiver); [GAP-DESIGN: path_count independent SCION paths require a
MULTIPATH Regime production not present in v2 grammar]; Dynamic: Not
specified⟩⟩; cca: Not specified (SCION UDP; no TCP CCA described); iterations:
Not specified; telemetry {app_metrics: true (OBU receiving rate %)}.

### multipath_scalable_video-ES5 — Video-streaming test, South Korea receiver (text-only)

**(i) Raw text.** "As expected, all packets were reliably delivered at the
South Korea receiver" [§3 Video-Streaming Test]; streaming bitrate: 88 Mbps
[§3 Streaming Bitrate]; server: ETH Zurich; receiver: South Korea via SCIERA
[§3 Testbed]; paths from ES2 candidate set (top two paths within each latency
band) [§3]; context: "networks exceeding 300 Mbps offered far more bandwidth
than the stream could utilize" [§3 Streaming Bitrate]; number of paths swept:
Not specified; duration / repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1 (single text-only result; no
path-count sweep stated)⟩; Experiment = ⟨Workflow(svc-video-streaming;
bitrate: 88 Mbps [§3]; codec: AV1; transport: SCION UDP) @ Regime⟨Static:
capacity_down: Not specified (high-capacity SCIERA paths, >300 Mbps [§3]);
[GAP-DESIGN: MULTIPATH Regime — multiple SCION paths; same structural gap as
ES4]; Dynamic: Not specified⟩⟩; cca: Not specified; iterations: Not specified;
telemetry {app_metrics: true (packet delivery: binary)}⟩.
