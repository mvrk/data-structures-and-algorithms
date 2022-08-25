import pytest
from quick_sort import quick_sort


def test_quick_sort():
    test_array = [1, 9, 3, 7, 5, 8, 2, 6]
    expected = [1, 2, 3, 5, 6, 7, 8, 9]
    actual = quick_sort(test_array, 0, len(test_array) - 1)
    assert actual == expected


def test_quick_sort_one():
    test_arr = [8]
    expected = [8]
    actual = quick_sort(test_arr, 0, 0)
    assert actual == expected


def test_quick_sort_empty():
    test_arr = []
    expected = []
    actual = quick_sort(test_arr, 0, 0,)
    assert actual == expected


def test_quick_sort_duplicates():
    test_arr = [1, 5, 9, 3, 7, 5, 8, 1]
    expected = [1, 1, 3, 5, 5, 7, 8, 9]
    actual = quick_sort(test_arr, 0, len(test_arr)-1)
    assert actual == expected
