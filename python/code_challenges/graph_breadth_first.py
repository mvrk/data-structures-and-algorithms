import collections
from data_structures.graph import Graph


def breadth_first(graph, root):

    visited = set()
    queue = collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                print(neighbor)
                queue.append(neighbor)

