document = open("day1.txt").read().splitlines()
total = 0
for i in document:
    for j in i:
        if j.isnumeric():
            total += int(j) * 10
            break
    for j in range(len(i)-1, -1, -1):
        if i[j].isnumeric():
            total += int(i[j])
            break 
print(total)