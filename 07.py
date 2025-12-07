import helper

data = helper.start(7)

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
helper.print_result_and_time(result)


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
helper.print_result_and_time(result)
