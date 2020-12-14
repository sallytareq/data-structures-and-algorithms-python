from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue
import pytest

def test_init():
    q = PseudoQueue()
    actual1 = q.stack1.top
    actual2 = q.stack2.top
    expected1 = None
    expected2 = None
    assert actual1 == expected1
    assert actual2 == expected2

def test_enqueue():
    q = PseudoQueue()
    q.enqueue(1)
    actual1 = q.stack1.top.value
    actual2 = q.stack2.top
    expected1 = 1
    expected2 = None
    assert actual1 == expected1
    assert actual2 == expected2

def test_dequeue():
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    actual = q.dequeue()
    expected = 1
    assert actual == expected
