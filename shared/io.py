def splitread(filename, char):
    with open(filename, 'r') as file:
        a = []
        b = []
        for line in file:
            buffer = line.strip().split(char)
            a.append(int(buffer[0]))
            b.append(int(buffer[1]))
        return a, b

def matrixread(filename):
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            buffer = [int(x) for x in line.strip().split()]
            matrix.append(buffer)
    return matrix

def textread(filename):
    with open(filename, 'r') as file:
        text = [line.strip() for line in file]
        return text

def splitpage(filename):
    with open(filename, 'r') as file:
        output = []
        aux = []
        for line in file:
            if line == '\n':
                output.append(aux)
                aux = []
                continue
            aux.append(line.strip())
        output.append(aux)
        return output