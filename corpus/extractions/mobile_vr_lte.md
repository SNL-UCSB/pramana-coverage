# mobile_vr_lte — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Scope | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| mobile_vr_lte-ES1 | Exp1 | OUT-OF-SCOPE (cellular/physical-layer: operational LTE, real VR apps) | n/a | n/a |
| mobile_vr_lte-ES2 | Exp2 | OUT-OF-SCOPE (cellular/physical-layer: operational LTE, emulated VR traffic) | n/a | n/a |
| mobile_vr_lte-ES3 | Exp3 | OUT-OF-SCOPE (physical-layer: USRP/OpenAirInterface LTE testbed) | n/a | n/a |
| mobile_vr_lte-ES4 | Exp4 | OUT-OF-SCOPE (physical-layer: USRP/OpenAirInterface, fault injection) | n/a | n/a |
| mobile_vr_lte-ES5 | Exp5 | OUT-OF-SCOPE (physical-layer: USRP/OpenAirInterface, SR-ConfigIndex sweep) | n/a | n/a |
| mobile_vr_lte-ES6 | Exp6 | OUT-OF-SCOPE (physical-layer: USRP/OpenAirInterface, 5G emulation) | n/a | n/a |

## Experiments

### mobile_vr_lte-ES1 — Real-VR-app measurement campaign over operational LTE

**(i) Raw text.** "8-month empirical study (12/2016-07/2017) over four U.S. carriers
(Verizon, AT&T, T-Mobile, and Sprint)" [§3, L344]; scenarios: static, walking (~0.5 m/s),
driving (~30 mph) [§3]; radio signal strength -120~-80 dBm [§3]; VR apps: VRidge
(DayDream/Cardboard) and StreamTheater (Gear VR), 60FPS, 1080p game streaming [§3,
L347-348]; trace tools: LTE signaling via MobileInsight, IP via tcpdump [§3];
3,165,000 LTE signaling messages [§3, L361]; Figs 2-4, 6-7, 10-11, 14-15, 20, 22-24,
Tabs 2-7, 11-13.

**(ii) Grammar.** Passive empirical measurement over operational 4G LTE carrier
networks collecting LTE signaling traces. No controlled bottleneck, no synthetic
traffic generation, no testbed under experimenter control. OUT-OF-SCOPE for Pramana
grammar — the measurand is LTE radio-layer protocol behavior (RLC/PDCP/MAC/PHY
latency components) on commercial carrier infrastructure.

### mobile_vr_lte-ES2 — Emulated-VR-traffic measurement campaign over operational LTE

**(i) Raw text.** Same 8-month study environment as Exp1; workload from Android VR
traffic generator + server emulator program "to run experiments on more phone models,
including Samsung S4" [§3 / A.1]; devices: Samsung S7 Edge, Huawei Nexus 6P, Google
Pixel, Samsung S4 [A.1]; traffic fidelity to real VR confirmed via Tab 13; shares
most figures/tables with Exp1.

**(ii) Grammar.** Operational cellular network measurement with software-emulated VR
traffic. Same structural category as Exp1: physical-layer cellular measurement over
commercial LTE carriers. OUT-OF-SCOPE.

### mobile_vr_lte-ES3 — Testbed overall evaluation of LTE-VR (§9.1)

**(i) Raw text.** "prototyped LTE-VR in a testbed with USRP and OpenAirInterface"
[§abstract, L128]; "A software-defined radio (USRP B210) (Figure 17b) runs as the VR
phone, while others as the base stations" [§9, L1678]; "We collect their network
traffic in a driving test (20,000 1080p frames), and replay them in our testbed"
[§9.1, L1832-1833]; radio signal strength [-95dBm, -105dBm] [§9.1]; compared
schemes: LTE-VR, Legacy LTE, Oracle LTE, LTE + 10× bandwidth [§9.1]; Figs 18-19,
Tab 8.

**(ii) Grammar.** Physical-layer LTE testbed using USRP B210 SDR hardware running
an OpenAirInterface LTE base-station stack. The experiment evaluates protocol-layer
latency in the LTE air interface (HARQ, RLC, MAC scheduling). OUT-OF-SCOPE for
Pramana grammar — the substrate is a software-defined radio operating LTE radio
protocols, not a tc/netem bottleneck.

### mobile_vr_lte-ES4 — Error-recovery fault-injection test (§9.2)

**(i) Raw text.** Same OpenAirInterface/USRP B210 testbed [§9]; "we inject random VR
data corruptions and M-NACK→M-ACK flips based on user traces (every 1.2s on average)"
[§9.2, L1941]; RLC timer T_reorder swept: {60.0 ms, 35.0 ms} [Tab 9]; "repeat
10,000 runs for each" [§9.2, L1941]; compared: legacy LTE vs LTE-VR recovery latency
[§9.2]; Tab 9.

**(ii) Grammar.** Physical-layer LTE testbed fault-injection experiment (RLC timer
parameter sweep + error injection). OUT-OF-SCOPE.

### mobile_vr_lte-ES5 — Proactive-uplink-allocation test (§9.2)

**(i) Raw text.** "The setup is identical to §9.1, but we repeat it with different
SR-ConfigIndex settings" [§9.2, L1963-1964]; "more than 50,000 uplink samples"
[§9.2, L1964]; SR-ConfigIndex values: SR 10 ms and SR 20 ms [Fig 21 legend];
compared: LTE-VR vs legacy LTE per-packet waiting delay [§9.2]; Fig 21.

**(ii) Grammar.** Physical-layer LTE testbed experiment sweeping LTE SR-ConfigIndex
(a 3GPP scheduling request periodicity parameter). OUT-OF-SCOPE.

### mobile_vr_lte-ES6 — 5G projection test (§10.1)

**(i) Raw text.** "Assume the signaling design as 4G LTE, we emulate the 5G radio
using 1000× bandwidth expansion and 0.2 ms slot. We rerun the evaluation of §9.1"
[§10.1, L2093]; workload: high-quality VR, 60FPS, 4K [§10.1]; compared: 1000×
bandwidth + 0.2 ms slot alone vs + LTE-VR [Tab 10]; Tab 10.

**(ii) Grammar.** Physical-layer LTE/5G radio testbed (USRP/OpenAirInterface with
5G-emulating parameters). OUT-OF-SCOPE.
