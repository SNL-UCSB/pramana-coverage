# decentralized_dns — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Description | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| decentralized_dns-ES1 | Exp1 | RTT to CDN replicas, US client via RIPE Atlas | sweep(resolver ∈ {local, AR, IN} × CDN ∈ {Akamai, CloudFront} × target ∈ top50 US sites [§2]) = Not specified | 5 RTT runs/site [§2] |
| decentralized_dns-ES2 | Exp2 | RTT to CDN replicas, German client (appendix) | sweep(resolver × CDN × target ∈ top50 DE sites [Fig 16 caption]) = Not specified | Not specified |
| decentralized_dns-ES3 | Exp3 | Institutional DNS-log k-anonymity analysis | 1 dataset (85,967 users, 2 weeks [§4.2]) | Not specified |
| decentralized_dns-ES4 | Exp4 | Cross-country DNS resolution-time measurement | sweep(country ∈ {AR, DE, IN, US} × DNS service × target ∈ top50 per country [§4.3]) = Not specified | 3 requests/resource [§4.3] |
| decentralized_dns-ES5 | Exp5 | DNS racing-configuration experiment | sweep(config ∈ {No Racing, Racing 2, Racing 3} [Tab. 3]) = 3 | Not specified |
| decentralized_dns-ES6 | Exp6 | DNS-variant privacy/performance tradeoff | sweep(variant ∈ {Tor, ISP, third-party, sharding, Ónoma} [§4.3.1]) = Not specified | Not specified |
| decentralized_dns-ES7 | Exp7 | CDN-popularity measurement across locales | sweep(country ∈ {AR, DE, IN, US} × CDN ∈ {Akamai, Amazon, Fastly} [Fig 9 caption]) = 4 × 3 = 12 | Not specified |
| decentralized_dns-ES8 | Exp8 | TTFB per (DNS service, CDN, country), Lighthouse | sweep(country × CDN × DNS service [§4.3.2]) = Not specified | 3 loads/resource [§4.3.2] |
| decentralized_dns-ES9 | Exp9 | Ónoma vs. sharding TTFB comparison | sweep(locale × CDN [§4.3.2]) = Not specified | 3 loads/resource [§4.3.2] |
| decentralized_dns-ES10 | Exp10 | End-to-end Ónoma evaluation | sweep(CDN × country [§6]) = Not specified | 3 runs/resource [§6] |

## Experiments

### decentralized_dns-ES1 — RTT to CDN replicas, US client (Fig 1, Fig 15)

**(i) Raw text.** "we select top50 Alexa sites in the US and resolve the
resources of these sites, hosted on the two most popular CDNs – Akamai and
Amazon CloudFront, using the Ripe Atlas DNS API. We use probes in the US …
median round-trip time (RTT) of five runs" [§2]; "9ms for the local resolver
and 160ms with a resolver in India in the case of Akamai" [§2]. Measurement
platform RIPE Atlas [§2]; distant resolvers in Argentina and India [§2].
Emulator/testbed: none — real Internet paths.

**(ii) Grammar.** No controlled network Regime; no Pramana Workflow. The
"experiment" is a passive RTT probe from real Atlas vantage points to real
CDN replicas via real DNS resolvers. Pramana grammar has no production for
"RIPE Atlas probe → real CDN endpoint over live Internet."
ExperimentSet ⟨leaves: Not specified; real-Internet measurement campaign⟩;
Regime: none imposed (exogenous — inhabited by real Internet paths and real
CDN replica-assignment logic); Dynamic: Not specified; telemetry: {RTT to
assigned CDN replica (app_metrics)}.

### decentralized_dns-ES2 — RTT to CDN replicas, German client (Fig 16)

**(i) Raw text.** "the importance of DNS for replica selection for the client
in Germany" [§A.1]; resources of top50 German websites [Fig 16 caption]; CDNs:
Akamai, Amazon CloudFront, Fastly [Fig 16 caption]; local resolver (cyan) vs.
distant ones in Sweden and India [Fig 16 caption]; metric: RTT to assigned
replica servers (/24) [Fig 16 caption]. Measurement platform: Not specified
(RIPE Atlas stated only for the US client in §2; not restated for Germany).

**(ii) Grammar.** Same as ES1 — no controlled Regime; passive RTT measurement
from a European vantage point to real CDN replicas. ExperimentSet ⟨leaves:
Not specified; real-Internet measurement, Germany client⟩; Regime: none
imposed; Dynamic: Not specified.

### decentralized_dns-ES3 — Institutional DNS-log k-anonymity analysis (Figs 2–4, Tab 1, Fig 8 y-axis)

**(i) Raw text.** "two weeks of users' DNS logs … 85,967 users" [§4.2];
"boolean vector … union of the 50 most popular domains" [§4.2]; sharding
values: no sharding, 2, 4, 8 [Fig 2 legend / §4.2.1]; insertion factors: no
insertion, 1, 2, 3 with sharding value of 2 [§4.2.2 / Fig 3 caption]; overhead:
"20.27% to 42.29%" for insertion factors 1–3 [Table 1 / §4.2.2]; k-anonymity
thresholds: "sharding value of 2, that is when a user's request stream can be
re-identified to 79%; the maximum sharding value of 8 → 49%" [§4.2.1].
No network collection; dataset analysis only.

**(ii) Grammar.** No Workflow, no Regime; this is an offline analysis of
pre-collected institutional DNS logs. The sharding/insertion "experiment" is an
algorithmic simulation over the log dataset (no packets sent). Not expressible
in Pramana grammar: no Foreground Workflow, no Regime, no network.
ExperimentSet ⟨leaves: sweep(insertion_factor ∈ {no-insertion, 1, 2, 3} ×
sharding_value ∈ {no-sharding, 2, 4, 8} [§4.2.1, §4.2.2]); dataset analysis,
not network collection⟩.

### decentralized_dns-ES4 — Cross-country DNS resolution-time measurement (Figs 5–7, 17–18)

**(i) Raw text.** "we measure the DNS resolution times with different DNS
services in different countries" [§4.3]; countries: Argentina, Germany, India,
US [§4.3]; "we select the top50 sites and issue multiple DNS requests (three)
for each of the resources included in those pages" [§4.3]; "We record the
minimum TTFB from the three repeated runs to ignore any transient spikes"
[§4.3]; vantage points via NordVPN [§4.3, "we use a VPN (NordVPN)"]; "maximum
(average) Kendall tau distance between rankings is 0.6 (0.37)" [§4.3 / Fig 6
caption]. DNS services: Google, Quad9, Cloudflare, plus two regional resolvers
per country [§4.3]. Emulator/testbed: none — real Internet DNS resolution.

**(ii) Grammar.** No controlled Regime; DNS resolution-time measurements issued
from VPN vantage points to real DNS resolvers over live Internet paths. Pramana
grammar has no production for "VPN-anchored DNS measurement campaign."
ExperimentSet ⟨leaves: sweep(country ∈ {AR, DE, IN, US} × DNS service × target
∈ top50 per country [§4.3]); real-Internet measurement⟩; Regime: none imposed
(exogenous); Dynamic: Not specified; telemetry: {DNS resolution time
(app_metrics)}.

### decentralized_dns-ES5 — DNS racing-configuration experiment (Tab 3)

**(i) Raw text.** "We shard 100 resources, in the top50 sites in the US,
across different DNS providers. We issue resolution requests to a randomly
selected resolver; races run between two and three resolvers for each
resolution request" [§4.3.1]; configurations: No Racing, Racing 2, Racing 3
[Table 3]; resolution time mean/std: No Racing 42.22/38.13, Racing 2 25.83/12.42,
Racing 3 21.34/6.53 [Table 3]; "Just racing two resolvers offers a percentage
improvement of 38.8%, while racing three provides an additional 17.88%
improvement" [§4.3.1]. Measurement location: Not specified.

**(ii) Grammar.** No controlled Regime; the experiment issues live DNS requests
to real DNS providers (Google, Quad9, Cloudflare, regional) and races them.
ExperimentSet ⟨leaves: sweep(config ∈ {No Racing, Racing 2, Racing 3}) = 3
[Table 3]⟩; Regime: none imposed (exogenous — real DNS resolver latency);
Dynamic: Not specified; telemetry: {DNS resolution time, request-stream
exposure (app_metrics)}.

### decentralized_dns-ES6 — DNS-variant privacy/performance tradeoff (Fig 8)

**(i) Raw text.** "we also show the tradeoff between privacy and performance
across different DNS variants, such as DNS over Tor, our ISP DNS, third-party
DNS services, sharding and Ónoma. Figure 8 shows box plots of resolution
times (x axis) … the y-axis shows the privacy gain for each DNS variant in
terms of the percentage of users that have at least 2-anonymity" [§4.3.1].
Workload / site list: Not specified. Measurement location: Not specified.
The 2-anonymity y-axis values come from ES3 (the DNS-log dataset analysis).

**(ii) Grammar.** No controlled Regime; resolution-time boxplots from live DNS
variant measurements; 2-anonymity values from the ES3 dataset analysis.
ExperimentSet ⟨leaves: sweep(DNS variant ∈ {Tor, ISP DNS, third-party, sharding,
Ónoma} [§4.3.1]); count Not specified; real-Internet measurement campaign⟩;
Regime: none imposed; Dynamic: Not specified; telemetry: {DNS resolution time
(app_metrics)}.

### decentralized_dns-ES7 — CDN-popularity measurement (Fig 9)

**(i) Raw text.** "each bar indicates the number of resources, from the top50
regional sites, hosted on a particular CDN" [§4.3.2]; countries: Argentina,
Germany, India, US [Fig 9 caption]; CDNs: Akamai, Amazon, Fastly [Fig 9 legend];
"Germany's popular resources seem to be preferentially hosted on Fastly (44%
resources)"; "the other three countries rely … on Akamai (ranging from 44% to
50%)" [§4.3.2]. CDN-identification method: Not specified.

**(ii) Grammar.** No controlled Regime; passive web resource enumeration and
CDN identification from top50 regional sites per country. ExperimentSet ⟨leaves:
sweep(country ∈ {AR, DE, IN, US} × CDN ∈ {Akamai, Amazon, Fastly}) = 4 × 3 =
12 [Fig 9]; passive enumeration, no network control⟩; Regime: none imposed;
Dynamic: Not specified; telemetry: {resource-count per CDN (app_metrics)}.

### decentralized_dns-ES8 — TTFB per (DNS service, CDN, country) via Lighthouse (Figs 10–11, 19)

**(i) Raw text.** "we then conduct an experiment measuring time-to-first-byte
(TTFB) as a proxy for Web QoE" [§4.3.2]; "We load each resource three times
using Google's lighthouse [30] for different (CDN, country) combinations using
the same VPN service" [§4.3.2]; "minimum TTFB from the three repeated runs"
[§4.3.2]; "Cloudflare shows 10% higher TTFB in the median case vs. best
service … for Fastly content in Germany" [§4.3.2]; "maximum (avg) Kendall tau
distance between rankings 0.4 (0.27) for Akamai and 0.7 (0.53) for Amazon"
[Fig 11 caption]. Vantage: NordVPN [§4.3.2].

**(ii) Grammar.** No controlled Regime; TTFB measurement from VPN vantage
points against real CDN-served content. ExperimentSet ⟨leaves: sweep(country ×
CDN × DNS service [§4.3.2]); count Not specified; real-Internet measurement⟩;
Regime: none imposed (exogenous); Dynamic: Not specified; telemetry:
{TTFB (app_metrics)}.

### decentralized_dns-ES9 — Ónoma vs. sharding TTFB comparison (Figs 12, 20)

**(i) Raw text.** "we compare the performance of Ónoma with that of sharding.
… We load each resource, of the regional top50 sites three times and compute
the minimum TTFB" [§4.3.2]; "median improvement of 9.34% in Argentina with
Akamai CDN" [§4.3.2]; locales/CDNs: AR-Akamai (Fig 12), US/AR for Amazon/Fastly
(Fig 20). Vantage: NordVPN (same as ES8) [§4.3.2].

**(ii) Grammar.** No controlled Regime; comparative TTFB measurement of Ónoma
vs. sharding from VPN vantage points against real CDN content. ExperimentSet
⟨leaves: sweep(locale × CDN [§4.3.2]); count Not specified; real-Internet
measurement⟩; Regime: none imposed; Dynamic: Not specified; telemetry:
{TTFB (app_metrics)}.

### decentralized_dns-ES10 — End-to-end Ónoma evaluation (Figs 14, 21)

**(i) Raw text.** "We set up the evaluation measurements in the selected locations
using a VPN service" [§6]; "the resources hosted on the top50 regional sites,
as the workload" [§6]; "measurement module loads the set of resources with
Google Lighthouse" [§6]; "minimum TTFB from three repeated runs" [§6]; "the
inter-quartile range (IQR) of Ónoma is 18.4% in the US for Akamai's content
vs. it ranges between 18.7% to 24.8%. For Akamai's content in India, Ónoma
gives an IQR of 1.7% and for other DNS services the IQR ranges between 1.7%
to 2.5%" [§6]; Ónoma implemented in "3,510 lines of Go code", client-side
application "under 500MB" [§5/§6].

**(ii) Grammar.** No controlled Regime; end-to-end evaluation of Ónoma's
measurement module from real VPN vantage points against real CDN-served
content across multiple countries. ExperimentSet ⟨leaves: sweep(CDN × country
[§6]); count Not specified; real-Internet measurement⟩; Regime: none imposed
(exogenous); Dynamic: Not specified; telemetry: {TTFB (app_metrics)}.
