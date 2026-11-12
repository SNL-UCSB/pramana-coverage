#!/usr/bin/env python3
"""Name the artifacts each experiment Pramana does not cover is missing, and rank additions by greedy set cover.

Reads results/verdicts.csv (from creation_only.py) and needs/needs.csv. For every NOT COVERED experiment it takes
each missing capability type, finds the needs values behind it, and maps each value to a named artifact with the
ordered table ARTIFACT below (first match wins; an unmatched value stops the run). Structural types (TOPO, ...)
map to one artifact each. Writes results/pramana_gap_artifacts.csv (es_id, type, value, artifact) and
results/pramana_gap_cover.csv (greedy order: the addition that newly covers the most experiments first).
An experiment counts as unblocked only when every one of its missing artifacts has been added.
CANNOT-DETERMINE experiments with no missing type are reported separately: no addition settles them.
"""
import csv, os, re, sys
import creation_only as C

ROOT = C.ROOT
ARTIFACT = [  # (pattern on the needs value, artifact name)
    (r'bbr ?v?3|bbrv3', 'BBRv3 kernel'), (r'bbr ?v?2|bbr2|bbr-v2', 'BBRv2 kernel'),
    (r'mptcp|^lia$|^olia|^balia|wvegas|^ecf$|daps|blest|scheduler', 'out-of-tree MPTCP kernel'),
    (r'deepcc', 'DeepCC kernel patch'), (r'orca', 'Orca kernel patch'), (r'c2tcp', 'C2TCP kernel patch'), (r'cwndgain', 'modified BBR kernel'),
    (r'on linux \d', 'specific kernel version'), (r'hystart', 'HyStart setting'), (r'ecn-based (dctcp|cubic)', 'host ECN setting'),
    (r'\d+ stacks|implementation set|pairwise of \d+', ['mvfst', 'chromium', 'msquic', 'quiche', 'lsquic', 'quic-go', 'quicly', 'quinn', 's2n-quic', 'xquic', 'neqo']),   # cambrian_quic Table 1: 11 stacks at pinned commits
    (r'quic stack (\w+)', None),  # named QUIC stack: artifact = 'QUIC stack: <name>'
    (r'vivace|\bpcc\b|pcc[-_]', 'PCC (user-space)'), (r'copa', 'Copa'), (r'indigo', 'Indigo'),
    (r'aurora', 'Aurora'), (r'genet', 'Genet'), (r'onlinerl', 'OnlineRL'), (r'sprout', 'Sprout'), (r'sabul', 'SABUL (UDT)'),
    (r'ledbat', 'LEDBAT'), (r'\bbc\b|bcv2|bc-top', 'BC schemes'), (r'astraea', 'Astraea'), (r'minerva', 'Minerva'),
    (r'mulcubic', 'MulCubic'), (r'^pcp$', 'PCP'), (r'taova', 'TaoVA (Remy)'), (r'^sage', 'Sage'),
    (r'panda', 'PANDA player'), (r'adaptech', 'Adaptech player'), (r'huang et al', 'BBA player (Android)'), (r'libdash', 'BBA player (libdash)'),
    (r'gordon', 'Gordon'), (r'inspector gadget|ig crawler', 'Inspector Gadget'), (r'cgreplay', 'CGReplay'),
    (r'nas abr|imdn', 'NAS ABR'), (r'streamtheater', 'StreamTheater'), (r'm-tput', 'M-TPUT probe'), (r'm-rtp', 'M-RTP probe'),
    (r'customized', 'customized Puffer'), (r'exoplayer', 'Android app automation (ExoPlayer)'),
    (r'usrp|openairinterface|5g sa', 'software-defined LTE/5G radio'), (r'tofino', 'Tofino switches'), (r'smartnic', 'SmartNIC'), (r'rdma', 'RDMA NIC testbed'),
    (r'25 gbps|datacenter', 'datacenter hardware fabric'),
    (r'ripe atlas', 'RIPE Atlas'), (r'caida ark', 'CAIDA Ark'), (r'speedchecker', 'Speedchecker'),
    (r'scion|sciera', 'SCION'), (r'vpn|^germany$|^india$|^us$', 'VPN exits'),
    (r'\btv\b|playstation', 'TVs and consoles'), (r'iphone|ipad', 'iOS devices'), (r'tablet|smartphones', 'phones and tablets'),
    (r'android|nexus|pixel|samsung|phone|gear vr', 'Android phones'),
    (r'cellular|lte|t-mobile|verizon|at&t|sprint|tethered|^5g$', 'cellular access connector'),
    (r'wi-?fi|access gateway|aps\b|access networks', 'Wi-Fi access connector'),
    (r'residential|home|household|raspberry pi', 'residential vantage points'),
    (r'users in|real clients|user devices', 'real users'), (r'campus|observation node', 'operator vantage point'),
    (r'aws|amazon|london|frankfurt|tokyo|california|sao paulo', 'cloud backend: AWS'), (r'azure|microsoft', 'cloud backend: Azure'),
    (r'gcp|google|us-|europe-', 'cloud backend: GCP'), (r'alibaba|^tyo$|^sv$|^ws\d', 'cloud backend: Alibaba'),
    (r'digital ?ocean|ams3|blr1|fra1|lon1|sfo2|sgp1|toronto', 'cloud backend: DigitalOcean'), (r'cloud', 'cloud backend (unnamed)'),
    (r'geni|fabric|planetlab|icsi|georgia tech|authors|eth zurich|cloudlab region|client in hk', 'remote-host (SSH) connector'),
    (r'bode|one-hop', 'research queue scheduler'),
]
STRUCT = {'TOPO': 'several shaped links', 'PERFLOW:any': 'per-flow delay for generated and tool flows',
          'XAPP': 'concurrent application workflows', 'APP': 'application workflow', 'CAPVAR:trace': 'capacity trace replay',
          'CAPVAR:schedule': 'capacity schedule', 'PATHVAR': 'delay/loss schedule', 'XGEN': 'generated competing traffic',
          'XTRACE': 'cross-traffic replay', 'SHAPE': 'bottleneck shaping'}
FIELD_OF = {'KERNEL_BUILD': 'congestion_control', 'USERSPACE_SW': None, 'SYSCTL': 'congestion_control', 'HOST_ECN': 'congestion_control',
            'KERNEL_VERSION': 'congestion_control', 'ANDROID_APP': 'applications', 'CUSTOM_QDISC': 'queue_discipline'}
TABLES = {'congestion_control': C.CCA, 'applications': C.APP, 'queue_discipline': C.QDISC, 'infrastructure': C.INFRA}


def artifact(value):
    """Names of the additions behind one needs value: one build, connector, workflow, or substrate capability each."""
    low = value.lower()
    for pat, name in ARTIFACT:
        m = re.search(pat, low)
        if m:
            if isinstance(name, list): return ['QUIC stack: ' + x for x in name]
            return [name or 'QUIC stack: ' + m.group(1).replace('quicgo', 'quic-go')]
    sys.exit(f'no artifact name for value {value!r}; extend ARTIFACT')


def main():
    needs = {r['es_id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'needs', 'needs.csv')))}
    rows, blocked, cd_only = [], {}, []
    for v in csv.DictReader(open(os.path.join(ROOT, 'results', 'verdicts.csv'))):
        miss = v['pramana_missing'].split()
        if v['pramana'] == 'CANNOT-DETERMINE' and not miss: cd_only.append(v['es_id']); continue
        if v['pramana'] != 'NOT COVERED': continue
        r, arts = needs[v['es_id']], set()
        for t in miss:
            if t in STRUCT: rows.append((v['es_id'], t, '', STRUCT[t])); arts.add(STRUCT[t]); continue
            if t.startswith('KSET:'): a = f'{t[5:]} stock kernel algorithms'; rows.append((v['es_id'], t, '', a)); arts.add(a); continue
            if t.startswith('KCCA:'): a = 'kernel module: ' + t[5:]; rows.append((v['es_id'], t, t[5:], a)); arts.add(a); continue
            fields = [FIELD_OF[t]] if FIELD_OF.get(t) else (['congestion_control', 'applications'] if t == 'USERSPACE_SW' else ['infrastructure'])
            found = False
            for f in fields:
                for p in C.parts(r[f]):
                    if t in C.classify(p, TABLES[f], f, v['es_id'], []):
                        for a in artifact(p): rows.append((v['es_id'], t, p, a)); arts.add(a)
                        found = True
            if not found: rows.append((v['es_id'], t, '', t)); arts.add(t)
        blocked[v['es_id']] = arts
    with open(os.path.join(ROOT, 'results', 'pramana_gap_artifacts.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['es_id', 'type', 'value', 'artifact']); w.writerows(sorted(set(rows)))
    added, order, left = set(), [], dict(blocked)
    while left:
        cand = {a for arts in left.values() for a in arts} - added
        best = max(sorted(cand), key=lambda a: sum(arts <= added | {a} for arts in left.values()))
        gain = [e for e, arts in left.items() if arts <= added | {best}]
        if not gain:   # no single addition unblocks anything: take the most frequent artifact
            best = max(sorted(cand), key=lambda a: sum(a in arts for arts in left.values())); gain = []
        added.add(best); order.append((best, len(gain), sum(best in a for a in blocked.values())))
        for e in gain: left.pop(e)
    with open(os.path.join(ROOT, 'results', 'pramana_gap_cover.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['rank', 'artifact', 'newly_unblocked', 'cumulative_unblocked', 'experiments_needing_it'])
        cum = 0
        for i, (a, g, n) in enumerate(order, 1): cum += g; w.writerow([i, a, g, cum, n])
    print(f'{len(blocked)} NOT COVERED experiments, {len({a for s in blocked.values() for a in s})} distinct artifacts; '
          f'{len(cd_only)} CANNOT-DETERMINE with every determinable need met (no addition settles them)')


if __name__ == '__main__':
    main()
