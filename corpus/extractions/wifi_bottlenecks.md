# wifi_bottlenecks — Experiment-Set Intent Corpus

## Experiment sets

| ES id | Rendering row | Description | Leaves |
| --- | --- | --- | --- |
| wifi_bottlenecks-ES1 | Exp1 | Access-ISP wired NDT7 throughput (Raspberry Pi, ~hourly) [§1, §3] | n/a |
| wifi_bottlenecks-ES2 | Exp2 | Home-WiFi NDT7 throughput (browser Chrome plugin, user-paced) [§1, §3] | n/a |

## Experiments

### wifi_bottlenecks-ES1 — Access-ISP wired NDT7 throughput collection

**(i) Raw text.** "a router-based speedtest performing measurements over the
wide-area from the user's wired network access point" [§1]. "Raspberry Pi
single-board computers … connected directly to routers or modems in their home
networks" [§3]. "We performed access throughput measurements for each household
approximately once per hour" [§3 Data collection]. "Measurement Lab's Network
Diagnostic Tool (NDT7) tool" [§3 Data collection]. Collection period: September
18, 2021 – June 30, 2023 [Table 1; §3 Data collection]. Scale: 52 households,
65 vantage points, 13,581 measurements [Table 1]. Location: Chicago area [§3
Limitations]. Per-household average 261 coincident measurements [§3 Data
analysis]. Other Netrics measurements (DNS lookup latency, packet loss rates)
"we do not analyze" [§3]. Incentives: $100 to install for one month, additional
$25 for six more months [§3 Participant recruitment]. No controlled network
conditions; no experimenter-configured Regime.

**(ii) Grammar.** OUT-OF-SCOPE. Passive real-world deployment: NDT7 download
throughput tests from Raspberry Pi wired to home router over real ISP links.
No controlled Regime; network conditions are exogenous (participants' actual ISP
service). The study's scientific value requires real ISP connections, not
emulated ones. No grammar translation is possible.

### wifi_bottlenecks-ES2 — Home-WiFi NDT7 throughput collection

**(i) Raw text.** "a browser-based plug-in that performs continual throughput
measurements from a user's wireless device inside the home to a speedtest server
running inside the home network at the router" [§1]. "we hosted a speed test
server on a Raspberry Pi, intended to be deployed at or near the home router"
[§3]. "direct his or her browser to the server at https://netrics.local/, which
would trigger the browser to run a Javascript-based NDT7 throughput test to the
server running on the Raspberry Pi" [§3]. "a public, open-source Chrome browser
plugin that would run periodic NDT7 tests from the user's browser to the server
running on the Raspberry Pi, even if the user didn't explicitly initiate a test"
[§3]. "designed to run every few hours, but the actual frequency of the tests
depended on whether someone was using device on which the browser plugin was
installed" [§3; §3 Data collection, "WiFi speed measurements did not follow a
fixed schedule"]. Client hardware, WiFi standard, band, channel: Not specified
[§3 Limitations]. No controlled network conditions; WiFi conditions exogenous.

**(ii) Grammar.** OUT-OF-SCOPE. Home WiFi throughput collection; the WiFi
physical layer is the central variable of the study. Measurement is passive
(user-device + Chrome plugin collecting natural WiFi throughput). No controlled
Regime; the WiFi link is the measurand, not a configurable parameter.
Per CORPUS_PROMPT_v4: "WiFi-PHY → OUT-OF-SCOPE." No grammar translation
is possible.
