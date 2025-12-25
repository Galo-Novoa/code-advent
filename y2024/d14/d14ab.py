import re

def robot_read(filename):
    regex = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    with open(filename, 'r') as file:
        matches = re.findall(regex, file.read())
    matches = (tuple(map(int, x)) for x in matches)
    safety_factor = tuple(((x, y), (vx, vy)) for x, y, vx, vy in matches)
    return safety_factor

robots = robot_read('input.txt')

quadrants = [0, 0, 0, 0]
arrangement = set()

map_range = (101, 103)
mid = (map_range[0] // 2, map_range[1] // 2)

def move(robot, seconds, part):
    (x, y), (vx, vy) = robot
    x = (x + vx * seconds) % map_range[0]
    y = (y + vy * seconds) % map_range[1]
    if part == 1:
        if x < mid[0] and y < mid[1]: quadrants[0] += 1
        elif x > mid[0] and y < mid[1]: quadrants[1] += 1
        elif x < mid[0] and y > mid[1]: quadrants[2] += 1
        elif x > mid[0] and y > mid[1]: quadrants[3] += 1
    arrangement.add((x, y))

for robot in robots: move(robot, 100, 1)

safety_factor = 1
for quad in quadrants: safety_factor *= quad

print("Part 1:", safety_factor)

map_grid = []

def create_map():
    map_grid.clear()
    for y in range(map_range[1]):
        line = []
        for x in range(map_range[0]):
            c = '█' if (x, y) in arrangement else ' '
            line.append(c)
        map_grid.append(line)

def print_map(file):
        for line in map_grid:
            for c in line:
                file.write(c)
            file.write('\n')
        file.write('\n\n\n\n\n')

filename = 'debug.txt'

with open(filename, 'w') as file:
    file.write('')
    for s in range(10001):
        arrangement.clear()
        for robot in robots: move(robot, s, 2)
        create_map()
        file.write(f"{s}\n")
        print_map(file)

tree_seconds = 8280 # la concha de tu madre

print("Part 2:", tree_seconds)