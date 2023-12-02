document = open("day2/day2.txt").read().splitlines()
maximum = {
    "r":12,
    "g":13,
    "b":14}
total = 0
for line in document:
    possible = True
    for character_index in range(8, len(line)):
        if line[character_index].isnumeric():
            num = int(line[character_index])
            if line[character_index + 1].isnumeric():
                num = num * 10 + int(line[character_index + 1])
                character_index += 1
            colour = line[character_index + 2]
            if num > maximum[colour]:
                possible = False
    if possible:
        num = int(line[5])
        if line[6].isnumeric():
            num = num * 10 + int(line[6])
            if line[7].isnumeric():
                num = num * 10 + int(line[7])
        total += num
print (total)