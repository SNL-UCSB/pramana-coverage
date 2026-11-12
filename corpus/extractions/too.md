# too — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Figures | OUT-OF-SCOPE class | Leaves |
| --- | --- | --- | --- | --- |
| too-ES1 | Exp1 | text-only | passive/exogenous | 1 (single measurement study; stream count Not specified) [§1] |
| too-ES2 | Exp2 | Fig 3 (a, b) | exogenous | 1 (single CDN deployment: baseline vs TOO; Θthres=50ms, n=4) [§3] |

## Experiments

### too-ES1 — Large-scale measurement study of live streams (text-only, §1)

**(i) Raw text.** "Our large-scale measurements show that 21.7% and 8.5% of live streams
suffer from at least 2 and 5 retransmissions for recovering some lost packet(s), respectively"
[§1]; "6.8% of resent losses become more deteriorated during recoveries, introducing additional
123.2ms (up to 279.3ms) recovery delay" [§1]; "over 290- and 3100-time on-off switching
experienced in 50% and 10% of live streams, resulting in 12s and 80s off-mode duration,
respectively" [§1]; platform: "real product networks" [§1, "from the deployment experience of
real product networks"]. Stream count, measurement period, geographic scope, vantage points,
bandwidth, CCA, topology: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — passive production measurement on real live streams; no
controllable network conditions or workload.

### too-ES2 — Real-world CDN deployment evaluation of TOO (Fig 3)

**(i) Raw text.** "We integrate all the components described in Section 2 into Tencent's CDN
servers (only sender-side upgrades) and implement the TOO prototype based on the user-space
QUIC protocol (with the version of LSQUIC Q043 [11])" [§3]; "The CDN proxy server that has
deployed TOO prototype can pull and transmit the requested live streaming from our live CDN to
real-network users" [§3]; "The CDN proxy servers all employ BBR (v1) [12] scheme as the
congestion controller" [§3]; TOO parameters: Θthres = 50 ms, n = 4, "according to the
production requirements" [§3]; Ewaiting update period example: 2×SRTT [§2.3, "updated
periodically (e.g., 2×SRTT)"]; Fig 3(a) metric: invalid-response-time (IRT) — "duration from
when any data is detected lost to when resending a recovery packet that will be successfully
received" [§3]; analysis population: "each stream's average IRT value of the lost data whose
recovery requires two or more retransmissions" [§3]; Fig 3(b) metrics: goodput and
retran_ratio [Fig 3(b) axes]; results: average IRT lowered by 16.0%, from 119.3 ms to
100.2 ms; 95th-percentile IRT reduced by 110 ms [§3]; average goodput deteriorates 2.4%
(from 974.3 Kbps to 951.1 Kbps); 1.9% average additional retran_ratio; 10% of streams
require an extra 6.5% of retran_ratio [§3]. Experiment duration, number of streams, regions,
network bandwidth, hardware: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — real-world production deployment evaluation; experiments run on
Tencent's live CDN infrastructure with real user traffic on uncontrolled real-network paths.
