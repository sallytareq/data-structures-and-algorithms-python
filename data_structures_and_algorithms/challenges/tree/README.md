# Trees

Create binary trees and binary search tree

## Challenge

**Code Challenge 15:**

Write tests to prove the following functionality:
    - Can successfully instantiate an empty tree
    - Can successfully instantiate a tree with a single root node
    - Can successfully add a left child and right child to a single root node
    - Can successfully return a collection from a preOrder traversal
    - Can successfully return a collection from an inOrder traversal
    - Can successfully return a collection from a postOrder traversal

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
