from data_structures_and_algorithms.challenges.graph.graph import Graph

def depth_first(graph):
    visited = set()
    def _walk(visited, node):
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                _walk(visited, next_node)
    return visited