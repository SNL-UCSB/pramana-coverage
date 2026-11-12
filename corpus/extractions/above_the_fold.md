# above_the_fold — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| above_the_fold-ES1 | Exp1 (Fig 1) | 1 (single illustrative page-load, unnamed page) [Fig 1 caption] | 1 | 1 |
| above_the_fold-ES2 | Exp2 (Fig 2) | 1 (single AATF plugin run on Amazon.com) [§2; Fig 2 caption] | 1 | 1 |
| above_the_fold-ES3 | Exp3 (text-only, §2 demo) | network_scenario ∈ {good_conditions, limited_bandwidth} [§2] | 2 | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Chrome extension implementing the AATF method [§2, "we developed a Chrome extension
> that implements AATF"]; metrics: DOM, PLT, AATF (time-instant) and ObjectIndex,
> ByteIndex, ImageIndex with early cut-off at AATF (time-integral), plus AATF-early-cut
> variants — 9 WebQoE metrics [§2]; implementation: JavaScript executes after onLoad
> event, detects visible DOM objects via position/size, Window.performance API for
> resource timing [§2]; browser: Chrome [§2]; hardware/testbed: Not specified.

---


## Experiments

### above_the_fold-ES1 — illustrative waterfall trace (Fig 1)

**(i) Raw text.** "the example 'waterfall' diagram in Fig. 1, where different objects of
the page are depicted as a Gantt chart" [§1]; above-the-fold portion "fully rendered in
about 2 seconds"; onload event "signaled at 8.5 seconds" [§1]; page identity: Not
specified ("an example page" [Fig 1 caption]); network conditions: Not specified;
browser: Not specified for this figure; repetitions: Not specified (single illustrative
trace).

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(browser; page load;
params.url: Not specified) ⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: Not specified, server: Not specified⟩; path.latency: Not specified;
cca: Not specified; iterations: 1; telemetry {app_metrics: true (ATF ≈ 2s [§1],
PLT = 8.5s [§1])}.

### above_the_fold-ES2 — AATF plugin run on Amazon.com (Fig 2)

**(i) Raw text.** "An illustration of these metrics is shown in Fig.2, when browsing the
Amazon webpage" [§2]; "rendered on or before ATF=5.37s but the page only finishes loading
at PLT=16.11sec" [Fig 2 caption]; "only 8 of the 154 images are located above-the-fold"
[§2]; browser: Chrome (Chrome extension) [§2, "we developed a Chrome extension"];
network conditions: Not specified; hardware: Not specified; repetitions: Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: 1⟩; Experiment = ⟨Workflow(browser;
params.url = amazon.com) ⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: local machine (Chrome), server: amazon.com (real Internet endpoint)⟩;
path.latency: Not specified; cca: Not specified; iterations: 1; telemetry {app_metrics:
true (ATF = 5.37s [Fig 2 caption], PLT = 16.11s [Fig 2 caption])}.

### above_the_fold-ES3 — planned live-demo campaign (text-only, §2)

**(i) Raw text.** "We will do a live demonstration of the plugin capabilities measuring
all WebQoE metrics in two network scenarios" [§2]; scenarios: "good network conditions
and limited bandwidth" [§2]; emulation: "We will emulate both scenarios using Google
chrome's network throttling tool" [§2]; metrics compared: "DOM, AATF, and PLT" [§2];
hardware: "one laptop, which requires internet connection, and one monitor" [§2];
setup time: "approximately 30 minutes" [§2]; bandwidth values: Not specified; websites
visited: Not specified; repetitions: Not specified; results: Not yet reported (prospective).

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(network_scenario ∈
{good_conditions, limited_bandwidth} [§2]) = 2⟩; Experiment = ⟨Workflow(browser;
params.url: Not specified) ⊗ Regime⟨Static: capacity Not specified ("limited bandwidth"
[§2], values Not specified); Dynamic: Not specified⟩⟩ @ Roles⟨client: laptop (Chrome),
server: Internet websites⟩; path.latency: Not specified; cca: Not specified; iterations:
Not specified; telemetry {app_metrics: true (DOM, AATF, PLT [§2])}.
