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

Code Challenge 16:

     Write tests to prove the following functionality:
        - Can successfully determine the maximum value in a tree

Code Challenge 17:

     Write tests to prove the following functionality:
        - Can successfully return a collection from a breadth-first traversal 

"""

# CC15
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


## CC16
def test_max_val(bst):
    actual = bst.find_maximum_value()
    expected = 9
    assert expected == actual

    bst.add(12)
    bst.add(24)
    bst.add(10)
    bst.add(7)

    actual_1 = bst.find_maximum_value()
    expected_1 = 24
    assert expected_1 == actual_1

def test_max_val_with_init():
    tree = BinarySearchTree(7)
    tree.add(6)
    tree.add(3)
    tree.add(2)
    tree.add(5)
    tree.add(1)
    actual = tree.find_maximum_value()
    expected = 7
    assert expected == actual

def test_max_val_empty():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = "Tree is empty"
    assert expected == actual

def test_max_val_tree(maximum):
    actual = maximum.find_maximum_value()
    expected = 14
    assert expected == actual

# CC17
def test_post_order(bt):
    actual = bt.breadth_first()
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert expected == actual


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

@pytest.fixture
def bt():
    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)
    return bt

@pytest.fixture
def maximum():
    maximum = BinaryTree(2)
    maximum.root.left = Node(-1)
    maximum.root.right = Node(3)
    maximum.root.left.left = Node(7)
    maximum.root.left.left.left = Node(10)
    maximum.root.left.left.right = Node(5)
    maximum.root.left.right = Node(14)
    maximum.root.right.left = Node(6)
    maximum.root.right.right = Node(9)
    return maximum
