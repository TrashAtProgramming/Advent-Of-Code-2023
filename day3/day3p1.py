document = open("day3/day3.txt").read().splitlines()
def check(document, x, y):
    positions = [(x-1, y), (x-1, y-1), (x-1, y+1), (x+1, y), (x+1, y-1), (x+1, y+1), (x, y-1), (x, y+1),]
    for new_x, new_y in positions:
        if 0 <= new_x < len(document[0]) and 0 <= new_y < len(document) and not document[new_y][new_x].isnumeric() and document[new_y][new_x] != '.':
            return True
    return False
total = 0
y = 0
while y < len(document):
    x = 0
    while x < len(document[y]):
        if document[y][x].isnumeric():
            num = int(document[y][x])
            part = check(document, x, y)
            if document[y][x+1].isnumeric():
                num = num * 10 + int(document[y][x+1])
                if not part:
                    part = check(document, x+1, y)
                x = x+1
                if document[y][x+1].isnumeric():
                    num = num * 10 + int(document[y][x+1])
                    if not part:
                        part = check(document, x+1, y)
                    x = x+1
            if part:
                total += num
        x += 1
    y += 1
print(total)