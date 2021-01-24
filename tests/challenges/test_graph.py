"""
Challenge - 40:
    Write tests that prove:
        - Node can be successfully added to the graph
        - An edge can be successfully added to the graph
        - A collection of all nodes can be properly retrieved from the graph
        - All appropriate neighbors can be retrieved from the graph
        - Neighbors are returned with the weight between nodes included
        - The proper size is returned, representing the number of nodes in the graph
        - A graph with only one node and edge can be properly returned
        - An empty graph properly returns null

Challenge - 41:
    Write tests that prove:
        -  two nodes as input and determines if a path exists between them
"""


import pytest
from data_structures_and_algorithms.challenges.graph.graph import Graph, Node


def test_init_empty():
    graph = Graph()
    actual = graph
    expected = None
    assert expected == actual

def test_add_node():
    graph = Graph()
    graph.add_node(5)
    actual = len(graph.adjacency_list)
    expected = 1
    assert expected == actual

# def test_():
    
#     actual = graph.add_edge(, 5, weight=1)
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