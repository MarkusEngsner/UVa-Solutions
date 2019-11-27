import collections


# A turtle:
# rank: int
# name: str
# position: int



def climb_up(tower, index):
    turtle = tower.pop(index)
    tower.insert(0, turtle)


def shell_sort(tower: list):
    """ Tower: list of Turtles"""
    is_sorted = False
    climb_history = []
    while not is_sorted:
        previous: dict = tower[0]
        turtle_to_move = None
        index = None
        for i, t in enumerate(tower[1:], start=1):
            if t["rank"] < previous["rank"]:
                if not turtle_to_move or t["rank"] > turtle_to_move["rank"]:
                    turtle_to_move = t
                    index = i
            else:
                previous = t
        if not turtle_to_move:
            is_sorted = True  # all elements in order
        else:
            climb_up(tower, index)
            climb_history.append(tower[0]["name"])
    return climb_history


test_cases = int(input())
for i in range(test_cases):
    turtle_count = int(input())
    turtle_original_order = []
    name_lookup = {}
    for x in range(turtle_count):
        name = input()
        turtle = {"name": name}
        turtle_original_order.append(turtle)
        name_lookup[name] = x
    for rank in range(turtle_count):
        name = input()
        current_pos = name_lookup[name]
        turtle_original_order[current_pos]["rank"] = rank
    order = shell_sort(turtle_original_order)
    for name in order:
        print(name)
    print()
