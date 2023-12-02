document = open("day1/day1.txt").read().splitlines()
nums = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9}
total = 0
for i in document:
    word = ''
    for j in i:
        if j.isnumeric():
            total += int(j) * 10
            break
        else:
            word = word + j
            if word in nums:
                total += nums[word] * 10
                break
            else:
                temp = True
                while temp:
                    for key in nums:
                        if word in key:
                            temp = False
                    if temp:
                        word = word[1:]        
    word = ''
    for j in range(len(i)-1, -1, -1):
        if i[j].isnumeric():
            total += int(i[j])
            break 
        else:
            word = i[j] + word
            if word in nums:
                total += nums[word]
                break
            else:
                temp = True
                while temp:
                    for key in nums:
                        if word in key:
                            temp = False
                    if temp:
                        word = word[:-1]
print(total)