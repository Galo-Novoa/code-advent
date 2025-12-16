import sys
import os
from operator import add, mul
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

ops = [mul, concat, add]

def analyze(result, operands):
    n = len(operands)
    
    def branch(acc, i):
        if acc > result: return False
        if i == n:
            return acc == result
        for operation in ops:
            if branch(operation(acc, operands[i]), i + 1):
                return True
        return False
    
    return branch(operands[0], 1)

output = sum(result for result, operands in data.items() if analyze(result, operands))

print(output)

# originalmente 10s con iteración sobre producto cartesiano
# ahora 1s con recursión que me enseñó la IA