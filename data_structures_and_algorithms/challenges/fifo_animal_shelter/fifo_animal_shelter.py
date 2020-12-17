from data_structures_and_algorithms.challenges.stacks_and_queues.stacks_and_queues import Queue

class AnimalShelter:

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.shelter = Queue()

    def enqueue(self,animal,name):
        if animal == "cat":
            self.cat.enqueue(name)
            self.shelter.enqueue(name)
            
        elif animal == "dog":
            self.dog.enqueue(name)
            self.shelter.enqueue(name)
         
        else: 
            return "Sorry! We do not accept animals that are not cat or dog"
    
    def dequeue(self, pref="shelter"):
        popped = ""
        if pref == "cat":

            popped = self.cat.dequeue()

            if popped == self.shelter.front.value:
                self.shelter.dequeue()
            else: 
                self.adjust(popped)

        elif pref == "dog":

            popped = self.dog.dequeue()

            if popped == self.shelter.front.value:
                self.shelter.dequeue()
            else: 
                self.adjust(popped)


        elif pref == "shelter":
            popped = self.shelter.dequeue()

            if popped == self.cat.front.value:
                self.cat.dequeue()
            elif popped == self.dog.front.value:
                self.dog.dequeue()


        else:
            return "Invalid Input"
        
        return popped

    def adjust(self, popped):
        current = self.shelter.front
        counter = 1
        temp = Queue()
        while current.next.value != popped:
            current = current.next
            counter += 1
        x = 0
        while x in range(0,counter):
            hold = self.shelter.dequeue()
            temp.enqueue(hold)
            x +=1
        self.shelter.dequeue()
        current = self.shelter.front
        while current != None:
            current = current.next
            hold = self.shelter.dequeue()
            temp.enqueue(hold)

        temp_current = temp.front
        while temp_current != None:
            temp_next = temp.dequeue()
            self.shelter.enqueue(temp_next)
            temp_current = temp_current.next





