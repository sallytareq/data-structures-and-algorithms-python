import pytest
from data_structures_and_algorithms.challenges.hashtable.hashtable import Hashtable
from data_structures_and_algorithms.challenges.left_join.left_join import left_join

def test_invalid_string():
    hm1 = 'hi'
    hm2 = 'hello'
    actual = left_join(hm1,hm2) 
    expected = 'Invalid Input'
    assert expected == actual

def test_invalid_int():
    hm1 = 1234
    hm2 = 125
    actual = left_join(hm1,hm2) 
    expected = 'Invalid Input'
    assert expected == actual

def test_invalid_list():
    hm1 = ['key','value']
    hm2 = ['key','value']
    actual = left_join(hm1,hm2) 
    expected = 'Invalid Input'
    assert expected == actual

def test_empty_hm1(hm2):
    hm1 = Hashtable(1024)
    actual = left_join(hm1,hm2).map
    expected = [None]*1024
    assert expected == actual

def test_empty_hm2(hm1):
    hm2 = Hashtable(1024)
    output = left_join(hm1,hm2)
    for valid in output.map:
        if valid:
            n = output.hash(valid.head.value[0])
            actual =  valid.head.value
            expected = [hm1.map[n].head.value[0],hm1.map[n].head.value[1]]
            assert expected == actual

def test_valid(hm1,hm2):
    output = left_join(hm1,hm2)
    for valid in output.map:
        if valid:
            n = output.hash(valid.head.value[0])
            actual =  valid.head.value
            print(actual)
            if hm2.map[n]:
                expected = [hm1.map[n].head.value[0],hm1.map[n].head.value[1],hm2.map[n].head.value[1]]
            else:
                expected = [hm1.map[n].head.value[0],hm1.map[n].head.value[1]]
            assert expected == actual



@pytest.fixture
def hm1():
    hm1 = Hashtable(1024)
    hm1.add('fond','enamored')
    hm1.add('wrath','anger')
    hm1.add('diligent','employed')
    hm1.add('seize','grab')
    hm1.add('guide','usher')
    return hm1

@pytest.fixture
def hm2():
    hm2 = Hashtable(1024)
    hm2.add('fond','averse')
    hm2.add('wrath','delight')
    hm2.add('diligent','idle')
    hm2.add('guide','follow')
    hm2.add('flow','jam')
    return hm2