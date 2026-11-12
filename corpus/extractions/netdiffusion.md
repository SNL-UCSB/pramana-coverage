# netdiffusion — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Sweep dims | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| netdiffusion-ES1 | Exp1 (NetDiffusion generation) | single generation campaign | 1 | Not specified |
| netdiffusion-ES2 | Exp2 (NetShare baseline generation) | single generation campaign | 1 | Not specified |
| netdiffusion-ES3 | Exp3 (random generation baseline) | format ∈ {NetFlow, raw pcap} (same campaign) | 1 | Not specified |
| netdiffusion-ES4 | Exp4 (tcpreplay retransmission) | single replay run | 1 | Not specified |

## Experiments

### netdiffusion-ES1 — NetDiffusion synthetic pcap generation campaign (Fig 2, Tabs 3–5, Fig 4, Tabs 6–9, Tab 11)

**(i) Raw text.** Stable Diffusion 1.5 pre-trained on LAION-5B ("over 5.85B
CLIP-filtered image-text pairs" [§3.2.2]); fine-tuned with LoRA [§3.2.2];
traffic encoding: nPrint bit-level, images 1088 pixels wide × 1024 pixels
high (one pixel row per packet) [§3.1.2, "1088 pixels wide × 1024 pixels
high"]; packets grouped "in groups of 1024" [§3.1.2]; ControlNet with M-LSD
line detection [§3.2.3]; post-generation heuristic "affects only ~8% of the
synthetic traffic features" [§4.2.2]; generated volume: "The volume of this
synthetic dataset adjusts based on specific evaluation requirements" [§4.1];
generation capped at 1,024 packets per flow sample [§6]. Network emulation
parameters: Not specified (no network emulation described for this campaign).

**(ii) Grammar.** OUT-OF-SCOPE — ML-model generation of synthetic network
traffic images. No network Regime, no Workflow, no CCA, no bottleneck link.
Grammar translation is not applicable.

### netdiffusion-ES2 — NetShare baseline synthetic NetFlow generation campaign (Tab 1, Tabs 3–4, Fig 4, Tabs 6, 8)

**(i) Raw text.** NetShare [141]: GAN-based generator, "produce[s]
IPFIX/NetFlow-style statistics on network traffic" [§2.2]; evaluation:
"Following the method in the original paper" [§2.3]; scenarios: "(1) training
and testing on real NetFlow data, (2) training on NetShare synthetic data and
testing on real data, and (3) vice versa" [§2.3]; training configuration
and generated volume: Not specified. Network emulation parameters:
Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — GAN-based NetFlow attribute generation.
No network experiment component.

### netdiffusion-ES3 — Naive random-generation baseline campaign (Tab 3)

**(i) Raw text.** "a naive random generation approach. The latter, by
generating purely random values, acts as a worst-case scenario, illustrating
the lower bounds of similarity" [§4.2.1]; generated formats: random NetFlow
AND random raw network traffic (pcap) [Table 3 rows]; tool, random-value
distribution, volume: Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — random-value synthesis baseline. No network
experiment component.

### netdiffusion-ES4 — tcpreplay retransmission run (Tab 10)

**(i) Raw text.** "All 1,024 packets were successfully sent without any
failures or truncations" [§4.3]; traffic replayed: NetDiffusion-generated
Amazon network traffic [Table 10 caption]; tool: tcpreplay [§4.3];
run characteristics: duration 0.613297 s [Table 10], rate 17.20 Mbps
[Table 10], 1318664 bytes [Table 10], 0 failed / truncated / retried
packets [Table 10]; network interface, host hardware, OS, repetitions:
Not specified.

**(ii) Grammar.** OUT-OF-SCOPE — retransmission of synthetically generated
pcap to validate that the synthetic trace is well-formed and transmissible.
The packets are derived from Exp1's ML-generated output; the measurand is
synthetic-traffic quality (parse-ability / retransmission fidelity), not
a controlled network experiment. No Regime bottleneck shaped; no
application workflow studied; no CCA exercised.
