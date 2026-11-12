# three_bits — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| three_bits-ES1 | Exp1 | path.reorder ∈ [0–40]% axis range [Fig 3(b)/(c)] | Not specified (axis-only; §5b.1) | Not specified |
| three_bits-ES2 | Exp2 | path.loss (Gilbert burst model; avg burst length ∈ [0–20] pkts [Fig 4(b)/(c)]) | Not specified (axis-only; §5b.1) | Not specified |
| three_bits-ES3 | Exp3 | n/a — OUT-OF-SCOPE (passive real-Internet TCP measurement [§4.1]) | n/a | n/a |
| three_bits-ES4 | Exp4 | n/a — OUT-OF-SCOPE (passive real-Internet TCP measurement [§4.1]) | n/a | n/a |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> QUIC emulation (ES1, ES2): Mininet [§3.1, "on an emulated network using Mininet"];
> QUIC implementation: minq, draft-05 [§1, "an open-source QUIC library (implementing
> the draft-05 version of QUIC)", footnote 1: github.com/pietdevaere/minq]; custom header
> modification: one additional measurement byte carrying spin bit and VEC in QUIC short header
> [§3]; base RTT: 40 ms (propagation delay without queuing) [§3.1]; workload: client
> continuously uploads data at constant rate below maximum link capacity [§3.1]; traffic
> adaptivity: non-adaptive only [§3.1, "We only present the results for non-adaptive traffic
> in this paper"]; impairment tool: NetEm [§3.1.1, §3.1.2]; four observer mechanisms
> compared in-campaign on same runs: Spin bit, Packet number, Heuristic, VEC [§3.1];
> observer vantage: sees both flow directions [§3.1]; metrics: error relative to RFC 6298
> client-estimated RTT and samples per RTT [§3.1]; bandwidth/link capacity: Not specified;
> queue size/discipline: Not specified; CCA: Not specified (non-adaptive traffic,
> constant rate below capacity); cross traffic: Not specified (silence); duration: Not
> specified; repetitions: Not specified.


## Experiments

### three_bits-ES1 — QUIC Mininet: packet-reordering sweep (Fig 3)

**(i) Raw text.** "We use NetEm [8] to randomly delay a configured fraction of packets by
1 ms" [§3.1.1]. ECDF at 10% reordering rate [Fig 3(a) caption, "for a 10% packet reordering
rate"]; sweep axis 0–40% [Fig 3(b)/(c) x-axis: "Packet reordering rate [%]" with ticks
0, 10, 20, 30, 40]. Four observer mechanisms (Spin bit, Packet number, Heuristic, VEC
+ VEC half-RTT) applied to same runs [§3.1]. Metrics: error vs RFC 6298 RTT, samples per
RTT [§3.1]. Base RTT 40 ms, constant-rate QUIC upload, Mininet, minq draft-05 [§3, §3.1].
Bandwidth, queue size/discipline, CCA, cross traffic, duration, repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(path.reorder ∈ [0–40]% [Fig 3(b)/(c)
x-axis]); count Not specified (axis-only)⟩; Experiment = ⟨Workflow(QUIC constant-rate
upload; tool: minq draft-05 with spin-bit/VEC header extensions [§1, §3]) @
path⟨latency: 40 ms [§3.1], reorder: swept [§3.1.1, "randomly delay a configured fraction
of packets by 1 ms"]⟩ ⊗ Regime⟨Static: capacity Not specified, queue: Not specified;
Dynamic: Not specified (silence — no positive no-cross-traffic statement)⟩⟩ @
Roles⟨client: Mininet host, server: Mininet host⟩; iterations Not specified;
telemetry {pcap: true (observer reads spin-bit/VEC from captured traffic [§3.1]),
app_metrics: true (client-side RFC 6298 RTT estimate as ground reference [§3.1])}.

### three_bits-ES2 — QUIC Mininet: burst-loss sweep (Fig 4)

**(i) Raw text.** "configured NetEm to emulate burst loss using the simple Gilbert model
[6]" [§3.1.2]. "The good reception periods have an average length of 100 packets" [§3.1.2].
"The average length of the loss bursts is varied" [§3.1.2]; ECDF at 10 packets [Fig 4(a)
caption, "for an average burst length of 10 packets"]; sweep axis 0–20 packets [Fig 4(b)/(c)
x-axis: "Average burst length [packets]" with ticks 0, 5, 10, 15, 20]. Four observer
mechanisms on same runs (shared methodology block A [§3.1]). Base RTT 40 ms, minq draft-05
[§3, §3.1]. Bandwidth, queue, CCA, cross traffic, duration, repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(path.loss (Gilbert burst model; avg burst
length ∈ [0–20] pkts [Fig 4(b)/(c)]); count Not specified (axis-only)⟩;
Experiment = ⟨Workflow(QUIC constant-rate upload; tool: minq draft-05 [§1]) @
path⟨latency: 40 ms [§3.1], loss: burst (Gilbert model; avg good-reception period 100 pkts
[§3.1.2]; avg burst-length swept [§3.1.2])⟩ ⊗
Regime⟨Static: capacity Not specified, queue: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Mininet host, server: Mininet host⟩; iterations Not specified;
telemetry {pcap: true [§3.1], app_metrics: true (RFC 6298 RTT estimate [§3.1])}.

### three_bits-ES3 — TCP testbed: inter-datacenter collection (Fig 5a, Fig 6a)

**(i) Raw text.** "we implemented the signal in a patch for Linux 4.9 and 4.15, using the
three reserved flag bits in the TCP header" [§4]. "set up a simple test web server on each
of them" [§4.1]. "virtual machines on cloud nodes in seven networks with a global distribution
— DigitalOcean VMs in regions NYC1, SFO2, AMS3, SGP1, BLR1, FRA1, and LON1" [§4.1, footnote 9].
Deployment date: "on 25 May 2018" [§4.1]. "49 traces of 120 seconds each" [§4.1]. "all traffic
between these nodes routed through an observation node running our VPP code in our local,
on-campus infrastructure" [§4.1]. Real Internet paths; no controlled bandwidth, latency, queue,
or CCA. Reported median error vs TCP timestamps: -0.03% [§4.1]; median samples per estimated
average RTT: 1.97 [§4.1].

**(ii) Grammar.** OUT-OF-SCOPE. Real-world passive Internet measurement: traffic flows over
real Internet paths between cloud VMs; no controlled bottleneck, no imposed Regime; a passive
VPP-based observer at a campus network point captures TCP traffic to validate spin-bit/VEC
RTT estimation vs TCP timestamps. No grammar translation is possible — there is no Regime to
configure and no controlled path parameters.

### three_bits-ES4 — TCP testbed: European access-network collection (Fig 5b/c, Fig 6b/c)

**(i) Raw text.** "we accessed each server from five access networks in Europe" [§4.1].
"On those networks where both wired and wireless endpoint connections were possible, we
measured both" [§4.1]. "also steering traffic past our measurement node" [§4.1]. "This
yielded 53 additional traces" [§4.1]. Real access-network paths. Median error: -0.04%
(wired), 1.04% (wireless) [§4.1]; median samples per estimated average RTT: 1.82 (wired,
high variance), 1.94 (wireless) [§4.1]. Path anomaly: TCP header manipulation at one
access router mangled spin signal [§4.1 footnote 12]; one wired node had high reordering
"probably due to traffic shaping" [§4.1]. Trace duration Not specified (120 s attaches to
the DC-to-DC 49 traces; Fig 5(b)/(c) axes span 0–120 s but this is the plotted window
only [rendering Exp4 notes]).

**(ii) Grammar.** OUT-OF-SCOPE. INHERITED rationale from ES3: real Internet access-network
paths; no controlled Regime; passive TCP spin-bit observer. The wired vs wireless distinction
is an exogenous access-medium variable, not a controlled parameter.
