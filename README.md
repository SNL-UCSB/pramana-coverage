# pramana-coverage

The corpus, per-experiment needs, capability sheets, and counting rule behind the coverage results in
*Pramana* (HotNets 2026). Given an experiment from the corpus and one system, can a researcher create the
experiment's conditions through that system's own interface? This repository answers that question for
Pramana's implementation, NetReplica, Mininet, netUnicorn, and NetGent, and lets anyone check every step.

```
python3 systems/verify_sheets.py      # check every public citation against its pinned commit
python3 rule/creation_only.py         # recompute results/ (deterministic; Python 3 stdlib only)
python3 rule/options.py               # counts under the open decisions D1-D3 (rule/RULE.md)
```

## From papers to results

| Step | Where | What it holds |
|---|---|---|
| 1. Select papers | `corpus/selection/`, `corpus/papers.csv` | the search and triage that produced 66 papers |
| 2. Extract experiments | `corpus/extractions/`, `pipeline/corpus/` | each experiment's quotes, with locators into its paper, and its intent in the grammar; the prompt, conventions, and mechanical gate that produced them |
| 3. Decide scope | `corpus/scope.csv` | all 387 experiments; 255 are in scope |
| 4. Record needs | `needs/needs.csv`, `pipeline/needs/` | what each in-scope experiment needs to create its conditions, read from the paper and independently re-checked |
| 5. State capabilities | `systems/*/sheet.json` | what each system provides at the anchor date |
| 6. Count | `rule/`, `results/` | the rule, its conventions, and the per-experiment verdicts |

`PROVENANCE.md` records, for every step, the tool, the exact model version, the date, and the prompt.

### Scope categories (`corpus/scope.csv`)

An experiment is in scope when it generates its own traffic, excluding simulation, passive capture, and
offline computation.

| Category | Count | Meaning |
|---|---|---|
| `IN-emulation` | 170 | generates its own traffic over conditions the experimenters emulate |
| `IN-realinfra` | 85 | generates its own traffic over real infrastructure |
| `OUT-exogenous` | 52 | observes traffic it does not generate (passive capture) |
| `OUT-offline` | 48 | computes on existing data |
| `OUT-simulator` | 32 | runs in a simulator |

## Capability sheets

- **Mininet, netUnicorn, NetReplica, NetGent** (public code): every credited capability cites a repository,
  a pinned commit, a file, and a string in that file. `systems/verify_sheets.py` clones each repository and
  checks all of them.
- **Pramana**: The Pramana implementation is not yet public. It will be released once it closes a substantial part of the gap between what the design expresses and what the implementation covers. Its sheet (`systems/pramana/sheet.json`) states each credited capability as an
  interface (endpoint and parameters) and names the commits that were scored.

## Results (anchor 2026-07-17)

| | Pramana | NetReplica | Mininet | netUnicorn | NetGent |
|---|---|---|---|---|---|
| covered (of 255) | 68 | 28 | 23 | 11 | 2 |

Checking applications by name against each system's workflow list instead of by type (decision D3) gives
Pramana 46. `rule/RULE.md` states the rule, every convention, and the sensitivity variants.

## Licenses

Code: MIT. Data, prompts, and sheets: CC BY 4.0. Quotations remain their authors' and are short excerpts
with locators. See `LICENSE`.
