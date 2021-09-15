from dag import *

equipments = {0: "undershorts", 1: "socks", 2: "compression shorts",
              3: "hose", 4: "cup", 5: "pants", 6: "skates",
              7: "leg pads", 8: "T-shirt", 9: "chest pad",
              10: "sweater", 11: "mask", 12: "catch glove", 13: "blocker"}

nodes = list(equipments.keys())
edges = [(0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5), (5, 6),
         (5, 10), (6, 7), (7, 12), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13)]

import random
random.shuffle(edges)

graph = Graph()
for node in nodes:
    graph.insert_node(node)

for node_from, node_to in edges:
    graph.insert_edge(node_from, node_to)

def topologicalSort(graph):
    """Sort an unweighted dag"""
    linear_order = []
    in_degree = [0] * len(graph)
    for edge in graph.get_edge_list():
        in_degree[edge.node_to] += 1

    next = [i for i in range(len(in_degree)) if in_degree[i] == 0]
    while next != []:
        u = next.pop(0)
        linear_order.insert(len(linear_order), u)
        for edge in graph.get_edge_list():
            if edge.node_from == u:
                in_degree[edge.node_to] -= 1
                if in_degree[edge.node_to] == 0:
                    next.insert(0, edge.node_to)

    return linear_order

keys = topologicalSort(graph)

output = []
for num in keys:
    output.append(equipments[num])
print(output)