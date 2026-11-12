#!/usr/bin/env python3
"""Counts under each combination of the three open decisions.

D1  netUnicorn credited for its Containernet connector. An experiment runs on one deployment, so
    netUnicorn covers it through its own connectors OR through Containernet (= Mininet's capabilities).
D2  only code on each system's main branch at 2026-07-17 counts (no unmerged branches).
D3  applications checked by name against each system's workflow inventory (not by type).
"""
import copy, csv, itertools, json
import os
import creation_only as C

BASE = C.load_capabilities()
ROWS = list(csv.DictReader(open(os.path.join(C.ROOT, 'needs', 'needs.csv'))))
MAIN_APPS = ['google-meet', 'puffer', 'roku', 'talky', 'teams', 'tubi', 'twitch', 'youtube', 'zoho', 'zoom']  # origin/main shared/scripts/workflow/*.json
SYS = ['pramana', 'netreplica', 'mininet', 'netunicorn', 'netgent']


def caps_for(d1, d2):
    c = copy.deepcopy(BASE['systems'])
    for k in c: c[k]['_apps'] = BASE['app_inventory'].get(k, [])
    if d2:
        c['pramana']['types'] = [t for t in c['pramana']['types'] if t not in ('PERFLOW:apps', 'XAPP')]
        c['pramana']['_apps'] = MAIN_APPS
        c['netgent']['types'] = [t for t in c['netgent']['types'] if t != 'XAPP']
    if d1:
        c['netunicorn_containernet'] = copy.deepcopy(c['mininet'])
    return c


def count(caps, d3):
    out = {k: 0 for k in SYS}
    for r in ROWS:
        n = C.needs_of(r, [])
        known = [t for t in n if t not in (C.CD, C.OWN)]
        names = C.app_names(r)
        ok = {k: C.CD not in n and all(C.has(cap, t, 'V2' if d3 else 'BASE', names) is True for t in known)
              for k, cap in caps.items()}
        ok['netunicorn'] = ok['netunicorn'] or ok.get('netunicorn_containernet', False)
        for k in SYS: out[k] += ok[k]
    return out


if __name__ == '__main__':
    print(f"{'D1':6s}{'D2':6s}{'D3':6s}  " + '  '.join(f'{k:>10s}' for k in SYS))
    for d1, d2, d3 in itertools.product([False, True], repeat=3):
        o = count(caps_for(d1, d2), d3)
        print(f"{'yes' if d1 else 'no':6s}{'yes' if d2 else 'no':6s}{'yes' if d3 else 'no':6s}  " + '  '.join(f'{o[k]:10d}' for k in SYS))
