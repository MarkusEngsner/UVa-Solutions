from collections import namedtuple
from math import inf, ceil


Road = namedtuple('Road', 'destination capacity')


class City:
    def __init__(self, index):
        self.widest_start = 0
        self.roads = []
        self.processed = False
        self.discovered = False
        self.index = index

    #    def __repr__(self):
    #        return f"{self.index + 1}; {self.widest_start}"

    def add_road(self, destination, capacity):
        self.roads.append(Road(destination, capacity))

    def djikstra_widest(self, end):
        self.discovered = True
        q = []
        v = self
        while v is not end:
            for u, e in v.roads:
                capacity = min(v.widest_start, e)
                if not u.discovered:
                    u.discovered = True
                    u.widest_start = capacity
                    q.append(u)
                    q.sort()
                elif not u.processed and capacity > u.widest_start:
                    u.widest_start = capacity
                    q.sort()
            v.processed = True
            if not q:
                return 10
            v = q.pop()
        return v.widest_start

    def initialize_widest_path(self, end):
        self.widest_start = inf
        return self.djikstra_widest(end)

    def __lt__(self, other):
        return self.widest_start < other.widest_start  # Inverted for heapq


def trips(start, dest, passengers, cities):
    if start == dest:
        return 0
    width = cities[start].initialize_widest_path(cities[dest])
    if width == 1:
        return 0
    return ceil(passengers / (width - 1))


def main():
    city_count, road_count = (int(x) for x in (input().split()))
    n = 1
    while city_count or road_count:
        cities = [City(x) for x in range(city_count)]
        for x in range(road_count):
            a, b, capacity = (int(x) for x in (input().split()))
            cities[a - 1].add_road(cities[b - 1], capacity)
            cities[b - 1].add_road(cities[a - 1], capacity)
        start, dest, passengers = (int(x) for x in (input().split()))
        ans = trips(start - 1, dest - 1, passengers, cities)
        print("Scenario #{}".format(n))
        print("Minimum Number of Trips = {}".format(ans))
        print()
        line = input()
        while not line:
            line = input()
        city_count, road_count = (int(x) for x in line.split())
        n += 1


main()
