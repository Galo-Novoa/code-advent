import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread
from collections import defaultdict

map_grid = textread('input.txt')
def in_map(pos): return 0 <= pos[0] < len(map_grid[0]) and 0 <= pos[1] < len(map_grid)

directions4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diagonals = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
def get_pos(pos, dir):
    return (pos[0] + dir[0], pos[1] - dir[1])

visited = set()

def region_price(pos):
    region = set()
    seed = map_grid[pos[1]][pos[0]]
    perimeter = 0

    def same_seed(npos):
        if in_map(npos) and map_grid[npos[1]][npos[0]] == seed: return True
        return False

    def corner_count(pos):
        count = 0
        for diag in diagonals:
            corner = get_pos(pos, diag)
            btwn1 = get_pos(pos, (diag[0], 0))
            btwn2 = get_pos(pos, (0, diag[1]))
            if same_seed(btwn1) == same_seed(btwn2):
                if (corner in region and not same_seed(btwn1)) or corner not in region: count += 1
        return count

    def scan_region(pos):
        visited.add(pos)
        region.add(pos)
        for npos in [get_pos(pos, dir) for dir in directions4]:
            if same_seed(npos) and npos not in visited: scan_region(npos)

    def scan_corners(pos):
        visited.add(pos)
        nonlocal perimeter
        perimeter += corner_count(pos)
        for npos in [get_pos(pos, dir) for dir in directions4]:
            if same_seed(npos) and npos not in visited: scan_corners(npos)

    scan_region(pos)
    visited.difference_update(region)
    scan_corners(pos)
    area = len(region)
    return area * perimeter

output = 0
for y, line in enumerate(map_grid):
    for x, s in enumerate(line):
        if (x, y) not in visited: output += region_price((x, y))

print(output)