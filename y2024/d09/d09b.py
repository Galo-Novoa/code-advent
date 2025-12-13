with open('input.txt', 'r') as file:
    disk = [int(c) for c in file.read().strip()]

files = disk[::2]
print(files)

checksum = 0
for right in reversed(range(len(files))):
    for left in range(right + 1):
        if files[right] < disk[left*2+1]: break
    offset = sum(disk[:left*2+1:2])
    for i in range(files[right]): checksum += right * (offset + i)
    print(right, left, disk)
    if left == right: continue
    disk[left*2+1] -= files[right]
    disk[left*2] += files[right]

print(checksum)