import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from itertools import product
from shared.io import splitread

with open('input.txt', 'r') as file:
    map_grid = [[int(c) for c in line.strip()] for line in file]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

map_range = set(product(range(len(map_grid[0])), range(len(map_grid))))

def surroundings(pos):
    return [(pos[0]+i, pos[1]+j) for i, j in directions]

def get_score(map_grid, startpos):
    peaks = set()
    def hike(height, pos):
        if height == 9: peaks.add(pos)
        for nx, ny in surroundings(pos):
            if (nx, ny) in map_range and map_grid[ny][nx] == height + 1: hike(height + 1, (nx, ny))
    hike(1, startpos)
    return len(peaks)

output = 0
for y, line in enumerate(map_grid):
    for x, height in enumerate(line):
        if height == 0: output += get_score(map_grid, (x, y))

print(output)