# device_aware_abr — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Collection description | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| device_aware_abr-ES1 | Exp1 (Fig 1) | PSS characterization: buffer size × video resolution sweep | 2 × 2 = 4 | Not specified |
| device_aware_abr-ES2 | Exp2 (Fig 2) | Illustrative YouTube run under memory pressure on Nexus 5 | 1 | 1 |
| device_aware_abr-ES3 | Exp3 (Fig 3) | Bitrate impact under high memory pressure: 1080p vs 720p | 2 | Not specified |
| device_aware_abr-ES4 | Exp4 (Fig 4) | DAVS evaluation: Fixed vs Dynamic (DAVS) under high memory pressure | 2 | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Network bandwidth, base latency, queue size, queue management, congestion
> control, transport protocol, cross traffic: **Not specified** for all four
> experiments. The paper studies the effect of device memory pressure on video
> QoE; no network Regime is imposed or characterized. The experimental variable
> across all ESes is device hardware state (memory, buffer size, memory pressure
> level), not network conditions.

**No network Regime is specified in any experiment in this paper.** All four ESes
study mobile device memory effects; network conditions are Not specified or
treated as background (uncontrolled real Wi-Fi or LAN).


## Experiments

### device_aware_abr-ES1 — PSS characterization vs. buffer size and resolution

**(i) Raw text.** "Figure 1 shows the PSS of the video player for different
playback buffer sizes and bitrates" [§2]; buffer sizes: 60s and 8s [Fig 1 subplot
titles "60s Buffer" and "8s Buffer"; §2: "decreasing the buffer from 60s to 8s
reduced the maximum PSS by 75MB"]; video resolutions: 720p and 1080p [Fig 1 legend;
§2: "for a 60s buffer, a 1080p video used 90MB more memory than a 720p video in
the worst-case"]. Network bandwidth, latency, queue, CCA, cross traffic, testbed,
hardware, duration, dataset: Not specified.

**(ii) Grammar.** This experiment measures video player memory footprint (PSS)
as a function of buffer size and resolution — both application/device parameters,
not network parameters. No network Regime is imposed or observed. Grammar
representation: out of Pramana grammar scope — no Workflow over a testbed
substrate is specified.

### device_aware_abr-ES2 — Illustrative YouTube run under memory pressure

**(i) Raw text.** "We start a 1080p YouTube video on a Nexus 5 phone" [§2];
"a Nexus 5 phone with 2GB memory" [§1]; "while it is being played the memory
pressure is being increased in the background" [§2]; "Android makes use of two
system daemons: kswapd and lmkd" [§2]. Network bandwidth, latency, queue, CCA,
cross traffic, duration, repetitions: Not specified.

**(ii) Grammar.** A single-run illustration of memory-pressure impact on a live
YouTube stream on a physical mobile phone. No network Regime is imposed by the
researcher. Grammar representation: out of Pramana grammar scope — the
experimental variable is memory pressure, not a network bottleneck or workflow
parameter.

### device_aware_abr-ES3 — Bitrate impact under high memory pressure

**(i) Raw text.** "Figure 3 shows that using a high bitrate reduces FPS and
increases chances of crashes under high memory pressure" [§2]; resolutions swept:
1080p and 720p [Fig 3(a) legend "1080p"/"720p"]; "720p did not crash" [Fig 3(b)
annotation]; "playing a 1080p video under low memory on a Nexus 5 phone with 2GB
memory led to frequent video player crashes, whereas switching the video quality
to 720p prevented crashes" [§1]. Network bandwidth, latency, queue, CCA, cross
traffic, player/framework, duration, repetitions: Not specified.

**(ii) Grammar.** Measures FPS distribution and time-to-crash under high memory
pressure for two video resolutions. No network Regime imposed; the swept dimension
is video resolution (a device/application parameter). Grammar representation: out
of Pramana grammar scope.

### device_aware_abr-ES4 — DAVS evaluation (Fixed vs Dynamic)

**(i) Raw text.** "we implement DAVS in the dash.js framework" [§1]; "The client
video player was a Firefox browser and the video server ran on a separate machine.
Our DASH setup is similar to Pensieve [5]" [§1 footnote 3]; "DAVS (Dynamic)
significantly improves FPS, increases the time to crash, and reduces the likelihood
of crashes ... under high memory pressure" [§3]; "DAVS reduced chances of crashes
by 66% compared to using a 1080p video" [§3]; threshold F "set to 88% the video
frame rate in our experiments" [footnote 4]. Network bandwidth, latency, queue,
CCA, cross traffic, device hardware, duration, repetitions, video content: Not
specified.

**(ii) Grammar.** Evaluates the DAVS adaptive bitrate algorithm (implemented in
dash.js) against a fixed-configuration baseline under high memory pressure.
Although a separate video server is mentioned, no network Regime is imposed —
bandwidth, latency, queue management, and CCA are all Not specified. The
experimental variable is the DAVS algorithm's memory-aware adaptation logic, not
any network condition. Grammar representation: out of Pramana grammar scope.
