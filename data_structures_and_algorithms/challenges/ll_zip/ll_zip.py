"""
A function called zipLists which takes two linked lists as arguments. 
Zip the two linked lists together into one so that the nodes alternate 
between the two lists and return a reference to the head of the zipped list. 
Try and keep additional space down to O(1). 
"""

from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList,Node

# def zipLists(list1 , list2):
#     ln = len(list1) + len(list2)
#     index_list1 = 1
#     index_list2 = 0
        
#     while index_list1 in range(0,ln):
#         list1.insert(index_list1,list2[index_list2])
#         index_list1 += 2
#         index_list2 += 1
        
#     return list1

def zipLists(list1 , list2):

    current = list1.head

    while current.next != None:

        next_node = list2.head
        list2.head = list2.head.next
        next_node.next = current.next
        current.next = next_node

        current = current.next.next

    if list2.head != None:
        current = list1.head

        while current.next != None:
            current = current.next
        current.next = list2.head
        
        list2.head = None

    return list1



if __name__ == "__main__":

    list1 = LinkedList()
    list1.insert(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    print(list1)

    list2 = LinkedList()
    list2.insert(11)
    list2.insert(10)
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)
    list2.insert(6)
    print(list2)

    zipLists(list1,list2)

    print(list1.head.value)
    print(list1.head.next.value)
    print(list1.head.next.next.value)
    print(list1.head.next.next.next.value)
    print(list1.head.next.next.next.next.value)
    print(list1.head.next.next.next.next.next.value)
    print(list1.head.next.next.next.next.next.next.value)
    print(list1.head.next.next.next.next.next.next.next.value)
    print(list1.head.next.next.next.next.next.next.next.next.value)
    print(list1.head.next.next.next.next.next.next.next.next.next.value)
    print(list1.head.next.next.next.next.next.next.next.next.next.next.value)
