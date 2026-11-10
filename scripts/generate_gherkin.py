import argparse, json, re
from pathlib import Path
from ai_client import chat
p=argparse.ArgumentParser(); p.add_argument('--input',required=True); p.add_argument('--output',required=True); a=p.parse_args()
issues=json.loads(Path(a.input).read_text(encoding='utf-8'))
system='You are a senior test engineer. Return only executable Gherkin. Each Scenario or Scenario Outline must have at most 5 step lines. Use Examples tables when useful. Add Jira key tags. Never invent missing rules; use @needs-clarification.'
content=chat(system,json.dumps(issues,ensure_ascii=False)); content=re.sub(r'^```(?:gherkin)?|```$','',content.strip(),flags=re.M)
out=Path(a.output); out.mkdir(parents=True,exist_ok=True); (out/'jira_generated.feature').write_text(content+'\n',encoding='utf-8')
