# cambrian_quic — Experiment-Set Intent Corpus (v4 re-render, grammar v2)

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| cambrian_quic-ES1 | E1 | (stack, cca) ∈ Table-1 supported set (22 per Table-1 ✓s) × RTT ∈ {10, 50} ms × bw ∈ {20, 100} Mbps × buffer ∈ {0.5, 1, 3, 5}×BDP [§4]; plus kernel-reference self-PE leaves | 22×2×2×4 = 352 QUIC-impl leaves; reference self-PE leaf count Not specified | 5 [§4] |
| cambrian_quic-ES2 | E2 | cwndgain ∈ [1.0, 4.0] (point count Not specified) [§3.3] | Not specified | 5 (Part-B inheritance [§4]) |
| cambrian_quic-ES3 | E3 | impl ∈ Fig-11 heatmap set (count Not specified); single condition (100 Mbps, 50 ms) [§4.2] | Not specified | 5 (Part-B inheritance) |
| cambrian_quic-ES4 | E4 | pair ∈ pairwise(23 QUIC CCA impls [§4.3]) × buffer 1 BDP; + CUBIC-vs-BBR pairs × 5 BDP [Fig 13b] | Not specified | 5 [§4.3] |
| cambrian_quic-ES5 | E5 | 1 (chromium CUBIC, flows 2→1, 1 BDP) [Table 4] | 1 | 5 (Part-B inheritance) |
| cambrian_quic-ES6 | E6 | 1 (mvfst BBR, pacing gain 1.25→1, 1 BDP) [Table 4] | 1 | 5 (Part-B inheritance) |
| cambrian_quic-ES7 | E7 | 1 (xquic BBR, cwnd gain 2.5→2, 1 BDP) [Table 4; Fig 14] | 1 | 5 (Part-B inheritance) |
| cambrian_quic-ES8 | E8 | 1 (quiche CUBIC, RFC 8312 disabled, 1 BDP) [Table 4; Fig 15] | 1 | 5 (Part-B inheritance) |
| cambrian_quic-ES9 | E9 | 1 (xquic CUBIC vs TCP-CUBIC-w/o-HyStart reference, 1 BDP) [§5; Table 4] | 1 | 5 (Part-B inheritance) |

## Experiments

### cambrian_quic-ES1 — main testbed conformance sweep (Figs 1–4, 6–10; Tables 3, 4-original)

**(i) Raw text.** Shared Part B block above, plus: "RTT (10 ms and 50 ms)",
"bottleneck bandwidth (20 Mbps and 100 Mbps)", "bottleneck buffer size (0.5,
1, 3, 5 times the BDP)" [§4]; subjects = 11 QUIC stacks at pinned commit
hashes [Table 1]; reference = Linux 5.13.0-44-generic kernel TCP [Table 1];
"simple 2-flow experiments without any background traffic" [§4].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.workflow ∈
{quicbench_pair(stack, cca)} over 22 Table-1-supported (stack, cca) pairs ×
static ∈ (capacity {20, 100} mbps × queue.args {0.5, 1, 3, 5}·BDP)) = 352; reference self-PE leaf family (tcp_reference_pair(cca), cca ∈ {cubic, bbr,
reno}), grid coverage Not specified⟩; Experiment = ⟨Workflow(quicbench_pair; shell; params {stack@Table-1-commit,
cca, duration 120 s [§3.1], socket_buffer 12582912 bytes [§3.4]}) ⊗
Regime⟨Static: capacity_down {20, 100} mbps [§4], capacity_up {20, 100} mbps
[§4], queue⟨discipline: droptail [§3.1] (pfifo spelling = compile
realization), size: Not specified (derived from k·BDP per leaf), params:
{limit: k·BDP(bw,RTT)} (per-leaf coupled value, flat-expanded, not a sweeps:
axis), ecn: Not specified, mode: Not specified⟩; Dynamic: mode none [§4
positive]⟩⟩; path⟨latency: {5, 25} ms one-way (RTT {10, 50} ms [§4] at the bottleneck via
tc/netem; cca⟨algo: {cubic, bbr, reno} (per leaf, kernel reference flow), stack: kernel,
version: 5.13.0-44 [§3.4], params: Not specified, flags: Not specified, build:
Not specified⟩ — kernel reference flow only; QUIC flow CCA rides
application.workflow.params (application-layer, not a kernel module); @ Roles⟨client: Node, server: Node (both lab machines [§3.4])⟩; iterations: 5 [§4]; telemetry {pcap: true ("computed offline via packet trace" [§3.1]), qtrace: Not
specified, app_metrics: Not specified}. confidence: high.

### cambrian_quic-ES2 — modified-kernel-BBR cwndgain sweep (Fig 5)

**(i) Raw text.** "We modified the kernel version of BBR by changing its
cwndgain and measured the Conformance and Conformance-T values for modified
implementations with a range of cwndgain values from 1.0 to 4.0" [§3.3]; "By
default, cwndgain is set to 2 in the Linux kernel" [§3.3]. Bandwidth, RTT,
buffer, number of cwndgain points: Not specified [gold E2].

**(ii) Grammar v2.** ExperimentSet⟨leaves: one per swept cwndgain value,
point count Not specified⟩ — the swept dimension is
"kernel BBR with cwndgain ∈ [1.0, 4.0]" [§3.3], which cannot be expressed as
`cca⟨algo: bbr, params: {cwndgain: X}⟩` because `cca.params` is not a sweeps:
axis; this remains the GAP-DESIGN below.
Experiment = ⟨Workflow(quicbench_pair variant: modified-kernel-BBR flow vs
kernel-BBR reference flow; both TCP) ⊗ Regime⟨Static: capacity_down/up Not
specified, queue⟨discipline: droptail [§3.1], size: Not specified, params: Not
specified, ecn: Not specified, mode: Not specified⟩; Dynamic: mode none [§4
positive]⟩⟩;
path⟨latency: Not specified (inherits §3.1 methodology; values not restated in
§3.3), jitter: Not specified, loss: Not specified, reorder: Not specified, dup:
Not specified⟩;
cca: inexpressible as a sweep axis (see Design below);
@ Roles⟨client, server: lab machines [§3.4]⟩; iterations: 5 (Part-B
inheritance [§4]); telemetry {pcap: true [§3.1]}.
confidence: high.

### cambrian_quic-ES3 — in-the-wild / AWS conformance (Fig 11)

**(i) Raw text.** "We repeated our experiments in §4.1 on the Internet. In
these measurements, the senders were run on aws instances and connected to
receivers on physical servers in our lab. We limited the link speed to 100
Mbps at the server. We measured the ping latency before every experiment and
added additional delay using Mahimahi [37] to keep the RTT constant at 50 ms
across all trials." [§4.2]; results = conformance heatmap [Fig 11: "Link
speed was locally limited to 100 Mbps" [Fig 11 caption]]. Buffer, trial count,
AWS instance type/region: Not specified [gold E3].

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.workflow over
the Fig-11 impl set; count Not specified); mapping: sender nodes on aws,
receiver nodes local [§4.2]⟩;
Experiment = ⟨Workflow(quicbench_pair(stack, cca)) ⊗ Regime⟨Static:
capacity_down 100 mbps [§4.2] (imposed at the server-side edge),
capacity_up Not specified, queue⟨discipline: Not specified, size: Not
specified, params: Not specified, ecn: Not specified, mode: Not specified⟩;
Dynamic: the real Internet path's cross traffic — inhabited, uncontrolled⟩⟩;
path⟨latency: 50 ms RTT-target (held constant via measure-ping-then-pad
[§4.2]; this is a CLOSED-LOOP CONDITION CONTROL with no A5 production —
the GAP-DESIGN below), jitter: Not specified (real WAN, uncontrolled), loss:
Not specified, reorder: Not specified, dup: Not specified⟩;
cca⟨algo: {cubic, bbr, reno} (per leaf, kernel reference), stack: kernel,
version: 5.13.0-44 [§3.4], params: Not specified, flags: Not specified,
build: Not specified⟩ — kernel reference flow; QUIC flow CCA in workflow.params;
@ Roles⟨client (sender): aws node, server (receiver): lab node⟩;
iterations: 5 (Part-B inheritance); telemetry {pcap: true [§3.1]}.
confidence: high.

### cambrian_quic-ES4 — pairwise bandwidth-share fairness (Figs 12, 13)

**(i) Raw text.** "a simple bandwidth-share-based analysis of the pairwise
combinations of all 23 QUIC CCA implementations investigated in this paper"
[§4.3]; "the two competing flows share a 20 Mbps bottleneck link, 50 ms RTT,
and a 1 BDP buffer" [§4.3]; throughputs "averaged across 5 trials" [§4.3];
CUBIC-vs-BBR at 5 BDP [Fig 13b]. Per-run duration: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: sweep(application.params.{impl_x,
impl_y} ∈ pairwise(23) × queue.params.limit ∈ {1·BDP, CUBIC-vs-BBR × 5·BDP});
exact leaf count Not specified⟩;
Experiment = ⟨Workflow(quic_pair(impl_x, impl_y); shell; both flows QUIC — no
kernel reference flow) ⊗ Regime⟨Static: capacity_down 20 mbps [§4.3],
capacity_up Not specified, queue⟨discipline: droptail [§3.1], size: Not
specified, params: {limit: 1 or 5 BDP}, ecn: Not specified, mode: Not
specified⟩; Dynamic: mode none [§4 positive]⟩⟩;
path⟨latency: 25 ms one-way (RTT 50 ms [§4.3]), jitter: Not specified, loss:
Not specified, reorder: Not specified, dup: Not specified⟩;
cca: Not specified (no kernel flow among the measured pair — compile
default-with-echo, §5b.2);
@ Roles⟨client, server: lab machines⟩;
iterations: 5 [§4.3]; telemetry {pcap: true (per-flow throughputs)}.
confidence: high.
interpreted: "20 Mbps" in §4.3 is one-sided bottleneck capacity (capacity_down);
capacity_up not stated, listed as Not specified.

### cambrian_quic-ES5 — chromium-CUBIC fix: emulated flows 2→1 (Table 4)

**(i) Raw text.** Table 4 row: chromium+ CUBIC, "Emulated flows reduced from
2 to 1", ΔLoC 1, Conf 0.6→0.78, Conf-T 0.74→0.85 [Table 4]; 1 BDP [Table 4
caption]. Bandwidth/RTT: Not specified [gold E5].

**(ii) Grammar v2.** ExperimentSet⟨leaves: 1⟩;
Experiment = ⟨Workflow(quicbench_pair(chromium_modified, cubic); the modified
build — emulated flows 2→1 — is a distinct application artifact; params:
{build: Table-4-patched-chromium}) ⊗ Regime⟨Static: capacity_down/up Not
specified, queue⟨discipline: droptail [§3.1], size: Not specified, params:
{limit: 1·BDP [Table 4]}, ecn: Not specified, mode: Not specified⟩;
Dynamic: mode none [§4 positive]⟩⟩;
path⟨latency: Not specified (bw/RTT not restated for this leaf), jitter: Not
specified, loss: Not specified, reorder: Not specified, dup: Not specified⟩;
cca⟨algo: cubic, stack: kernel, version: 5.13.0-44 [§3.4], params: Not
specified, flags: Not specified, build: Not specified⟩ (reference flow);
QUIC flow CCA in workflow.params (chromium_modified, cubic);
@ Roles⟨client, server: lab machines⟩; iterations: 5 (Part-B inheritance);
telemetry {pcap: true [§3.1]}.
confidence: high.

### cambrian_quic-ES6 — mvfst-BBR fix: pacing gain 1.25→1 (Table 4)

**(i) Raw text.** Table 4 row: mvfst+ BBR, "pacing gain reduced from 1.25 to
1", ΔLoC 2, Conf 0→0.8, Conf-T 0.7→0.8 [Table 4]; 1 BDP [Table 4 caption].
Bandwidth/RTT: Not specified.

**(ii)–(iv).** Identical structure to ES5 with the subject swapped (modified
mvfst build vs kernel BBR reference; reference cca⟨algo: bbr, stack: kernel,
version: 5.13.0-44⟩). confidence: high.

### cambrian_quic-ES7 — xquic-BBR fix: cwnd gain 2.5→2 (Fig 14; Table 4)

**(i) Raw text.** "we found its cwndgain was set to 2.5 instead of the
RFC-recommended value of 2. By setting the cwndgain to 2, we were able to
marginally improve conformance as shown in Figure 14." [§5]; Table 4 row:
xquic BBR, "cwnd gain reduced from 2.5 to 2", ΔLoC 2, Conf 0.15→0.38, Conf-T
0.42→0.47 [Table 4; Fig 14 captions]; 1 BDP [Table 4 caption]. Bandwidth/RTT:
Not specified.

**(ii)–(iv).** INHERITED from ES5, delta: subject = patched xquic build (BBR),
reference cca⟨algo: bbr, stack: kernel, version: 5.13.0-44⟩. confidence: high.

### cambrian_quic-ES8 — quiche-CUBIC fix: RFC 8312 disabled (Fig 15; Table 4)

**(i) Raw text.** "When we disabled it in quiche CUBIC, we saw an immediate
improvement in its conformance from 0.08 to 0.55 as shown in Figure 15." [§5];
Table 4 row: quiche CUBIC, "Disabled RFC8312 [46]", ΔLoC 14, Conf 0.08→0.55,
Conf-T 0.55→0.66 [Table 4]; 1 BDP [Table 4 caption]. Bandwidth/RTT: Not
specified.

**(ii)–(iv).** INHERITED from ES5, delta: subject = patched quiche build
(CUBIC), reference cca⟨algo: cubic, stack: kernel, version: 5.13.0-44⟩. confidence: high.

### cambrian_quic-ES9 — xquic-CUBIC vs TCP-CUBIC-without-HyStart (Table 4)

**(i) Raw text.** "To verify that this missing mechanism was the main cause of
low conformance, we evaluated the conformance of xquic CUBIC with respect to
TCP CUBIC with HyStart disabled." [§5]; Table 4: xquic CUBIC, Conf 0.55→0.72,
Conf-T 0.64→0.81, "Compared to TCP CUBIC w/o HyStart" [Table 4]; 1 BDP [Table
4 caption]. Bandwidth/RTT: Not specified.

**(ii) Grammar v2.** ExperimentSet⟨leaves: 1⟩;
Experiment = ⟨Workflow(quicbench_pair(xquic, cubic) — the UNMODIFIED xquic
build) ⊗ Regime⟨Static: capacity_down/up Not specified, queue⟨discipline:
droptail [§3.1], size: Not specified, params: {limit: 1·BDP [Table 4]}, ecn:
Not specified, mode: Not specified⟩; Dynamic: mode none [§4 positive]⟩⟩;
path⟨latency: Not specified, jitter: Not specified, loss: Not specified,
reorder: Not specified, dup: Not specified⟩;
cca: cubic — but the reference flow requires HyStart disabled [§5], a
configuration qualifier that `cca.params` cannot carry as a sweeps: axis or as
an enum-validated field (the GAP-DESIGN below);
@ Roles⟨client, server: lab machines⟩; iterations: 5 (Part-B inheritance);
telemetry {pcap: true [§3.1]}.
confidence: high.
