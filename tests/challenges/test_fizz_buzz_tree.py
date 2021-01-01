import pytest
from data_structures_and_algorithms.challenges.tree.tree import BinaryTree, Node
from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree

def test_valid(bt):
    actual = fizz_buzz_tree(bt).preOrder()
    expected = ['11', 'FizzBuzz', '14', 'Buzz', 'Fizz', 'Fizz', '2']
    assert expected == actual

def test_invalid():
    actual = fizz_buzz_tree("Hello World")
    expected = "Invalid Input"
    assert expected == actual 
    
    actual = fizz_buzz_tree([1,2,3,4])
    expected = "Invalid Input"
    assert expected == actual 

    actual = fizz_buzz_tree(1)
    expected = "Invalid Input"
    assert expected == actual 

    actual = fizz_buzz_tree((1,2))
    expected = "Invalid Input"
    assert expected == actual 

def test_empty():
    tree = BinaryTree()
    actual = fizz_buzz_tree(tree)
    expected = "Tree is empty"
    assert expected == actual

def test_duplication(bt):
    actual = fizz_buzz_tree(bt).preOrder()
    expected = bt.preOrder()
    assert expected != actual


@pytest.fixture
def bt():
    bt = BinaryTree(11)
    bt.root.left = Node(15)
    bt.root.right = Node(3)
    bt.root.left.left = Node(14)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(2)

    return bt