import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread

soup = textread('db.txt')
directions = {(x, y) for x in range(-1, 2) for y in range(-1, 2)} - {(0, 0)}
word = 'XMAS'
output = 0

for i in range(len(soup)):
    for j in range(len(soup[i])):
        if soup[i][j] == word[0]:
            scan = []
            for x, y in directions:
                if i+(len(word)-1)*x in range(len(soup[0])) and j+(len(word)-1)*y in range(len(soup)):
                    scan.append(''.join(soup[i+l*x][j+l*y] for l in range(len(word))))
            output += scan.count(word)

print(output)