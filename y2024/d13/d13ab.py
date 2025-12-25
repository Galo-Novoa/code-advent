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
    a_values, b_values, prize = machine

    det = a_values[0] * b_values[1] - a_values[1] * b_values[0]
    if det == 0: return 0

    # regla de Cramer
    det_a = (prize[0] * b_values[1] - prize[1] * b_values[0])
    det_b = (a_values[0] * prize[1] - a_values[1] * prize[0])

    if det_a % det == 0 and det_b % det == 0:
        a_presses = det_a // det
        b_presses = det_b // det
        return 3 * a_presses + b_presses
    else: return 0

machines = prize_read('input.txt')

part_1 = 0
for mach in machines:
    part_1 += check(mach)

part_2 = 0
for mach in machines:
    new_mach = (mach[0], mach[1], (mach[2][0] + 10 ** 13, mach[2][1] + 10 ** 13))
    part_2 += check(new_mach)

print(f"Part 1: {part_1} Part 2: {part_2}")