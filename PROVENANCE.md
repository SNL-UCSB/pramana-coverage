# Provenance

Every artifact in this repository, how it was produced, by what, and when.

| Artifact | Produced by | Model | Date | Inputs / prompt |
|---|---|---|---|---|
| `corpus/selection/` | Search of ACM venues by keyword, then manual triage | none (scripted search + manual review) | 2026 (see file history) | `keyword_to_search.md`, `CCS_list.md`, `fetch_acm_papers.ipynb` |
| `corpus/extractions/` | One model worker per paper, rendering each experiment as quotes with locators plus a grammar translation; checked by the Tier-1 mechanical gate | **not recorded** (to be filled in) | 2026-07-06 to 2026-07-07 | `pipeline/corpus/PROMPT.md`, `CALIBRATION.md`, `grammar.md` |
| Red-team review of the extractions | Codex adversarial gates | `gpt-5.4` (OpenAI Codex) | 2026-07-06 | gates in `pipeline/corpus/CALIBRATION.md` §4 |
| `corpus/scope.csv` | Scope decision per experiment (in: emulation or real infrastructure; out: simulation, passive traces, analysis) | as for the extractions | 2026-07 | `PROMPT.md` §2 |
| `needs/needs.csv` | Five readers (51 experiments each) recorded each experiment's needs from its extraction; five independent reviewers re-checked every field of every row against the same source; conventions applied as documented in `rule/RULE.md` | `claude-opus-5-5` | 2026-10-20 | `pipeline/needs/BRIEF.md`, `REVIEW_BRIEF.md`, `reader_prompt.md`, `reviewer_prompt.md`, `own_software_reread_prompt.md` |
| `systems/<public system>/sheet.json` | Capabilities read from each system's code at the anchor commit; every claim cites (repo, commit, path, string) | `claude-opus-5-5` assisting the authors | 2026-10-20 | checked mechanically by `systems/verify_sheets.py` |
| `systems/pramana/sheet.json` | Capabilities stated as interfaces, with the scored commits named; the implementation is not yet public | authors | 2026-10-20 | |
| `results/` | `rule/creation_only.py` | none (deterministic) | regenerated on every run | `needs/needs.csv`, `systems/*/sheet.json` |

The extraction step is prompt-driven and is not expected to regenerate identical text; it is reproducible
through its prompts, conventions, gate, and outputs, all released here. Everything after it (needs table,
sheets, rule, results) is checkable line by line, and the rule is deterministic: two runs produce
byte-identical outputs.

Validation of the rule (2026-10-20, `claude-opus-5-5`): an independent re-implementation written from
`rule/RULE.md` alone matched all 1,275 verdicts (255 experiments x 5 systems); five rounds of adversarial
review, with each finding checked against code before it was applied.
