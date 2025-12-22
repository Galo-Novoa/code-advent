import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from shared.io import splitpage
import re

def prize_read(filename):
    buttonre = r"Button [AB]: X\+(\d+), Y\+(\d+)\n"
    prizere = r"Prize: X=(\d+), Y=(\d+)"
    fullre = buttonre + buttonre + prizere

    blocks = list(map('\n'.join, splitpage(filename)))
    machines = set()
    for block in blocks:
        m = tuple(map(int, re.findall(fullre, block)[0]))
        machines.add(tuple(zip(m[::2], m[1::2])))
    return machines

def check(machine):
    A, B, prize = machine

    possibilities = set()
    for a in range(101):
        for b in range(101):
            if (a * A[0] + b * B[0], a * A[1] + b * B[1]) == prize: possibilities.add(3 * a + b)
    
    tokens = min(possibilities) if possibilities != set() else 0
    return tokens

machines = prize_read('input.txt')
output = 0

for mach in machines:
    output += check(mach)

print(output)