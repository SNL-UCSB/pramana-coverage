# gcp_netperf — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| gcp_netperf-ES1 | Exp1 (topology pilot scan) | target ∈ all U.S. speed test servers (1,329) [§4]; region ∈ 5 GCP U.S. regions [§4; Table 1] | 1,329 × 5 (pilot) → ~100 servers selected per region [§4] | 1 (one-time selection) [§3.1] |
| gcp_netperf-ES2 | Exp2 (differential prelim.) | Speedchecker VP × GCP VM pair × GCP routing tier ∈ {premium, standard} [§3.1] | Not specified ("more than 100 measurements" threshold per tuple [§3.1]) | Not specified |
| gcp_netperf-ES3 | Exp3 (topology longitudinal) | region ∈ {us-west1, us-west2, us-east1, us-east4, us-central1} × test server ∈ topology-selected set [Table 1] | ~411 region-server pairs [Table 1: 106+25+184+40+56] | 1/hr for 5 months (May–Sep 2020) [§1] |
| gcp_netperf-ES4 | Exp4 (differential longitudinal) | region ∈ {us-central1, us-east1, europe-west1} × tier ∈ {premium, standard} × test server ∈ differential-selected set [§4] | 47 region-server pairs (15+15+17) × 2 tiers [§4] | 1/hr for 2 months (Aug–Sep 2020) [§4] |

## Shared methodology (raw text, Exp3 and Exp4) (quoted from the paper)


> CLASP measurement methodology [§3.2]; web-based speed tests via "a Chromium browser,
> capturing results reported on the web interface" [§3.2]; platforms: Ookla, M-Lab,
> Comcast Xfinity [§3.1]; GCP VMs type n1-standard-2 or n2-standard-2; "downlink/uplink
> throttled to 1Gbps/100Mbps using Linux tc" [§3.2]; each throughput test ≤ 120 s [§3.2];
> tests executed hourly via cron jobs [§3.2]; tcpdump packet-header capture; scamper
> paris-traceroute after each test [§3.2]. Congestion control algorithm, queue
> management, cross traffic: Not specified.


## Experiments

### gcp_netperf-ES1 — Topology-based pilot scan (server selection)

**(i) Raw text.** Pilot scan from GCP VMs: bdrmap to discover interdomain links, then
traceroutes to all speed test servers in the U.S. [§3.1]; "1,329" total U.S. servers
[§4]; "around 100 servers that traversed unique interconnections" selected per region
[§4]; interdomain links per region 5,293 / 6,609 / 6,217 / 5,255 / 6,582
(us-west1 / us-west2 / us-east1 / us-east4 / us-central1) [Table 1]; "pilot tests
to select test servers only once in the beginning of the experiment" [§5]. Pilot
VM type, date, traceroute count: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(target ∈ all U.S. speed test servers
× source ∈ 5 GCP regions); count: 1,329 servers × 5 regions ATTEMPTED [§4; Table 1]⟩;
Experiment = ⟨Workflow(bdrmap + scamper traceroute; shell) ⊗
Regime⟨Static: Not specified (no imposed bottleneck; passive path measurement);
Dynamic: Not specified⟩⟩ @
Roles⟨client: GCP VM (premium tier), server: real third-party speed test servers⟩;
iterations: 1 (one-time pilot) [§3.1]; telemetry {app_metrics: true (traceroute
hop adjacencies, interdomain link coverage [§3.1])}.

### gcp_netperf-ES2 — Differential-based preliminary latency test (server selection)

**(i) Raw text.** Speedchecker vantage points (>10,000 networks, 200 countries) [§3.1];
latency from VPs to GCP VMs on both premium and standard tiers; tuples with <100
measurements discarded [§3.1]; |premium_RTT − standard_RTT| ≥ 50 ms or < 10 ms
threshold [§3.1]; "15-16 speed test servers" selected [§3.1]; "15 (us-central1 and
us-east1) and 17 (europe-west1) servers" [§4] — paper-internal inconsistency,
reported as printed. Collection date, VM type, number of VPs, probe count: Not
specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(Speedchecker VP × GCP VM ×
tier ∈ {premium, standard}); count: Not specified (tuples surviving >100-measurement
threshold [§3.1])⟩; Experiment = ⟨Workflow(latency probe; Speedchecker platform)
⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Speedchecker third-party vantage points, server: GCP VMs (premium +
standard tiers)⟩; iterations Not specified; telemetry {app_metrics: true (latency
per (city, AS, VM region, tier) tuple [§3.1])}.

### gcp_netperf-ES3 — Topology-based longitudinal throughput campaign

**(i) Raw text.** "five months, May - September, 2020" [§1]; "5 GCP regions in the
U.S." [§4]; servers per region: 106 (us-west1), 25 (us-west2), 184 (us-east1),
40 (us-east4), 56 (us-central1) [Table 1]; GCP VMs "n1-standard-2 or n2-standard-2"
[§3.2]; "downlink/uplink throttled to 1Gbps/100Mbps using Linux tc" [§3.2]; each
throughput test ≤ 120 s [§3.2]; "one throughput test per hour per test server" [§3.2];
Chromium web-based speed tests (Ookla, M-Lab, Comcast Xfinity) [§3.1]; default
premium tier routing. CCA, queue, cross traffic: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(region ∈ {us-west1, us-west2, us-east1,
us-east4, us-central1} × test-server ∈ topology-selected set); count: ~411
region-server pairs (106+25+184+40+56) [Table 1]⟩; Experiment =
⟨Workflow(web speed test; Chromium browser [§3.2]) ⊗
Regime⟨Static: VM egress capped at 1 Gbps downlink / 100 Mbps uplink via tc [§3.2];
path: Not specified (real Internet path beyond the VM); Dynamic: Not specified⟩⟩ @
Roles⟨client: GCP VM (premium tier), server: real third-party speed test endpoints⟩;
iterations: hourly for 5 months [§1]; telemetry {app_metrics: true (throughput,
latency, packet loss per speed test [§3.2])}.

### gcp_netperf-ES4 — Differential-based longitudinal throughput campaign

**(i) Raw text.** "2 months of data, August - September, 2020" [§4]; regions:
us-central1, us-east1, europe-west1 [§4]; "15 (us-central1 and us-east1) and
17 (europe-west1) servers" [§4]; "one pair of VMs in each region" — premium + standard
[§4]; "three pairs of VMs" total [§4.1]; same CLASP methodology as Exp3 [§3.2].
CCA, queue, cross traffic: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(region ∈ {us-central1, us-east1,
europe-west1} × tier ∈ {premium, standard} × test-server ∈ differential-selected set);
count: (15+15+17) × 2 = 94 region-server-tier combinations [§4]⟩; Experiment =
⟨Workflow(web speed test; Chromium browser [§3.2]) ⊗
Regime⟨Static: VM egress capped at 1 Gbps downlink / 100 Mbps uplink via tc [§3.2];
path: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: GCP VM pair (premium + standard tier), server: real third-party speed
test endpoints⟩; iterations: hourly for 2 months [§4]; telemetry {app_metrics:
true (throughput, latency per tier [§4.1])}.
