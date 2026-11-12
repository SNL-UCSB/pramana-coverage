# diffrl — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Collection description | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| diffrl-ES1 | Exp1 (Fig 4 panel c) | Pensieve DRL agent training — reward curves and checkpoint extraction | 2 (H=128, H=64) | Not specified (RL training steps) |
| diffrl-ES2 | Exp2 (Figs 4ab, 5, 6) | Pensieve symbolic-property verification campaign (3 properties × 2 model sizes × 6 checkpoints × coverage levels) | Not specified | Not specified |
| diffrl-ES3 | Exp3 (Figs 7, 8) | CMARS symbolic-property verification campaign (3 properties × 4 model variants × 2 action-space sizes) | Not specified | Not specified |
| diffrl-ES4 | Exp4 (Table 1) | Aurora symbolic-property verification campaign (3 properties × 2 coverage levels × 3 solvers) | Not specified | Not specified |

## Shared methodology (raw text, inherited unless overridden) (quoted from the paper)


> "All experiments were conducted on an Intel(R) Xeon(R) Silver 4314 machine
> with a 2.40GHz CPU" [§5]; per-query timeout 600 seconds [§5]; outcomes
> classified as safe / unsafe / unknown [§5]; verification backends: Marabou v2
> in Split-and-Conquer mode with default settings [§5], Gurobi under an academic
> license with 28 threads [§5], Alpha-Beta-CROWN extended by the authors [§5];
> artifacts at https://github.com/mhmd97z/diffRL [§5].

**No network infrastructure is used in any experiment in this paper.** All four
ESes are formal or computational analyses of pre-trained neural network models;
no packets are generated, no network topology is configured.


## Experiments

### diffrl-ES1 — Pensieve DRL agent training

**(i) Raw text.** "two configurations of Pensieve's policy network, with hidden
layer sizes H = 128 and H = 64" [§6.3]; "π128^Pensieve with 103 174 parameters
and π64^Pensieve with 27 142 parameters" [§6.3]; "ckpt 0 refers to the randomly
initialized policy before any training and ckpt i corresponds to the model
checkpoint at i × 10k training steps" [§6.3]; "the two model sizes follow nearly
identical reward trajectories" [§6.3, Fig 4(c)]. Training algorithm,
hyperparameters, training environment, network traces, and training hardware: Not
specified.

**(ii) Grammar.** This is a DRL model training run, not a network experiment.
There is no Workflow (no network application executing over a testbed), no Regime
(no bottleneck link configured), and no telemetry in the Pramana sense. The
"experiment" produces trained model checkpoints consumed by ES2. Grammar
representation: out of Pramana grammar scope — no ExperimentSet production
applies.

### diffrl-ES2 — Pensieve symbolic-property verification campaign

**(i) Raw text.** "We investigate Pensieve [36]" [§6]; "6 invalid output neuron
pairs – and thus 6 verification queries – for each monotonicity property and 12
for the robustness property" [§6.3]; perturbation bound ε = 0.01 [§6.3]; tolerance
d = 3 bitrate levels [§6.3]; input-domain coverage levels "ranging from 60% to
100% of each feature's entire operational range" [§6.3]; "we analyze Pensieve's
properties using the remaining two verification backends" (MIP and Alpha-Beta-CROWN
— Marabou excluded due to unsupported input slicing) [§6.3]; "the smaller model
produces approximately 45% fewer unknown results" [§6.3].

**(ii) Grammar.** This is a formal-verification (SMT/MIP solver) campaign over
pre-trained neural network models. No Workflow runs over a network; no Regime is
configured. Grammar representation: out of Pramana grammar scope — no
ExperimentSet production applies.

### diffrl-ES3 — CMARS symbolic-property verification campaign

**(i) Raw text.** "We study CMARS [66]" [§7]; "two architectural variants – using
either two or three fully connected layers – and two action-space sizes, with M ∈
{15, 30}" [§7.1]; "diffRL generates 28 and 105 invalid output neuron pairs for
the two monotonicity properties when M = 15 and M = 30, respectively; the number
of queries is doubled for the robustness property" [§7.3]; perturbation bound ε =
0.01 [§7.3]; tolerance values d = 8 for M = 15 and d = 16 for M = 30 resource
units [§7.3]; backends: Marabou, MIP, and Alpha-Beta-CROWN [§7.3]; "for π3,15^CMARS
Marabou identifies up to 30% more violations than MIP" [§7.3].

**(ii) Grammar.** Formal-verification campaign over CMARS neural network models
(a radio resource allocation DRL agent). No network traffic generated; no Regime
configured. Grammar representation: out of Pramana grammar scope.

### diffrl-ES4 — Aurora symbolic-property verification campaign

**(i) Raw text.** "We investigate Aurora [24]" [§8]; architecture Input(9) →
FC(128) → ReLU → FC(128) → ReLU → FC(128) → Output(1) [§8.1]; "we replace these
[tanh] with ReLU activations ... and use a retrained model from [45] that obtains
comparable performance" [§8.1]; input-domain coverage "70% and 100% coverage of
each input feature" [§8.3]; "under a perturbation bound of ε = 0.01" [§8.3];
"all engines resolve all queries at 70% coverage, all three properties safe; at
100% only MIP resolves all queries, finding unsafe behaviors for all three
properties" [§8.3]; the standard deviation is fixed to σ = 0.5 [§8.1].

**(ii) Grammar.** Aurora is a DRL-based congestion-control algorithm. The
experiment does NOT run Aurora over a network — it verifies the Aurora DNN model's
symbolic properties using formal solvers. No network traffic generated; no Regime
configured. Grammar representation: out of Pramana grammar scope.
