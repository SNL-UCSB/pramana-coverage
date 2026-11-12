# wisely_short_video — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Upstream row | Scope verdict | Reason |
| --- | --- | --- | --- |
| wisely-ES1 | Exp1 — Douyin/Kuaishou platform measurement [§1] | OUT-OF-SCOPE | Passive measurement of commercial platforms; no controlled network or bottleneck; no locator for measurement method |
| wisely-ES2 | Exp2 — IRB-approved user study [§1] | OUT-OF-SCOPE | Exogenous user study; real user behavior; no controlled network parameters |
| wisely-ES3 | Exp3 — In-the-wild evaluation, 400 volunteers [§3] | OUT-OF-SCOPE | Field deployment with real users and real networks; no controlled bottleneck or CCA |

## Experiments

### wisely-ES1 — Douyin/Kuaishou prefetching measurement

**(i) Raw text.** "Our measurements on two popular platforms Douyin [3] and Kuaishou [5]
(i.e., the Chinese versions of TikTok and Kwai) show that prefetching only applies to the
first chunk of the next few videos." [§1] No measurement method, device type, network
environment, or sample size is stated.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### wisely-ES2 — IRB-approved user study

**(i) Raw text.** "Our key insight derived from an extensive IRB-approved user study is
that prefetching must be guided by both user swiping behavior … and network condition …"
[§1] Participant count, protocol, and network conditions are not specified.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### wisely-ES3 — In-the-wild evaluation (Fig 2)

**(i) Raw text.** "The preliminary evaluation results are derived from in-the-wild short
video viewing experiments with 400 volunteers." [§3] "As shown in Figure 2, our framework
drastically reduces the average data wastage to merely 8.3% of the video size." [§3]
"improved our user-perceived QoE by at least 19.8%" [§3]. Five schemes compared: Ours,
Douyin, Kuaishou, Dashlet, Incendio. Network conditions, device types, video corpus,
session duration: Not specified.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.
