with open("03.txt") as file:
    data = file.read()


def find_highest_in_range(line, start, end):
    for n in range(9, 0, -1):
        i = line.find(str(n), start, end)
        if i != -1:
            return i
    return -1


def optimal_joltage(line, bats):
    digits = ""
    start = 0
    for d in range(bats - 1, -1, -1):
        pos = find_highest_in_range(line, start, len(line) - d)
        if pos == -1:
            print("ERROR")
            return 0
        digits += line[pos]
        start = pos + 1
    return int(digits)


max_joltage1 = 0
max_joltage2 = 0

for line in data.split():
    max_joltage1 += optimal_joltage(line, 2)
    max_joltage2 += optimal_joltage(line, 12)

print(f"Part 1: {max_joltage1}")
print(f"Part 2: {max_joltage2}")
