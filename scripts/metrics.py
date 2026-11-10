import json, sys
from pathlib import Path
from xml.etree import ElementTree as ET
root=ET.parse(sys.argv[1]).getroot(); stat=root.find('./statistics/total/stat')
passed=int(stat.attrib.get('pass','0')); failed=int(stat.attrib.get('fail','0')); skipped=int(stat.attrib.get('skip','0')); total=passed+failed+skipped
critical=sum(1 for t in root.findall('.//test') if t.find('status') is not None and t.find('status').attrib.get('status')=='FAIL' and 'critical' in [x.text for x in t.findall('./tags/tag')])
data={'total':total,'passed':passed,'failed':failed,'skipped':skipped,'pass_rate':round(passed/total*100 if total else 0,2),'critical_failures':critical}
Path(sys.argv[2]).write_text(json.dumps(data,indent=2),encoding='utf-8')
