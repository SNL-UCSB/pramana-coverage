# quince — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Nature | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| quince-ES1 | Exp1 | exogenous crowdsourcing human-subject study — OUT-OF-SCOPE | n/a | n/a |

## Shared methodology (raw text) (quoted from the paper)


> Two one-week IRB-approved preliminary studies on Amazon Mechanical Turk in October and
> November 2018 [§3, "two one-week IRB-approved preliminarily studies on MTurk in October
> and November, 2018"]. 70 distinct subjects recruited across both studies [§3, "we recruited
> 70 distinct subjects"]. Subjects used their own devices and access networks; no controlled
> network conditions. Three measurement task types: (1) customized video player simulating
> rebuffering/quality changes + YouTube player API streams, with 5-point Likert QoE rating
> by the subject [§2]; (2) M-Lab NDT and fast.com speed tests [§2]; (3) OS-level traceroute
> to MANIC-project-selected destinations [§2]. Two-phase design: Phase 1 requires all tasks
> once (USD$2 credit); Phase 2 longitudinal opt-in [§2.1]. Per-task cool-down timer 2 min
> to 1 hour [§2.1]. Metrics: subject engagement scores (Fig 2); lowest YouTube QoE Likert
> rating per NDT throughput bin (Fig 3). Network bandwidth, RTT, queue, loss: Not specified
> (subjects' real uncontrolled access links). CCA: Not specified. Topology: Not specified.


## Experiments

### quince-ES1 — Two one-week MTurk crowdsourcing studies (Figs 2, 3)

**(i) Raw text.** "two one-week IRB-approved preliminarily studies on MTurk in October and
November, 2018" [§3]; "we recruited 70 distinct subjects" [§3]; subjects perform three task
types on their own devices and real access links [§2]; YouTube QoE self-rated on 5-point
Likert scale (1:Bad–5:Excellent) [§2]; engagement scores measured by a gamified points system
(USD$2 after completing all tasks once; USD$0.1 per additional 100 points [§3]); 25% of
subjects performed at least 50 tasks [§3]; "even for subjects with downlink throughput as
high as 50Mbps, the YouTube performance could be unsatisfactory (rating less than 3)" [§3].
No controlled network conditions. Fig 2: CDF of engagement scores of all subjects [§3].
Fig 3: lowest YouTube QoE rating per NDT throughput bin (0–150 Mbps, 25 Mbps buckets)
[Fig 3 x-axis labels; §3].

**(ii) Grammar.** OUT-OF-SCOPE. The experiment's controlled variables are incentive structure,
task sequencing, and cool-down timers — not network conditions. The network is the real
in-the-wild uncontrolled access link of each MTurk subject; it is not set by the experimenter
and cannot be expressed as a Regime production (Static or Dynamic). The primary measurands
are (a) subject engagement behavior (points earned, task repetitions — Fig 2) and (b)
subjective 5-point Likert YouTube QoE ratings stratified by NDT-measured throughput (Fig 3).
Neither is a network quantity expressible in the v2 grammar's Workflow × Regime × Roles
space; human QoE ratings and MTurk engagement behavior are outside the grammar's scope.
No grammar-v2 translation is generated.
