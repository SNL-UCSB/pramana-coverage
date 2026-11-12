# cloud_overlays — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Scope classification | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- | --- |
| cloud-ES1 | Exp1 | passive measurement | paths ∈ RIPE Atlas pairs across US/EU/Asia/OC | 22K paths [§5.1] | Not specified (passive probing) |
| cloud-ES2 | Exp2 | exogenous WA (PlanetLab/Azure) | paths ∈ 45 PlanetLab WA paths; coding params fixed at r=2/6, s=1/5 [§5.2] | 45 [§5.2] | 500–800 samples/path [§5.2] |
| cloud-ES3 | Exp3 | multi-path overlay + time-varying outage | scheme ∈ {Internet, Fwd, CR-WAN} | Not specified [§5.3] | Not specified |
| cloud-ES4 | Exp4 | exogenous (Emulab) + multi-segment overlay | scheme ∈ {TCP, TCP-over-J-QoS-CR-WAN} | 2 [§5.4] | 10K requests/scheme [§5.4] |
| cloud-ES5 | Exp5 | physical-layer mobile (LTE) | single LTE-tethered modified Skype testbed; mini-studies: bandwidth, WhatsApp, battery [§5.5] | Not specified | 20 min (battery trials) [§5.5] |
| cloud-ES6 | Exp6 | passive measurement (mobile networks) | provider ∈ {Amazon, Microsoft, Google} × network ∈ {Verizon-LTE-east, T-Mobile-LTE-east, T-Mobile-LTE-west} | 3 × 3 = 9 [§5.5] | 1,000 pings/combination [§5.5] |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> J-QoS is a cloud overlay QoS system comprising three services: forwarding
> (replicates packets via a cloud path), caching (stores and replays lost
> packets at the receiver-side DC), and coding/CR-WAN (network-coded packet
> recovery using cross-stream cooperation at two DCs). Implementation: C++
> user-space, Reed-Solomon codes via zfec library [§4]. UDP for application
> traffic and coded packets; TCP for control channel [§4]. Each experiment
> section uses a distinct testbed platform (RIPE Atlas, PlanetLab/Azure,
> LAN-emulation testbed, Emulab, LTE-tethered mobile testbed). Controlled
> network parameters: Not specified as a shared setting (each platform has its
> own conditions). Cross-traffic background: Not specified for the shared
> methodology; per-experiment where present.

---


## Experiments

### cloud-ES1 — RIPE Atlas feasibility study of J-QoS service delays (§5.1)

**(i) Raw text.** "We use the RIPE Atlas testbed [13] and Amazon Web Services (AWS) [2] data centers to measure latencies of public Internet and cloud overlay paths" [§5.1]. "Overall, we measure 22K paths spanning four continents, US, EU, Asia, and Oceania" [§5.1]. Measured quantities: δ (S/R-DC latency), x (DC1-DC2 inter-DC latency), y (direct S-R latency) [§5.1]. Derived service delays computed analytically: forwarding = x + δ_S−DC1 + δ_R−DC2; caching = y + 2δ_R−DC2 + Δ; coding = y + 2δ_R−DC2 + 2δ_R′−DC2 + Δ [§5.1]. Fig 6(e) sub-analysis: northern EU nodes to Stockholm DC (opened 2018) vs Frankfurt DC (2014) vs Ireland (2007) [§5.1]. No workload, no bottleneck control, no repetitions stated.

**(ii) Grammar-v2 translation.** This experiment is a passive measurement study — it does not generate any foreground traffic; it collects existing Internet latency probes from RIPE Atlas. No Regime (no controlled bottleneck link), no Foreground workflow, no CCA, no Dynamic pressure. The only "sweep" is over pairs of RIPE Atlas nodes (22K paths [§5.1]) on the live Internet. This topology is entirely outside the Pramana grammar model. No grammar-v2 translation is possible.

### cloud-ES2 — CR-WAN deployment on Azure + PlanetLab (§5.2)

**(i) Raw text.** "We ran CR-WAN as a service on five different DCs of Microsoft Azure [4], located in US (East, West), EU, Asia, and OC" [§5.2]. "We evaluate 45 PlanetLab wide area paths spanning four different continents" [§5.2]. Duration: "for over a month" [§5.2]; typically 500–800 samples/path, 3–5 weeks of measurement collection per path [§5.2]. Workload: simple constant bitrate application; ON/OFF with Poisson OFF times (mean 55 min [§5.2]), ON = 5 minutes at 10 ms packet frequency [§5.2]. Coding: r = 2/6, s = 1/5 [§5.2]. Loss accounting: any packet taking longer than one RTT to recover is lost [§5.2]. UDP for application and coded traffic; TCP for control channel [§4]. Fig 7(c) is a what-if re-analysis of the same probes (not a new collection).

**(ii) Grammar-v2 translation.** The experiment runs on live PlanetLab WA paths with real Internet loss/latency; no controlled bottleneck. Attempt: ExperimentSet⟨leaves: paths ∈ 45 PlanetLab WA paths [§5.2]⟩; Foreground = Workflow(UDP CBR sender over real Internet; ON/OFF: 5 min ON at 10 ms frequency, mean 55 min OFF [§5.2]) @ Regime⟨real WA Internet: loss Not controlled, latency Not controlled (real Internet behavior)⟩. The Regime is live Internet, not a Pramana-controlled Regime. Grammar cannot be completed: no `Regime.Static` capacity, no `Regime.Dynamic.pressure` — the loss/latency conditions are observed, not configured. OUT-OF-SCOPE.

### cloud-ES3 — Skype video-conferencing case study on a LAN testbed (§5.3)

**(i) Raw text.** "We connect clients running Skype for Linux 4.3 in a LAN, and emulate wide area path characteristics such as latency, packet loss rate, and jitter" [§5.3]. Emulation tool: Not specified. Three schemes compared in one campaign: (i) Internet path with Skype's built-in FEC; (ii) forwarding service (all Skype packets duplicated over cloud path); (iii) CR-WAN (selective coded packets over cloud path) [§5.3, "we leverage the cloud path to run the video conference in three experiments"]. Condition: "When a 30 second outage occurs along the Internet path" [§5.3]; a 0% loss reference case [§5.3]. CR-WAN parameters: s = 0 (no in-stream coding on cloud path [§5.3]), r = 1/4 with k = 4, NACK timeout 25 ms [§5.3]. QoE: PSNR scores per frame via VQMT [§5.3]. Bandwidth overhead: 13.4% as many packets, 13.6% as many bytes as the forwarding service [§5.3]. Duration/repetitions: Not specified.

**(ii) Grammar-v2 translation.** The experiment requires two simultaneous network paths: the emulated "Internet path" (with controlled latency/loss/jitter) and the cloud overlay path (forwarding/coding via real Azure DCs). The three schemes differ in which path(s) carry Skype traffic. The 30s outage is a time-varying condition applied to the Internet path during the session. Attempt: ExperimentSet⟨leaves: scheme ∈ {Internet, Fwd, CR-WAN} [§5.3]; condition ∈ {0% loss baseline, 30s outage}⟩; Foreground = Workflow(Skype Linux 4.3 video call; params: screen-share mode, prerecorded video [§5.3]) ⊗ Regime⟨Static: path = ⟨latency: Not specified, loss: Not specified, jitter: Not specified⟩ (emulated WA characteristics [§5.3]); Dynamic: 30s total path outage (time-varying)⟩. The grammar cannot express the multi-path overlay topology (Internet path + cloud overlay path) or schedule a time-varying outage on one path. OUT-OF-SCOPE.

### cloud-ES4 — TCP short-flow performance on Emulab (§5.4)

**(i) Raw text.** "Using Emulab, we emulate the same topology and loss model as used in the Google study" [§5.4]. "200 ms RTT between end hosts" [§5.4]; burst loss: "loss probabilities of 0.01 for losing the first packet in a burst and 0.5 for each subsequent loss" [§5.4]. Overlay latencies: "RTT between server/client-DC paths is 30 ms; RTT of 200 ms on the DC1-DC2 path" [§5.4]. Workload: "client sends a 12B request and receives a 50 KB response from the server" [§5.4]. Repetitions: "We make 10K requests each for TCP and TCP over J-QoS" [§5.4]. TCP uses SACK [§5.4]. Selective-duplication variant (prose-only, same campaign): duplicate only SYN-ACK packets; reduces tail by 33% (83% with full duplication) [§5.4]. Bandwidth / queue size / queue management: Not specified.

**(ii) Grammar-v2 translation.** The experiment requires a three-segment network topology: client ↔ 30 ms RTT ↔ DC1 ↔ 200 ms RTT ↔ DC2 ↔ 30 ms RTT ↔ server, with burst loss on the direct client–server path. The overlay scheme (J-QoS CR-WAN) intercepts packets at DC1 and sends coded packets via DC2. Attempt: ExperimentSet⟨leaves: scheme ∈ {TCP, TCP-over-J-QoS-CR-WAN} = 2 [§5.4]⟩; Foreground = Workflow(TCP file transfer: 12B request, 50KB response [§5.4]) ⊗ Regime⟨Static: path.latency 200 ms RTT [§5.4], path.loss burst (p₁ = 0.01, subsequent = 0.5) [§5.4]; overlay path: 30 ms RTT client-DC1 [§5.4], 200 ms RTT DC1-DC2 [§5.4]⟩; iterations = 10K requests/scheme [§5.4]. The multi-segment overlay path requires three independent controlled link values; Pramana models one bottleneck. OUT-OF-SCOPE.

### cloud-ES5 — Mobile (LTE-tethered) Skype/CR-WAN testbed (§5.5)

**(i) Raw text.** "We modified our Skype testbed (§5.3) to tether the sending host to a mobile device connected to an LTE network" [§5.5]. Bandwidth: "overall bandwidth required by CR-WAN to duplicate a Skype video stream was 1.5 Mbps, within the LTE uplink bandwidth (~5.0 Mbps)" [§5.5]. Concurrent-transfer test: "transfer time for 5 MB files over WhatsApp is not affected by CR-WAN running simultaneously" [§5.5]. Battery: "We ran 20 minute trials of Skype video calls, with and without cloud path duplication. We observed that in both cases the battery drain was ∼20 mAh" [§5.5]. Outage recovery: mobile Skype testbed recovered packets during an outage [§5.5, "(fig 8(a))"]. Mobile carrier, device model, hardware: Not specified.

**(ii) Grammar-v2 translation.** The experiment uses a physical LTE-tethered mobile device as the access network for the sending host. The LTE uplink is the access link (~5.0 Mbps [§5.5]), with real LTE protocol behavior. Attempt: ExperimentSet; Foreground = Workflow(Skype video call over CR-WAN with LTE access) ⊗ Regime⟨Static: path.capacity (LTE uplink ~5.0 Mbps [§5.5])⟩. However, the access technology is physical LTE — the regime is not a controlled bottleneck link but a real mobile radio channel. OUT-OF-SCOPE.

### cloud-ES6 — Mobile-network latency (ping) study (text-only, §5.5)

**(i) Raw text.** "We conducted a short study to quantify this effect" [§5.5]. "pinging three major cloud providers (Amazon, Microsoft, and Google) 1,000 times using different mobile networks" [§5.5]. Networks: "Verizon's LTE network (east coast) and T-Mobile's LTE network (both east and west coasts)" [§5.5]. Results: median ping times typically 50–60 ms [§5.5]; 50%–90% RTTs approximately 50–100 ms [§5.5]. Hardware / device / DC targets / time of day: Not specified.

**(ii) Grammar-v2 translation.** Passive measurement (ICMP ping over real LTE networks). ExperimentSet⟨leaves: provider ∈ {Amazon, Microsoft, Google} × network ∈ {Verizon-LTE-east, T-Mobile-LTE-east, T-Mobile-LTE-west} = 3 × 3 = 9 [§5.5]⟩; Foreground = Workflow(ICMP ping) @ Regime⟨real LTE: no controlled Regime⟩; iterations = 1,000 pings/combination [§5.5]. No controlled bottleneck; passive probing over real LTE. OUT-OF-SCOPE.
