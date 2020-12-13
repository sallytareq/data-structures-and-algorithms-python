import pytest
from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Stack, Queue 

"""
Can successfully push onto a stack
Can successfully push multiple values onto a stack
Can successfully pop off the stack
Can successfully empty a stack after multiple pops
Can successfully peek the next item on the stack
Can successfully instantiate an empty stack
Calling pop or peek on empty stack raises exception
"""

def test_push(stack):
    actual = stack.size
    expected = 2
    assert expected == actual

def test_pop(stack):
    actual = stack.pop()
    expected = 2
    assert expected == actual
    actual = stack.size
    expected = 1
    assert expected == actual

def test_peek(stack):
    actual = stack.peek()
    expected = 2
    assert expected == actual

def test_stack_isEmpty(stack):
    stack.pop()
    stack.pop()
    actual = stack.isEmpty()
    expected = True
    assert expected == actual


def test_stack_inst():
    stack1 = Stack()
    actual = stack1.top
    expected = None
    assert expected == actual

def test_except_pop(stack):
    stack.pop()
    stack.pop()
    actual = stack.pop()
    expected = "The Stack is empty"
    assert expected == actual

def test_except_peek(stack):
    stack.pop()
    stack.pop()
    actual = stack.peek()
    expected = "The Stack is empty"
    assert expected == actual

"""
Can successfully enqueue into a queue
Can successfully enqueue multiple values into a queue
Can successfully dequeue out of a queue the expected value
Can successfully peek into a queue, seeing the expected value
Can successfully empty a queue after multiple dequeues
Can successfully instantiate an empty queue
Calling dequeue or peek on empty queue raises exception
"""
def test_enqueue(queue):
    actual = queue.size
    expected = 2
    assert expected == actual

def test_dequeue(queue):
    actual = queue.dequeue()
    expected = 1
    assert expected == actual
    actual = queue.size
    expected = 1
    assert expected == actual

def test_peek(queue):
    actual = queue.peek()
    expected = 1
    assert expected == actual

def test_queue_isEmpty(queue):
    queue.dequeue()
    queue.dequeue()
    actual = queue.isEmpty()
    expected = True
    assert expected == actual


def test_queue_inst():
    queue1 = Queue()
    actual = queue1.front
    expected = None
    assert expected == actual

def test_except_dequeue(queue):
    queue.dequeue()
    queue.dequeue()
    actual = queue.dequeue()
    expected = "The Queue is empty"
    assert expected == actual

def test_except_peek(queue):
    queue.dequeue()
    queue.dequeue()
    actual = queue.peek()
    expected = "The Queue is empty"
    assert expected == actual
    

@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    return stack

@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    return queue