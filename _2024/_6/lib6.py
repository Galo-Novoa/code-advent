from 6b

def next_pos(position, pointing):
    x, y = position
    dx, dy = directions[pointing % 4]
    return (x+dx, y-dy)

def step_override(pointing, char):
    match char:
        case '.': return char_from_dir[pointing % 4]
        case c if c == char_from_dir[(pointing + 2) % 4]: return double_dir_chars[pointing % 2]

def scan_back(pointing, position):
    nxb, nyb = position
    while nyb in range(len(map)) and nxb in range(len(map[0])) and map[nyb][nxb] != '#':
        map[position[1]][position[0]] = step_override(pointing, map[position[1]][position[0]])
        position = (nxb, nyb)
        nxb, nyb = next_pos(position, (pointing % 4))