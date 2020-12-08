from data_structures_and_algorithms.challenges.ll_zip.ll_zip import zipLists

def test_merged_head():
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,10]
    expected = list1[0]
    actual = zipLists(list1,list2)[0]
    assert expected == actual

def test_merged_in_list():
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    actual = zipLists(a,b)
    expected = [1,6,2,7,3,8,4,9,5,10]
    assert expected == actual    

def test_length():
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,10]
    actual = len(zipLists(list1,list2))
    expected = 10
    assert expected == actual

def test_single_elements():
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    expected = [1,6,2,7,3,8,4,9,5,10]
    y = 0
    for x in range(10):
        if x%2 == 0:
            actual = a[y]
        else:
            actual = b[y]
            y +=1
        assert expected[x] == actual 





    