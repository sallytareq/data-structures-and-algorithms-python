"""
A function called zipLists which takes two linked lists as arguments. 
Zip the two linked lists together into one so that the nodes alternate 
between the two lists and return a reference to the head of the zipped list. 
Try and keep additional space down to O(1). 
"""

def zipLists(list1 , list2):
    ln = len(list1) + len(list2)
    index_list1 = 1
    index_list2 = 0
        
    while index_list1 in range(0,ln):
        list1.insert(index_list1,list2[index_list2])
        index_list1 += 2
        index_list2 += 1
        
    return list1

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# actual = zipLists(list1,list2)[1]
# print(actual)