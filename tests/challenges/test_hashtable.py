"""
Challenge - 30:
    Write tests that prove:
        - Can add a key/value to your hashtable results in the value being in the data structure
        - Can retrieve a value stored based on a key
        - Can successfully return null for a key that does not exist in the hashtable
        - Can successfully handle a collision within the hashtable
        - Can successfully retrieve a value from a bucket within the hashtable that has a collision
        - Can successfully hash a key to an in-range value
"""

import pytest
from data_structures_and_algorithms.challenges.hashtable.hashtable import Hashtable


def test_init():
    table = Hashtable(12)
    actual = len(table.map)
    expected = 12
    assert expected == actual

def test_add():
    table = Hashtable(10)
    table.add( 'a' , 1 )
    actual = table.map[1].head.value
    expected = [ 'a' , 1 ]
    assert expected == actual
    
def test_get(ht):
    actual = ht.get('cloud')
    expected = 21
    assert expected == actual

def test_get_not_found(ht):
    actual = ht.get('world')
    expected = 'Value not found'
    assert expected == actual


def test_contains_true(ht):
    actual = ht.contains('red')
    expected = True
    assert expected == actual    

def test_contains_false(ht):
    actual = ht.contains('black')
    expected = False
    assert expected == actual   

    

@pytest.fixture
def ht():
    ht = Hashtable(1024)
    ht.add( 'Hello' , 24 )
    ht.add( 'could' , 321 )
    ht.add( 'cloud' , 21 )
    ht.add( 'red' , 88 )
    ht.add( 'coldu' , 21 )
    return ht