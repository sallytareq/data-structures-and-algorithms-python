from data_structures_and_algorithms.challenges.tree.tree import BinaryTree, Node

def tree_intersection(one,two):
    if one.root == None or two.root == None:
        return 'Invalid Input'
    
    t_one = one.preOrder()
    t_two = two.preOrder()

    t_one_set = set(t_one)
    print(t_one_set)

    duplicates = []

    for x in t_two:
        if x in t_one_set:
            duplicates.append(x)
    
    if len(duplicates) == 0:
        return 'No duplicates'
    return duplicates


if __name__ == "__main__":
    one = BinaryTree(1)
    one.root.left = Node(2)
    one.root.right = Node(3)
    one.root.left.left = Node(4)
    one.root.left.left.left = Node(8)
    one.root.left.left.right = Node(9)
    one.root.left.right = Node(5)
    one.root.right.left = Node(6)
    one.root.right.right = Node(7)

    two = BinaryTree(8)
    two.root.left = Node(7)
    two.root.right = Node(13)
    two.root.left.left = Node(24)
    two.root.left.left.left = Node(18)
    two.root.left.left.right = Node(29)
    two.root.left.right = Node(4)
    two.root.right.left = Node(0)
    two.root.right.right = Node(17)

    print(tree_intersection(one,two))

