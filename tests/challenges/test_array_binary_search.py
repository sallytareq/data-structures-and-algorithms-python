from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary_search

"""
Binary Search Tests:
    - Valid cases:
        [4,8,15,16,23,42] , 15  ->  2
        [0,1,2,3,4,5,6,7] , 8   -> -1
    - Special cases:
        [] , 15   -> -1
        [4] , 15  -> -1
        [15] , 15 ->  0
    - Invalid cases:
        15 , 15     -> 'Invalid Input'
        [15] , '15' -> 'Invalid Input'

"""

# Valid
def test_there():
    actual =  binary_search([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected

def test_not_there():
    actual =  binary_search([1,2,3,4,5],8)
    expected = -1
    assert actual == expected

# Special cases
def test_single():
    actual =  binary_search([4], 15)
    expected = -1
    assert actual == expected

def test_single_valid():
    actual =  binary_search([15], 15)
    expected = 0
    assert actual == expected

def test_empty():
    actual =  binary_search([], 15)
    expected = -1
    assert actual == expected

# Invalid cases
def test_string_value():
    actual =  binary_search([15], '15')
    expected = 'Invalid Input'
    assert actual == expected

def test_not_list():
    actual =  binary_search(15, 15)
    expected = 'Invalid Input'
    assert actual == expected