from region import map_grid, visited, region

output = 0
for y, line in enumerate(map_grid):
    for x, s in enumerate(line):
        if (x, y) not in visited: output += region((x, y)).price()

print(output)