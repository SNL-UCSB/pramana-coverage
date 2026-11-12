# Review brief: verify every row of a needs table against the paper extraction

You are an independent reviewer. Another reader filled `batchN.csv` (one row per experiment) following
`BRIEF.md`. Your job: check EVERY row, EVERY field, against the source, and produce a verified table.
Read `BRIEF.md` first; its definitions apply, with ONE change below.

Source per experiment: the `### <es_id>` section of `corpus/extractions/<paper>.md` (paper = es_id before
"-ES"; for inherited experiments also read the parent section). Use the paper's own descriptions and
quotes. Ignore analysts' notes about tools, registries, gaps, verdicts.

## Schema change (apply to every row)
Split the old `cross_traffic=trace-replay` into two independent fields:
- `cross_traffic`: `none` | `generated` | `cross-traffic-trace` (recorded competing traffic replayed into the bottleneck) | `real-app` — several values separated by ";" if several apply
- `capacity_variation` (NEW column, placed after `bottleneck`): `none` | `capacity-trace` (a recorded time-varying capacity/bandwidth trace, e.g. Mahimahi cellular/FCC traces, Chrome DevTools throttling profiles replayed over time) | `synthetic-schedule` (capacity changed on a programmed schedule, e.g. step changes) | `cannot-determine`

## For each row
1. Read the source section.
2. For each field, decide: correct as written, or wrong. If wrong, replace the value. Prefer `cannot-determine` over a guess when the source does not settle it; but if the source DOES settle a field the reader marked `cannot-determine`, fill it.
3. Keep or replace the `quote` so it supports the least obvious field; add a quote for every correction.

## Output
Write `verified_batchN.csv` (same directory) with columns:
es_id, topology, bottleneck, capacity_variation, cross_traffic, queue_discipline, per_flow_path, applications,
congestion_control, infrastructure, confidence, quote, notes, status, changes
- `status`: `confirmed` (no field changed except adding capacity_variation / splitting trace-replay) or `corrected`
- `changes`: for each changed field: `<field>: <old> -> <new> because "<exact quote>"` (separate with " || ")
One row per es_id in the batch, none extra. Do not edit any other file.
Final message under 150 words: rows, how many corrected, and the fields most often corrected.
