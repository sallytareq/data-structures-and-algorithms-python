from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

"""
Insersion Tests:
    - Valid lists:
        [1,2,3,4]   -> [1,2,8,3,4] 
        [1,2,3,4,5] -> [1,2,3,8,4,5]
    - Special lists:
        []  -> [8]
        [0] -> [0,8]
    - Invalid lists:
        10   -> 'Invalid Input'
        '10' -> 'Invalid Input'
"""
even = [1,2,3,4]
odd = [1,2,3,4,5]

# Valid lists
def test_even_list():
    actual = insertShiftArray(even, 8)
    expected = [1,2,8,3,4]
    assert actual == expected

def test_odd_list():
    actual = insertShiftArray(odd, 8)
    expected = [1,2,3,8,4,5]
    assert actual == expected

# Special lists
def test_empty_list():
    actual = insertShiftArray([], 8)
    expected = [8]
    assert actual == expected

def test_one_list():
    actual = insertShiftArray([0], 8)
    expected = [0,8]
    assert actual == expected

# Invalid lists
def test_not_list_num():
    actual = insertShiftArray(10, 8)
    expected = 'Invalid Input'
    assert actual == expected

def test_not_list_string():
    actual = insertShiftArray('10', 8)
    expected = 'Invalid Input'
    assert actual == expected