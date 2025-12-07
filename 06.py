with open("06.txt") as file:
    data = file.read()

lines = [line.split() for line in data.splitlines()]
numbers = lines[:-1]
operators = lines[-1]

total = 0

for i, op in enumerate(operators):
    if op == "+":
        for row in numbers:
            total += int(row[i])
    else:
        mul = 1
        for row in numbers:
            mul *= int(row[i])
        total += mul

print(f"Part 1: {total}")

lines = data.splitlines()[:-1]


def read_col(i):
    string = ""
    for line in lines:
        if i < len(line):
            string += line[i]
    return string.strip()


total = 0
i = 0
for op in operators:
    mul = 1
    col = read_col(i)
    while len(col) > 0:
        if op == "+":
            total += int(col)
        else:
            mul *= int(col)
        i += 1
        col = read_col(i)
    if op == "*":
        total += mul
    i += 1

print(f"Part 2: {total}")
