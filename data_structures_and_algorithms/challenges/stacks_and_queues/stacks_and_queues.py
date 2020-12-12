class Node:
    def __init__(self, value):

        self.value = value
        self.next = None

class Stack:
    
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        try:
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            return popped.value
        except:
            return "The Stack is empty"

    def peek(self):
        try: 
            return self.top.value
        except:
            return "The Stack is empty"

    def isEmpty(self):
        if self.top == None:
            return True
        else: 
            return False


class Queue:
    
    def __init__(self):
        self.front = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.front == None:
            self.front = node
        else:
            current = self.front
            while current.next != None:
                current = current.next
            current.next = node
            node.previous = current
            node.next = None
        self.size += 1
    
    def dequeue(self):
        try:
            removed = self.front
            self.front = self.front.next
            self.size -= 1
            return removed.value
        except:
            return "The Queue is empty"

    def peek(self):
        try: 
            return self.front.value
        except:
            return "The Queue is empty"

    def isEmpty(self):
        if self.front == None:
            return True
        else: 
            return False
