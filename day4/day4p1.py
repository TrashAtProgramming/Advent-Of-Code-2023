document = open("day4/day4.txt").read().splitlines()
winning = []
cards = []
for lines in document:
    winning.append(lines[41 : len(lines)] + " ")
    cards.append(lines[10:39])
total = 0
for index, lines in enumerate(cards):
    won = 0
    i = 0
    while i < len(lines):
        if lines[i].isnumeric():
            num = int(lines[i])
            if i + 1 < len(lines) and lines[i + 1].isnumeric():
                num = num * 10 + int(lines[i + 1])
                i += 1
            num = " " + str(num) + " "
            if num in winning[index]:
                won += 1
        i += 1
    if won > 0:
        total = total + 2 ** (won - 1)
print(total)
