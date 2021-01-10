"""
Code Challenge 31:
    - Write a function that accepts a lengthy string parameter.
    - Without utilizing any of the built-in library methods available to your language, 
        return the first word to occur more than once in that provided string.
"""

from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeated_word


def test_type_check():
    actual = repeated_word([1,2,3])
    expected = 'Invalid Input'
    assert expected == actual

def test_short_text():
    text = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(text)
    expected = 'a'
    assert expected == actual

def test_long_text():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(text)
    expected = 'it'
    assert expected == actual

def test_no_repeats():
    text = 'Hello world, welcome to the no reapeat test.... !'
    actual = repeated_word(text)
    expected = 'No repeats'
    assert expected == actual
