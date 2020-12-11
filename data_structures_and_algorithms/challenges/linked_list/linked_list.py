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
    
    def __init__(self):
        self.head = None
        self.size = 0
        self.links = []

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

        self.links.insert(0, self.head.value)
        self.size += 1
    
    def includes(self, num):
        for x in self.links:
            if x == num:
                return True
        else: 
            return False

    def __len__(self):
        return self.size

    def __str__(self):
        start = "{ "
        curly = " } -> { "
        string = curly.join(str(n) for n in self.links)
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
            node.next = None

        self.links.insert(index, node.value)
        self.size += 1

    def insertBefore(self, val, newVal):
        if self.head.value == val:
            self.insert(newVal)
        else:
            node = Node(newVal)
            current = self.head.next
            index = 0
            if self.includes(val):
                while index <= self.size:
                    if current != val:
                        # print(current.value)
                        if current.next != None:
                            current = current.next
                            index += 1
                        else: break
                node.previous = current.previous
                current.previous = node
                current.next = current
                current = node    
                self.links.insert(index, node.value)
                self.size += 1
            else:
                return "invalid"            

    def insertAfter(self, val, newVal):
        if self.head.value == val:
            node = Node(newVal)
            node.previous = self.head
            self.head.next = node
            index = 0
        else:
            node = Node(newVal)
            current = self.head
            index = 1
            while current.value != val:
                current = current.next
                index += 1
                    
            node.previous = current
            node.next = current.next
            current.next = node

            self.links.insert(index, node.value)
            self.size += 1

    def kthFromEnd(self,k):
        if k < 0 or k > len(self.links):
            return "Invalid Input"
        if k == len(self.links):
            return self.head.value
        
        index = len(self.links)-k
        counter = 1
        current = self.head
        while counter < index:
            if current.next != None:
                current = current.next
            else: break
            counter += 1
        num = current.value
        return num


if __name__ == "__main__":

    # lnk = LinkedList()
    # lnk.insert(3)
    # lnk.insert(2)
    # lnk.insert(1)
    # lnk.append(4)
    # lnk.append(5)
    # lnk.append(6)

    # print(lnk.kthFromEnd(1))
    # print(lnk.kthFromEnd(2))
    # print(lnk.kthFromEnd(3))
    # print(lnk.kthFromEnd(4))
    # print(lnk.kthFromEnd(0))
    # print(lnk.kthFromEnd(-1))

    # before_after = LinkedList()
    # before_after.links = []
    # before_after.insert(1)
    # before_after.append(2)
    # before_after.append(3)
    # before_after.append(4)
    # before_after.append(5)
    # before_after.append(6)
    # before_after.append(7)
    # before_after.append(8)
    # before_after.append(9)
    # before_after.insertBefore(1,0)
    # before_after.insertAfter(1,10)
    # before_after.insertAfter(5,11)
    # before_after.insertBefore(7,12)
    # print(before_after.links)
    pass