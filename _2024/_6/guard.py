import sys
import os
import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread

map_grid = [list(row) for row in textread('db.txt')]

directions = {'int': [(0, 1), (1, 0), (0, -1), (-1, 0)], 'str':['^', '>', 'v', '<']}

map_size = {'y': range(len((map_grid))), 'x': range(len(map_grid[0]))}

obs_positions = set()

class guard:

    def __init__(self, pos, pointing):
        self.pos = pos
        self.pointing = pointing
        self.trace_grid = [[{c} if c != '.' else set() for c in row] for row in map_grid]

    def get_pos(self, pointing):
        x, y = self.pos
        dx, dy = directions['int'][pointing]
        return (x+dx, y-dy)

    def scan_back(self):
        px, py = self.get_pos(self.steer(2))
        while py in map_size['y'] and px in map_size['x'] and map_grid[py][px] != '#':
            px, py = self.get_pos(self.steer(2))
            self.trace_grid[pos[1]][pos[0]].add(directions['str'][self.pointing])
            pos = (px, py)

    def patrol(self):
        nx, ny = self.get_pos(self.pointing)
        while ny in map_size['y'] and nx in map_size['x']:
            if map_grid[ny][nx] == '#':
                self.scan_back()
                self.pointing = self.steer(1)
                nx, ny = self.get_pos(self.pointing)
            elif check_guard(self.pos, self.pointing, self.trace_grid).patrol():
                obs_positions.add((nx, ny))
            self.trace_grid[pos[1]][pos[0]].add(directions['str'][self.pointing])
            pos = (nx, ny)
            nx, ny = self.get_pos(self.pointing)
        self.trace_grid[pos[1]][pos[0]].add(directions['str'][self.pointing])

    def steer(self, value):
        pointing = (self.pointing + value) % 4
        return pointing

class check_guard(guard):
    def __init__(self, pos, pointing, trace_grid):
        super().__init__(pos, pointing)
        self.trace_grid = copy.deepcopy(trace_grid)

    def patrol(self):
        nx, ny = self.get_pos(self.pointing)
        while ny in map_size['y'] and nx in map_size['x']:
            if map_grid[ny][nx] == '#':
                self.scan_back()
                pointing = (pointing + 1) % 4
                nx, ny = self.get_pos(self.pointing)
            self.trace_grid[self.pos[1]][self.pos[0]].add(directions['str'][pointing])
            if directions['str'][pointing] in self.trace_grid[ny][nx]: return True
            self.pos = (nx, ny)
            nx, ny = self.get_pos(self.pointing)
        return False