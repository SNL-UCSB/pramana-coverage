#!/usr/bin/env python3
"""Creation-only coverage: which systems can, by themselves, create each experiment's conditions.

Inputs:  needs.csv (one verified row per experiment), capabilities.json (cited, per system).
Outputs: verdicts.csv (per experiment, per system, with reasons), summary.json.
Usage:   python3 creation_only.py [--variant V1|V2|V3|V4|V5] [--needs FILE]

A pure function of its two inputs: no sampling, thresholds, or reading of paper text. Each needs
value is mapped to a capability type by the ordered pattern tables below (first match wins). A value
that matches no pattern stops the run, so nothing is dropped silently. README.md states the rule.
"""
import csv, json, os, re, sys
from collections import Counter

NEED_FIELDS = ['topology', 'bottleneck', 'capacity_variation', 'cross_traffic', 'queue_discipline',
               'per_flow_path', 'applications', 'congestion_control', 'infrastructure']
CD = 'CD'      # the paper does not settle this value
OWN = 'OWN'    # the paper's own software: the thing under test, not a condition (README, convention 2)
NO = None      # no need

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_capabilities():
    """Assemble the per-system capability sheets (systems/<name>/sheet.json) into one table."""
    import glob as _g
    systems, inv = {}, {}
    order = ['pramana', 'netreplica', 'mininet', 'netunicorn', 'netgent']
    for path in sorted(_g.glob(os.path.join(ROOT, 'systems', '*', 'sheet.json')), key=lambda x: order.index(os.path.basename(os.path.dirname(x)))):
        k = os.path.basename(os.path.dirname(path)); sh = json.load(open(path))
        cites = dict(sh.get('evidence') or sh.get('interfaces') or {})
        systems[k] = {'name': sh['system'], 'types': sh['types'], 'qdiscs': sh['qdiscs'], 'kernel_ccas': sh['kernel_ccas'],
                      'kset15_is_ccanalyzer': sh.get('kset15_is_ccanalyzer', False), '_cite': cites}
        inv[k] = sh.get('app_inventory', [])
    return {'systems': systems, 'app_inventory': inv}


KERNEL = ['bbr', 'bic', 'cdg', 'cubic', 'dctcp', 'highspeed', 'htcp', 'hybla', 'illinois', 'lp', 'nv',
          'reno', 'scalable', 'vegas', 'veno', 'westwood', 'yeah']   # Linux mainline TCP modules

QDISC = [  # (pattern, token)
    (r'cannot-determine|others not specified', CD), (r"paper'?s own", OWN),
    (r'^default$|^fifo$|^tdrop$|token bucket|\btbf\b', 'QDISC:default'),   # drop-tail; tbf is the shaper
    (r'802\.11e|wmm', NO),                                # part of the Wi-Fi AP (infrastructure need)
    (r'cake', 'QDISC:cake'), (r'fq_codel', 'QDISC:fq_codel'), (r'^codel$', 'QDISC:codel'),
    (r'^pie$', 'QDISC:pie'), (r'^red$', 'QDISC:red'), (r'ecn marking', 'QDISC:ecn'),
    (r'^fq\b', 'QDISC:fq'), (r'^drr$', 'QDISC:drr'), (r'^hdrop$', 'QDISC:pfifo_head_drop'),
    (r'^bode$|^one-hop$', 'CUSTOM_QDISC'),               # research schedulers, not Linux qdiscs
]
CCA = [
    (r'cannot-determine', CD), (r"paper'?s own", OWN),
    (r'^not set|observed-remote|^tcp$|^tcp with sack|variant not specified|\bgcc\b|non-adaptive|constant-rate', NO),
    (r'bursty aggregate not specified|other schemes|legend schemes', CD),   # schemes the text does not name
    (r'chrome/firefox builds', NO),                      # the browser's own QUIC, part of the application
    (r'kernel ccas \(count not stated\)', CD),
    (r'^\d+ (built-in )?linux', 'KSET:'),                # N kernel algorithms, not named one by one
    (r'^sage-(s|m|l|top4?)$', OWN),                      # retrained variants of the paper's own Sage
    (r'quic stack|copa|vivace|\bpcc\b|pcc[-_]|indigo|aurora|sprout|sabul|genet|onlinerl|minerva|ledbat|'
     r'^pcp$|\bbc\b|bcv2|bc-top|mulcubic|astraea|^sage$|taova', 'USERSPACE_SW'),   # user-space stacks: programs on an endpoint
    (r'dcqcn', 'SPECIAL_HW'),                            # runs in RDMA NICs
    (r'on linux \d+\.\d+|bbr ?v?2|bbr2|bbr ?v3|bbr-v2|mptcp|^lia$|^olia$|^balia$|^wvegas$|^ecf$|daps|blest|'
     r'schedulers|cwndgain|modified kernel|orca|deepcc|c2tcp', 'KERNEL_BUILD'),   # needs a different kernel
    (r'hystart disabled|^ecn-based (dctcp|cubic)$', 'SYSCTL'),   # one kernel setting on a stock kernel
    (r'^paced new ?reno$', 'KCCA:reno'),
    (r'^(?:cross: |competitor: )?(new ?reno|reno)$', 'KCCA:reno'),
    (r'^(?:cross: |competitor: )?(' + '|'.join(KERNEL) + r')(?: \(v1\))?$', 'KCCA:'),
]
APP = [
    (r'cannot-determine \(bulk transfer flow\)', 'TOOLS'),   # same need as 'large-file download (tool not stated)'
    (r'cannot-determine|webrtc-(cm|t|v)$', CD),
    (r'chrome browser plugin', 'APP'),                   # NDT7 run inside Chrome: browser automation          # WebRTC-CM/T/V: the source does not say who built them
    (r'^chrom(e|ium)( \d+)? page loads?', 'APP'),        # a Chrome page load is browser use even with the paper's loader
    (r"paper'?s own|custom abr|siploader|kwikr|j-qos|over icn", OWN),   # each is the paper's own system
    (r'^none$|camera streams|counterfactual|^10-min video|channel access delay estimator', NO),   # parameters or analysis
    (r'pensieve|fugu|vroom|fawkes|mpc abr|random bitrate', 'APP'),   # research players/loaders run in a browser: browser automation
    (r'panda|adaptech|libdash|huang et al|gordon|inspector gadget|ig crawler|'
     r'streamtheater|customized|cgreplay', 'USERSPACE_SW'),       # research prototypes from other papers
    (r'^tcp$|^http \d|paced udp|websearch workload|traces$|tslp|bdrmap|findcdn|mobileinsight', 'TOOLS'),
    (r'^tool-only|tcpdump|^curl|^iperf|^ping|rtt measurement|^srtt$|icmp echo|traceroute|scamper|snmp|'
     r'harpoon|h2load|^ss$|apache|web server|large-file download|perftest|netperf|wget|speed ?test|dns', 'TOOLS'),
    (r'pensieve|fugu|vroom|fawkes|mpc abr|random bitrate', 'APP'),   # research players/loaders run in a browser: browser automation
    (r'nas abr|imdn|m-tput|m-rtp', 'USERSPACE_SW'),   # research prototypes run as programs on an endpoint
    (r'exoplayer', 'ANDROID_APP'),                       # ExoPlayer is an Android-only library
    (r'.', 'APP'),                                       # any other named real application
]
INFRA = [
    (r'cannot-determine', CD),
    (r'rdma|tofino|smartnic|usrp|openairinterface|5g sa testbed|25 gbps|physical datacenter', 'SPECIAL_HW'),
    (r'^ecmp$', NO),                                     # a routing feature of the multi-node topology
    (r'caida ark|ripe atlas|speedchecker|scion|sciera|vpn|^germany$|^india$', 'WAN_PLATFORM'),  # DE/IN: VPN exits
    (r'campus network|observation node', 'OPERATOR_VANTAGE'),
    (r'users in|real clients|user devices', 'REAL_USERS'),
    (r'phones/devices laptops', 'LOCAL'),                # laptops; the access network is its own item
    (r'phone tethered', 'ACCESS'),                       # the phone is the host's cellular uplink
    (r'phone|android|iphone|ipad|tablet|playstation|nexus|pixel|samsung|gear vr', 'DEVICES'),
    (r'cellular|t-mobile|wi-?fi|residential|access networks?|^5g$|raspberry pi', 'ACCESS'),
    (r'^public internet target', 'INET'),
    (r'\baws\b|amazon|^(london|frankfurt|tokyo|n\. california|sao paulo)$', 'CLOUD:aws'),
    (r'azure|^microsoft$', 'CLOUD:azure'),
    (r'\bgcp\b|^google$|^(us|europe)-[a-z]+\d', 'CLOUD:gcp'),
    (r'alibaba|^(tyo|sv)$|^ws\d', 'CLOUD:alibaba'),
    (r'digital ?ocean|^(ams3|blr1|fra1|lon1|sfo2|sgp1|toronto)$', 'CLOUD:digitalocean'),
    (r'cloud(?!lab)', 'CLOUD:unnamed'),
    (r'\bgeni\b|fabric|planetlab|icsi|georgia tech|authors\' servers|eth zurich|'
     r'different cloudlab region|^client in hk$', 'REMOTE_HOSTS'),   # wide-area paths between sites
    (r'public internet|m-lab|dns resolvers', 'INET'),
    (r'local emulation|\blab\b|emulab|cloudlab|geni|pc-3|workstation|mac ?mini|macbook|windows|'
     r'desktop|laptop|hardware testbed|sdsc', 'LOCAL'),   # Emulab/CloudLab: emulated links on cluster nodes
]


def parts(v):
    return [p.strip() for p in re.split(r';(?![^()]*\))', v or '') if p.strip()]


VALUE_MAP = {}
TOOLPAT = [(r'iperf|^tcp$|paced udp', 'iperf'), (r'ping|icmp echo|rtt measurement|srtt', 'ping'),
           (r'wget|http \d|large-file download|bulk transfer', 'wget'), (r'curl', 'curl'), (r'tcpdump|tshark', 'capture'),
           (r'speed ?test', 'speedtest'), (r'ndt', 'ndt'), (r'tcpreplay|traces$', 'tcpreplay'),
           (r'traceroute|scamper|tnt', 'traceroute'), (r'netperf', 'netperf'), (r'flent', 'flent'), (r'h2load', 'h2load'),
           (r'dns', 'dns'), (r'apache|web server', 'httpserver'), (r'snmp', 'snmp'), (r'harpoon|websearch', 'flowgen'),
           (r'perftest', 'perftest'), (r'^ss$', 'ss'),
           (r'tslp|bdrmap|findcdn|mobileinsight|ripe atlas|speedchecker|latency probes', 'measurement-tool')]


def tool_name(value):
    low = value.lower()
    return next((nm for pat, nm in TOOLPAT if re.search(pat, low)), 'unnamed')


def classify(value, table, field, es, unmapped):
    out = set()
    for p in parts(value):
        low = re.sub(r'\s*\(.*', '', p).strip().lower() or p.lower()
        for pat, tok in table:
            if re.search(pat, low) or re.search(pat, p.lower()):   # with or without the parenthetical
                if tok == 'KSET:':
                    tok = 'KSET:' + re.match(r'\d+', low).group(0)
                if tok == 'KCCA:':
                    tok = 'KCCA:' + re.search('|'.join(KERNEL), low).group(0)
                if tok == 'TOOLS':
                    tok = 'TOOL:' + tool_name(p)
                VALUE_MAP[(field, p)] = 'no need' if tok is NO else tok
                if tok is not NO:
                    out.add(tok)
                break
        else:
            unmapped.append((field, p, es))
    return out


WHERE = {'CLOUD', 'REMOTE_HOSTS', 'ACCESS', 'WAN_PLATFORM', 'REAL_USERS', 'OPERATOR_VANTAGE'}   # where it ran


def needs_of(r, unmapped):
    es, n = r['es_id'], set()
    one = lambda f: r[f].split(' ')[0].split(';')[0].strip().lower()
    if one('topology') == 'cannot-determine': n.add(CD)
    elif r['topology'].lower().startswith('multi'): n.add('TOPO')
    b = r['bottleneck'].strip().lower()
    if b.startswith('cannot-determine'): n.add(CD)
    elif b.startswith('shaped') or (b and not b.startswith('none')):
        n.add('SHAPE')
        if re.search(r'gilbert|markov|burst loss', b): n.add('BURSTLOSS')
        if re.search(r'(?<!zero )\bloss\b', b) and not re.search(r'burst loss', b): n.add('LOSS')
        if re.search(r'(?<!throughput )jitter', b): n.add('JITTER')
        if re.search(r'netem reordering', b): n.add('REORDER')
        if re.search(r'time-varying|per-second|varied at random', b) and re.search(r'latency|rtt|loss', b): n.add('PATHVAR')
    cv = r['capacity_variation'].lower()
    if 'cannot-determine' in cv: n.add(CD)
    else:
        if 'capacity-trace' in cv: n.add('CAPVAR:trace')          # recorded time-varying capacity
        if 'synthetic-schedule' in cv: n.add('CAPVAR:schedule')   # programmed steps or schedule
    ct = r['cross_traffic'].lower()
    if 'cannot-determine' in ct: n.add(CD)
    n |= {t for k, t in (('generated', 'XGEN'), ('cross-traffic-trace', 'XTRACE'), ('real-app', 'XAPP')) if k in ct}
    if one('per_flow_path') == 'yes': n.add('PERFLOW')   # refined below: browser apps only, or any traffic
    elif one('per_flow_path') == 'cannot-determine': n.add(CD)
    n |= classify(r['queue_discipline'], QDISC, 'queue_discipline', es, unmapped)
    n |= classify(r['applications'], APP, 'applications', es, unmapped)
    n |= classify(r['congestion_control'], CCA, 'congestion_control', es, unmapped)
    infra = classify(r['infrastructure'], INFRA, 'infrastructure', es, unmapped)
    if 'SHAPE' in n:   # the experiment sets its own link conditions: where it ran does not matter (convention 6)
        infra = {t for t in infra if t.split(':')[0] not in WHERE and t != CD} | {'LOCAL'}
    n |= infra
    if 'TOPO' in n and 'SHAPE' not in n:   # unshaped: the paths are the real infrastructure, counted there (convention 6)
        n.discard('TOPO')
    if 'PERFLOW' in n:   # generated or tool flows that need their own delay need per-flow paths for any traffic
        n.discard('PERFLOW'); n.add('PERFLOW:any' if 'XGEN' in n or any(t.startswith('TOOL:') for t in n) else 'PERFLOW:apps')
    if n & {'TOOL:iperf'} and not n & {'APP', 'XAPP', 'USERSPACE_SW'} and not any(t.startswith('TOOL:') and t != 'TOOL:iperf' for t in n):
        n = {('KCCA_IPERF:' + t[5:]) if t.startswith('KCCA:') else t for t in n}   # every sender is iperf: iperf3 -C sets it per socket
    if 'TOOL:ping' in n and 'INET' in n:                # pinging public targets, not hosts inside an emulation
        n.discard('TOOL:ping'); n.add('TOOL:ping-inet')
    n.discard('QDISC:default')                           # every system leaves the default in place
    if n & {'KCCA:cubic'} == n & {t for t in n if t.startswith('KCCA:')} and 'KCCA:cubic' in n:
        n.discard('KCCA:cubic')                          # Cubic alone is Linux's default (convention 5)
    return n


def has(cap, t, variant, app_names):
    if t.startswith('QDISC:'): return t[6:] in cap['qdiscs']
    if t.startswith('KCCA:'): return t[5:] in cap['kernel_ccas']
    if t.startswith('KCCA_IPERF:'): return t[11:] in cap['kernel_ccas'] or 'TOOL:iperf' in cap['types']   # iperf3 -C <algo>
    if t == 'PERFLOW:apps': return bool({'PERFLOW:apps', 'PERFLOW:any'} & set(cap['types']))
    if t.startswith('KSET:'):                            # N unnamed kernel algorithms
        k = int(t[5:])
        if len(cap['kernel_ccas']) < k: return False
        return True if k == 15 and cap.get('kset15_is_ccanalyzer') else None
    if t == 'APP' and variant == 'V2': return bool(app_names) and app_names <= set(cap.get('_apps', []))
    if t == 'ACCESS' and variant == 'V4': return False
    if t == 'CLUSTER': return 'REMOTE_HOSTS' in cap['types']
    return t in cap['types']


APPNAME = [(r'youtube', 'youtube'), (r'zoom', 'zoom'), (r'meet', 'google-meet'), (r'teams', 'teams'),
           (r'twitch', 'twitch'), (r'puffer', 'puffer'), (r'webex', 'webex'), (r'jitsi', 'jitsi'),
           (r'hulu', 'hulu'), (r'disney', 'disney-plus'), (r'tiktok', 'tiktok'), (r'reddit', 'reddit')]


def app_names(r):
    names = set()
    for p in parts(r['applications']):
        if re.search(r"tool-only|paper'?s own|^none$|cannot-determine", p, re.I): continue
        hit = [nm for pat, nm in APPNAME if re.search(pat, p, re.I)]
        names |= set(hit) if hit else {'other:' + p.lower()[:40]}
    return names


def main():
    args = sys.argv[1:]
    variant = args[args.index('--variant') + 1] if '--variant' in args else 'BASE'
    needs_file = args[args.index('--needs') + 1] if '--needs' in args else os.path.join(ROOT, 'needs', 'needs.csv')
    caps = load_capabilities()
    systems = caps['systems']
    for k, s in systems.items():                          # self-check: every credited type is cited
        missing = [t for t in s['types'] + (['qdiscs'] if s['qdiscs'] else []) + (['kernel_ccas'] if s['kernel_ccas'] else [])
                   if t not in s['_cite'] and not (t.startswith('TOOL:') and 'TOOL:*' in s['_cite'])]
        missing = [m for m in missing if m != 'kernel_ccas' or 'kernel_ccas' in s['_cite']]
        if missing: sys.exit(f'{k}: capability without citation: {missing}')
        s['_apps'] = caps['app_inventory'].get(k, [])
    rows = list(csv.DictReader(open(needs_file)))
    ids = [r['es_id'] for r in rows]
    if len(ids) != len(set(ids)): sys.exit('duplicate es_id in needs table')
    unmapped, out = [], []
    for r in rows:
        n = needs_of(r, unmapped)
        if variant == 'V3' and 'LOCAL' in n and re.search(r'emulab|cloudlab|geni', r['infrastructure'], re.I):
            n = (n - {'LOCAL'}) | {'CLUSTER'}
        if variant == 'V5' and OWN in n: n.add('OWN_UNMET')
        known = sorted(t for t in n if t not in (CD, OWN))
        cd_fields = [f for f in NEED_FIELDS if 'cannot-determine' in r[f].lower()] if CD in n else []
        row = {'es_id': r['es_id'], 'needs': ' '.join(known) + (' +cannot-determine' if CD in n else ''),
               'unsettled_fields': ' '.join(cd_fields) or ('see notes' if CD in n else '')}
        names = app_names(r)
        for k, cap in systems.items():
            res = {t: has(cap, t, variant, names) for t in known}
            miss = [t for t, v in res.items() if v is False]
            undecided = CD in n or any(v is None for v in res.values())
            row[k] = 'NOT COVERED' if miss else ('CANNOT-DETERMINE' if undecided else 'COVERED')
            row[k + '_missing'] = ' '.join(miss)
        out.append(row)
    if unmapped:
        for f, p, es in unmapped: print(f'UNMAPPED {f}: {p!r} ({es})')
        sys.exit(f'{len(unmapped)} unmapped values; extend the pattern tables')
    suffix = '' if variant == 'BASE' else '_' + variant
    if variant == 'BASE':
        with open(os.path.join(ROOT, 'results', 'value_map.csv'), 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['field', 'value', 'type'])
            w.writerows(sorted((f, v, t) for (f, v), t in VALUE_MAP.items()))
    with open(os.path.join(ROOT, 'results', f'verdicts{suffix}.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    summary = {k: dict(Counter(r[k] for r in out)) for k in systems}
    json.dump({'variant': variant, 'experiments': len(out), 'summary': summary}, open(os.path.join(ROOT, 'results', f'summary{suffix}.json'), 'w'), indent=1)
    print(f'{variant}: {len(out)} experiments')
    for k in systems:
        c = summary[k]
        print(f"  {systems[k]['name'][:44]:44s} covered {c.get('COVERED', 0):3d} ({100 * c.get('COVERED', 0) / len(out):4.1f}%)"
              f"  cannot-determine {c.get('CANNOT-DETERMINE', 0):3d}  not {c.get('NOT COVERED', 0):3d}")


if __name__ == '__main__':
    main()
