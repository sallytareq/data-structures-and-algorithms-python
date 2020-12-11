from data_structures_and_algorithms.challenges.ll_zip.ll_zip import zipLists
from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList, Node
import pytest

# def test_merged_head():
#     list1 = [1,2,3,4,5]
#     list2 = [6,7,8,9,10]
#     expected = list1[0]
#     actual = zipLists(list1,list2)[0]
#     assert expected == actual

# def test_merged_in_list():
#     a = [1,2,3,4,5]
#     b = [6,7,8,9,10]
#     actual = zipLists(a,b)
#     expected = [1,6,2,7,3,8,4,9,5,10]
#     assert expected == actual    

# def test_length():
#     list1 = [1,2,3,4,5]
#     list2 = [6,7,8,9,10]
#     actual = len(zipLists(list1,list2))
#     expected = 10
#     assert expected == actual

# def test_single_elements():
#     a = [1,2,3,4,5]
#     b = [6,7,8,9,10]
#     expected = [1,6,2,7,3,8,4,9,5,10]
#     y = 0
#     for x in range(10):
#         if x%2 == 0:
#             actual = a[y]
#         else:
#             actual = b[y]
#             y +=1
#         assert expected[x] == actual 

def test_merged_head(list1):
    expected = 1
    actual = list1.head.value
    assert expected == actual

def test_merged_in_list(list1):
    current = list1.head
    index =  0
    control = [1,6,2,7,3,8,4,9,5,10,11]
    while current != None:

        actual = current.value
        expected = control[index]
        assert expected == actual
        current = current.next
        index +=1    

def test_length(list1):
    current = list1.head
    counter =  0
    while current != None:
        current = current.next
        counter +=1
    actual = counter
    expected = 11
    assert expected == actual


@pytest.fixture
def list1():
    list1 = LinkedList()

    list1.insert(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)

    list2 = LinkedList()
    list2.insert(11)
    list2.insert(10)
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)
    list2.insert(6)

    list1 = zipLists(list1,list2)

    return list1






    