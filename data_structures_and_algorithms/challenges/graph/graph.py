from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []

    def add_edge(self, start_node, end_node, weight=1):
        pass

    def get_nodes(self):
        return [self.adjacency_list.keys()]

    def get_neighbors(self, node):
        pass


    def size(self):
        return len(self.get_nodes())

    # def bfs(self, start_node):
    #     nodes = [] 
    #     visited = set() 
    #     breadth = Queue()
    #     breadth.enqueue(start_node)
    #     visited.add(start_node)
    #     while len(breadth)>0:
    #         node = breadth.dequeue()
    #         nodes.append(node)
    #         for n in self.adjacency_list[node]:
    #             if n not in visited:
    #                 breadth.enqueue(n)
    #                 visited.add(n)
    #     return nodes
