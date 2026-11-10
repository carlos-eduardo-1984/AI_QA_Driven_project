import argparse, json, os, requests
p=argparse.ArgumentParser(); p.add_argument('--label',required=True); p.add_argument('--out',required=True); a=p.parse_args()
base=os.environ['JIRA_BASE_URL'].rstrip('/')
r=requests.get(base+'/rest/api/3/search/jql', params={'jql':f'labels = "{a.label}" ORDER BY updated DESC','fields':'summary,description,labels,priority','maxResults':100}, auth=(os.environ['JIRA_EMAIL'],os.environ['JIRA_API_TOKEN']), headers={'Accept':'application/json'}, timeout=60)
r.raise_for_status(); issues=[]
for item in r.json().get('issues',[]):
    f=item.get('fields',{}); issues.append({'key':item['key'],'summary':f.get('summary'),'description':f.get('description'),'labels':f.get('labels',[]),'priority':(f.get('priority') or {}).get('name')})
open(a.out,'w',encoding='utf-8').write(json.dumps(issues,ensure_ascii=False,indent=2))
