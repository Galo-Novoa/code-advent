import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import matrixread

matrix = matrixread('db.txt')

output = 0

for r in matrix:
    wdampened = [r] + [r[:i] + r[i+1:] for i in range(len(r))]
    dist = [[current - next for current, next in zip(D, D[1:])] for D in wdampened]
    checks = [abs(sum(D)) for D in dist]
    goals = [sum([abs(d) for d in D]) for D in dist]
    if any(all(abs(d) in range(1, 4) for d in D) and checks[dist.index(D)] == goals[dist.index(D)] for D in dist) : output += 1

print(output)