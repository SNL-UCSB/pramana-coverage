#!/usr/bin/env python3
"""Check every citation in the public systems' capability sheets against the pinned commits.

Usage: python3 systems/verify_sheets.py [--cache DIR]
Clones each cited public repository (once, into DIR), and for every evidence entry checks that the file
exists at the pinned commit and contains the cited string, or that a cited commit has the cited message.
Exits 1 if any citation fails. Pramana's sheet states capabilities as interfaces; its implementation is not yet public.
"""
import glob, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
cache = sys.argv[sys.argv.index('--cache') + 1] if '--cache' in sys.argv else os.path.join(HERE, '.repo_cache')
os.makedirs(cache, exist_ok=True)

def git(repo_dir, *args):
    return subprocess.run(['git', '-C', repo_dir, *args], capture_output=True, text=True)

def repo_dir(url):
    d = os.path.join(cache, url.rstrip('/').split('github.com/')[-1].replace('/', '_'))
    if not os.path.isdir(d):
        subprocess.run(['git', 'clone', '-q', url, d], check=True)
    return d

fails = checked = 0
for path in sorted(glob.glob(os.path.join(HERE, '*', 'sheet.json'))):
    sheet = json.load(open(path)); name = os.path.basename(os.path.dirname(path))
    if name == 'pramana':
        continue
    for cap_type, entries in sheet['evidence'].items():
        for e in entries:
            meta = sheet['repos'][e['repo']]; d = repo_dir(meta['url']); checked += 1
            if 'message' in e:
                got = git(d, 'log', '-1', '--format=%s', e['commit']).stdout.strip()
                ok = got == e['message']; what = f"commit {e['commit']} message"
            else:
                src = git(d, 'show', f"{meta['commit']}:{e['path']}")
                ok = src.returncode == 0 and e['contains'] in src.stdout; what = f"{e['path']} @ {meta['commit']}"
            if not ok:
                fails += 1; print(f"FAIL {name} {cap_type}: {what} does not contain {e.get('contains', e.get('message'))!r}")
print(f'{checked} citations checked, {fails} failed')
sys.exit(1 if fails else 0)
