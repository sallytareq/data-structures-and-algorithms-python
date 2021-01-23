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

**Challenge 17**
Extend BinaryTree class:
    - "breadth_first" that will return a list of the values in the tree 
      in the order they were encountered.


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
            # self.max_val = value
        else:
            self.root = None
            # self.max_val = 0

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
    
    # def breadth_first(self):
    #     queue = Queue()
    #     output = []
    #     queue.enqueue(self.root)
    #     def _walk(node):
    #         if not node:
    #             return
    #         while queue.front:
    #             node = queue.dequeue()s
    #             output.append(node.value)
    #             # print(node.value)
    #             # print(output)
    #             if node.left:
    #                 # print(node.left.value)
    #                 queue.enqueue(node.left)
    #             if node.right:
    #                 # print(node.right.value)
    #                 queue.enqueue(node.right)
    #             _walk(node.left)
    #             _walk(node.right)                
    #     _walk(self.root)
    #     return output

    def breadth_first(self):
        if self.root:
            queue = Queue()
            output = []
            queue.enqueue(self.root)
            while queue.front:
                node = queue.dequeue()
                output.append(node.value)
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return output
        else: return "empty"
    
    # def max_checker(self,val):
    #     if val > self.max_val:
    #         self.max_val = val
    
    # def find_maximum_value(self):
    #     return self.max_val
    
    def find_maximum_value(self):
        if not self.root:
            return "Tree is empty"
        
        max_val = self.root.value
        current = self.root
        def max_checker(current, max_val):
            if current.value >= max_val:
                max_val = current.value
            if current.left:
                left = max_checker(current.left, max_val)
                if left > max_val:
                    max_val = left
            if current.right:
                right = max_checker(current.right, max_val)
                if right > max_val:
                    max_val = right

            return max_val
        
        return max_checker(current, max_val) 

class BinarySearchTree(BinaryTree):
    def add(self, value):
        # self.max_checker(value)
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

# def merge(bt1,bt2):
#     if not bt1.root and not bt2.root:
#         return "Invalid"
    
#     if not bt.root:
#         return bt2
    
#     if not bt.root:
#         return bt1
    

#     def _walk(node1,node2):

#         new_node = Node(node1.value + node2.value)
        
#         if node1.left and node2.left:
#             new_node.left = _walk(node1.left,node2.left)
#         else:
#             if node2.left:
#                 new_node.left = node2.left
#             if node1.left:
#                 new_node.left = node1.left
        
#         if node1.right and node2.right:
#             new_node.right = _walk(node1.right,node2.right)
#         else:
#             if node2.right:
#                 new_node.right = node2.right
#             if node1.right:
#                 new_node.right = node1.right

#         return new_node

#     new = BinaryTree()
#     new.root = _walk(bt1.root,bt2.root)
#     return new

def merge(bt1,bt2):

    def _walk(node1,node2):

        node1.value += node2.value
        
        if node1.left and node2.left:
            _walk(node1.left,node2.left)
        else:
            if node2.left:
                node1.left = node2.left

        if node1.right and node2.right:
            _walk(node1.right,node2.right)
        else:
            if node2.right:
                node1.right = node2.right
    _walk(bt1.root,bt2.root)
    return bt1

def sum_bt(bt1):
    def _walk(node):
        if node:
            total = node.value
            if node.left:
                total += _walk(node.left)
            if node.right:
                total += _walk(node.right)
            return total
            
    return _walk(bt1.root)

def third_largest(bt):
    if not bt.root:
        return "Invalid"
    
    traversed = []
    def _traversal(node):
        if node:
            _traversal(node.left)
            traversed.append(node.value)
            _traversal(node.right)

    _traversal(bt.root)
    print(traversed)
    for x in range(0,len(traversed)):
        for i in range(x+1, len(traversed)):
            if traversed[x]>traversed[i]:
                traversed[x],traversed[i] = traversed[i],traversed[x]
    print(traversed)
    
    return traversed[len(traversed)-3]

       


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
        # 8  9

        #         1
        #     2       3
        #   4   5   6   7
        # 8        1


        #         2
        #     1       3
        #   7   14       9
        # 10  5


        #           3
        #      3          6
        #   11   19     6   16
        # 18  5        1

    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.left.left = Node(8)

    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.left.left = Node(1)
    bt.root.right.right = Node(7)

    maximum = BinaryTree(2)
    maximum.root.left = Node(1)
    maximum.root.right = Node(3)
    maximum.root.left.left = Node(7)
    maximum.root.left.left.left = Node(10)
    maximum.root.left.left.right = Node(5)
    maximum.root.left.right = Node(14)
    
    maximum.root.right.right = Node(9) 
    # [1,2,3,5,7,9,10,14]
    # [3,3,6,]

    print(bt.preOrder())
    print(maximum.preOrder())
    x = merge(bt,maximum)
    print(x.preOrder())
    # print(f"Max value = {x}")

    bt1 = BinaryTree(1)
    bt1.root.left = Node(2)
    bt1.root.right = Node(3)
    bt1.root.left.left = Node(4)
    print(sum_bt(bt1))

    print(third_largest(maximum))


























































































