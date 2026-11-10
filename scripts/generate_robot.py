import argparse
from pathlib import Path
from ai_client import chat
p=argparse.ArgumentParser(); p.add_argument('--features',required=True); p.add_argument('--output',required=True); a=p.parse_args()
source='\n\n'.join(f.read_text(encoding='utf-8') for f in Path(a.features).glob('*.feature'))
system='Convert approved Gherkin to Robot Framework 7. Use Browser Library for UI, RequestsLibrary for API, resources, environment variables, Jira tags, and no secrets. Return files as ### FILE: relative/path.robot followed by content.'
answer=chat(system,source); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); current=None; lines=[]
def save():
    if current:
        target=out/current; target.parent.mkdir(parents=True,exist_ok=True); target.write_text('\n'.join(lines).strip()+'\n',encoding='utf-8')
for line in answer.splitlines():
    if line.startswith('### FILE:'): save(); current=line.split(':',1)[1].strip(); lines=[]
    elif not line.startswith('```'): lines.append(line)
save()
if not current: raise SystemExit('AI response missing ### FILE delimiter')
