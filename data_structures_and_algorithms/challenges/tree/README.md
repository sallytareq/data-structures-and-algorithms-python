# Trees

Create binary trees and binary search tree

## Challenge

**Challenge 15:**

Create a Node class with properties:
    - value stored of node
    - left child node
    - right child node

Create a BinaryTree class with methods:
    - preOrder
    - inOrder
    - postOrder
    *note: all return array of values in correct order.*

Create a BinarySearchTree class with methods:
    - "add" which adds a new node with that value in the correct location in the binary search tree.
    - "contains" which returns a boolean indicating whether or not the value is in the tree at least once.

**Challenge 16:**

Extend BinaryTree class:
    - "find-maximum-value" which will return the maximum value stored in the tree assuming all values stored in the tree will be numeric.

## Approach & Efficiency

I used recursion and iteration to create and search in the tree.

## API

Available methods:

| Method | Usage|
| --- | --- |
| `preOrder` | returns an array of the values, ordered root=>left=>right |
| `inOrder` | returns an array of the values, ordered left=>root=>right |
| `postOrder` | returns an array of the values, ordered left=>right=>root |
| `add(VAL)` | accepts a value, and adds a new node with that value in the correct location in the binary search tree |
| `contains(VAL)` | accepts a value, and returns a boolean indicating whether or not the value is in the tree |
| `find_maximum_value` | returns the maximum value stored in the tree |
