# Papers for Replication

**[CC Classification] 1. VCCAnalyzer: Identifying Congestion Control Algorithms used by Video Streaming Services** ⭐ Awesome
Darshil D. Kaneria, Ranysha Ware, Srinivasan Seshan | ACM PACM Networking 2025 | Citations: N/A (very recent)
*Replication assessment: Strong candidate. Classifies CCAs used by major video streaming platforms (Disney+, Hulu, Twitch) using bottleneck selection and queue occupancy analysis.*

**[CC Classification] 3. CCAnalyzer: An Efficient and Nearly-Passive Congestion Control Classifier**
Ranysha Ware et al. | ACM SIGCOMM 2024 | ~26 citations
*Replication assessment: Strong candidate. Passive classification approach is well-suited for controlled replication.*

**[CC Classification] 3. Prudentia: Findings of an Internet Fairness Watchdog*
Adithya Abraham Philip et al. | ACM SIGCOMM 2024 | ~8 citations
*Replication assessment: Strong candidate. Internet fairness measurement methodology is reproducible in a lab setting.*

**[CC Algorithm Design] 4. PCC: Re-architecting Congestion Control for Consistent High Performance**
Mo Dong et al. | USENIX NSDI 2015 | ~579 citations
*Replication assessment: Strong candidate. A highly influential and well-documented system.*

**[CC Classification] 5. CClinguist: An Expert-Free Framework for Future-Compatible Congestion Control Algorithm Identification**
Jiahui Li et al. | ACM SIGCOMM 2025 | Citations: N/A (very recent)
*Replication assessment: Good candidate. Expert-free, data-driven identification framework should be reproducible.*

**[CC Classification] 6. Containing the Cambrian Explosion in QUIC Congestion Control**
Ayush Mishra, Ben Leong | ACM IMC 2023 | ~18 citations
*Replication assessment: Strong candidate. Network setup is straightforward; however, availability and correct operation of all tested QUIC congestion control variants should be verified before proceeding.*

**[CC Classification] 7. TCP Congestion Signatures**
Srikanth Sundaresan et al. | ACM IMC 2017 | ~28 citations
*Replication assessment: Good candidate. The dual-bottleneck topology is the main complexity to address.*

**[CC Algorithm Design] 8. Promises and Potential of BBRv3**
Danesh Zeynali et al. | Passive and Active Measurement (PAM) 2024 | Citations: N/A (recent)
*Replication assessment: Feasible. Requires multiple simultaneous clients to reproduce cross-traffic experiments. Cross-traffic can potentially be modeled using MAWI traces.*

**[CC Algorithm Design] 9. Mutant: Learning Congestion Control from Existing Protocols via Online Reinforcement Learning**
Lorenzo Pappone et al. | USENIX NSDI 2025 | Citations: N/A (very recent)
*Replication assessment: Partial replication feasible. The Pantheon-based components can be reproduced; the cellular data collection component is out of scope.*

**[CC Algorithm Design] 10. Computers Can Learn from the Heuristic Designs and Master Internet Congestion Control (Sage)**
Chen-Yu Yen et al. | ACM SIGCOMM 2023 | ~16 citations
*Replication assessment: Partial replication feasible. The wired/emulated components are reproducible; the cellular data collection component is out of scope.*

**[Video Quality Inference] 11. Inferring Streaming Video Quality from Encrypted Traffic: Practical Models and Deployment Experience (NetMicroscope)**
Francesco Bronzino et al. | ACM SIGMETRICS / POMACS 2019 | ~59 citations
*Replication assessment: Challenging. Ground-truth QoE collection depends on a Chrome extension that is likely no longer functional with current browser/streaming platform versions.*

**[Video Quality Inference] 12. Estimating WebRTC Video QoE Metrics Without Using Application Headers (NDT-RR)**
Taveesh Sharma et al. | ACM IMC 2023 | Citations: limited (recent)
*Replication assessment: Moderate. The network emulation layer (using `tc` for bottleneck shaping) can be reproduced, but the overall approach is not a top-priority candidate.*

**[Active Queue Management] 13. CAKE (Common Applications Kept Enhanced)**
*Replication assessment: Strong candidate. Note: no associated peer-reviewed publication; implementation is available as a Linux `tc` qdisc.*


# New 
Converge: QoE-driven Multipath Video Conferencing overWebRTC

BONES: Near-Optimal Neural-Enhanced Video Streaming

Measuring the network performance of Google Cloud Platform

Fusing Speed Index during Web Page Loading

Characterizing the Relationship Between Application QoE andNetwork QoS for Real-Time Services

Web Quality of Experience from Encrypted Packets


A practical method for measuring Web above-the-fold time

Poster: Towards Network Model Generalizationusing Strategic Data Collection --> They used NetUnicorn


Estimating Video Quality Using Coarse-Grained Features:Insights and Limitations from Gaussian Mixture Models

Principles for Internet Congestion Management

DEMO: The GhostTwin: Towards Live Digital Twins via SmartNICNetwork Emulation

A Longitudinal Study of the Prevalence of WiFi Bottlenecks inHome Access Networks  --> PINOT + GRE Tunneling

Veritas: Answering Causal Queries from Video Streaming Traces

# newer
Judicious QoS using Cloud Overlays

MPCC: Online Learning Multipath Transport

ABR Streaming with Separate Audio and Video Tracks: Measurements and Best Practices

Perceiving QUIC: Do Users Notice or Even Care?


Characterizing User Platforms for Video Streaming in Broadband Networks

NetDiffusion: Network Data Augmentation Through Protocol-Constrained Traffic Generation

Xatu: Richer Neural Network Based Prediction for Video Streaming

ABM: Active Buffer Management in Datacenters

Decentralization, privacy and performance for DNS

