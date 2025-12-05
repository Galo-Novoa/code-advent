from guard import guard, map_grid, obs_positions

for i, line in enumerate(map_grid):
    if '^' in line:
        start = (line.index('^'), i)
        break

main_guard = guard(start, 0)
main_guard.patrol()

output = 0

for row in main_guard.trace_grid:
    for cell in row:
        if cell == set(): cell.add('.')

with open('debug.txt', 'w') as file:
    for line in main_guard.trace_grid:
        for c in line:
            file.write(c.pop())
        file.write('\n')

output = len(obs_positions)

print(output)