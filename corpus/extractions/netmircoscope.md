# netmircoscope — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Gold row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| netmircoscope-ES1 | Exp1 | service ∈ {Netflix, YouTube-TCP, YouTube-QUIC, Twitch, Amazon} × content item (25 NF / 15 AM / 30 YT videos / Twitch feed [§4.1]) × vantage ∈ 6 residential sites [§4.1, lines 289-292] | Not specified (session stream, not a stated factorial; combined curated total 13,765 with ES2 [§4.1, line 333]) | 1 session per leaf instance; "8 to 12 minutes" [§4.1, line 295] |
| netmircoscope-ES2 | Exp2 | service × content (as ES1) × path envelope ∈ {stable draws from capacity "50 kbps" to "30 Mbps" × loss_pct "between 0% and 1%" × latency "between 0 ms and 30 ms" [§4.1, lines 321-322]} × vantage ∈ 5 lab machines; varied-at-random-intervals family is separate (see (iv)) | Not specified (ranges stated; grid not enumerated) | 1 session; "8 to 12 minutes" |
| netmircoscope-ES3 | Exp3 | Not translated: passive observation, no attempted leaf space (66 homes, 932 devices [Tab 3, line 643]) | n/a | n/a (passive) |
| netmircoscope-ES4 | Exp4 | Not translated: passive observation with ground-truth labeling (5 homes [§6.2]) | n/a | n/a (passive) |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Curated collections (ES1/ES2): DASH video sessions, five categories
> (Netflix, YouTube TCP, YouTube QUIC, Twitch, Amazon), ChromeDriver-
> automated [§4.1]; sessions "8 to 12 minutes", playback start point varied
> for long videos [§4.1, line 295]; `netflix-1080p` extension for 1080p on
> Chrome [§4.1, line 311]; traces via tcpdump on the client interface; ground
> truth from a Chrome extension (Netflix overlay text, YouTube iframe API,
> Twitch/Amazon video-tag parsing) [§4.1]; collection "November 20, 2017" –
> "May 3, 2019" [§4.1, line 325]; combined curated dataset 13,765 sessions
> [§4.1, line 333]. Deployment collections (ES3/ES4): embedded monitors on
> Raspberry Pi and Odroid [§6.1, line 619], bridge-mode gateway or passive span
> port [§6.1, lines 622-624]; features aggregated over "five-second intervals",
> uploaded hourly [§6.1, lines 627-630]; active speed tests "four times per day"
> [§6.2, line 683]. CCA/queue/AQM/base-RTT: Not specified throughout.


## Experiments

### netmircoscope-ES1 — real-home curated collection (Figs 1–12, Tab 2 %Home, with ES2)

**(i) Raw text.** "All experiments within homes ran with no other modifications
of network conditions to emulate realistic home network conditions" [§4.1];
six residential vantage points: three homes with download speeds "100 Mbps,
18 Mbps, and 6 Mbps", a student residence, a US campus apartment, a rural US
home [§4.1, lines 289-292]; %Home per service in Tab 2 [lines 276-282].
ChromeDriver automates sessions; sessions "8 to 12 minutes" [§4.1, line 295];
tcpdump on client interface; Chrome extension for ground-truth labels [§4.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(workflow.params.service ∈ 5
categories × workflow.params.content ∈ per-service libraries × node ∈ 6
residential vantages); count Not specified⟩; Experiment = ⟨Workflow(video
session, ChromeDriver-equivalent NFA; params: content, start-point) ⊗
Regime⟨Static: none imposed — inhabited (probe characterizes); Dynamic: none
— stated ("no other modifications") [§4.1], a §5b.9 baseline⟩⟩ @
Roles⟨client: residential node, server: real streaming services⟩; iterations: 1;
telemetry {pcap: true (tcpdump), app_metrics: true (extension-parsed QoE
labels: resolution, startup)}.

### netmircoscope-ES2 — lab tc-emulated curated collection (Figs 1–12, Tab 2 %Lab, with ES1)

**(i) Raw text.** Conditions "either stable for the whole session or varied
at random intervals" [§4.1, line 320]; capacity "50 kbps" to "30 Mbps", loss
"between 0% and 1%", added latency "between 0 ms and 30 ms" [§4.1, lines
321-322]; four WiFi laptops + one Ethernet desktop [§4.1, lines 292-293];
%Lab per service in Tab 2.

**(ii) Grammar.** This ES has two sub-families:

**Stable-envelope family (in-grammar):**
ExperimentSet⟨leaves: sweep(workflow.params.service × workflow.params.content
× imposed envelope ∈ stable draws from capacity "50 kbps" to "30 Mbps"
[§4.1] × path.loss_pct "between 0% and 1%" [§4.1] × path.latency "between
0 ms and 30 ms" [§4.1]); count Not specified; five lab machines⟩;
Experiment = ⟨Workflow(video session as ES1) ⊗ Regime⟨Static: imposed
(capacity_down ∈ stated range; mode: imposed — probe verifies, spec §2);
Dynamic: Not specified (silence on cross traffic per §5b.2)⟩⟩ @
Roles⟨client: lab node, server: real streaming services⟩;
path.latency per-workflow ∈ "between 0 ms and 30 ms"; path.loss_pct per-workflow
∈ "between 0% and 1%"; telemetry as ES1.

**Varied-at-random-intervals family (OUT-OF-SCOPE in v2):**
Not translated into a grammar production. Per CORPUS_PROMPT_v4 §2.3 v2
disposition: the conditions are varied within a session — capacity changes
over time are not schedulable in v2 grammar (A5 static is fixed per experiment
and identity-hashed once; the model does not schedule the bottleneck).
Marked OUT-OF-SCOPE. (Was GAP-DESIGN / spec-gap #6 in v1.)

### netmircoscope-ES3 — 66-home passive deployment (Tab 3, Figs 15–18 arXiv)

**(i) Raw text.** 66 homes (60 US + 6 France), 932 unique devices, 216,173
sessions, "January 23, 2018" – "March 12, 2019" [§6.2, lines 671-677; Tab 3,
line 643]; passive monitors; residents' own viewing; active speed tests
"four times per day" [§6.2, line 683]; downstream "18 Mbps to 1 Gbps"
[§6.2, line 675].

**(ii) Grammar.** Not translated: the collection is passive observation of
resident-generated traffic at a fixed vantage; there is no intent-issued
workflow and no leaf space to attempt (the "four times per day" speed tests
are the only platform-issued component).

### netmircoscope-ES4 — 5-home ground-truth collection (Figs 13/Tab 4/Fig 14 arXiv)

**(i) Raw text.** Ground truth inside the deployment environment via the Chrome
extension, 5 homes, 2,347 sessions [§6.2, line 668]; validates the domain-
adapted models [§6.2].

**(ii) Grammar.** Not translated: resident-generated viewing with an
instrumented browser — passive with respect to the platform (no issued
intents), labeled at the client.
