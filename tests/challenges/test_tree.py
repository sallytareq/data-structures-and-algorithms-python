import pytest
from data_structures_and_algorithms.challenges.tree.tree import Node , BinaryTree , BinarySearchTree

"""
Code Challenge 15:

    Write tests to prove the following functionality:
        - Can successfully instantiate an empty tree
        - Can successfully instantiate a tree with a single root node
        - Can successfully add a left child and right child to a single root node
        - Can successfully return a collection from a preOrder traversal
        - Can successfully return a collection from an inOrder traversal
        - Can successfully return a collection from a postOrder traversal        
"""

def test_empty_tree():
    empty = BinaryTree()
    actual = empty.root
    expected = None
    assert expected == actual

def test_tree_with_root():
    tree = BinaryTree(9)
    actual = tree.root.value
    expected = 9
    assert expected == actual

def test_add_left():
    tree = BinarySearchTree(6)
    tree.add(3)
    actual = tree.root.left.value
    expected = 3
    assert expected == actual

def test_add_right():
    tree = BinarySearchTree(6)
    tree.add(9)
    actual = tree.root.right.value
    expected = 9
    assert expected == actual

def test_pre_order(bst):
    actual = bst.preOrder()
    expected = [4, -1, 3, 9, 6, 5, 8]
    assert expected == actual

def test_in_order(bst):
    actual = bst.inOrder()
    expected = [-1, 3, 4, 5, 6, 8, 9]
    assert expected == actual

def test_post_order(bst):
    actual = bst.postOrder()
    expected = [3, -1, 5, 8, 6, 9, 4]
    assert expected == actual

def test_contains(bst):
    actual_t = bst.contains(8)
    expected_t = True
    assert expected_t == actual_t

    actual_f = bst.contains(7)
    expected_f = False
    assert expected_f == actual_f

@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    return bst 
