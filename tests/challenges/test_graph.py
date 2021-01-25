"""
Challenge - 40:
    Write tests that prove:
        - Node can be successfully added to the graph
        - An edge can be successfully added to the graph
        - A collection of all nodes can be properly retrieved from the graph
        - All appropriate neighbors can be retrieved from the graph
        - The proper size is returned, representing the number of nodes in the graph

Challenge - 41:
    Write tests that prove:
        -  two nodes as input and determines if a path exists between them
"""


import pytest
from data_structures_and_algorithms.challenges.graph.graph import Graph, Node


def test_init_empty():
    graph = Graph()
    actual = graph.size()
    expected = 0
    assert expected == actual

def test_add_node():
    graph = Graph()
    graph.add_node(5)
    actual = len(graph.adjacency_list)
    expected = 1
    assert expected == actual

def test_nodes():
    graph = Graph()
    graph.add_node(5)   
    graph.add_node(4)    
    graph.add_node(3)    
    actual = [x.value for x in graph.get_nodes()]
    expected = [5,4,3]
    assert expected == actual

def test_size():
    graph = Graph()
    graph.add_node(5)   
    graph.add_node(4)    
    graph.add_node(3)   
    actual = graph.size()
    expected = 3
    assert expected == actual

def test_neighbors():
    graph = Graph()
    graph.add_node(5) 
    graph.add_node(4)  
    nodes = graph.adjacency_list.keys()
    graph.add_edge(nodes[0], nodes[1])
    actual = graph.get_neighbors(nodes[0])
    expected = 0
    assert expected == actual

# def test_():
#     actual = 
#     expected =
#     assert expected == actual

# def test_():
#     actual = 
#     expected =
#     assert expected == actual

# def test_():
#     actual = 
#     expected =
#     assert expected == actual

# def test_():
#     actual = 
#     expected =
#     assert expected == actual

# def test_():
#     actual = 
#     expected =
#     assert expected == actual