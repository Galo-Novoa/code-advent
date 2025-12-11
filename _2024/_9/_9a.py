with open('db.txt', 'r') as file:
    disk = [int(c) for c in file.read().strip()]

files = disk[::2]

checksum = 0
i = 0
lid = 0
rid = len(files) - 1
for pos, item in enumerate(disk):
    for _ in range(item):
        if lid > rid: break
        if pos % 2 == 0:
            checksum += lid * i
            files[lid] -= 1
            if files[lid] == 0: lid += 1
        else:
            checksum += rid * i
            files[rid] -= 1
            if files[rid] == 0: rid -= 1
        i += 1

print(checksum)