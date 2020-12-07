"""
Challenge - 05:
    - Node class (node value and next node)
    - LinkedList class (head property)
    - Instantiation created an empty linked list
    - Methods:
        1. insert -> adds new node to the head of the list
        2. includes -> returns boolean depending if node exists in list
        3. __str__ -> "{ a } -> { b } -> { c } -> NULL"

Challenge - 06:
    - append(value) adds a new node to the end of the list
    - insertBefore(value, newVal) adds a new node immediately before the first value node
    - insertAfter(value, newVal) adds a new node immediately after the first value node 

Challenge - 07:
    - Create a method called kthFromEnd that takes the argument (k) and returns the node 
      that is k from the end of the linked list.
"""
class Node:
    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None

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
            self.head.previous = node
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

    def append(self, value):
        node = Node(value)
        if self.head == None:
            node.previous = self.head
            self.head = node

        else:
            current = self.head
            index = 1
            while current.next != None:
                current = current.next
                index += 1
            current.next = node
            node.previous = current

        LinkedList.links.insert(index, node.value)
        self.size += 1

    def insertBefore(self, val, newVal):
        node = Node(newVal)
        if self.head.value == val:
            node.next = self.head
            self.head = node
            index = 0
        else:
            current = self.head
            index = 1
            while current.next.value != val:
                current = current.next
                index += 1
            node.previous = current.previous
            current.previous = node
            current.next = current
            current = node
        LinkedList.links.insert(index, node.value)
        self.size += 1

    def insertAfter(self, val, newVal):
        node = Node(newVal)
        if self.head.value == val:
            node.previous = self.head
            self.head.next = node
            index = 0
        else:
            current = self.head
            index = 1
            while current.value != val:
                current = current.next
                index += 1
            node.previous = current
            node.next = current.next
            current.next = node
        LinkedList.links.insert(index, node.value)
        self.size += 1

    def kthFromEnd(self,k):
        if k < 0 or k > len(LinkedList.links):
            return "Invalid Input"
        if k == 1:
            return self.head.value
        
        index = len(LinkedList.links)-k
        counter = 0
        current = self.head
        while counter < index:
            current = current.next
            counter += 1
        num = current.value
        return num


if __name__ == "__main__":
    LinkedList.links = []
    lnk = LinkedList()
    lnk.insert(3)
    lnk.insert(5)
    # x = lnk.size
    # print(x)
    lnk.insert(8)
    # y = lnk.size
    # p = lnk.head.value
    # n = lnk.head.next.value
    # print(y , p , n)
    # t = lnk.includes(5)
    # f = lnk.includes(3)
    # print(t , f )
    s = lnk
    print(s)
    lnk.append(7)
    lnk.append(1)
    print(s)
    lnk.insertAfter(5,4)
    print(s)
    lnk.insertAfter(1,3)
    print(s)
    lnk.insertBefore(7,9)
    print(s)
    lnk.insertBefore(8,2)
    print(s)