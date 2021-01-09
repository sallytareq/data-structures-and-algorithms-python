from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        index = self.hash(key)

        if self.map[index] == None:
            self.map[index] = LinkedList()

        self.map[index].insert([key,value])

    def get(self, key):
        index = self.hash(key)

        if self.map[index] == None:
            return 'Value not found'

        current = self.map[index].head

        while current.next != None:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        

    def contains(self, key):
        index = self.hash(key)

        if self.map[index] == None:
            return False
        
        current = self.map[index].head

        while current != None:
            if current.value[0] == key:
                return True
            current = current.next

    def hash(self, key):
        ascii_total = 0

        for ch in key:
            ascii_total += ord(ch)

        return (ascii_total * 23) % self.size



if __name__=='__main__':
    pass