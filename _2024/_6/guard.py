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
        self.trace_grid = [[set() if c == '.' else {c} for c in row] for row in map_grid]

    def in_grid(self, position):
        x, y = position
        return y in map_size['y'] and x in map_size['x']

    def get_pos(self, pointing):
        x, y = self.pos
        dx, dy = directions['int'][pointing]
        return (x+dx, y-dy)

    def patrol(self):
        nx, ny = self.get_pos(self.pointing)
        while self.in_grid((nx, ny)):
            if map_grid[ny][nx] == '#':
                self.pointing = self.steer(1)
                nx, ny = self.get_pos(self.pointing)
            else:
                map_grid[ny][nx] = 'O'
                if check_guard(self.pos, self.pointing, self.trace_grid).patrol():
                    obs_positions.add((nx, ny))
                map_grid[ny][nx] = '.'
            self.trace_grid[self.pos[1]][self.pos[0]].add(directions['str'][self.pointing])
            with open('debug.txt', 'w') as file:
                for line in self.trace_grid:
                    for c in line:
                        if c: file.write(next(iter(c)))
                        else: file.write('.')
                    file.write('\n')
            self.pos = (nx, ny)
            nx, ny = self.get_pos(self.pointing)
        self.trace_grid[self.pos[1]][self.pos[0]].add(directions['str'][self.pointing])

    def steer(self, value):
        pointing = (self.pointing + value) % 4
        return pointing

class check_guard(guard):
    def __init__(self, pos, pointing, trace_grid):
        super().__init__(pos, pointing)
        self.trace_grid = copy.deepcopy(trace_grid)

    def patrol(self):
        nx, ny = self.get_pos(self.pointing)
        while self.in_grid((nx, ny)):
            if map_grid[ny][nx] in ['#', 'O']:
                self.pointing = self.steer(1)
                nx, ny = self.get_pos(self.pointing)
            self.trace_grid[self.pos[1]][self.pos[0]].add(directions['str'][self.pointing])
            if directions['str'][self.pointing] in self.trace_grid[self.pos[1]][self.pos[0]]: return True
            self.pos = (nx, ny)
            nx, ny = self.get_pos(self.pointing)
        return False

class back_guard(guard):
    
    def __init__(self, pos, pointing):
        super().__init__(pos, pointing)

    def scan_back(self, main_guard):
        px, py = self.get_pos(self.steer(2))
        while self.in_grid((px, py)) and map_grid[py][px] != '#':
            main_guard.trace_grid[self.pos[1]][self.pos[0]].add(directions['str'][self.pointing])
            self.pos = (px, py)
            px, py = self.get_pos(self.steer(2))