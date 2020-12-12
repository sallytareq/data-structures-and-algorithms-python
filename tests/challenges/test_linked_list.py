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

Challenge - 07:
    Tests:
        - k is greater than the length of the linked list
        - k and the length of the list are the same
        - k is not a positive integer
        - the linked list is of a size 1
        - k is in the middle of the linked list

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
    print(actual)
    expected = '{ 8 } -> { 5 } -> { 3 } -> { 7 } -> { 1 } -> NULL'
    assert expected == actual



# after and before:
def test_before_head(before_after):
    before_after.insertBefore(1,0)
    actual = before_after.head.value
    expected = 0
    assert expected == actual

def test_after_head(before_after):
    before_after.insertAfter(1,10)
    actual = before_after.head.next.value
    expected = 10
    assert expected == actual

def test_after_five(before_after):
    before_after.insertAfter(5,11)
    actual = before_after.includes(11)
    expected = True
    assert expected == actual

def test_before_seven(before_after):
    before_after.insertBefore(7,12)
    actual = before_after.includes(12)
    expected = True
    assert expected == actual

def test_after_end(before_after):
    before_after.insertAfter(9,13)
    actual = before_after.includes(13)
    expected = True
    assert expected == actual



#kthFromEnd
def test_k_greater(kth):
    k = 10
    actual = kth.kthFromEnd(k)
    expected = "Invalid Input"
    assert expected == actual

def test_k_length(kth):
    k = 9
    actual = kth.kthFromEnd(k)
    expected = 1
    assert expected == actual

def test_k_negative(kth):
    k = -1
    actual = kth.kthFromEnd(k)
    expected = "Invalid Input"
    assert expected == actual

def test_k_middle(kth):
    k = 4
    actual = kth.kthFromEnd(k)
    expected = 5
    assert expected == actual

def test_k_one(kth):
    k = 1
    actual = kth.kthFromEnd(k)
    expected = 8
    assert expected == actual

def test_k_zero(kth):
    k = 0
    actual = kth.kthFromEnd(k)
    expected = 9
    assert expected == actual

def test_k_size_one():
    lst = LinkedList()
    lst.insert(3)
    k = 1
    actual = lst.kthFromEnd(k)
    expected = 3
    assert expected == actual





@pytest.fixture
def linked():
    linked = LinkedList()
    linked.links = []
    linked.insert(3)
    linked.insert(5)
    linked.insert(8)
    linked.append(7)
    linked.append(1)

    return linked

@pytest.fixture
def kth():
    kth = LinkedList()
    kth.links = []
    kth.insert(1)
    kth.append(2)
    kth.append(3)
    kth.append(4)
    kth.append(5)
    kth.append(6)
    kth.append(7)
    kth.append(8)
    kth.append(9)
    return kth

@pytest.fixture
def before_after():
    before_after = LinkedList()
    before_after.links = []
    before_after.insert(1)
    before_after.append(2)
    before_after.append(3)
    before_after.append(4)
    before_after.append(5)
    before_after.append(6)
    before_after.append(7)
    before_after.append(8)
    before_after.append(9)
    
    return before_after