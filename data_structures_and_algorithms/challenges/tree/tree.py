class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None

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

class BinarySearchTree(BinaryTree):
    def add(self, value):
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

