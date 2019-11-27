from collections import deque

class Node:
    def __init__(self):
        self.discovered: bool = False
        self.color: bool = False
        self.edges = []

    def insert(self, new_node):
        self.edges.append(new_node)


def is_bicolorable(nodes: list) -> bool:
    queue = deque()
    start_node: Node = nodes[0]
    start_node.discovered = True
    start_node.color = True
    queue.append(start_node)
    while queue:
        v = queue.popleft()
        for u in v.edges:
            if u.discovered:
                if u.color == v.color:
                    return False
            else:
                u.discovered = True
                u.color = not v.color
                queue.append(u)
    return True


while True:
    node_count = int(input())
    if node_count == 0:
        break
    edge_count = int(input())
    node_list = [Node() for x in range(node_count)]
    a = b = 0
    for i in range(edge_count):
        a, b = (int(x) for x in input().split())
        node_list[a].insert(node_list[b])
        node_list[b].insert(node_list[a])

    print("BICOLORABLE." if is_bicolorable(node_list) else "NOT BICOLORABLE.")
