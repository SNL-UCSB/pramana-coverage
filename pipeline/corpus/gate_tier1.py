#!/usr/bin/env python3
"""Tier-1 mechanical gate for the intent corpus (CORPUS_PROMPT_v4 §5).

Runs the no-judgment checks that used to consume expensive codex review:
  C5  value grounding  — every numeric value with a locator must appear in the
                          paper PDF text (the anti-hallucination check; replaces
                          gold triangulation with a grep).
  G1  leaf arithmetic  — every "a x b x c = N" product must be correct.
  TOK verdict tokens   — design/impl/mininet verdicts from the closed set;
                          OUT-OF-SCOPE design => impl "n/a".
  G2  vocabulary (lite) — flag grammar/field terms not in the v2 menu.

Usage:  python gate_tier1.py papers/<slug>.md [--pdf <path>]
Exit 0 = clean; exit 1 = flags (routes the paper to Tier-2). This is a v1 for
team iteration : it is deliberately conservative — it FLAGS for review,
it does not auto-fail, and every flag names its line so Tier-2 is targeted.
"""
import sys, re, os, subprocess, glob, argparse

# --- v2 grammar vocabulary (Reference Pack item 1); extend as the spec evolves
V2_FIELDS = {
    # bottleneck (Regime)
    "capacity_down","capacity_up","capacity","queue","discipline","size","ecn","mode","pressure","replay","load","ctp",
    # per-workflow path
    "path","latency","jitter","loss","reorder","dup",
    # cca
    "cca","algo","stack","version","params","flags","build",
    # structure
    "workflow","node","role","foreground","iterations","until","event","telemetry","qtrace","pcap","app_metrics",
    "static","dynamic","regime","roles","secrets","leaves","sweep",
}
DESIGN_TOK = {"SATISFIED","GAP-DESIGN","OUT-OF-SCOPE"}
IMPL_TOK   = {"SATISFIED","GAP-IMPL","n/a"}
MININET_TOK= {"M-SAT","M-PARTIAL","M-UNSAT"}

def pdf_text(pdf):
    txt = pdf.rsplit(".",1)[0] + ".txt"
    if not os.path.exists(txt):
        subprocess.run(["pdftotext","-q",pdf,txt],check=False)
    try:
        return open(txt,encoding="utf8",errors="replace").read()
    except OSError:
        return ""

def find_pdf(slug):
    # exact match first (avoids 'pcc' matching 'MPCC.pdf')
    for exact in (f"pdfs/{slug}.pdf",):
        if os.path.exists(exact): return exact
    stem = slug.replace("_","").replace("-","").lower()
    for c in glob.glob("paper_extraction/fig_to_exp/paper_pdf/*.pdf"):
        b = os.path.basename(c).rsplit(".",1)[0].replace("_","").replace("-","").lower()
        if b == stem:              # exact stem, not substring
            return c
    return None

def norm(s):  # normalize numbers for grep: strip commas/spaces
    return re.sub(r"[,\s]","",s.lower())

def check_c5(md, ptext):
    """Every 'NUMBER UNIT [locator]' value should appear in the PDF text."""
    flags=[]; checked=0
    pnorm = norm(ptext)
    # values that carry a locator on the same line
    for i,line in enumerate(md.splitlines(),1):
        if "[" not in line: continue
        # numeric value with unit, followed later by a [locator]
        for m in re.finditer(r"(\d[\d,]*\.?\d*)\s*(mbps|kbps|gbps|ms|s|pkt|packets|bytes|kb|mb|gb|%|bdp)\b", line, re.I):
            val=m.group(1)
            if re.search(r"\[(§|Fig|Tab|Table)[^]]*\]", line):
                checked+=1
                if norm(val) not in pnorm and norm(val+"") not in pnorm:
                    # allow the bare integer/float to appear anywhere
                    if norm(val) not in pnorm:
                        flags.append(f"  L{i}: value '{m.group(0).strip()}' not found in PDF text (possible hallucination)")
    return checked, flags

def check_g1(md):
    """Every 'a x b [x c] = N' product must be correct."""
    flags=[]; checked=0
    for i,line in enumerate(md.splitlines(),1):
        for m in re.finditer(r"((?:\d[\d,]*\s*[×x*]\s*)+\d[\d,]*)\s*=\s*([\d,]+)", line):
            factors=[int(x.replace(",","")) for x in re.findall(r"\d[\d,]*", m.group(1))]
            total=int(m.group(2).replace(",",""))
            if len(factors)>=2:
                checked+=1
                prod=1
                for f in factors: prod*=f
                if prod!=total:
                    flags.append(f"  L{i}: leaf arithmetic '{m.group(0)}' -> product {prod} != {total}")
    return checked, flags

def check_tokens(md):
    """Verdict tokens in-set; OUT-OF-SCOPE design => impl n/a on the same ES row.
    Skips delta/comparison rows (v1->v2 deltas) which are not per-ES verdict rows."""
    flags=[]
    for i,line in enumerate(md.splitlines(),1):
        if re.search(r"\bES\d+\b", line) and line.count("|")>=4:
            # skip delta / comparison / mixed rows — not a clean per-ES verdict
            if re.search(r"→|->|\bvs\b|delta|split|mixed|GAP-DESIGN.*SATISFIED|SATISFIED.*GAP", line, re.I):
                continue
            cells=[c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells)>=4:
                d,im=cells[1],cells[-2]
                # only fire when the design cell is a CLEAN single OUT-OF-SCOPE verdict
                if d.strip() in ("OUT-OF-SCOPE","OUT-OF-SCOPE.") and "n/a" not in im:
                    flags.append(f"  L{i}: design OUT-OF-SCOPE but impl is not n/a ({im[:30]})")
    return flags

ALLOW_SUFFIX = ("_system","_id","_pct","_mbps","_ms","_range","_count","_size","_rate","_filter")
ALLOW_EXTRA  = {"leaf_count","source","local_dir","min_available","host_kernel","flow_size",
                "loss_pct","reorder_pct","dup_pct","capacity_down","capacity_up","ack_filter"}
def check_vocab(md):
    """Lite/advisory: flag snake_case terms used like a top-level grammar field
    that aren't in the v2 menu. Handles nested (a.b) fields by checking the head,
    and allows dict-key / program-name / A5-suffix contexts (these were the FP
    sources in the gold re-render)."""
    flags=[]
    for i,line in enumerate(md.splitlines(),1):
        for m in re.finditer(r"(?<![.\w])([a-z]+_[a-z_]+)\s*[:=]", line):  # not preceded by a dot (nested)
            term=m.group(1)
            head=term.split(".")[0]
            if (term in V2_FIELDS or head in V2_FIELDS or term in ALLOW_EXTRA
                    or term.endswith(ALLOW_SUFFIX)):
                continue
            flags.append(f"  L{i}: '{term}' used as a field but not in v2 vocabulary (verify or map)")
    seen=set(); out=[]
    for f in flags:
        k=f.split("'")[1] if "'" in f else f
        if k not in seen: seen.add(k); out.append(f)
    return out[:15]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("mdfile"); ap.add_argument("--pdf")
    a=ap.parse_args()
    md=open(a.mdfile,encoding="utf8",errors="replace").read()
    # strip the reproduced Tier-1 gate output / red-team log sections: checking
    # them re-flags the gate's own output (paper slugs look like snake_case fields).
    md=re.split(r"(?im)^#{1,3}\s*(tier-1 gate|red-team|gate output|tier1)", md)[0]
    slug=os.path.basename(a.mdfile).rsplit(".",1)[0]
    pdf=a.pdf or find_pdf(slug)
    ptext=pdf_text(pdf) if pdf else ""
    print(f"== Tier-1 gate: {slug} ==  PDF: {pdf or 'NOT FOUND'}")
    total_flags=0
    if ptext:
        n,f=check_c5(md,ptext); total_flags+=len(f)
        print(f"[C5 grounding]  {n} located values checked, {len(f)} flagged"); print("\n".join(f))
    else:
        print("[C5 grounding]  SKIPPED (no PDF text) — Tier-2 must cover grounding")
    n,f=check_g1(md); total_flags+=len(f)
    print(f"[G1 arithmetic] {n} products checked, {len(f)} flagged"); print("\n".join(f))
    f=check_tokens(md); total_flags+=len(f)
    print(f"[TOK verdicts]  {len(f)} flagged"); print("\n".join(f))
    f=check_vocab(md); total_flags+=len(f)
    print(f"[G2 vocab-lite] {len(f)} flagged"); print("\n".join(f))
    print(f"== {'CLEAN' if total_flags==0 else str(total_flags)+' FLAGS -> route to Tier-2'} ==")
    sys.exit(1 if total_flags else 0)

if __name__=="__main__":
    main()
