import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from collections import defaultdict

from shared.io import textread

map_grid = textread('db.txt')

antinodes = set()
antennas = defaultdict(set)

for y, line in enumerate(map_grid):
    for x, c in enumerate(line):
        if c != '.': antennas[c].add((x, y))

def in_grid(pos): return pos[0] in range(len(map_grid[0])) and pos[1] in range(len(map_grid))

def get_dist(p1, p2): return (p1[0] - p2[0], p1[1] - p2[1])

for freq in antennas:
    while antennas[freq]:
        p1 = antennas[freq].pop()
        for p2 in antennas[freq]:
            dx, dy = get_dist(p1, p2)
            an1 = (p1[0] + dx, p1[1] + dy)
            an2 = (p2[0] - dx, p2[1] - dy)
            if in_grid(an1): antinodes.add(an1)
            if in_grid(an2): antinodes.add(an2)

with open('debug.txt', 'w') as file:
    for y, line in enumerate(map_grid):
        for x, c in enumerate(line):
            if (x, y) in antinodes and c == '.': c = '#'
            file.write(c)
        file.write('\n')

output = len(antinodes)
print(output)