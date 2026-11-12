<!-- Agent prompt as run on 2026-10-21 (UTC), model claude-opus-5-5; batch 1 shown, batches 2-5 identical except the batch number. -->

Read-only except one output file. Working directory: needs/.

Input: custom_apps.json — experiments whose `applications` field lists the paper's own (custom) software. Source per experiment: the `### <es_id>` section of corpus/extractions/<paper>.md (paper = es_id before "-ES"; read the parent section if it says it inherits).

The `applications` field must record ONLY what GENERATES THE EXPERIMENT'S TRAFFIC (the programs on the endpoints whose packets cross the network during the experiment). Analysis, classification, measurement-processing, or estimation software that runs on collected data, or that only observes traffic (a classifier, a model, an estimator, a packet analyzer, a sketch), is NOT an application need.

For each experiment, decide from the source:
- `traffic-generating custom`: the paper's own program does generate the traffic (e.g., a custom video client/player, a custom QUIC client/server, a custom traffic generator, a custom ABR implementation inside a player). Keep it.
- `analysis-only`: the paper's own program only analyzes/observes. Then say what DOES generate the traffic, written in BRIEF.md's vocabulary: `none`, `tool-only:<tools>`, or named application(s); or `cannot-determine` if the source does not say.

Write applications_fix.csv with columns: es_id, verdict (traffic-generating custom | analysis-only), new_applications (the corrected full applications field value, using ";" between items), quote (short exact quote from the source supporting the decision). One row per experiment in custom_apps.json. Final message under 120 words: counts per verdict and any you were unsure about.