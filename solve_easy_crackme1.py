# solution 1
'''
for i in range(1, 0x2000+1):
    for j in range(1, 0x2000+1):
        if i // j != 4:
            continue
        if i * j != 0x6AE9BC:
            continue
        if i ^ j != 0x12FC:
            continue

        print("The Answer is %d %d" % (i, j))
'''

# solution 2
for i in range(1, 0x2000+1):
    j = i ^ 0x12FC

    if i * j != 0x6AE9BC:
        continue

    if i // j != 4:
        continue

    print("The Answer is %d %d" % (i, j))