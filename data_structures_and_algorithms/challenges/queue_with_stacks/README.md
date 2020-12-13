# Pseudo Queue

Two stacks to function like a queue.

## Challenge

**Challenge 11**

* Create a PseudoQueue class that will implement our standard queue interface, but will internally only utilize 2 Stack objects.
* enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
* dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Approach & Efficiency

I created a class which included the required methods.

## API

Available methods:
| Method | Usage|
| --- | --- |
| `enqueue(VAL)` |  takes any value as an argument and adds a new node with that value to the back of the queue |
| `dequeue()` | removes the node from the front of the queue, and returns the node’s value |
