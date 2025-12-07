from concurrent.futures import ProcessPoolExecutor
from guard import guard, map_grid

for i, line in enumerate(map_grid):
    if '^' in line:
        start = (line.index('^'), i)
        map_grid[i][start[0]] = '.'
        break

main_guard = guard(start, 0)
main_guard.patrol(map_grid)

map_grid = tuple(tuple(row) for row in map_grid)

visited_pos = set()
for (x, y, _) in main_guard.trace - {(start[0], start[1], '^')}: visited_pos.add((x, y))
timelines = []
for (x, y) in visited_pos:
    timeline = [list(row) for row in map_grid]
    timeline[y][x] = '#'
    timelines.append(timeline)

def test_timeline(timeline):
    temp_guard = guard(start, 0)
    return temp_guard.patrol(timeline)

results = list(ProcessPoolExecutor().map(test_timeline, timelines))
output = results.count(True)

print(output)