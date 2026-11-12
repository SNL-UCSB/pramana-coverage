# netdpsyn — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Scope class | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| netdpsyn-ES1 | Exp1 (main synthesis + downstream evaluation, ε = 2.0) | OUT-OF-SCOPE: offline synthetic data generation | method ∈ {NetDPSyn, NetShare, PGM, PrivMRF} × dataset ∈ {UGR16, CIDDS, TON, CAIDA, DC} = 4 × 5 = 20 [§4.1] | 1 synthesis run per leaf; 10 per sketch run [§4.2]; otherwise Not specified |
| netdpsyn-ES2 | Exp2 (ε-sweep ablation, Appendix F) | OUT-OF-SCOPE: offline synthetic data generation | ε ∈ {0.1, 1.0} new runs × {methods} × {datasets} (exact product Not specified; scope limited to TON for Fig 7 and TON + UGR16 for Tab 6/7 [App F]) | Not specified |
| netdpsyn-ES3 | Exp3 (GUMMI vs GUM ablation, Appendix F) | OUT-OF-SCOPE: offline synthetic data generation | variant ∈ {GUMMI, GUM} × update_iterations ∈ {1,2,3,4,5,10,20} = 2 × 7 = 14 [App F] | Not specified |
| netdpsyn-ES4 | Exp4 (Gaussian copula, text-only, §2.4) | OUT-OF-SCOPE: offline synthetic data generation | Not specified | Not specified |

## Shared methodology (raw text) (quoted from the paper)


> Offline synthetic network trace generation on one workstation [§4.1]. Testbed: 20.04.1-Ubuntu,
> AMD 3970x CPU (32 cores), 256 GB memory [§4.1]. Python 3.11.4 [§4.1]. Five public datasets
> (UGR16, CIDDS, TON, CAIDA, DC) obtained from the NetShare authors — subsets of the originals
> [App D]. No live network infrastructure, no emulation, no controlled bottleneck.
> Network conditions: Not applicable throughout.


## Experiments

### netdpsyn-ES1 — Main synthesis + downstream-evaluation campaign (ε = 2.0)

**(i) Raw text.** All four synthesis methods (NetDPSyn, NetShare, PGM, PrivMRF) applied to 5 public
datasets at default privacy budget ε = 2.0 [§4.1]; δ = 10^−5 for NetShare [§4.1]. Downstream tasks:
(1) data sketching — CAIDA srcip and DC dstip, 4 algorithms (CMS, CS, UM, NS), 10 repetitions per
sketch run [§4.2]; (2) flow classification — TON, UGR16, CIDDS, 5 ML models (DT, LR, RF, GB, MLP),
80%/20% train/test split [§4.3]; (3) packet anomaly detection — CAIDA, DC, NetML OCSVM, 6 modes
[§4.3]; (4) efficiency/running time — 5 datasets [§4.4]; (5) attribute JSD/EMD — TON (Fig 5) and
CAIDA (Fig 6) [App E]. MIA re-analysis: 64.01% / 55.87% attack accuracy on raw / ε=2 TON [App G].
All on one workstation [§4.1]. Any field not listed above is Not specified.

**(ii) Grammar.** [OUT-OF-SCOPE — offline synthetic data generation; no network infrastructure; see
design verdict. For reference only: the experimental unit is a ⟨method, dataset⟩ pair; 4 × 5 = 20
such pairs; no Regime, no Workflow, no Roles in the grammar sense.]

### netdpsyn-ES2 — ε-sweep ablation (Appendix F, "Noise scale")

**(i) Raw text.** ε reduced to 1.0 and 0.1 (new synthesis runs outside the ε=2.0 default) [App F,
"we reduce ε to 1.0 and 0.1"]; TON classification accuracy under DT and RF in Fig 7; large ε range
(4.0, 8.0, 16.0, 32.0, 64.0, 10^3, 10^10 stated in text; table rows: 4.0, 16.0, 32.0, 64.0, 10^3,
10^10 — 8.0 absent, contradiction reported as printed [App F, Tab 6, Tab 7]) for NetDPSyn vs
NetShare on TON (Tab 6) and UGR16 (Tab 7) [App F]. MIA re-analysis at ε=0.1: attack accuracy
drops to 40.85% [App G]. Testbed, datasets, software: as ES1.

**(ii) Grammar.** [OUT-OF-SCOPE — offline ε-sweep ablation; see design verdict.]

### netdpsyn-ES3 — GUMMI vs GUM record-synthesis ablation (Appendix F)

**(i) Raw text.** NetDPSyn run with GUMMI and GUM record-synthesis variants separately on TON;
update iterations swept over {1, 2, 3, 4, 5, 10, 20} [App F, "We choose 7 values for update
iterations, {1, 2, 3, 4, 5, 10, 20}"]; metrics: DT and GB classification accuracy on TON [Fig 8
caption]; ε = 2.0 [§4.1 blanket statement; not restated in App F for these runs]; at 1 update
iteration GUM ≈ 0.45 vs GUMMI ≈ 0.85 for decision tree [App F]. Testbed as ES1.

**(ii) Grammar.** [OUT-OF-SCOPE — offline record-synthesis ablation; see design verdict.]

### netdpsyn-ES4 — Gaussian copula preliminary experiment (text-only, §2.4)

**(i) Raw text.** "We did preliminary experiments with Gaussian copula, but the result was
unsatisfactory" [§2.4]. No figure or table. Dataset(s), metrics, hardware, privacy budget: Not
specified.

**(ii) Grammar.** [OUT-OF-SCOPE — text-only offline synthesis experiment; see design verdict.]
