class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight: int = 0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()

        edge = Edge(end_vertex, weight)

        self._adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def get_nodes(self):
        return self._adjacency_list.keys()

    def depth_first_search(self, start_vertex):
        visited = []
        visited.append(start_vertex.value)

        def traverse(vertex):
            edge = self._adjacency_list[vertex]
            for v in edge:
                my_vertex = v.vertex.value
                if my_vertex not in visited:
                    visited.append(my_vertex)
                    traverse(v.vertex)

        traverse(start_vertex)

        return visited

class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight: int):
        self.vertex = vertex
        self.weight = weight
