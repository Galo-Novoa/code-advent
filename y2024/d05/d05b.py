import sys
import os
from math import floor

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import splitpage

raw_rules, raw_updates = splitpage('input.txt')

rules = [tuple(map(int, t)) for t in (r.split('|') for r in raw_rules)]
updates = [list(map(int, t)) for t in (u.split(',') for u in raw_updates)]
output = 0

for u in updates:
    filtered_rules = list(filter(lambda t, u=set(u): t[0] in u and t[1] in u, rules))
    value_to_index = {v: i for i, v in enumerate(u)}
    if not all(value_to_index[r[0]] < value_to_index[r[1]] for r in filtered_rules):
        sorted_u = [u[0]]
        for p in u[1:]:
            for s in sorted_u:
                if (p, s) in filtered_rules: sorted_u.insert(sorted_u.index(s), p); break
            if p not in sorted_u: sorted_u.append(p)
        output += sorted_u[floor(len(sorted_u)/2)]

print(output)