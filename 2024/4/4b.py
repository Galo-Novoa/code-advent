import sys
import os
from itertools import permutations

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.io import textread

soup = textread('db.txt')
directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
unwraps = [''.join(x) for x in permutations('MMSS') if ''.join(x) not in ('MSMS', 'SMSM')]
output = 0

for i in range(1, len(soup)-1):
    for j in range(1, len(soup[i])-1):
        if soup[i][j] == 'A':
                check = (''.join([soup[i+x][j+y] for x, y in directions]))
                if check in unwraps: output += 1

print(output)