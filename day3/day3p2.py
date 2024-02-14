document = open("day3/day3.txt").read().splitlines()


def find_nums(document, adjacents):
    nums = []
    for i in adjacents:
        num = int(document[i[1]][i[0]])
        for j in range(1, 3):
            if document[i[1]][i[0] - j].isnumeric():
                num = num + int(document[i[1]][i[0] - j]) * 10**j
            else:
                break
        for j in range(1, 3):
            if document[i[1]][i[0] + j].isnumeric():
                num = num * 10 + int(document[i[1]][i[0] + j])
            else:
                break
        nums.append(num)
    nums = list(set(nums))
    return nums


def check(document, x, y):
    positions = [
        (x - 1, y),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y),
        (x + 1, y - 1),
        (x + 1, y + 1),
        (x, y - 1),
        (x, y + 1),
    ]
    adjacents = []
    for new_x, new_y in positions:
        if (
            0 <= new_x < len(document[0])
            and 0 <= new_y < len(document)
            and document[new_y][new_x].isnumeric()
        ):
            adjacents.append((new_x, new_y))
    nums = find_nums(document, adjacents)
    if len(nums) == 2:
        return nums[0] * nums[1]
    return 0


total = 0
for y in range(len(document)):
    for x in range(len(document[y])):
        if document[y][x] == "*":
            total += check(document, x, y)
print(total)
