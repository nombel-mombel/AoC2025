with open("07.txt") as file:
    data = file.read()


lines = data.split()
height = len(lines)

start = lines[0].index("S")

visited = set()


def follow_beam(x, y):
    if y == height or (x, y) in visited:
        return 0
    visited.add((x, y))
    if lines[y][x] == "^":
        return follow_beam(x - 1, y) + follow_beam(x + 1, y) + 1
    return follow_beam(x, y + 1)


result = follow_beam(start, 0)
print(f"Part 1: {result}")


cache = {}


def follow_beam_paths(x, y):
    if (x, y) in cache:
        return cache[(x, y)]
    if y == height:
        return 0
    if lines[y][x] == "^":
        result = follow_beam_paths(x - 1, y) + follow_beam_paths(x + 1, y) + 1
    else:
        result = follow_beam_paths(x, y + 1)
    cache[(x, y)] = result
    return result


result = follow_beam_paths(start, 0) + 1
print(f"Part 2: {result}")
