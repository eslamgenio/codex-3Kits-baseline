"""Validate this reusable baseline; does not test application behavior."""
import argparse, collections, hashlib, json, pathlib, re, sys
import yaml
def validate(root):
 root=pathlib.Path(root).resolve()
 errors=[];warnings=[];counts=collections.Counter()
 catalog=json.loads((root/".agents/skill-catalog.json").read_text(encoding="utf-8"))
 entries=catalog["skills"];names=set()
 for e in entries:
  p=root/e["path"];name=e["name"];counts[e["family"]]+=1
  if name in names:errors.append("Duplicate skill "+name)
  names.add(name)
  if not p.is_file():errors.append("Missing entrypoint "+str(p));continue
  text=p.read_text(encoding="utf-8")
  m=re.match(r"\A---\s*\n(.*?)\n---\s*\n",text,re.S)
  if not m:errors.append("Invalid frontmatter "+e["path"]);continue
  try:meta=yaml.safe_load(m.group(1))
  except yaml.YAMLError as exc:errors.append("Invalid YAML "+e["path"]+": "+str(exc));continue
  if meta.get("name")!=name or p.parent.name!=name:errors.append("Name mismatch "+name)
  if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name) or len(name)>64:errors.append("Invalid skill name "+name)
  if not isinstance(meta.get("description"),str) or not meta["description"].strip():errors.append("Missing description "+name)
  if "disable-model-invocation" in meta:errors.append("Host-specific invocation field "+name)
  ui=p.parent/"agents/openai.yaml"
  if not ui.exists():errors.append("Missing UI metadata "+name);continue
  u=yaml.safe_load(ui.read_text(encoding="utf-8"))
  if u.get("policy",{}).get("allow_implicit_invocation") != (not e["explicit_only"]):errors.append("Invocation policy changed "+name)
  if "$"+name not in u.get("interface",{}).get("default_prompt",""):errors.append("Wrong default prompt "+name)
  for md in p.parent.rglob("*.md"):
   body=md.read_text(encoding="utf-8")
   visible=[];fence_marker=None
   for line in body.splitlines():
    fence=re.match(r"^[ \\t]*(`{3,}|~{3,})",line)
    if fence:
     mark=fence.group(1)[0]
     if fence_marker is None:fence_marker=mark
     elif fence_marker==mark:fence_marker=None
     continue
    if fence_marker is None:visible.append(line)
   body="\n".join(visible)
   body=re.sub(r"(`+).*?\1","",body)
   for target in re.findall(r"\]\(([^)\n]+)\)",body):
    t=target.split("#",1)[0].strip()
    if not t or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",t) or t.startswith(("#","<")) or any(x in t for x in (" ","{","}","<",">")):continue
    resolved=(md.parent/t).resolve()
    if not resolved.exists():warnings.append(str(md.relative_to(root))+" -> "+t)
  if e["experimental"] and not meta["description"].startswith("Experimental"):errors.append("Experimental status lost "+name)
 discovered={p.parent.name for p in (root/".agents/skills").glob("*/SKILL.md")}
 if discovered!=names:errors.append("Discovery catalog mismatch: "+repr(discovered.symmetric_difference(names)))
 all_discovered=list(root.rglob("SKILL.md"))
 # Non-active SKILL.md files would be accidentally offered by broad installers.
 if len(all_discovered)!=len(entries):errors.append("Unexpected additional SKILL.md files")
 for rel,want in catalog["source_files"].items():
  p=root/rel
  if not p.exists():errors.append("Missing source snapshot "+rel);continue
  if hashlib.sha256(p.read_bytes()).hexdigest()!=want:errors.append("Changed source snapshot "+rel)
 for lib in catalog["libraries"]:
  if not any((root/"licenses").glob(lib+"-*")):errors.append("Missing license "+lib)
 for required in ("AGENTS.md","README.md","PROJECT.md","docs/WORKFLOW.md","docs/SKILLS.md","docs/UPSTREAM.md",".agents/CODEX-COMPATIBILITY.md"):
  if not (root/required).is_file():errors.append("Missing baseline document "+required)
 for forbidden in (".cursor",".claude"):
  if (root/forbidden).exists():errors.append("Unexpected active host integration "+forbidden)
 return {"skills":len(entries),"families":dict(counts),"source_snapshots":len(catalog["source_files"]),"errors":errors,"unresolved_local_links":sorted(set(warnings))}
if __name__=="__main__":
 parser=argparse.ArgumentParser();parser.add_argument("root",nargs="?",default=str(pathlib.Path(__file__).resolve().parents[1]));parser.add_argument("--json",action="store_true")
 args=parser.parse_args();result=validate(args.root)
 if args.json:print(json.dumps(result,indent=2))
 else:
  print("Skills:",result["skills"],result["families"])
  print("Source snapshots:",result["source_snapshots"])
  for e in result["errors"]:print("ERROR:",e)
  for w in result["unresolved_local_links"]:print("UNRESOLVED:",w)
  print("Structural result:","PASS" if not result["errors"] and not result["unresolved_local_links"] else "FAIL")
 sys.exit(1 if result["errors"] or result["unresolved_local_links"] else 0)
