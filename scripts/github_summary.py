import json, os, sys
m=json.load(open(sys.argv[1])); s=f"## Robot Framework Results\n\n| Metric | Value |\n|---|---:|\n| Pass rate | **{m['pass_rate']}%** |\n| Passed | {m['passed']} |\n| Failed | {m['failed']} |\n| Skipped | {m['skipped']} |\n| Critical failures | {m['critical_failures']} |\n"
open(os.environ['GITHUB_STEP_SUMMARY'],'a').write(s)
