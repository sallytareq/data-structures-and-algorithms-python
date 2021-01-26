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
        if start_node not in self.adjacency_list:
            self.adjacency_list[f'{start_node}']=[{'node': end_node, 'weight':weight}]
        else:
            self.adjacency_list[f'{start_node}'].append({'node': end_node, 'weight':weight})

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, node):
        output = []
        for x in self.adjacency_list[node]:
            output.append(x)
        return output

    def size(self):
        return len(self.adjacency_list)

    def bfs(self, start_node):
        nodes = [] 
        visited = set() 
        breadth = Queue()
        breadth.enqueue(start_node)
        visited.add(start_node)
        while len(breadth)>0:
            node = breadth.dequeue()
            nodes.append(node)
            for n in self.adjacency_list[node]:
                if n not in visited:
                    breadth.enqueue(n)
                    visited.add(n)
        return nodes
    
    def path_exists(self, start_node, end_node):
        connected = self.bfs(start_node)
        set_connected = set(connected)
        if end_node in connected: 
            return True
        return False

    