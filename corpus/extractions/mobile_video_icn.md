# mobile_video_icn — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Scope classification | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- | --- |
| mvicn-ES1 | Exp1 (text-only, §2–§3) | OUT-OF-SCOPE (ICN networking layer; not IP/TCP) | single demo campaign; access type ∈ {WiFi 802.11n, LTE, Ethernet} (emulated); ABR algo ∈ {BBA, PANDA, BOLA, Adaptech} [§2] | Not specified (no quantitative sweep stated) | Not specified |

## Experiments

### mvicn-ES1 — ICN-enabled DASH live demonstration over emulated heterogeneous wireless access (text-only, §2–§3)

**(i) Raw text.** "The mobile video architecture considered in the demo (Figure 1) consists of several DASH clients, both physical (tablets or desktop computers) and emulated (via Linux containers, LXC)" [§2]. "Clients are connected using either WiFi 802.11n, LTE or Ethernet" [§2]; "Different wireless accesses are emulated (WiFi 802.11n and LTE)" [§2]. Transport/protocol: application-level selection of ICN (CICN, NDN/CCNx-style) or standard TCP/IP [§2]. "the following state-of-the-art bitrate adaptation logics: BBA [6], PANDA [8], BOLA [13], Adaptech [7]" [§2]. Server: "an HTTP server that can stream content over ICN or standard TCP/IP directly" [§2]. ICN features: "simple LRU in-network caching" [§1]; "sub-round trip time loss control by delegation at key nodes" [§3(2)]; "packet-level load balancing over multiple and dynamically discovered network accesses" [§3(3)]. "A live monitoring of network status and of key video performance metrics is provided in the demo" [§1]. Network bandwidth / base latency / RTT / queue size / queue management / cross traffic / loss rates: Not specified. Number of clients, exact topology, repetitions, duration: Not specified.

**(ii) Grammar-v2 translation.** The experiment's networking layer is ICN (CICN). Attempt: ExperimentSet; Foreground = Workflow(DASH video streaming; ABR algo ∈ {BBA, PANDA, BOLA, Adaptech} [§2]) ⊗ Regime⟨Static: path = ⟨capacity: Not specified, latency: Not specified⟩ (emulated WiFi 802.11n and LTE accesses [§2])⟩. However, the transport is ICN — not TCP/IP. Named-data forwarding, in-network caching policies, and ICN routing are also outside the grammar vocabulary. No complete grammar-v2 translation is possible. OUT-OF-SCOPE. 