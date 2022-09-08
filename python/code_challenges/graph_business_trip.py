from data_structures.graph import Graph


def direct_flights(graph, city):
    if len(city) == 0:
        return
    nodes = {}
    for vertex in graph.get_nodes():
        nodes[vertex.value] = vertex

    cost = 0
    flag = False

    for cn in range(len(city) - 1):
        edge = graph.get_neighbors(city[cn])
        for e in edge:
            if city[cn + 1] == e.vertex:
                cost += e.weight
                flag = True

    if not flag:
        cost = 0
        flag = False
        return f'{flag},${cost}'

    return f'{flag},${cost}'
