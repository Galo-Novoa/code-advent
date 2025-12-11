import sys
import os
import operator
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import dictread

data = dictread('input.txt')

def concat(a, b):
    digits = 1
    temp = b
    while temp:
        digits *= 10
        temp //= 10
    return a * digits + b

ops = {operator.add, concat, operator.mul}

def analyze(result, operands):
        acc = operands[0]
        n = len(operands)
        for c in ops:
            i = 0
            acc = c(acc, operands[i])
            if acc > result: break
        return 

output = 0
for result, operands in data.items():
    if analyze(result, operands) == result:
        output += result
        break

print(output)

# versión que hice (10s)

"""

# versión más rápida que me hizo la IA con memoización (2s)

def can_reach(result, operands):
    n = len(operands)

    def dfs(i, acc):
        if i == n:
            return acc == result
        for op in ops:
            if dfs(i + 1, ops[op](acc, operands[i])):
                return True
        return False

    return dfs(1, operands[0])

for result, operands in data.items():
    if can_reach(result, tuple(operands)):
        output += result
"""