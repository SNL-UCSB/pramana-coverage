# Creation-only coverage of the Pramana corpus

Given an experiment from the corpus and only one system, can a researcher realize the experiment's
conditions through that system's own interface, or must they write ad hoc scripts? A system is credited
only for what its interface provides. The answer is computed by one deterministic script from two
inputs a reader can check line by line.

```
python3 rule/creation_only.py                      # base rule -> verdicts.csv, summary.json, value_map.csv
python3 rule/creation_only.py --variant V3         # sensitivity variants (see below)
python3 rule/creation_only.py --variant V1 --needs needs/needs_V1_silence_unknown.csv
python3 rule/options.py                            # counts under the open decisions D1-D3
```
Python 3 standard library only; the scripts can be run from any directory and write their outputs next
to themselves. Two runs give byte-identical outputs (check with `shasum -a 256`).

## Scoring anchor

Every system is scored at the same date. The current numbers use the HotNets submission (2026-07-17).
The anchor moves to the camera-ready snapshot for **all five systems** at once; at that point each
system's commit is recorded in the system's sheet (`systems/<name>/sheet.json`) and every capability is re-checked against it.

## Inputs

| File | What it is | How it was made |
|---|---|---|
| `needs.csv` | One row per experiment (255): what the experiment needs, in nine fields, read from the paper's own description of the experiment. | A reader filled each row from the extraction (`papers_v2/<paper>.md`, the paper's quotes); an independent reviewer then checked every field of every row against the same source. `status` = confirmed or corrected; `changes` gives each correction with its supporting quote. |
| `systems/*/sheet.json` | What each system provides through its own interface at the anchor, as capability types. | Public systems: read from code at pinned commits, every claim cited and checked by `systems/verify_sheets.py`. Pramana: capabilities stated as interfaces, with the scored commits named (the implementation is not yet public). |

## The rule

A system **covers** an experiment if it provides every capability type the experiment needs.
It is **not covered** if any determinable need is missing. It is **cannot-determine** if all
determinable needs are met but the paper leaves some need unsettled (for example, it does not state
the congestion-control algorithm of its video sender). Only *covered* counts; *covered + cannot-determine*
is the upper bound. Recording what the experiment measures is not checked (creation only).

### Capability types

| Type | Needed when the experiment ... |
|---|---|
| `TOPO` | shapes two or more links: parallel paths for a multipath transport, or links in series |
| `SHAPE` | sets the capacity, delay, or buffer of a bottleneck link |
| `LOSS`, `JITTER`, `REORDER`, `BURSTLOSS` | sets random loss / delay jitter / packet reordering / burst (Gilbert or Markov) loss on that link |
| `PATHVAR` | changes delay or loss over time (a per-second RTT/loss sequence, or a schedule) |
| `CAPVAR:trace` | varies the capacity left for the application over time following a recording |
| `CAPVAR:schedule` | changes capacity on a programmed schedule (e.g., step changes) |
| `XGEN` / `XTRACE` / `XAPP` | adds competing traffic: generated flows / a replayed traffic trace / real applications |
| `QDISC:<name>` | sets a non-default queue discipline (checked by name) |
| `PERFLOW:apps` / `PERFLOW:any` | gives competing flows different delay or loss through one shared bottleneck, where those flows are all browser applications / include generated or tool flows |
| `TOOL:<name>` | runs a named packaged command-line tool (iperf, ping, wget, curl, capture, speedtest, ndt, traceroute, flent, h2load, an HTTP server, ...); every system that runs commands provides all of them |
| `USERSPACE_SW` | runs a user-space program that must be built for the experiment: a command-line research prototype (PANDA on libdash, Gordon, CGReplay, ...) or a user-space transport stack (QUIC stacks, PCC, Copa, Indigo, Aurora, Sprout, ...) |
| `APP` | drives an application through its interface (browser automation): a commercial service, a browser loading web pages, a player in a browser (dash.js, Shaka), or a research player or page loader that runs in a browser (Pensieve, MPC, Fugu, Vroom, Fawkes) |
| `ANDROID_APP` | runs an Android-only application (ExoPlayer) |
| `KCCA:<name>` / `KSET:<n>` | sets its senders to a stock Linux congestion-control module / to n unnamed ones |
| `SYSCTL` | needs one kernel setting on a stock kernel (ECN at the host, Cubic's HyStart switch) |
| `KERNEL_BUILD` | needs a kernel other than the stock one (BBRv2/v3, out-of-tree MPTCP and its algorithms and schedulers, a modified BBR, kernel-patch schemes such as Orca and C2TCP, a specific kernel version) |
| `LOCAL`, `INET` | runs on local machines / reaches public Internet targets |
| `CLOUD:<provider>`, `REMOTE_HOSTS`, `ACCESS` | runs hosts in a named cloud / at remote sites over wide-area paths / on real access networks (cellular, Wi-Fi, residential) |
| `DEVICES` | runs on phones, tablets, TVs, or consoles |
| `WAN_PLATFORM`, `SPECIAL_HW`, `REAL_USERS`, `OPERATOR_VANTAGE` | needs a measurement platform (RIPE Atlas, CAIDA Ark, VPN exits, SCION) / special hardware (RDMA NICs, Tofino, SDR, 25 Gbps fabric) / real users / an operator's vantage point |

`value_map.csv` lists every distinct value in `needs.csv` and the type it maps to.
The mapping is a table of ordered patterns in `creation_only.py`; a value that matches no pattern stops the run.

### Conventions (each applies identically to every system)

1. **Credit only what the system's interface provides, without ad hoc engineering.** A packaged
   command-line tool (installable from the distribution and run with one command: iperf3, wget, curl,
   ping, traceroute, flent, netperf, h2load, an HTTP server) counts for every system that runs a command on
   an endpoint (Pramana and NetGent shell workflows, Mininet `Node.cmd()`, netUnicorn `ShellCommand`,
   NetReplica `run_client`); so do concurrent iperf3 flows as competing traffic. Software that must be built
   from source for the experiment (QUIC stacks at given commits, PCC, research prototypes) counts for no
   system: that a workflow generator could build it is a design claim, the same as kernel choice
   (convention 9), until the system's code contains a workflow that builds and runs it.
2. **Browser automation counts for NetGent and Pramana only.** Driving an application through its
   interface is a stated feature of NetGent, which Pramana subsumes.
3. **Silence on an optional feature means absent.** When a paper says nothing about competing
   traffic, capacity variation, per-flow path, or a non-default queue discipline, the feature is
   absent: a paper that adds competing traffic describes it, because it is part of the method.
   Ambiguity stays cannot-determine. Variant V1 reverses this convention.
4. **The paper's own software is the thing under test, not a condition.** Its new algorithm, player,
   or scheduler is not a need for any system. Variant V5 counts it as a need no system meets.
5. **Cubic alone needs no congestion-control setting.** It is Linux's default.
6. **Where an experiment ran matters only when the real network is what it measures.** If the experiment
   shapes its own bottleneck, a system that reproduces those conditions covers it: the location (cloud,
   remote sites, access networks, platforms) and an unnamed testbed are dropped. If it shapes nothing,
   or the studied path is the real one, the location is a need. Phones and special hardware stay needs.
   The same holds for several paths or links: a multi-node topology is a need only when the experiment
   shapes its links; an unshaped experiment's paths are the real infrastructure it runs on, counted there.
7. **Time-varying capacity from a recording is created by replaying rate-capped cross-traffic profiles
   (CTPs) on a static envelope** (Regime = Static ⊗ Dynamic, NTC '26 §3), through Pramana's `/replay` and
   NetReplica's `ctp()`. This creates time-varying capacity from recorded traffic; it does not replay the
   specific capacity trace a paper used.
   A programmed capacity schedule (steps every few seconds) is a simple `tc` CLI step on a shaped
   bottleneck, so every system that shapes a bottleneck and runs commands provides it (Pramana, NetReplica, Mininet);
   the same holds for delay and loss changed on a schedule with `tc netem` (`PATHVAR`).
8. **Infrastructure is credited where a system ships a working connector that runs hosts there.**
   netUnicorn's SSH connector runs on any Linux host the researcher can reach. Pramana's implemented backends
   are local Docker and AWS (EC2 hosts in hybrid mode); `gcp` and `remote` are stubs.
9. **Kernel choice is credited to no implementation.** Pramana's workers run as containers on a fixed host image and share its kernel.
10. **Named things are checked by name where the system's code enumerates them**: queue
    disciplines (Pramana and NetReplica pass any name to `tc`; Mininet's TCLink has fixed options), and
    kernel algorithms (Pramana's 15-entry list). Applications are credited by type (decision D3 checks them by name).
11. Throughout: companion packages from the tool's team count; composition counts through
    the composing system's own interface; code is credited once.

### Precise readings

- Free-text fields are split into values on `;` outside parentheses; each value is looked up in `value_map.csv`.
- `topology`: any value containing `multi-node` needs `TOPO`. `bottleneck`: a value starting with `none` is no need; `cannot-determine` is cannot-determine; any other value needs `SHAPE`, plus `LOSS` (the word "loss", not "zero loss" or "burst loss"), `BURSTLOSS` ("gilbert", "markov", "burst loss"), `JITTER` ("jitter", not "throughput jitter"), `REORDER` ("netem reordering"), `PATHVAR` (one of "time-varying", "per-second", "varied at random" AND one of "latency", "rtt", "loss" in the same value; "time-varying capacity" alone is `CAPVAR`, not `PATHVAR`).
- `capacity_variation`: `capacity-trace` needs `CAPVAR:trace`, `synthetic-schedule` needs `CAPVAR:schedule`. `cross_traffic`: each of `generated`, `cross-traffic-trace`, `real-app` needs its type.
- Cubic alone: `KCCA:cubic` is dropped when it is the only kernel algorithm in the field, whatever else the field holds.
- `QDISC:default` is no need. `KCCA:<name>` is met only if the system lists the name. `CUSTOM_QDISC`, `KERNEL_BUILD`, `ANDROID_APP`, `SYSCTL`, `USERSPACE_SW` (software built from source) is provided by no system. A system's `types` list in the system's sheet (`systems/<name>/sheet.json`) is authoritative for every other type (e.g., `REORDER` and `BURSTLOSS` for Pramana and NetReplica through `netem`).
- `KSET:n`: not met if the system lists fewer than n kernel algorithms; met for n = 15 only where the system's sheet (`systems/<name>/sheet.json`) marks the list as the CCAnalyzer set; for any other n it is cannot-determine (which n algorithms is not stated).
- `per_flow_path: yes` needs `PERFLOW:any` if the experiment also needs `XGEN` or a `TOOL:`, else `PERFLOW:apps`; a system with `PERFLOW:any` meets both.
- `TOPO` is dropped when `SHAPE` is not needed (convention 6).
- Convention 6 is applied after classification: when `SHAPE` is needed, the infrastructure types `CLOUD:*`, `REMOTE_HOSTS`, `ACCESS`, `WAN_PLATFORM`, `REAL_USERS`, `OPERATOR_VANTAGE` and an infrastructure `cannot-determine` are replaced by `LOCAL`; `DEVICES` and `SPECIAL_HW` stay. Without `SHAPE`, nothing is replaced.
- Precedence: any unmet determinable need gives NOT COVERED; otherwise any `cannot-determine` gives CANNOT-DETERMINE.

## Open decisions (computed by `options.py`; the base rule uses "no" for all three)

| | Question |
|---|---|
| D1 | Credit netUnicorn's Containernet connector (CCS '23 Table 8), which takes Mininet's API? Modelled as one deployment per experiment. |
| D2 | Count only code merged into each system's main branch at the anchor? (Pramana's per-flow-path and concurrent-application branches are not merged.) |
| D3 | Check applications by name against each system's workflow inventory instead of by type? |

## Sensitivity variants

| Variant | Change |
|---|---|
| V1 | silence on optional features read as cannot-determine |
| V3 | Emulab/CloudLab experiments need the testbed (credited only via an SSH connector) |
| V4 | access networks credited to no system |
| V5 | the paper's own software counted as a need no system meets |

## Limits

- The needs table rests on the extraction of each paper, read by a reader and an independent
  reviewer; a field the extraction gets wrong is wrong here. Corrections are listed per row.
- Several schemes are classified as user-space or kernel from their public implementations with less
  certainty (Sage, Astraea, LEDBAT, MulCubic, Minerva, PCP, the BC schemes, Genet, OnlineRL). No covered
  verdict depends on them.
- Many experiments Pramana covers come from papers its implementation was built around (Prudentia,
  CCAnalyzer, vCCAnalyzer, CAKE); `verdicts.csv` lists them.
