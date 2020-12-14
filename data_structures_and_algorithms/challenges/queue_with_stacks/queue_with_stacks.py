from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Stack , Queue

class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self , val):
        self.stack1.push(val)

    def dequeue(self):
        while range(0,self.stack1.size):
            self.stack2.push(self.stack1.pop())
        
        popped = self.stack2.pop()

        while range(0,self.stack2.size):
            self.stack1.push(self.stack2.pop())

        return popped


if __name__ == "__main__":
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    
    x = q.dequeue()
    print(x)
    y = q.dequeue()
    print(y)
    z = q.dequeue()
    print(z)
    n = q.dequeue()
    print(n)


