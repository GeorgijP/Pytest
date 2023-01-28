import pytest
from utils import arrs, dicts


@pytest.fixture
def variable():
    return [1, 2, 3, 4]


def test_get(variable):
    assert arrs.get(variable, 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice(variable):
    assert arrs.my_slice(variable, 1, 3) == [2, 3]
    assert arrs.my_slice(variable, 1) == [2, 3, 4]
    assert arrs.my_slice(variable, -1) == [4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(variable, 0) == [1, 2, 3, 4]
    assert arrs.my_slice(variable, -5, 0) == []


def test_get_val():
    assert dicts.get_val({1:"I", 2:"You", 3:"They"}, 1) == "I"
    assert dicts.get_val({1:"I", 2:"You", 3:"They"}, 4) == "git"
    assert dicts.get_val({}, 3, "Not git") == "Not git"