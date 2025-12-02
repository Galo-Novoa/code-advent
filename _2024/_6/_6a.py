import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread

def next_pos(position, pointing):
    x, y = position
    dx, dy = directions[pointing % 4]
    return (x+dx, y-dy)

grid = [list(row) for row in textread('db.txt')]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

obs_positions = set()

for i, line in enumerate(grid):
    if '^' in line:
        start = (line.index('^'), i)
        break

pointing = 0
position = start

nx, ny = next_pos(position, pointing)

while ny in range(len(grid)) and nx in range(len(grid[0])):
    grid[position[1]][position[0]] = 'X'
    if grid[ny][nx] == '#':
        pointing = (pointing + 1) % 4
        nx, ny = next_pos(position, pointing)
    position = (nx, ny)
    nx, ny = next_pos(position, pointing)
grid[position[1]][position[0]] = 'X'

output = 0

for line in grid:
    output += line.count('X')

with open('debug.txt', 'w') as file:
    for line in grid:
        file.write(''.join(line) + '\n')

print(output)