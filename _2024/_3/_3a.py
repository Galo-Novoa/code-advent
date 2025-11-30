import re
import math

def mulparse(filename):
    with open(filename, 'r') as file:
        regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do(?:n't)?\(\))"
        parse = [do if do else (int(a), int(b)) for a, b, do in re.findall(regex, file.read())]
    return parse

text = mulparse('db.txt')

muls = [math.prod(item) for item in text if isinstance(item, tuple)]

output = sum(muls)

print(output)