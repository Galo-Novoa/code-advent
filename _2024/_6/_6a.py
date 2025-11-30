import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread
from lib6 import next_pos

map = [list(row) for row in textread('db.txt')]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i, line in enumerate(map):
    if '^' in line:
        start = (line.index('^'), i)
        break

pointing = 0
position = start

nx, ny = next_pos(position, pointing)

while ny in range(len(map)) and nx in range(len(map[0])):
    map[position[1]][position[0]] = 'X'
    if map[ny][nx] == '#':
        pointing += 1
        nx, ny = next_pos(position, pointing)
    position = (nx, ny)
    nx, ny = next_pos(position, pointing)
map[position[1]][position[0]] = 'X'

output = 0

for line in map:
    output += line.count('X')

with open('debug.txt', 'w') as file:
    for line in map:
        file.write(''.join(line) + '\n')

print(output)