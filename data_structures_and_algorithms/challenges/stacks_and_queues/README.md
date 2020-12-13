# Stacks and Queues

Working with Stacks and Queues

## Challenge

**Challenge 10**

* Can successfully push onto a stack
* Can successfully push multiple values onto a stack
* Can successfully pop off the stack
* Can successfully empty a stack after multiple pops
* Can successfully peek the next item on the stack
* Can successfully instantiate an empty stack
* Calling pop or peek on empty stack raises exception
* Can successfully enqueue into a queue
* Can successfully enqueue multiple values into a queue
* Can successfully dequeue out of a queue the expected value
* Can successfully peek into a queue, seeing the expected value
* Can successfully empty a queue after multiple dequeues
* Can successfully instantiate an empty queue
* Calling dequeue or peek on empty queue raises exception

## Approach & Efficiency

I created a class which included the required methods.

## API

Available methods for Stacks:
| Method | Usage|
| --- | --- |
| `push(VAL)` | takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance |
| `pop()` |  removes the node from the top of the stack, and returns the node’s value |
| `peek()` |  returns the value of the node located on top of the stack, without removing it from the stack |
| `isEmpty()` | returns a boolean indicating whether or not the stack is empty |

Available methods for Queues:
| Method | Usage|
| --- | --- |
| `enqueue(VAL)` |  takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance. |
| `dequeue()` | removes the node from the front of the queue, and returns the node’s value |
| `peek()` | returns the value of the node located in the front of the queue, without removing it from the queue |
| `isEmpty()` | returns a boolean indicating whether or not the queue is empty |
