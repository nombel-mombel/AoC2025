import helper

data = helper.start(2)

ranges = [list(map(int, r.split("-"))) for r in data.split(",")]

invalid_counter1 = 0
invalid_counter2 = 0

for [a, b] in ranges:
    for n in range(a, b + 1):
        s = str(n)

        if len(s) % 2 == 0 and s[: len(s) // 2] == s[len(s) // 2 :]:
            invalid_counter1 += n

        for i in range(1, len(s) // 2 + 1):
            reps = len(s) // i
            if reps * i == len(s) and s[:i] * reps == s:
                invalid_counter2 += n
                break


helper.print_result(invalid_counter1)
helper.print_result_and_time(invalid_counter2)
