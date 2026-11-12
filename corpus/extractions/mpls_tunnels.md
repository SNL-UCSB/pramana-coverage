# mpls_tunnels — Experiment-Set Intent Corpus (v2 render)

## Experiment sets

| ES id | Rendering row | Scope class | Leaves | Iterations/leaf |
| --- | --- | --- | --- | --- |
| mpls_tunnels-ES1 | Exp1 (cross-validation) | OUT-OF-SCOPE: active probing, real Internet | tool ∈ {PyTNT, TNT} = 2 | 3 runs per tool [§3] |
| mpls_tunnels-ES2 | Exp2 (May 2025 Ark 262 VP) | OUT-OF-SCOPE: internet-scale probing campaign | 1 campaign | 1 (continuous, ≈8 h [§4.1]) |
| mpls_tunnels-ES3 | Exp3 (Aug 2025 ITDK) | OUT-OF-SCOPE: internet-scale probing + production ITDK | 1 campaign | 1 (continuous, 2 weeks [§4.1]) |
| mpls_tunnels-ES4 | Exp4 (HDN revelation) | OUT-OF-SCOPE: PyTNT probing from real Internet VPs | 9,239 HDNs [§4.5] | 1 per HDN (no stated repetitions) |
| mpls_tunnels-ES5 | Exp5 (Tier-1 interview) | OUT-OF-SCOPE: qualitative interview, no measurement | n/a | n/a |

## Shared methodology (raw text) (quoted from the paper)


> Measurement tool: PyTNT (Python reimplementation of TNT using scamper's Python bindings) [§3].
> Underlying prober: scamper [§3]. TNT methodology: MPLS detection (FRPLA, RTLA, duplicate-IP, qTTL)
> and revelation (DPR, BRPR) [§2.3, §2.4; §3]. Probes: traceroutes + pings for initial-TTL
> fingerprinting [§3]. Router fingerprinting: (255, 64) TTL-signature technique of Vanaubel et al.
> 2013 [§4.2]. Probing rate: low packet-per-second rates [Appendix A]. Protocol: IPv4 (except
> Table 12 IPv6 analysis in ES3) [§4.6]. Any unspecified field is `Not specified`.


## Experiments

### mpls_tunnels-ES1 — PyTNT vs TNT cross-validation

**(i) Raw text.** From a server at authors' institution, both PyTNT and original TNT probed 660,058
destination IP addresses (one per /24 from RouteViews mapping, March 10, 2025 [§3]). Each tool ran
3 times over the full target set [§3]. Results reported in Table 3.

**(ii) Grammar.** [OUT-OF-SCOPE — active probing of real Internet paths; see design verdict.]
For reference: conceptually ExperimentSet⟨leaves: tool ∈ {PyTNT, TNT} = 2⟩; Workflow = traceroute
+ ping probes to 660,058 live IP addresses; no controllable bottleneck regime.

### mpls_tunnels-ES2 — May 2025 CAIDA Ark 262 VP PyTNT campaign

**(i) Raw text.** PyTNT deployed on all 262 CAIDA Ark vantage points [§4.1]. Bootstrapped from
CAIDA's existing traceroute cycle to 11.9 M routed /24s [§4.1]. Campaign: May 2025 [§4.1], total
probing ≈8 hours [§4.1]. Results: 11.9 M traceroutes; 61.0% (7,056,488) contained at least one
tunnel [§4.1]. Vendor annotation (Table 7): SNMPv3 + light-weight fingerprinting, 346,610 unique
MPLS tunnel IPs, 95,013 identified (49,390 SNMPv3; 45,623 fingerprinting) [§4.2]. AS annotation
(Table 9): bdrmapIT for 86.2% of 206,857 router IPs [§4.3]. Geolocation (Fig 7, Table 11): Hoiho
+ IPinfo for 129,874/201,774 (64.4%) [§4.4].

**(ii) Grammar.** [OUT-OF-SCOPE — internet-scale active measurement; see design verdict.]

### mpls_tunnels-ES3 — August 2025 ITDK campaign

**(i) Raw text.** PyTNT deployed continuously for two weeks to collect data for CAIDA's August 2025
ITDK [§4.1]. Companion ITDK probing: SNMPv3 probes to all inferred router interfaces; ICMP echo
requests for TTL fingerprinting; team-probing traceroutes [§4.2]. Scale: 6,522,537 total tunnels in
ITDK column [Tab 4]; 628,326 IPv4 router interfaces with vendor + TTL signatures [Tab 6]; 68,848 IPv6
router interfaces [Tab 12]. AS annotation (Table 10): bdrmapIT [§4.3]. Geolocation (Fig 8): Hoiho +
IPinfo for 71.2% of 2,848,307 MPLS router IPs [§4.4]. IPv6 tunnel signatures also reported [§4.6].

**(ii) Grammar.** [OUT-OF-SCOPE — continuous internet-scale ITDK production measurement; see design
verdict.]

### mpls_tunnels-ES4 — HDN revelation campaign (March 2025 ITDK seed)

**(i) Raw text.** Using March 2025 ITDK traceroutes as seed, identified 9,239 HDNs (inferred routers
with ≥128 outgoing edges, adjacency rules applied) [§4.5]. For each HDN, used seed traceroutes "as
the seed for PyTNT's analysis" [§4.5] — PyTNT issued additional pings and traceroute probes. Results:
1,623 HDNs as ingress LERs of invisible tunnels, 724 explicit, 196 opaque [§4.5]. HDN definition: ≥128
outgoing edges [§4.5]. Alias resolution: MIDAR, iffinder, SNMPv3 from March 2025 ITDK [§4.5].

**(ii) Grammar.** [OUT-OF-SCOPE — active probing of real Internet HDNs from real VPs; see design
verdict.] Notionally: ExperimentSet⟨leaves: HDN ∈ 9,239 [§4.5]⟩; Workflow = PyTNT probe sequence
per HDN; no controllable bottleneck.

### mpls_tunnels-ES5 — Tier-1 operator interview (text-only, §5)

**(i) Raw text.** Interview with a network operator at a Tier-1 network [§5]. Operator's network is
in the top-ten MPLS operator list (§4.3) and has deployed MPLS for over 25 years [§5]. Five key
takeaways: (1) MPLS in network core, some edge networks IP-only; (2) both PHP and UHP used (UHP
partly legacy, partly to tunnel IPv6 over IPv4); (3) ttl-propagate at vendor defaults; (4) Juniper,
Cisco, Nokia routers; (5) MPLS to route between ASes under organizational control [§5].

**(ii) Grammar.** [OUT-OF-SCOPE — qualitative interview; no measurement campaign; see design verdict.]
