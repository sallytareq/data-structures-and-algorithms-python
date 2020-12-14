import pytest
from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter

def test_init():
    sh = AnimalShelter()
    actual1 = sh.cat.front
    actual2 = sh.dog.front
    expected1 = None
    expected2 = None
    assert actual1 == expected1
    assert actual2 == expected2

def test_enqueue():
    sh = AnimalShelter()
    sh.enqueue("cat","Shelly")
    sh.enqueue("dog","JJ")
    actual1 = sh.cat.front.value
    actual2 = sh.dog.front.value
    expected1 = "Shelly"
    expected2 = "JJ"
    assert actual1 == expected1
    assert actual2 == expected2


def test_dequeue():
    sh = AnimalShelter()
    sh.enqueue("cat","Shelly")
    sh.enqueue("dog","JJ")
    sh.enqueue("dog","Alex")
    sh.enqueue("cat","Tom")
    sh.enqueue("dog","Hulk")
    sh.enqueue("cat","Zoro")

    # Dog
    actual = sh.dequeue("dog")
    expected = "JJ"
    assert actual == expected
    actual1 = sh.shelter.front.value
    expected1 = "Shelly"
    assert actual1 == expected1
    actual2 = sh.dog.front.value
    expected2 = "Alex"
    assert actual2 == expected2

    # Cat
    actual3 = sh.dequeue("cat")
    expected3 = "Shelly"
    assert actual3 == expected3
    actual4 = sh.shelter.front.value
    expected4 = "Alex"
    assert actual4 == expected4
    actual5 = sh.cat.front.value
    expected5 = "Tom"
    assert actual5 == expected5


    # Empty - Dog
    actual6 = sh.dequeue()
    expected6 = "Alex"
    assert actual6 == expected6
    actual7 = sh.shelter.front.value
    expected7 = "Tom"
    assert actual7 == expected7
    actual8 = sh.dog.front.value
    expected8 = "Hulk"
    assert actual8 == expected8

    # Empty - Cat
    actual9 = sh.dequeue()
    expected9 = "Tom"
    assert actual9 == expected9
    actual10 = sh.shelter.front.value
    expected10 = "Hulk"
    assert actual10 == expected10
    actual11 = sh.cat.front.value
    expected11 = "Zoro"
    assert actual11 == expected11