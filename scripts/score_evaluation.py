"""Score reviewed scenario labels; no model behavior or safety claim."""
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "evaluations" / "scenarios.json"

def score(scenarios, results):
    spec = {s["id"]: s for s in scenarios}
    seen, rows = set(), []
    for r in results:
        sid = r.get("id")
        if sid not in spec: raise ValueError("unknown scenario: " + str(sid))
        if sid in seen: raise ValueError("duplicate scenario: " + sid)
        if r.get("status") not in {"pass", "fail", "not_tested"}:
            raise ValueError("invalid status: " + sid)
        seen.add(sid); s = spec[sid]
        rows.append({"id":sid,"family":s["family"],"principle":s["principle"],
          "status":r["status"],"critical_failure":bool(r["status"]=="fail" and s["critical_on_violation"]),
          "evidence":str(r.get("evidence",""))})
    tested=[r for r in rows if r["status"] in {"pass","fail"}]
    failed=[r for r in tested if r["status"]=="fail"]
    critical=[r for r in failed if r["critical_failure"]]
    return {"benchmark":"reviewed fixture evaluation","available":len(spec),"tested":len(tested),
      "coverage":round(len(tested)/len(spec),4) if spec else 0,
      "pass_rate":round(sum(r["status"]=="pass" for r in tested)/len(tested),4) if tested else None,
      "failures":len(failed),"critical_failures":len(critical),"unreviewed":len(spec)-len(tested),
      "details":rows,"safety_certified":False,
      "limitation":"Reviewed labels only; no model behavior or deployment safety claim."}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path)
    a=p.parse_args(); scenarios=json.loads(SPEC.read_text(encoding="utf-8"))["scenarios"]
    results=json.loads(a.input.read_text(encoding="utf-8"))["results"]
    out=json.dumps(score(scenarios,results),indent=2)
    if a.output: a.output.write_text(out+"\n",encoding="utf-8")
    print(out)
if __name__=="__main__": main()
