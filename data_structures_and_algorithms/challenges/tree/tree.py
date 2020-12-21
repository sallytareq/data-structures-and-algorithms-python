"""
**Challenge 15**
Create a Node class with properties: 
    - value stored of node 
    - left child node
    - right child node
Create a BinaryTree class with methods:
    - preOrder
    - inOrder
    - postOrder 
        *note: all return array of values in correct order.
Create a BinarySearchTree class with methods:
    - "add" which adds a new node with that value in the correct 
      location in the binary search tree.
    - "contains" which returns a boolean indicating whether or not
      the value is in the tree at least once.

**Challenge 16**
Extend BinaryTree class:
    - "find-maximum-value" which will return the maximum value stored
      in the tree assuming all values stored in the tree will be numeric. 

"""
from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
            self.max_val = value
        else:
            self.root = None
            self.max_val = 0

    def preOrder(self):
        output = []
        def _walk(node):
            if node != None:
                output.append(node.value) 
                _walk(node.left)
                _walk(node.right)
                
        _walk(self.root)
        return output

    def inOrder(self):
        output = []
        def _walk(node):
            if node != None:
                _walk(node.left)
                output.append(node.value) 
                _walk(node.right)
                
        _walk(self.root)
        return output
    
    def postOrder(self):
        output = []
        def _walk(node):
            if node != None:
                _walk(node.left)
                _walk(node.right)
                output.append(node.value) 
                
        _walk(self.root)
        return output
    
    def breadth_first(self):
        queue = Queue()
        output = []
        def _walk(node):
            if not node:
                return

            queue.enqueue(node)
            if queue.front:
                node = queue.front.value
                output.append(queue.peek().value)

                print(output)
                if node.left:
                    _walk(node.left)
                if node.right:
                    _walk(node.right)

                queue.dequeue()
                    
     
        _walk(self.root)
        return output
    
    def max_checker(self,val):
        if val > self.max_val:
            self.max_val = val
    
    def find_maximum_value(self):
        return self.max_val

class BinarySearchTree(BinaryTree):
    def add(self, value):
        self.max_checker(value)
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
            _walk(self.root)

    def contains(self, value):
        current = self.root
        boolean = False
        while current  != None:
            if current.value == value:
                boolean = True
                break
            elif value < current.value:
                # print(f"Going left of {current.value}")
                current = current.left
            elif value > current.value:
                # print(f"Going right of {current.value}")
                current = current.right
        return boolean



if __name__ == '__main__':

    # 4, -1, 3, 9, 6, 5, 8
    # -1, 3, 4, 5, 6, 8, 9
    # 3, -1, 5, 8, 6, 9, 4  

    #        4
    #     /    \
    #  -1       9
    #    \     /
    #     3   6
    #        / \
    #       5   8
    
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    x = bst.find_maximum_value()


        #         1
        #     2       3
        #   4   5   6   7

    hi = BinaryTree(1)
    hi.root.left = Node(2)
    hi.root.right = Node(3)
    hi.root.left.left = Node(4)
    hi.root.left.right = Node(5)
    hi.root.right.left = Node(6)
    hi.root.right.right = Node(7)

    print(hi.breadth_first())
    print(f"Max value = {x}")
