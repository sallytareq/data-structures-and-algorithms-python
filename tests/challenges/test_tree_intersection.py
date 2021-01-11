"""
Code Challenge 32:
    - Write a function called tree_intersection that takes two binary tree parameters.
    - Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.
"""
import pytest
from data_structures_and_algorithms.challenges.tree.tree import BinaryTree, Node
from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection


def test_empty_tree():
    one = BinaryTree()
    two = BinaryTree()
    actual = tree_intersection(one,two)
    expected = 'Invalid Input'
    assert expected == actual

def test_true(one,two):
    actual = tree_intersection(one,two)
    expected = [8, 7, 4]
    assert expected == actual

def test_false(one,three):
    actual = tree_intersection(one,three)
    expected = 'No duplicates'
    assert expected == actual


@pytest.fixture
def one():
    one = BinaryTree(1)
    one.root.left = Node(2)
    one.root.right = Node(3)
    one.root.left.left = Node(4)
    one.root.left.left.left = Node(8)
    one.root.left.left.right = Node(9)
    one.root.left.right = Node(5)
    one.root.right.left = Node(6)
    one.root.right.right = Node(7)

    return one

@pytest.fixture
def two():
    two = BinaryTree(8)
    two.root.left = Node(7)
    two.root.right = Node(13)
    two.root.left.left = Node(24)
    two.root.left.left.left = Node(18)
    two.root.left.left.right = Node(29)
    two.root.left.right = Node(4)
    two.root.right.left = Node(0)
    two.root.right.right = Node(17)

    return two

@pytest.fixture
def three():
    three = BinaryTree(28)
    three.root.left = Node(17)
    three.root.right = Node(13)
    three.root.left.left = Node(24)
    three.root.left.left.left = Node(18)
    three.root.left.left.right = Node(29)
    three.root.left.right = Node(14)
    three.root.right.left = Node(0)
    three.root.right.right = Node(17)

    return three