# user_controllable_congestion — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Upstream row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| uccong-ES1 | Exp1 | pacing_rate ∈ {none [alone], none [unpaced], 5–35 Mbps range + 49 Mbps [§3.2]; grid Not specified} | Not specified (≥3: alone, unpaced, ≥1 paced point; full paced-rate grid not stated in text) | 30 round-robin [§3.1] |

## Shared methodology (raw text) (quoted from the paper)


> Single end-host testbed; `tc` utility emulates a 50 Mbps last-mile FIFO
> bottleneck [§2]; default Linux queue of 1000 packets [§2]; Google Chrome for
> Testing on two virtual monitors, controlled by Selenium [§2]; Microsoft Teams
> RTC application; Dailymail.co.uk loaded once per minute [§3.1]; NFQueue
> ingress rate-limiter, 150 lines C++ [§2], redirects all TCP & QUIC traffic
> on ports 443 and 80 [§2]; pacer queue sized to match BDP assuming 50 ms RTT ×
> user-defined bandwidth [§2] (50 ms is a sizing assumption, not an asserted
> emulated path RTT — base path RTT Not specified); scenarios: (1) RTC alone,
> (2) alongside unpaced HTTP, (3) alongside paced HTTP at varying rates [§3.1];
> each experiment run 30 times in round-robin fashion [§3.1]; 12-minute runs,
> first and last 30 seconds excluded [§3.1]; metrics: FPS events (FPS < 10 in a
> 1-second window, Zhuge standard [§3.1]); WebRTC freezes (deviation from
> 1-second moving-average FPS [§3.1]); PLT = 95% of above-the-fold region [§3.1].


## Experiments

### uccong-ES1 — Teams RTC + Dailymail browsing: alone / unpaced / paced-rate sweep (Figs 2–3)

**(i) Raw text.** Scenarios: (1) RTC alone, (2) alongside unpaced HTTP, (3)
alongside paced HTTP at different rates [§3.1]; pacing "applied from 5 Mbps to
35 Mbps" achieves up to 67% reduction in low-FPS events [§3.2]; "42%
improvement over the baseline with 49 Mbps pacing on a 50 Mbps link" [§3.2];
20 Mbps identified as trade-off point: ~50% reduction in WebRTC freezes, ~67%
reduction in low-FPS events; PLT within 95% CI of unpaced baseline above 20 Mbps
[§3.2]; unpaced Dailymail increases low-FPS events by over 10x vs. Teams-alone
baseline [§3.2]; current deployment: "hard-coded 20 Mbps pacing strategy" [§4];
30 round-robin repetitions [§3.1]; 12-minute runs, first/last 30 s excluded
[§3.1]; webpage loaded once per minute [§3.1].

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(pacing_rate ∈ {none [alone],
none [unpaced], 5–35 Mbps range + 49 Mbps [§3.2], grid Not specified}); count
Not specified⟩; Experiment = ⟨Foreground = {Workflow(teams_rtc) @ node_1,
Workflow(web_browser, url=dailymail.co.uk, params.load_frequency=1/min) @ node_1
[§3.1]} [for unpaced / paced leaves; teams_rtc alone for alone leaf] ⊗
Regime⟨Static: capacity_down=50 Mbps [§2], queue: FIFO 1000 pkt [§2]; Dynamic:
none (no external CTP pressure; Dailymail workflow is a co-located foreground
runner, not background replay)⟩⟩ @ path.latency: Not specified (50 ms is an
internal BDP-sizing assumption for the NFQueue pacer queue [§2], not an emulated
path RTT); cca: Not specified; iterations=30 round-robin [§3.1]; telemetry
{app_metrics: true (FPS events [§3.1], WebRTC freeze events [§3.1], PLT [§3.1])};
UNREPRESENTED DIMENSION: pacing_rate (NFQueue per-port 443/80 ingress rate cap,
swept over 5–35 Mbps range + 49 Mbps) — no v2 grammar production covers this
knob.⟩
