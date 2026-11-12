# qoe_qos_realtime — Experiment-Set Intent Corpus

## Shared methodology (ES1 raw text) (quoted from the paper)


> Two WebEx clients C1 and C2 connected to a WebEx media bridge; each node
> in a container inside the same VM [§3, "Each node is running in a container
> inside the same VM"]. Network impairments applied with Linux tc on the
> C1–media bridge link only; C2 link unimpaired [§3, "The link between C2 and
> the media bridge has no network impairment"; Fig.1a caption]. Video source:
> KristenAndSara_1280x720_60.y4m and FourPeople_1280x720_60.y4m from
> https://media.xiph.org/video/derf/y4m [§3 fn.1]. Maximum video resolution:
> 720p [§2]. Monitoring: passive traffic capture at C1, C2, and MB (both
> ingress and egress), one pcap per monitoring point; flows split by RTP header
> type to distinguish video, audio, FEC, RTCP [§3]. QoE ground truth: WebEx
> client logs [§3, "we collect the logs from WebEx client to get information
> about the QoE of the run, which are used as ground truth"]. Processing:
> QoS and QoE values averaged over run after removal of initial/final transient
> phases [§3].

---


## Experiments

### qoe_qos_realtime-ES1 — Fully controlled testbed campaign (Figs 1b-e, 2, 3, Tab.2)

**(i) Raw text.**
"For each set of impairment values, we make 20 runs" [§3]; "a meeting of 10
minutes between the two clients. Overall, we collect data for over 1300 hours
of meetings" [§3]. Impairment sweep from Table 1 [Tab.1]:
- Bandwidth: 1, 2 and 10 Mbps
- Jitter: 0, 5, 10, 15, 20, 30, 40 and 50 ms
- Delay: 0, 5, 15, 30, 50, 75, 150 ms
- Loss model: Bernoulli and Markov Chain
- Loss rate (Bernoulli): 0, 5, 10, 15, 20 %
- Loss rate (Markov): P13 up to 20, P31 = 40
"In our experiments the maximum video resolution is set to 720p" [§2].
Application: Cisco WebEx video conferencing, two-client meeting via a media
bridge [§3, "In this work we focus on Cisco WebEx"; "two clients, C1 and C2,
are connected to a WebEx media bridge"]. QoE metrics: resolution, smoothness
(fps), concealment; residual losses used as concealment proxy [§2; §4.1].

**(ii) Grammar-v2 translation.**
ExperimentSet⟨leaves: sweep(
  Regime.Static.capacity ∈ {1, 2, 10} Mbps [Tab.1]
  × path.latency ∈ {0, 5, 15, 30, 50, 75, 150} ms one-way delay [Tab.1]
  × path.jitter ∈ {0, 5, 10, 15, 20, 30, 40, 50} ms [Tab.1]
  × path.loss: {Bernoulli(p ∈ {0, 5, 10, 15, 20} %) ∪
                Markov(P13 ≤ 20, P31 = 40)} [Tab.1]
  ; exact cross-product grid Not specified);
  leaf count Not specified⟩;

Experiment = ⟨
  Foreground: Workflow(webex-video-conference;
    participants = 2 (C1, C2) via media bridge;
    video-input = {KristenAndSara_1280x720_60.y4m,
                   FourPeople_1280x720_60.y4m} [§3 fn.1];
    max-resolution = 720p [§2]) @ C1 (impaired path), C2 (unimpaired path);
  Regime⟨
    Static:
      capacity ∈ {1, 2, 10} Mbps [Tab.1]
      (applied via tc on C1→media-bridge link; direction Not specified [§3];
       C2 link capacity Not specified / unimpaired);
      queue: Not specified (tc queueing discipline not stated [§3]);
    Dynamic: none
  ⟩;
  path (per C1 workflow; C2 path = unimpaired baseline):
    latency ∈ {0, 5, 15, 30, 50, 75, 150} ms [Tab.1];
    jitter ∈ {0, 5, 10, 15, 20, 30, 40, 50} ms [Tab.1];
    loss: Bernoulli(p ∈ {0, 5, 10, 15, 20} %) ∪
          Markov(params: {P13 ≤ 20, P31 = 40}) [Tab.1];
  cca: Not specified [§3; rendering §Exp1];
⟩;
iterations = 20 runs per config [§3];
telemetry {pcap: true (passive tshark at C1/C2/MB ingress+egress [§3]);
           app_metrics: true (WebEx client logs: resolution, fps, concealment,
             residual-loss [§3; §2])};
Roles ⟨clients: C1, C2 (containers in VM [§3]);
       server/bridge: WebEx media bridge (container [§3])⟩.

### qoe_qos_realtime-ES2 — Partially controlled "in the wild" campaign (Figs 1b-e, 4, 5)

**(i) Raw text.**
"6 clients instantiated in Paris, running a Mac OS instance of the WebEx application,
in different home networks" [§5.1]; "one Webex media bridge deployed in a VM in the
public cloud (AWS London)" [§5.1]; "Clients run in different home networks, thus
providing variability in terms of network condition, ISPs. etc." [§5.1]; "We run the
tests for more then one month" [§5.1, sic]; "daily runs of a 10 minutes long WebEx
meeting with 6 participants" [§5.1].

**(ii–iv) Grammar / requirements / match.**
**Design: OUT-OF-SCOPE.**
Network conditions are determined by real home networks and ISPs — no controlled
bottleneck Regime is applied by the experimenters. The experiment is an observational
deployment study of WebEx performance under real, uncontrolled network paths
(exogenous conditions). Pramana's grammar applies to experiments where the experimenter
controls the Regime; this study is structurally outside that model.

**Implementation: n/a** (design is OUT-OF-SCOPE).
**Mininet: n/a.**

**confidence: high**
