# Singly Linked List

Working with linked lists.

## Challenge

Creating node and a linked list class and then:

**Challenge 05:**

* Within your LinkedList class, include a head property.
* Upon instantiation, an empty Linked List should be created.
* Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
* Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
* Define a method `__str__` which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:

   >  "{ a } -> { b } -> { c } -> NULL"

**Challenge 06:**

* append(value) adds a new node to the end of the list
* insertBefore(value, newVal) adds a new node immediately before the first value node
* insertAfter(value, newVal) adds a new node immediately after the first value node

## Approach & Efficiency

I created a class which included the required methods.

## API

Available methods:
| Method | Usage|
| --- | --- |
| `LinkedList()` | Create empty linked list |
| `.insert()` | Add node to the beginning of the list |
| `.includes(num)` | Looks into list and checks if the list includes the value `num` |
| `str("LIST NAME")` | Returns a string representing all the values in the Linked List, formatted as: <br> "{ a } -> { b } -> { c } -> NULL" |
| `len("LIST NAME")` | Returns how many nodes are in the list |
| `append(VALUE)` | adds a new node to the end of the list |
| `insertAfter(value, newVal)` | adds a new node immediately after the first value node |
| `insertBefore(value, newVal)` |  adds a new node immediately before the first value node |