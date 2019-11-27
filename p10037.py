# UVA Problem 10037: Bridge
import collections


def new_traverse_bridge(people: list):
    def ordered_append(deck: collections.deque, item):
        """ Inserts an item before or after current item in deck, smallest first"""
        if item < deck[0]:
            deck.appendleft(item)
        else:
            deck.append(item)

    people.sort()
    flashlight_location = "start"
    traverse_order = []
    if len(people) == 1:
        traverse_order.append(people[0])
        return traverse_order
    if len(people) == 2:
        traverse_order.append([people[0], people[1]])
        return traverse_order
    at_start = collections.deque(people)
    shuttlers_at_start = collections.deque([at_start.popleft(), at_start.popleft()])  # the two fastest
    shuttlers_at_end = collections.deque()
    fastest = shuttlers_at_start[0]
    second_fastest = shuttlers_at_start[1]
    while at_start or shuttlers_at_start:
        if flashlight_location == "start":
            moving_people = []
            if not shuttlers_at_end:
                moving_people = [shuttlers_at_start.popleft(), shuttlers_at_start.popleft()]
                shuttlers_at_end = collections.deque(moving_people)
            elif len(at_start) + len(shuttlers_at_start) == 2:
                moving_people = [shuttlers_at_start.popleft(), at_start.pop()]
                ordered_append(shuttlers_at_end, moving_people[0])
            elif at_start[-2] > 2 * second_fastest - fastest:
                moving_people = [at_start.pop(), at_start.pop()]
            else:  # send fastest and slowest
                moving_people = [shuttlers_at_start.popleft(), at_start.pop()]
                ordered_append(shuttlers_at_end, moving_people[0])
            moving_people.sort()
            traverse_order.append(moving_people)
            flashlight_location = "end"
        else:
            traverse_order.append(shuttlers_at_end[0])
            shuttlers_at_start.append(
                shuttlers_at_end.popleft())  # since fastest one is always sent back first, this will always result in ordered deque
            flashlight_location = "start"
    return traverse_order


def total(order: list):
    result = 0
    for e in order:
        if type(e) == list:
            result += max(e)
        else:
            result += e
    return result


def print_order(order: list):
    """ order: list of pairs and numbers"""
    print(total(order))
    for e in order:
        if type(e) == list:
            print(f"{e[0]} {e[1]}")
        else:
            print(e)


def solve_problem(people):
    answer = new_traverse_bridge(people)
    print_order(answer)


test_cases = int(input())
people = [[] for x in range(test_cases)]

for x in range(test_cases):
    input()  # skip blank line
    people_count = input()
    for y in range(int(people_count)):
        person = int(input())
        people[x].append(person)

for i, case in enumerate(people):
    if test_cases > i > 0:
        print()
    solve_problem(case)
