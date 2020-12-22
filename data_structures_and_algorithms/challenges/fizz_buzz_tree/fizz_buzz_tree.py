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

    fb = bt

    # bt_arr = bt.preOrder()
    # fb_arr = []
    # for x in bt_arr:
    #     if x%3 == 0 and x%5 == 0:
    #         fb_arr.append(Node("FizzBuzz"))
    #     elif x%3 == 0:
    #         fb_arr.append(Node("Fizz"))
    #     elif x%5 == 0:
    #         fb_arr.append(Node("Buzz"))
    #     else:
    #         fb_arr.append(Node(str(x)))

    def _walk(node):
        if node != None:
            if node.value % 3 == 0 and node.value % 5 == 0:
                node.value = "FizzBuzz"
            elif node.value % 3 == 0:
                node.value = "Fizz"
            elif node.value % 5 == 0:
                node.value = "Buzz"
            else:
                node.value = str(node.value)
        
            # fb_arr.append(node.value)
            _walk(node.left)
            _walk(node.right)
            
    _walk(fb.root)
    
    # print(bt_arr)
    # print(fb_arr)
    return fb
       

if __name__ == "__main__":
    bt = BinaryTree(11)
    bt.root.left = Node(15)
    bt.root.right = Node(3)
    bt.root.left.left = Node(14)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(2)

    fizz_buzz_tree(bt)

    assert type(bt) == BinaryTree 
