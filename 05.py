import helper

data = helper.start(5)

fresh_ranges, ingredients = data.strip().split("\n\n")

fresh_ranges = [tuple(map(int, r.split("-"))) for r in fresh_ranges.split()]
ingredients = list(map(int, ingredients.split()))


done = False
i = 0
while i < len(fresh_ranges):
    start, end = fresh_ranges[i]
    j = i + 1
    while j < len(fresh_ranges):
        a, b = fresh_ranges[j]
        if start <= a <= end <= b:
            end = b
            fresh_ranges[i] = (start, end)
            fresh_ranges.pop(j)
            j = i + 1
        elif a <= start <= b <= end:
            start = a
            fresh_ranges[i] = (start, end)
            fresh_ranges.pop(j)
            j = i + 1
        elif start <= a <= b <= end:
            fresh_ranges.pop(j)
        elif a <= start <= end <= b:
            fresh_ranges.pop(i)
            i -= 1
            break
        else:
            j += 1

    i += 1

amount = sum(b - a + 1 for a, b in fresh_ranges)
helper.print_result_and_time(amount, 2)


fresh_ingredients_count = 0

for ingredient in ingredients:
    for a, b in fresh_ranges:
        if a <= ingredient <= b:
            fresh_ingredients_count += 1
            break


helper.print_result_and_time(fresh_ingredients_count, 1)
