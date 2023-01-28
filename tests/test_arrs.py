from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], 0) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -4, 0) == []


def test_get_val():
    assert dicts.get_val({1:"I", 2:"You", 3:"They"}, 1) == "I"
    assert dicts.get_val({1:"I", 2:"You", 3:"They"}, 4) == "git"
    assert dicts.get_val({}, 3, "Not git") == "Not git"