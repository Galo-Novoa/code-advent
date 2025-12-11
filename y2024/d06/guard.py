import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread

directions = {'int': [(0, 1), (1, 0), (0, -1), (-1, 0)], 'str':['^', '>', 'v', '<']}

map_grid = [list(row) for row in textread('input.txt')]

map_size = {'y': range(len((map_grid))), 'x': range(len(map_grid[0]))}

class guard:

    def __init__(self, pos, pointing):
        self.x, self.y = pos
        self.pointing = pointing
        self.trace = set()

    def in_grid(self, pos):
        x, y = pos
        return y in map_size['y'] and x in map_size['x']

    def get_pos(self, pointing):
        dx, dy = directions['int'][pointing]
        return (self.x+dx, self.y-dy)

    def steer(self):
        self.pointing = (self.pointing + 1) % 4

    def step(self):
        self.trace.add((self.x, self.y, directions['str'][self.pointing]))

    def patrol(self, map_grid):
        nx, ny = self.get_pos(self.pointing)
        while self.in_grid((nx, ny)):
            while map_grid[ny][nx] == '#':
                self.steer()
                nx, ny = self.get_pos(self.pointing)
            if (self.x, self.y, directions['str'][self.pointing]) in self.trace: return True
            self.step()
            self.x, self.y = (nx, ny)
            nx, ny = self.get_pos(self.pointing)
        self.step()
        return False