# quicker_video_streaming — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims (leaf space, ATTEMPTED) | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| quicker_video_streaming-ES1 | Exp1 | cca.stack ∈ {quic, tcp} [Abstract] | 2 | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> 2-page poster. Only measurement activity reported is "preliminary experimentation" [Abstract]
> using "Chrome and Firefox builds with working QUIC clients ... for adaptive bitrate streaming
> using MPEG-DASH" [§3]. The MPEG-DASH dash.js player is mentioned as a base for HAS
> statistics logging [§3]. Network conditions (bandwidth, RTT, queue, loss, reorder), server
> software, QUIC version/implementation, number of repetitions, video dataset, and CCA —
> all Not specified. Results are qualitative only: "simply running contemporary HAS
> implementations over QUIC does not improve but actually hurts streaming performance
> compared to a traditional TCP deployment" [Abstract]. No numeric figures or tables.


## Experiments

### quicker_video_streaming-ES1 — Preliminary HAS-over-QUIC vs TCP streaming trials (text-only)

**(i) Raw text.** "preliminary experimentation has shown that simply running contemporary
HTTP Adaptive Streaming (HAS) implementations over QUIC does not improve but actually
hurts streaming performance compared to a traditional TCP deployment" [Abstract]; "Both
Chrome and Firefox provide builds with working QUIC clients which we have already
successfully used for adaptive bitrate streaming using MPEG-DASH" [§3]; "MPEG-DASH dash.js
player as a base for our HAS statistics" [§3 — described as ongoing logging framework, not
necessarily an Exp1 parameter]. Rendering merge assumption: abstract's "preliminary
experimentation" and §3 Chrome/Firefox MPEG-DASH trials treated as one campaign; confirmed
in rendering (Exp1 notes, caveat 1). QUIC implementation Not specified. CCA Not specified.
Network conditions all Not specified.

**(ii) Grammar.** ExperimentSet⟨leaves: sweep(cca.stack ∈ {quic, tcp} [Abstract]) = 2 × 1 = 2;
Experiment = ⟨Workflow(browser; app: mpeg-dash [§3]; client: Chrome | Firefox [§3]) @
path: Not specified ⊗ Regime⟨Static: Not specified; Dynamic: Not specified⟩⟩ @
Roles⟨client: browser host; server: DASH video server⟩; iterations: Not specified;
telemetry {app_metrics: true (streaming performance, qualitative [Abstract]); pcap: Not
specified; qtrace: Not specified}⟩.
