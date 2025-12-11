import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import splitread

left, right = splitread('input.txt', '   ')

output = 0

for n in left:
    output += n * right.count(n)

print(output)