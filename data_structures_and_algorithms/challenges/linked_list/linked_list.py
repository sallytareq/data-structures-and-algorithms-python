"""
Create a Node class that has properties for the value stored in the Node, 
and a pointer to the next Node.

Within your LinkedList class, include a head property. 

Upon instantiation, an empty Linked List should be created.

Define a method called insert which takes any value as an argument 
and adds a new node with that value to the head of the list 
with an O(1) Time performance.

Define a method called includes which takes any value as an argument 
and returns a boolean result depending on whether that value exists 
as a Node’s value somewhere within the list.

Define a method called toString (or __str__ in Python) which takes in no arguments 
and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    links = []
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            current.previous = node
            node.next = self.head
            self.head = node

        LinkedList.links.insert(0, self.head.value)
        self.size += 1
    
    def includes(self, num):
        for x in LinkedList.links:
            if x == num:
                return True
        else: 
            return False

    def __len__(self):
        return self.size

    def __str__(self):
        start = "{ "
        curly = " } -> { "
        string = curly.join(str(n) for n in LinkedList.links)
        end = " } -> NULL"
        return f"{start}{string}{end}"


if __name__ == "__main__":
    LinkedList.links = []
    lnk = LinkedList()
    lnk.insert(5)
    x = lnk.size
    print(x)
    lnk.insert(8)
    y = lnk.size
    p = lnk.head.value
    n = lnk.head.next.value
    print(y , p , n)
    t = lnk.includes(5)
    f = lnk.includes(3)
    print(t , f )
    s = lnk
    print(s)
