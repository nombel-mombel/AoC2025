import helper


data = helper.start(9)
# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""

dots = [tuple(map(int, line.split(","))) for line in data.split()]

winner = 0
for i, dot in enumerate(dots):
    for other in dots[i + 1 :]:
        rect = (abs(dot[0] - other[0]) + 1) * (abs(dot[1] - other[1]) + 1)
        if rect > winner:
            winner = rect

helper.print_result_and_time(winner)
