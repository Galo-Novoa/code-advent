import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread

map_grid = textread('input.txt')
def in_map(pos): return 0 <= pos[0] < len(map_grid[0]) and 0 <= pos[1] < len(map_grid)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def surroundings(pos):
    return [(pos[0]+i, pos[1]+j) for i, j in directions]

visited = set()

def region_price(pos):
    region = set()
    seed = map_grid[pos[1]][pos[0]]
    perimeter = 0

    def scan(pos):
        nonlocal perimeter
        visited.add(pos)
        region.add(pos)
        for npos in surroundings(pos):
            if not in_map(npos): perimeter += 1
            elif map_grid[npos[1]][npos[0]] != seed: perimeter += 1
            elif npos not in visited: scan(npos)

    scan(pos)
    area = len(region)
    return area * perimeter

output = 0
for y, line in enumerate(map_grid):
    for x, s in enumerate(line):
        if (x, y) not in visited: output += region_price((x, y))

print(output)