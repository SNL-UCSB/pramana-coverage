# Brief: record what each experiment needs (creation only), from the paper's own description

You read networking-paper experiments ("ES" = experiment set) and record, for each, what is needed to
CREATE the experiment's conditions. You record what the EXPERIMENT needs, as the paper describes it.

Sources, per paper: `corpus/extractions/<paper>.md` (each experiment is a `### <es_id>` section with the
paper's quotes, the extracted intent, and analysts' notes). Use the paper's own descriptions and quotes.
IGNORE analysts' notes about any system's registry, implementation gaps, or verdicts ("not in NetGent
registry", "GAP-IMPL", "SAT-v2", "M-PARTIAL", "/shape", "Pramana", "NetReplica", "Mininet", etc.): they
describe tools, not the experiment. If a section says it inherits from another experiment ("same setup as
ES1"), read that experiment's section too and record the combined needs.

For each experiment, fill one CSV row with these columns (use ";" to separate multiple values, never ","
inside a field; quote fields that contain commas):

es_id
topology: `none` (one link/path) | `multi-node` (≥2 links, multi-hop, multipath, parking lot, dual bottleneck)
bottleneck: `none` (no link is shaped) | `shaped` (capacity/delay/loss/queue of a bottleneck is set) — give values if stated
cross_traffic: `none` | `generated` (iperf/bulk/synthetic competing flows) | `trace-replay` (recorded traffic or a recorded capacity trace replayed) | `real-app` (competing traffic from real applications)
queue_discipline: `default` (unspecified or drop-tail/FIFO) | the named discipline(s), e.g. `fq_codel`, `CAKE`, `RED`, `ECN marking`, `PIE`
per_flow_path: `no` | `yes` (competing flows need different RTT/loss through one shared bottleneck)
applications: `none` | `tool-only:<tools>` (only iperf, wget, curl, ping, traceroute, netperf, speed tests, DNS tools) | the specific application(s), e.g. `YouTube`, `dash.js player`, `ExoPlayer`, `Netflix`, `Google Meet`, `Chrome page loads of <pages>`, `custom ABR client`, `paper's own app`
congestion_control: `not set` (experiment does not choose its senders' algorithm) | `observed-remote` (it measures what real servers run) | the specific algorithm(s) its own senders use, e.g. `BBR (v1)`, `Cubic`, `BBRv2`, `BBRv3`, `PCC Vivace`, `paper's own: <name>`, `MPTCP <variant>`, `QUIC stack <name>`
infrastructure: `local emulation` | `public Internet targets from any host` | the specific infrastructure, e.g. `AWS <region>`, `GCP <regions>`, `Azure`, `CloudLab`, `Emulab`, `GENI`, `FABRIC`, `PlanetLab`, `RIPE Atlas`, `VPN exits in <countries>`, `cellular <carrier/LTE/5G>`, `Wi-Fi testbed/APs`, `residential ISP`, `satellite`, `phones/devices <type>`
confidence: `high` | `medium` | `low`
quote: one short exact quote from the paper text in the section that best supports the least obvious field
notes: one line; say `cannot-determine: <field>` for any field the text truly does not settle (do not guess)

Rules: be literal and consistent; prefer `cannot-determine` over a guess; do not judge whether any tool can
do it. Write your CSV with a header row to the output path you are given.
