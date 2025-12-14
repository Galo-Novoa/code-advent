with open('input.txt', 'r') as file:
    disk = [int(c) for c in file.read().strip()]

files = disk[::2]

checksum = 0
for right in reversed(range(len(files))):
    for left in range(right + 1):
        if files[right] <= disk[left*2+1]: break
    if left == right: offset = sum(disk[:left*2])
    else: offset = sum(disk[:left*2+1])
    checksum += right * (files[right] * offset + (files[right]-1) * files[right] // 2) # fórmula cerrada
    if left == right: continue
    disk[left*2] += files[right]
    disk[left*2+1] -= files[right]

print(checksum) # 3 s