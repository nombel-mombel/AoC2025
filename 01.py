with open("01.txt") as file:
    data = file.read()

pos = 50
count1 = 0
count2 = 0

for line in data.split():
    n = int(line[1:])
    d = line[0]
    if d == "L":
        n *= -1

    negative_left_compensation = pos == 0 and d == "L"
    pos += n
    rounds = abs(pos // 100)
    pos %= 100
    positive_left_compensation = pos == 0 and d == "L"
    count2 += rounds - negative_left_compensation + positive_left_compensation

    if pos == 0:
        count1 += 1

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")
