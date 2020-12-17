from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_invalid_int():
    actual = multi_bracket_validation(21)
    expected = "Invalid Input"
    assert expected == actual

def test_invalid_list():
    actual = multi_bracket_validation(["[","]"])
    expected = "Invalid Input"
    assert expected == actual

def test_valid_true_reg():
    actual = multi_bracket_validation("[]{}()")
    expected = True
    assert expected == actual

def test_valid_true_nested():
    actual = multi_bracket_validation("[{()}]")
    expected = True
    assert expected == actual

def test_valid_true_with_text():
    actual = multi_bracket_validation("()[[Extra Characters]]")
    expected = True
    assert expected == actual

def test_valid_false():
    actual = multi_bracket_validation("{}()[)")
    expected = False
    assert expected == actual

def test_valid_false_missing():
    actual = multi_bracket_validation("[](")
    expected = False
    assert expected == actual

def test_valid_false_nested():
    actual = multi_bracket_validation("{(})")
    expected = False
    assert expected == actual




