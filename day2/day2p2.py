document = open("day2/day2.txt").read().splitlines()
total = 0
for line in document:
    maximum = {
    "r":0,
    "g":0,
    "b":0}
    for character_index in range(8, len(line)):
        if line[character_index].isnumeric():
            num = int(line[character_index])
            if line[character_index + 1].isnumeric():
                num = num * 10 + int(line[character_index + 1])
                character_index += 1
            colour = line[character_index + 2]
            if num > maximum[colour]:
                maximum[colour] = num
    power = maximum["r"] * maximum["g"] * maximum["b"]
    total += power
print(total)