import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from collections import defaultdict
from itertools import product
from shared.io import textread

map_grid = textread('db.txt')

antinodes = set()
antennas = defaultdict(set)

for y, line in enumerate(map_grid):
    for x, c in enumerate(line):
        if c != '.': antennas[c].add((x, y))

map_range = {pos for pos in product(range(len(map_grid[0])), range(len(map_grid)))}

def sub_pos(p1, p2): return (p1[0] - p2[0], p1[1] - p2[1])

for freq in antennas:
    for p1 in antennas[freq]:
        for p2 in antennas[freq] - {p1}:
            dist = sub_pos(p1, p2)
            ant = p2
            while ant in map_range:
                antinodes.add(ant)
                ant = sub_pos(ant, dist)

with open('debug.txt', 'w') as file:
    for y, line in enumerate(map_grid):
        for x, c in enumerate(line):
            if (x, y) in antinodes and c == '.': c = '#'
            file.write(c)
        file.write('\n')

output = len(antinodes)
print(output)

# Velocidad sin debug: 2.8 ms B)