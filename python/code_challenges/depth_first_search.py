from data_structures.graph import Graph, Vertex


def depth_first(self, start_vertex):
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
