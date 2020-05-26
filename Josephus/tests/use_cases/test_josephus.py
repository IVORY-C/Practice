import pytest
from unittest import mock
from collections.abc import Iterable

from domain.shared.person import Person
from domain.use_cases import josephus as jsp


@pytest.fixture
def people_example():
    return [
        Person('Morty', 12, 'male'),
        Person('Rick', 53, 'male'),
        Person('Summer', 16, 'female'),
        Person('Beth', 34, 'female'),
        Person('Jerry', 36, 'male')
    ]

def test_josephus_init_with_reader():
    reader = mock.MagicMock()
    ring = jsp.Ring(reader)

    reader.__iter__.assert_called_with()
    assert ring.start == 1
    assert ring.step == 1

def test_josephus_init_with_invalid_reader():
    reader = mock.Mock()
    with pytest.raises(TypeError):
        jsp.Ring(reader)

def test_josephus_init_without_reader():
    ring = jsp.Ring()

    assert ring.start == 0
    assert ring.step == 1
    assert ring._people == []

def test_josephus_append():
    someone: Person = Person('Morty', 12, 'male')
    ring = jsp.Ring()
    ring.append(someone)
    
    assert ring._people == [someone]

def test_josephus_pop(people_example):
    ring = jsp.Ring()
    ring._people = people_example
    ring.pop()

    assert ring._people == [
        Person('Rick', 53, 'male'),
        Person('Summer', 16, 'female'),
        Person('Beth', 34, 'female'),
        Person('Jerry', 36, 'male')
    ]
    
def test_josephus_query_list(people_example):
    ring = jsp.Ring()
    ring._people = people_example
    result = ring.query_list()

    assert result == [
        Person('Morty', 12, 'male'),
        Person('Rick', 53, 'male'),
        Person('Summer', 16, 'female'),
        Person('Beth', 34, 'female'),
        Person('Jerry', 36, 'male')
    ]

def test_josephus_is_iterable():
    ring = jsp.Ring()

    assert isinstance(ring, Iterable)

def test_josephus_len(people_example):
    ring = jsp.Ring()
    ring._people = people_example

    assert len(ring) == 5


def test_josephus_output_result(people_example):
    ring = jsp.Ring(people_example)
    ring.start = 2
    ring.step = 5
    ring.reset()

    result = []
    for item in ring:
        result.append(item)

    assert result == [
        Person('Rick', 53, 'male'),
        Person('Summer', 16, 'female'),
        Person('Jerry', 36, 'male'),
        Person('Morty', 12, 'male'),
        Person('Beth', 34, 'female')
    ]