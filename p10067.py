import sys


def connected(v: int):
    one = v % 10
    ten = v % 100 - one
    hundred = v % 1000 - ten - one
    thousand = v % 10000 - hundred - ten - one
    result = [
        thousand + hundred + ten + below[one],
        thousand + hundred + ten + above[one],
        thousand + hundred + above[ten // 10] * 10 + one,
        thousand + hundred + below[ten // 10] * 10 + one,
        thousand + above[hundred // 100] * 100 + ten + one,
        thousand + below[hundred // 100] * 100 + ten + one,
        above[thousand // 1000] * 1000 + hundred + ten + one,
        below[thousand // 1000] * 1000 + hundred + ten + one,
    ]
    return result


def FewestTurns(start: int, end: int, edges,  discovered) -> int:
    if start == end:
        return 0
    if discovered[start] or discovered[end]:
        return -1
    queue = [start]
    cost = [-1] * 10000
    discovered[start] = True
    cost[start] = 0
    for v in queue:
        for u in edges[v]:
            if not discovered[u]:
                queue.append(u)
                cost[u] = cost[v] + 1
                discovered[u] = True
                if u == end:
                    return cost[u]
    return -1


def handle_case(edges):
    str = sys.stdin.readline()
    if str == '\n':  # To skip the newline between inputs.
        str = sys.stdin.readline()
    start_val = int(str.replace(" ", "").rstrip())
    end_val = int(sys.stdin.readline().replace(" ", "",).rstrip())
    forbidden_count = int(sys.stdin.readline().replace(" ", "",).rstrip())
    discovered = [False] * 10000
    for i in range(forbidden_count):
        discovered[int(sys.stdin.readline().replace(" ", "",).rstrip())] = True
    print(FewestTurns(start_val, end_val, edges, discovered))


above = [(x + 1) % 10 for x in range(10)]
below = [(x - 1) % 10 for x in range(10)]
edge_lookup = [connected(x) for x in range(10000)]
case_count = int(input())
for x in range(case_count):
    handle_case(edge_lookup)

