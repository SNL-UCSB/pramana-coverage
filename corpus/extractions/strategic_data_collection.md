# strategic_data_collection — Experiment-Set Intent Corpus

**Paper:** Poster: Towards Network Model Generalization using Strategic Data Collection — Benjamin Hoffman, Alexander Dietmüller, Laurent Vanbever, ACM SIGCOMM 2025 Posters and Demos (doi:10.1145/3744969.3748407).

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| strategic_dc-ES1 | Exp1 | n/a — OUT-OF-SCOPE (real-world exogenous collection, Ohio [§2 Evaluation]) | n/a | n/a |
| strategic_dc-ES2 | Exp2 | n/a — OUT-OF-SCOPE (real-world exogenous collection, Zurich [§2 Evaluation]) | n/a | n/a |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> Application: video streaming to real clients [§2, "the video streaming data collection
> infrastructure from Puffer"]; infrastructure: customized Puffer video-streaming
> data-collection infrastructure [§2]; deployment: NetUnicorn to data centers worldwide
> [§2, "we utilize NetUnicorn [4] to deploy our infrastructure to data centers worldwide"];
> clients: real clients across the globe — real-world networks, no emulation [§2, "stream
> to real clients across the globe"; §2 Evaluation, "we stream to real clients globally"];
> environment type: real-world (no emulated bandwidth/latency/loss/queueing) [§1, "we
> collect real-world traffic data using servers and clients globally"]; metrics: RTT and
> throughput distributions [Fig 1 axes: "RTT (Density) [µs]", "Throughput (Density) [B/s]"];
> model: encoder-decoder for chunk Transmission Time Prediction [§2, "encoder to estimate
> the latent network state from history and a decoder to predict the chunk transmission time
> from the action and estimated latent state"]; congestion control: Not specified;
> transport/protocol: Not specified; collection period/duration: Not specified;
> number of clients/sessions: Not specified; dataset sizes: Not specified.


## Experiments

### strategic_dc-ES1 — Ohio collection (Fig 1, Fig 2)

**(i) Raw text.** "training one model per dataset, each collected in a distinct environment:
Ohio (server hosted in an AWS data center in Ohio, USA)" [§2 Evaluation]. "we stream to real
clients globally" [§2 Evaluation]. Dataset character: "the Ohio-environment has either high
throughput or high RTT, lacking broad coverage in between" [§2 Environment Analysis, Fig 1].
Real-world clients on real Internet paths. Congestion control, transport, collection
duration, client count, dataset size: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE. Real-world Internet data collection: an AWS server in Ohio
streams video to real clients globally; network conditions are entirely exogenous (real
Internet RTT/throughput from diverse client paths across the globe). No bottleneck is
imposed; no Regime.Static or Regime.Dynamic is configured. No grammar translation is
possible — there is no experimental parameter corresponding to a controlled Regime.

### strategic_dc-ES2 — Zurich collection (Fig 1, Fig 2)

**(i) Raw text.** "Zurich (server hosted at ETH Zürich, Switzerland)" [§2 Evaluation].
"we stream to real clients globally" [§2 Evaluation]. "The Zurich environment covers areas
of higher RTT and lower throughput more broadly" [Fig 1 caption]. Real clients on real
Internet paths. Congestion control, transport, collection duration, client count, dataset
size: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE. INHERITED rationale from ES1: real-world Internet collection
from an ETH Zürich server to real global clients; no controlled Regime.
