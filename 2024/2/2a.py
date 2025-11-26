import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import matrixread

matrix = matrixread('db.txt')

output = 0

for r in matrix:
    distances = [current - next for current, next in zip(r, r[1:])]
    checksum = abs(sum(distances))
    actualsum = sum([abs(x) for x in distances])
    if all(abs(x) > 0 and abs(x) < 4 for x in distances) and checksum == actualsum:
        output += 1

print(output)