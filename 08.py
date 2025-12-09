import helper

data = helper.start(8)
count = 1000

boxes = [tuple(map(int, line.split(","))) for line in data.split()]


distances = []

for i, a in enumerate(boxes):
    for b in boxes[i + 1 :]:
        if a == b:
            continue
        distance = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
        distances.append((distance, a, b))

distances.sort(key=lambda a: a[0])
print("Preperation")
helper.print_time()

graph = {}
for _, a, b in distances[:count]:
    conns = graph.get(a, set())
    conns.add(b)
    graph[a] = conns

    conns = graph.get(b, set())
    conns.add(a)
    graph[b] = conns

graph.keys()
clusters = []

while len(graph.keys()) > 0:
    start = next(iter(graph.keys()))
    queue = [start]
    cluster = set()
    while len(queue) > 0:
        box = queue.pop()
        if box in cluster:
            continue
        cluster.add(box)
        connections = graph.pop(box)
        for conn in connections:
            queue.append(conn)
    clusters.append(len(cluster))


result = 1
clusters.sort()
for cluster in clusters[-3:]:
    result *= cluster

helper.print_result_and_time(result)

clusters = {}

iterations = 0
for _, a, b in distances:
    iterations += 1
    if a not in clusters:
        clusters[a] = {a, b}
    if b not in clusters:
        clusters[b] = {a, b}

    if clusters[a] == clusters[b]:
        continue
    cluster = clusters[a]
    cluster.update(clusters[b])
    for entry in clusters[b]:
        clusters[entry] = cluster

    if len(clusters[a]) == len(boxes):
        helper.print_result_and_time(a[0] * b[0])
        break
