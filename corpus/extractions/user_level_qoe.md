# user_level_qoe — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| ulqoe-ES1 | Exp1 (Fig 1) | algorithm ∈ {Alg1, Alg2, Alg3} [§2.1] | 3 | 5 days (daily observations) [§2.1] |
| ulqoe-ES2 | Exp2 (Figs 2,3,4,5,8,9) | 1 collection, no network-condition sweep [§2.1–§5.1] | 1 | 1 (log corpus, 1.5M trajectories [§2.2]) |
| ulqoe-ES3 | Exp3 (no figures) | 1 collection, 100 users [§5.2] | 1 | 2 weeks [§5.2] |
| ulqoe-ES4 | Exp4 (Figs 10, 11) | user_model ∈ {rule-based(64 rules), data-driven} × method ∈ {fixed, L(F), L(B)} × stall_param ∈ [1,20] × switch_param ∈ [0,4] [§5.2] | 64 rules × 3 methods × 20 × 5 + data-driven × 3 methods = Not fully enumerated (ranges stated [§5.2]) | Not specified (M × Tsample [§3.2]) |
| ulqoe-ES5 | Exp5 (Figs 12,13,14,15) | arm ∈ {LingXi, control} [§5.3] | 2 | 10 days [§5.3] |

## Shared methodology (raw text) (quoted from the paper)


> Production video streaming platform: Kuaishou short-video [§1, "On short video platform
> Kuaishou"]; ABR family: HYB (hybrid bitrate selection preventing buffer underflows)
> [§5.3]; QoE objective: QoElin = quality − μ × stall_time − switching [§2.1, Eq. 1];
> all production experiments use real user traffic (no network emulation or lab testbed);
> hardware: Not specified.

---


## Experiments

### ulqoe-ES1 — 5-day motivational A/B test of QoS-objective variants (production)

**(i) Raw text.** "We conduct a comprehensive 5-day A/B testing experiment to evaluate
algorithm performance across different optimization objectives" [§2.1]; three variants:
production baseline, Alg3 (quality priority), Alg1 (stall reduction) [§2.1]; metrics:
normalized video bitrate, stall time, QoElin, overall watch time [Fig 1 subcaptions (a)–(d)];
deployed on Kuaishou production system, real user traffic [§2.1]; traffic share, user
counts, and hardware: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE. The experiment is a production A/B test on an
exogenous platform (Kuaishou) over which the researchers have no infrastructure control.
No network conditions are emulated; the regime is whatever the real production network
delivers. Foreground workflows are proprietary production ABR algorithms inside the
Kuaishou serving stack, not Pramana-controllable workloads.

### ulqoe-ES2 — Production-log collection & analysis (1.5M playback trajectories)

**(i) Raw text.** "1.5 million playback trajectories from the production environment"
[§2.2]; contents: user IDs (anonymized), watch timestamps, total video lengths, user
watch time, segment buffer/bitrate/size/download-time/stall-time [§2.2]; video quality
tiers: LD, SD, HD, Full HD [§2.2]; predictor dataset: "approximately 100,000 entries,
extracted from online logs exhibiting stall events" [§3.3]; collection window: Not
specified; network conditions: real production networks, no emulation [§2.2, "from the
production environment"].

**(ii) Grammar.** OUT-OF-SCOPE. The experiment is a passive analysis of production
system logs. No experimental conditions are authored; the data is an observation of
organic user traffic on Kuaishou's platform. There is no Regime, no Foreground workflow
under researcher control, and no emulated or lab environment.

### ulqoe-ES3 — 100-user two-week engagement collection (training data, no figures)

**(i) Raw text.** "we collect historical engagement data from online users" [§5.2];
"100 active users whose daily watch time ranks in the 90th to 95th percentiles" [§5.2];
"collect their watch engagement over two weeks" [§5.2]; output: individual exit
predictors fitted per user [§5.2]; environment: online/production users; network
conditions, hardware, dates: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE. The experiment extracts historical engagement data from
online production users. No network conditions are authored; the collection is from an
exogenous production system. Maps to no figure (reference/training-data rule); retained
as an ES because it is a genuine data-collection campaign.

### ulqoe-ES4 — Offline simulation evaluation of LingXi (rule-based + data-driven user models)

**(i) Raw text.** "Prior to online deployment, we conduct comprehensive offline
evaluations in a simulated environment" [§5.2]; "The simulation framework incorporates
online bandwidth traces and actual video data to ensure environmental fidelity" [§5.2];
baselines: RobustMPC [34], Pensieve [20] [§5.2]; user-engagement models: (a) rule-based
— "deterministic exit rules ... cumulative stall time and stall counts ... thresholds
for both metrics are systematically varied between 2 and 9, generating a comprehensive
set of 64 distinct engagement rules" [§5.2]; (b) data-driven — individual exit
predictors fitted from Exp3 data [§5.2]; methods compared: "fixed parameters, LingXi
with fixed candidate parameters (L(F)), and LingXi optimized through Bayesian
optimization (L(B))" [§5.2]; performance metric: video completion rate [§5.2]; Monte
Carlo samples M and Tsample: Not specified numerically [§3.2].

**(ii) Grammar.** OUT-OF-SCOPE. The experiment is an offline software simulation of
ABR video playback. It does not involve actual network transmission, packet routing,
or queuing — it simulates chunk download times and bitrate decisions using a
mathematical playback model (Eq. 3 [§3.2]) driven by pre-recorded bandwidth traces.
This is a trace-driven discrete-event SIMULATOR (the v4 §2 simulator criterion), not
a network emulation experiment where traffic is actually shaped.

### ulqoe-ES5 — 10-day difference-in-differences A/B test of LingXi in production

**(i) Raw text.** "10-day difference-in-differences A/B test in the production
environment" [§5.3]; "utilizing 8% of total traffic" [§5.3]; "experimental cohort of
30 million daily active users" [§5.3.1]; "During the first 5 days, we carried out an
AA test ... On the 6th day, we applied the intervention" [§5.3]; ABR under adjustment:
HYB [§5.3]; Kuaishou production environment, C++ integration [§4]; hardware: Not
specified; network conditions: real production traffic [§5.3].

**(ii) Grammar.** OUT-OF-SCOPE. The experiment is a production A/B test on Kuaishou's
live platform. No regime is authored; the bottleneck link, network conditions, and
serving infrastructure are all exogenous. The 30-million-DAU scale and the proprietary
C++ production integration are outside any researcher-controlled emulation environment.
