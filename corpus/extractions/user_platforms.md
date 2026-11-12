# user_platforms — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| uplat-ES1 | Exp1 (Tab.1, Figs.3,5,6, Tabs.5,6, Figs.12,13,14) | user_platform(30) × provider(4) × protocol_variant [§3.1, §3.2] | ~120 (per Table 1; exact counts per platform/provider; some providers TCP-only [§3.2]) | >100 video sessions per user_platform [§3.1] |
| uplat-ES2 | Exp2 (Tabs.3,4) | user_platform(same devices, different OS/agent versions [§4.3.2]) × provider(4) | Not specified (flows spread "evenly across all user platforms" [§4.3.2]; grid not enumerated) | Not specified |
| uplat-ES3 | Exp3 (Figs.7,8,9,10,11) | 1 campus deployment (passive monitoring, no researcher-controlled conditions) | 1 | 100+ million flows over 4 months [§5.2] |
| uplat-ES4 | Exp4 (no figures; §5.1 text-only) | 1 sanity-check campaign (all available user platforms, lab under campus system) | Not specified (">1000 video sessions" [§5.1], per-platform count not given) | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Video providers: YouTube, Netflix, Amazon Prime Video, Disney+ [§3.1]; devices:
> 3 mobile (iPhone, iPad, Android phone), 2 Windows PCs, 2 macOS MacBooks, 2 smart
> TVs (Android TV system + Android TV set-top box), 1 PlayStation gaming console [§3.1];
> software agents: native provider apps + Chrome, Firefox, Safari, Edge [§1, §3.1], Samsung
> Internet on Android mobile [Table 1]; 30 user platforms (device × software agent), 17
> unique types [§3.1]; transport: HTTPS over TCP or QUIC; only YouTube supports QUIC
> [§4.3, "at the time of this writing, only YouTube supports QUIC"]; capture: PCAP files
> at access gateway via Wireshark [§3.1]; session duration: at least 1 minute [§3.1];
> hardware: commodity blade server (Exp3) with 8-core Intel Xeon E5-2620, 64 GB DDR4
> RAM [§5.1]; no network condition emulation applied in Exp1/Exp2.

---


## Experiments

### uplat-ES1 — Lab traffic-trace collection (§3.1)

**(i) Raw text.** "our experimental framework to collect traffic trace files (i.e., PCAPs)
for video streaming sessions" [§3.1]; devices connect via Wi-Fi to the access gateway for
Internet access [§3.1]; PCAPs collected at the access gateway using Wireshark [§3.1];
"nearly 10,000 flows" total, "more than 100 video sessions per user platform" [§3.1];
each session ≥ 1 minute [§3.1]; "most recent versions" of OS, browsers, apps [§3.1];
network bandwidth / base latency / queue size / queue management / cross traffic / loss:
Not specified (real Wi-Fi + Internet, no emulation stated); 10-fold cross-validation
on the collected dataset [§4.3.1]; random forest, MLP, KNN classifiers [§4.3.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(user_platform × provider × protocol_variant,
~120 ATTEMPTED per Table 1 [§3.1, §3.2]) = ~120⟩; Experiment =
⟨Foreground = {Workflow(app_streaming, provider=<youtube|netflix|amazon|disney>,
params.user_platform=<device × browser/app>) @ node_client} ⊗
Regime⟨Static: capacity Not specified (real Wi-Fi/Internet link [§3.1]);
queue Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: lab device (mobile/PC/TV/console), server: real provider CDN⟩;
path.latency: Not specified; path.jitter: Not specified; path.loss: Not specified;
cca: Not specified (kernel default, no CCA authoring);
iterations: >100 video sessions per user_platform [§3.1]; telemetry {pcap: true
(PCAP at access gateway via Wireshark [§3.1])}.
DESIGN NOTE — The user_platform dimension (30 combinations of device × browser × OS)
is captured as a Workflow parameter (params.user_platform) within the Foreground
production. The v2 grammar does not have a dedicated browser_engine or device_type
field, but the Foreground = { Workflow_i @ node_i } production is open-ended and can
express sweeps over workflow configurations.

### uplat-ES2 — Home-network open-set collection (§4.3.2)

**(i) Raw text.** "dataset collected by one of the authors from their home network"
[§4.3.2]; "the devices in the home are the same as those in our experimental setup,
the OS versions as well as those of the software agents are different" [§4.3.2];
"over 2000 video flows spread evenly across all user platforms" [§4.3.2]; providers:
YouTube (TCP/QUIC), Netflix, Disney+, Amazon [Table 3]; models trained on Exp1 lab
data, evaluated on this home dataset (open-set evaluation) [§4.3.2]; collection
method, capture tool, topology, session duration, dates, network conditions: Not
specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(user_platform × provider × protocol_variant,
same platform set as Exp1 with different OS/agent versions [§4.3.2]); count Not
specified (>2000 flows "evenly spread" [§4.3.2]; per-platform/provider cell counts
not stated)⟩; Experiment =
⟨Foreground = {Workflow(app_streaming, provider=<youtube|netflix|disney|amazon>,
params.user_platform=<device × browser/app (home OS/agent versions)>) @ node_client}
⊗ Regime⟨Static: Not specified (home network, real ISP link [§4.3.2]);
Dynamic: Not specified⟩⟩ @
Roles⟨client: home devices, server: real provider CDN⟩;
path.latency: Not specified; path.loss: Not specified; cca: Not specified;
iterations: Not specified; telemetry {pcap: Not specified (capture method not stated
[§4.3.2])}.

### uplat-ES3 — Four-month campus deployment (§5.1–§5.2)

**(i) Raw text.** "analyze traffic between our university campus network ... and the
Internet in real time" [§5.1]; "server receives a copy of the traffic from the
university network border router" [§5.1]; two 10 Gbps network interfaces inbound and
outbound [§5.1]; "July 7th 2023, 00:00 to November 9th 2023, 23:59" [§5.2]; "over
100 million streaming video flows" [§5.2]; "about 20% of sessions with low
classification confidence excluded" [§5.2]; no control over traffic-generating users;
network conditions: passive observation of real user traffic [§5.1].

**(ii) Grammar.** OUT-OF-SCOPE. The experiment is a passive monitoring deployment on
a real campus network. The researchers observe copies of real user traffic (staff,
students, visitors, dormitory residents [§5.2]) over which they have no control.
No Regime is authored; no Foreground workload is issued by the researchers.
This is the passive-measurement OUT-OF-SCOPE criterion.

### uplat-ES4 — Campus ground-truth sanity check (text-only, §5.1)

**(i) Raw text.** "an additional sanity check of the classification methodology" [§5.1];
"over 1000 video sessions played using all available user platforms in the university
lab" [§5.1]; "captured by our system" (the deployed campus VNF) [§5.1]; results:
"misclassified instances less than 4% of streams" [§5.1]; providers, per-platform
counts, dates, network conditions: Not specified; results reported in prose only
(no figure or table).

**(ii) Grammar.** ExperimentSet⟨leaves: Not specified (>1000 sessions total [§5.1],
per-(user_platform × provider) counts not stated; "all available user platforms" implies
the same 30-platform set as Exp1 [§3.1])⟩; Experiment =
⟨Foreground = {Workflow(app_streaming, params.user_platform=<all available platforms>)
@ node_client} ⊗ Regime⟨Static: Not specified (campus lab environment, real Internet
link [§5.1]); Dynamic: Not specified⟩⟩ @
Roles⟨client: lab devices (all platforms), server: real provider CDN⟩;
path.latency: Not specified; cca: Not specified; iterations: Not specified;
telemetry {pcap: captured by campus VNF (deployed system) [§5.1]}.
