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
            print(f"added to cat: {animal} {name}")
        elif animal == "dog":
            self.dog.enqueue(name)
            self.shelter.enqueue(name)
            print(f"added to dog: {animal} {name}")
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
            print(f"{pref} removed from cat")

        elif pref == "dog":

            popped = self.dog.dequeue()

            if popped == self.shelter.front.value:
                self.shelter.dequeue()
            else: 
                self.adjust(popped)

            print(f"{pref} removed from dog")


        elif pref == "shelter":
            popped = self.shelter.dequeue()

            if popped == self.cat.front.value:
                self.cat.dequeue()
            elif popped == self.dog.front.value:
                self.dog.dequeue()

            print(f"{pref} removed")

        else:
            return "Invalid Input"
        
        return popped

    def adjust(self, popped):
        current = self.shelter.front

        while current.next.value != popped:
            current = current.next
        current.next = current.next.next

