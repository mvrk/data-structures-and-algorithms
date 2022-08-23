import pytest
from insertion_sort import insertion_sort


def test_insert_sort():
    test_arr = [1, 9, 3, 7, 5]
    expected = [1, 3, 5, 7, 9]
    actual = insertion_sort(test_arr)
    assert actual == expected


def test_insert_sort_one():
    test_arr = [0]
    expected = [0]
    actual = insertion_sort(test_arr)
    assert actual == expected


def test_insert_sort_empty():
    test_arr = []
    expected = None
    actual = insertion_sort(test_arr)
    assert actual == expected


def test_insert_sort_equal():
    test_arr = [1, 5, 9, 3, 7, 5]
    expected = [1, 3, 5, 5, 7, 9]
    actual = insertion_sort(test_arr)
    assert actual == expected
