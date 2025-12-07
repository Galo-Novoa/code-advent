import sys
import os
import operator
from itertools import product
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import dictread

data = dictread('db.txt')
ops = {'+': operator.add, '*': operator.mul}

def analyze(combination, operands):
    if len(operands) == 1: return operands[0]
    else: return ops[combination[0]](operands[-1], analyze(combination[1:], operands[:-1]))

output = 0
for result in data:
    combinations = list(product('+*', repeat=len(data[result]) - 1))
    if any(analyze(comb, data[result]) == result for comb in combinations): output += result

print(output)