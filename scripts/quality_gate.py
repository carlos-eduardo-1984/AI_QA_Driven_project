import json, os, sys
m=json.load(open(sys.argv[1])); minimum=float(os.getenv('MIN_PASS_RATE','95')); maximum=int(os.getenv('MAX_CRITICAL_FAILURES','0')); errors=[]
if m['pass_rate'] < minimum: errors.append(f"Pass rate {m['pass_rate']}% is below {minimum}%")
if m['critical_failures'] > maximum: errors.append(f"Critical failures {m['critical_failures']} exceed {maximum}")
if errors: print('QUALITY GATE FAILED\n'+'\n'.join(errors)); sys.exit(1)
print('QUALITY GATE PASSED')
