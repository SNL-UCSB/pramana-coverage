# sammy — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Exp(s) | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| sammy-ES1 | Exp7 (Fig 7) | algorithm ∈ {Sammy, Netflix-production-ABR} [§6] | 1×2 = 2 | Not specified |
| sammy-ES2 | Exp8–Exp11 (Fig 8a–d) | neighboring_workload ∈ {UDP-5Mbps, TCP-Reno, HTTP-3MB, video-session} × algorithm ∈ {Sammy, Netflix-production-ABR} [§6] | 4×2 = 8 | Not specified; Exp11 override: 4 trials [§6] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Lab environment [§6]. Single shared bottleneck link: capacity = 40 Mbps [§6, "In all
> experiments, we use a 40 Mbps link"], RTT = 5ms [§6, "with a 5ms RTT"], queue size =
> 4×BDP [§6, "Queue size: 4 times the bandwidth-delay product"]. Queue discipline: Not
> specified. AQM: Not specified. Video workload: Sammy plays a video with a maximum bitrate
> of 3.3 Mbps [§6]. Transport: TCP. Netflix's default CCA is TCP Reno [§6, stated in the
> context of the TCP neighbor in Exp9: "the congestion control algorithm Netflix uses by
> default"]. Foreground video CCA: Not specified (not explicitly stated for the video flow
> itself). Testbed software/hardware/emulator: Not specified. Any field not listed is
> Not specified.

---


## Experiments

### sammy-ES1 — Lab: single Sammy flow vs. control (Exp7, Fig 7)

**(i) Raw text.** "we will first look at how it performs on its own. Figure 7 shows the
throughput and RTT for a single Sammy flow, compared to a single control flow running
Netflix's production ABR algorithm" [§6]. Setup: shared methodology block (40 Mbps, 5ms RTT,
4×BDP). "playback starts after about three seconds, when Sammy begins pacing; pace rate ~15 Mbps
('The pace rate it picks is about 15 Mbps')" [§6]. "RTT is the minimum of 5ms" [§6]. "Sammy
reduces throughput by 53% … and RTTs by 47%" [§6]. No neighboring traffic [§6 — explicitly
distinct from Exp8–11 which introduce a neighbor].

**(ii) Grammar.**
```
ExperimentSet⟨
  leaves: sweep(algorithm ∈ {Sammy, Netflix-production-ABR}) = 2 [§6]
⟩;
Experiment = ⟨
  Foreground: Workflow(video-session;
                params: {pacing: Sammy | none, max_bitrate: 3.3 Mbps [§6]})
  @ path.latency: 5ms [§6, "5ms RTT"]
  ⊗ Regime⟨
    Static: capacity = 40 Mbps [§6],
            queue: ⟨size: 4×BDP [§6], discipline: Not specified⟩
    Dynamic: none [§6 — single flow only, no neighbor described]
  ⟩
⟩;
Roles⟨client: lab host, server: Not specified⟩;
cca: Not specified (foreground video TCP flow; §6 TCP Reno note is specific to Exp9 neighbor);
iterations: Not specified;
telemetry: {app_metrics: {chunk_throughput [§6], rtt_per_packet [§6]}}
```

### sammy-ES2 — Lab: neighboring-workload experiments (Exp8–Exp11, Fig 8a–d)

**(i) Raw text.** Shared procedure: "We run an experiment where a video session using
Netflix's production algorithm runs at the same time as a neighboring application. We repeat
the same experiment using Sammy and observe how the neighbor's QoE changes" [§6]. Four
distinct neighbor types:
- Exp8 (Fig 8a): "neighboring traffic is a 5 Mbps paced UDP flow" [§6]; metric = "one-way
  delay measured for UDP packets" [§6]; result: "Sammy eliminates queueing delay for the UDP
  traffic, reducing one-way delay by 51%" [§6].
- Exp9 (Fig 8b): "a standard, congestion window limited TCP Reno connection — the congestion
  control algorithm Netflix uses by default" [§6]; "begins 10 seconds after playback starts"
  [§6]; metric = TCP throughput [§6]; result: Sammy increases TCP throughput "by 28% to an
  average of 25.7 Mbps" [§6].
- Exp10 (Fig 8c): "We repeatedly issue 3MB HTTP requests during video playback" [§6]; metric
  = HTTP response time [§6]; result: "Sammy improves average HTTP response times by 18%,
  reducing them from 1095ms to 898ms" [§6].
- Exp11 (Fig 8d): "We run another experiment to measure the impact of Sammy on a neighboring
  video session" [§6]; "after a few seconds we start a neighboring session using Netflix's
  production algorithm" [§6]; metric = play delay of neighboring session [§6]; "Over four
  trials" [§6]; result: "Sammy consistently improves the neighbor's play delay by 4% — an
  average of 50ms" [§6].

**(ii) Grammar.**
```
ExperimentSet⟨
  leaves: sweep(
    neighboring_workload ∈ {
      udp-5mbps-paced [§6, Exp8],
      tcp-reno          [§6, Exp9],
      http-3mb-requests [§6, Exp10],
      video-netflix     [§6, Exp11]
    } × algorithm ∈ {Sammy, Netflix-production-ABR} [§6]
  ) = 4×2 = 8
⟩;
Experiment = ⟨
  Foreground: Workflow(video-session;
                params: {pacing: Sammy | none, max_bitrate: 3.3 Mbps [§6]})
  @ path.latency: 5ms [§6, "5ms RTT"]
  ⊗ Regime⟨
    Static: capacity = 40 Mbps [§6],
            queue: ⟨size: 4×BDP [§6], discipline: Not specified⟩
    Dynamic: pressure = load(neighboring_workflow ↦ neighbor_node)
      where neighboring_workflow ∈ {
        udp-5mbps-paced       [§6, Exp8; cca: n/a — UDP],
        tcp-reno              [§6, Exp9; cca: ⟨algo: reno⟩; start_offset: 10s [§6]],
        http-3mb-requests     [§6, Exp10; cca: Not specified],
        video-session-netflix [§6, Exp11; cca: Not specified]
      }
  ⟩
⟩;
Roles⟨client: lab host (foreground), neighbor_node: lab host, server: Not specified⟩;
cca: Not specified (foreground video flow);
iterations: Not specified (Exp8–10); Exp11 override: iterations = 4 [§6, "Over four trials"];
telemetry: {
  app_metrics: {
    Exp8: udp_one_way_delay [§6],
    Exp9: tcp_throughput [§6],
    Exp10: http_response_time [§6],
    Exp11: video_play_delay [§6]
  }
}
```
