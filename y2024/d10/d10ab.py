from itertools import product

with open('input.txt', 'r') as file:
    map_grid = [[int(c) for c in line.strip()] for line in file]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

map_range = set(product(range(len(map_grid[0])), range(len(map_grid))))

def surroundings(pos):
    return [(pos[0]+i, pos[1]+j) for i, j in directions]

def get_stats(map_grid, startpos):
    peaks = set()
    rating = 0
    def hike(height, pos):
        nonlocal rating
        if height == 9:
            peaks.add(pos)
            rating += 1
        for nx, ny in surroundings(pos):
            if (nx, ny) in map_range and map_grid[ny][nx] == height + 1: hike(height + 1, (nx, ny))
    hike(0, startpos)
    return (len(peaks), rating)

tscore, trating = 0, 0
for y, line in enumerate(map_grid):
    for x, height in enumerate(line):
        if height == 0:
            score, rating = get_stats(map_grid, (x, y))
            tscore += score
            trating += rating

print(f"Total trailhead score: {tscore}. Total trailhead rating: {trating}.")