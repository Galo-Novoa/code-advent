import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import splitread

left, right = splitread('input.txt', '   ')

output = []

for _ in range(len(left)):
    output.append(abs(left.pop(left.index(min(left))) - right.pop(right.index(min(right)))))

print(sum(output))