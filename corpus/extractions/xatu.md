# xatu — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Upstream row | Scope verdict | Reason |
| --- | --- | --- | --- |
| xatu-ES1 | Exp1 — Real-user dataset collection (~100K traces, 2017 publisher) [§3] | OUT-OF-SCOPE | Passive measurement / trace collection from a live publisher; no controlled network or bottleneck |
| xatu-ES2 | Exp2 — Controlled home-network dataset collection [§7] | OUT-OF-SCOPE | Real home network, uncontrolled; ABR disabled; no bottleneck shaping or CCA control |
| xatu-ES3 | Exp3 — Testbed emulation: Xatu+MPC vs CS2P+MPC (Chrome DevTools) [§6] | OUT-OF-SCOPE | Network emulation via Chrome DevTools API (browser-level simulator, not tc/netem); no substrate bottleneck |
| xatu-ES4 | Exp4 — Testbed emulation: Xatu+MPC vs Pensieve (Chrome DevTools) [§6] | OUT-OF-SCOPE | Same simulator-type emulation as Exp3; Chrome DevTools network emulation |
| xatu-ES5 | Exp5 — Fugu emulation: FuguABR+XatuDist vs FuguABR+FuguNN (Mahimahi) [§6.1] | OUT-OF-SCOPE | Mahimahi network emulator (simulator); outside the grammar's emulation model |

## Shared methodology (raw text, for context) (quoted from the paper)


> Exp1: ~100,000 video session traces from real users over three months in 2017 from a
> US publisher; per-chunk size, TTFB, and download start/end times recorded [§3]. Primary
> DataSet: ~27K traces after ISP/CDN/city/time-of-day clustering [§3.1]. Exp2: 500 videos
> from Twitch, Vimeo, ESPN streamed over a home network for 7 days with ABR disabled [§7].
> Exp3/4: Dash.js video player on Chrome from Apache server; network throughput and TTFB
> emulated via Chrome DevTools API per trace; one 8-core Intel i7 desktop, 12 GB RAM,
> Ubuntu 16.04 [§6]. Exp5: Mahimahi emulation, FuguABR, 10-minute video [§6.1].

---


## Experiments

### xatu-ES1 — Real-user trace dataset (passive collection)

**(i) Raw text.** "approximately 100,000 video session traces from real users collected
over the course of three months in 2017 from a publisher in the United States" [§3].
"served by 2 CDNs and 89 ISPs across 1406 cities" [§3]. Per-chunk: size, TTFB,
start/end download times [§3]. No controlled network conditions.

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xatu-ES2 — Controlled home-network measurement (§7)

**(i) Raw text.** "collected over a home network during a 7 day period" [§7]; 500 videos
from Twitch, Vimeo, ESPN; ABR disabled, highest bit rate for all chunks [§3.2];
CDN-layer headers added to HTTP requests [§7].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xatu-ES3 — Chrome DevTools emulation: Xatu+MPC vs CS2P+MPC (§6)

**(i) Raw text.** "we emulate traces from the testing set above (§5.2), and vary both
the network throughput and the TTFB as per the trace" [§6]; Chrome DevTools API /
Chrome-Remote-Interface used to emulate network throughput and latency between client
and servers per trace [§6]; Dash.js video player on Chrome from Apache server [§6];
ABR server queries CS2P or Xatu prediction model [§6]; 500 traces, average chunk
download rate < 10 Mbps [§6]; 1 minute client buffer [§6]; QoE-lin with P1=9.1 and
P2=1 [§6].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xatu-ES4 — Chrome DevTools emulation: Xatu+MPC vs Pensieve (§6)

**(i) Raw text.** "a subset of 9K traces chosen from the 27K traces in the Primary
DataSet" [§6]; same physical testbed as Exp3 (Chrome DevTools network emulation); 500
traces from the testing set with average chunk download rates under 10 Mbps [§6];
Pensieve retrained; Xatu limited (no static features, only chunk size and download time)
[§6].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.

### xatu-ES5 — Mahimahi emulation: FuguABR+XatuDist vs FuguABR+FuguNN (§6.1)

**(i) Raw text.** "We used the same evaluation setup used by Fugu [66], which involved
emulating traces using Mahimahi [49]" [§6.1]; 10 minute pre-recorded video clip [§6.1];
QoE-SSIM metric [§6.1]; FuguNN and XatuDist trained on Primary DataSet (§5.2 splits)
[§6.1]; testing-set traces with average chunk download rates not significantly exceeding
4.1 Mbps [§6.1].

**(ii) Grammar.** n/a — OUT-OF-SCOPE.
