# Simple eval runner placeholder
import json
with open('eval_set.jsonl') as f:
    data = json.load(f)
print('Loaded', len(data), 'eval items')
