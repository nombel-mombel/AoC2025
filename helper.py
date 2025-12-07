from time import time

part = 1


def start(day: int):
    global t
    print(f">>>Day {day}<<<\n")
    with open(f"{day:02}.txt") as file:
        data = file.read()
    t = time()
    return data


def print_result(result: int, part_overide: int | None = None):
    global part
    if part_overide is not None:
        part = part_overide
    print(f"Part {part}: {result}")
    part += 1


def print_result_and_time(result: int, part_overide: int | None = None):
    global t
    print_result(result, part_overide)
    t1 = time()
    print(f"-> Took {(t1 - t) * 1000:.2f}ms")
    t = t1
