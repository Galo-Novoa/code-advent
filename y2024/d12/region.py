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

class region():
    def __init__(self, startpos):
        self.startpos = startpos
        self.plots = set()
        self.seed = map_grid[startpos[1]][startpos[0]]
        self.perimeter = 0

    def same_seed(self, npos):
        if in_map(npos) and map_grid[npos[1]][npos[0]] == self.seed: return True
        return False

    def corner_count(self, pos):
        count = 0
        for diag in diagonals:
            corner = get_pos(pos, diag)
            btwn1 = get_pos(pos, (diag[0], 0))
            btwn2 = get_pos(pos, (0, diag[1]))
            if self.same_seed(btwn1) == self.same_seed(btwn2):
                if (corner in self.plots and not self.same_seed(btwn1)) or corner not in self.plots: count += 1
        return count

    def scan_region(self, pos):
        self.plots.add(pos)
        for npos in [get_pos(pos, dir) for dir in directions4]:
            if self.same_seed(npos) and npos not in self.plots: self.scan_region(npos)

    def scan_corners(self, pos):
        visited.add(pos)
        self.perimeter += self.corner_count(pos)
        for npos in [get_pos(pos, dir) for dir in directions4]:
            if self.same_seed(npos) and npos not in visited: self.scan_corners(npos)

    def price(self):
        self.scan_region(self.startpos)
        self.scan_corners(self.startpos)
        area = len(self.plots)
        return area * self.perimeter