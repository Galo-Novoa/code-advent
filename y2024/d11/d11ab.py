import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from math import floor, log10

from shared.io import matrixread

stones = matrixread('input.txt')[0]

def spliteven(n):
    digits = floor(log10(n)) + 1
    divisor = (10 ** (digits // 2))
    left = n // divisor
    right = n % divisor
    return left, right

def count_stones(stones, blinks):
    memo = {}
    def blink(stn, i):
        if i == blinks: return 1
        if (stn, i) in memo: return memo[(stn, i)]
        match stn:
            case 0: count = blink(1, i + 1)
            case x if floor(log10(x) + 1) % 2 == 0:
                left, right = spliteven(stn)
                count = blink(left, i + 1) + blink(right, i + 1)
            case _: count = blink(stn * 2024, i + 1)
        memo[(stn, i)] = count
        return count
    tcount = 0
    for stn in stones:
        tcount += blink(stn, 0)
    return tcount

print(f"After 25 blinks: {count_stones(stones, 25)}, After 75 blinks: {count_stones(stones, 75)}")