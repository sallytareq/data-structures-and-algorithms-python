"""
**Code Challenge 18:**

    Write a function called FizzBuzzTree which takes a k-ary tree as an argument and 
    determines whether or not the value of each node is divisible by 3, 5 or both. 

    Create a new tree with the same structure as the original, 
    but the values modified as follows:
        - If the value is divisible by 3, replace the value with “Fizz”
        - If the value is divisible by 5, replace the value with “Buzz”
        - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
        - If the value is not divisible by 3 or 5, simply turn the number into a String.
"""
from data_structures_and_algorithms.challenges.tree.tree import BinaryTree, Node

def fizz_buzz_tree(bt):
    if type(bt) != BinaryTree:
        return "Invalid Input"
    if not bt.root:
        return "Tree is empty"


    def _walk(bt_node):
        if bt_node != None:
            if bt_node.value % 3 == 0 and bt_node.value % 5 == 0:
                fb_node = Node("FizzBuzz")
            elif bt_node.value % 3 == 0:
                fb_node = Node("Fizz")
            elif bt_node.value % 5 == 0:
                fb_node = Node("Buzz")
            else:
                fb_node = Node(str(bt_node.value))

            if bt_node.left: fb_node.left = _walk(bt_node.left)
            if bt_node.right: fb_node.right = _walk(bt_node.right)

            return fb_node

    fb = BinaryTree()
    fb.root = _walk(bt.root) 
    
    return fb
       



if __name__ == "__main__":
    
    bt = BinaryTree(11)
    bt.root.left = Node(15)
    bt.root.right = Node(3)
    bt.root.left.left = Node(14)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(2)

    fb = fizz_buzz_tree(bt)
    print(fb.preOrder())
    print(bt.preOrder())

    assert type(bt) == BinaryTree 
