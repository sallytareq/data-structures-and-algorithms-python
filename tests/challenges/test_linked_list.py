"""
Challenge - 05:
    Write tests to prove the following functionality:
        - Can successfully instantiate an empty linked list
        - Can properly insert into the linked list
        - The head property will properly point to the first node in the linked list
        - Can properly insert multiple nodes into the linked list
        - Will return true when finding a value within the linked list that exists
        - Will return false when searching for a value in the linked list that does not exist
        - Can properly return a collection of all the values that exist in the linked list

Challenge - 06:
    Tests:
        - add a node to the end of the linked list
        - add multiple nodes to the end of a linked list
        - insert a node before a node located i the middle of a linked list
        - insert a node before the first node of a linked list
        - insert after a node in the middle of the linked list
        - insert a node after the last node of the linked list
"""
from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList, Node
import pytest


def test_empty():
    empty = LinkedList()
    actual = empty.size
    expected = 0
    assert expected == actual

def test_insert_multiple():
    linked = LinkedList()
    LinkedList.links = []
    linked = LinkedList()
    linked.insert(3)
    linked.insert(5)
    linked.insert(8)
    actual = linked.size
    expected = 3
    assert expected == actual

def test_head():
    linked = LinkedList()
    LinkedList.links = []
    linked = LinkedList()
    linked.insert(3)
    linked.insert(5)
    linked.insert(8)
    actual = linked.head.value
    expected = 8
    assert expected == actual

def test_head_next():
    linked = LinkedList()
    LinkedList.links = []
    linked = LinkedList()
    linked.insert(3)
    linked.insert(5)
    linked.insert(8)
    actual = linked.head.next.value
    expected = 5
    assert expected == actual

def test_includes_true(linked):
    actual = linked.includes(3)
    expected = True
    assert expected == actual

def test_includes_false(linked):
    actual = linked.includes(6)
    expected = False
    assert expected == actual

def test_str(linked):
    actual = str(linked)
    expected = '{ 2 } -> { 8 } -> { 5 } -> { 4 } -> { 3 } -> { 9 } -> { 7 } -> { 1 } -> { 3 } -> NULL'
    assert expected == actual


@pytest.fixture
def linked():
    linked = LinkedList()
    LinkedList.links = []
    linked = LinkedList()
    linked.insert(3)
    linked.insert(5)
    linked.insert(8)
    linked.append(7)
    linked.append(1)
    linked.insertAfter(5,4)
    linked.insertAfter(1,3)
    linked.insertBefore(7,9)
    linked.insertBefore(8,2)
    return linked
