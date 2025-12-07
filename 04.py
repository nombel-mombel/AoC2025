import helper

data = helper.start(4)


data = [list(line) for line in data.split()]

height = len(data)
width = len(data[0])

accessible_count = 0

for x in range(width):
    for y in range(height):
        if data[y][x] == "@":
            count = 0
            for dx in range(max(0, x - 1), min(width, x + 2)):
                for dy in range(max(0, y - 1), min(height, y + 2)):
                    if data[dy][dx] == "@":
                        count += 1
            if count <= 4:
                accessible_count += 1


helper.print_result_and_time(accessible_count)


removable_count = 0
changed = True
while changed:
    changed = False
    for x in range(width):
        for y in range(height):
            if data[y][x] == "@":
                count = 0
                for dx in range(max(0, x - 1), min(width, x + 2)):
                    for dy in range(max(0, y - 1), min(height, y + 2)):
                        if data[dy][dx] == "@":
                            count += 1
                if count <= 4:
                    removable_count += 1
                    data[y][x] = "."
                    changed = True


helper.print_result_and_time(removable_count)
