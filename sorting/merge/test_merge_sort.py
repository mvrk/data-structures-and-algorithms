import pytest
from merge_sort import merge_sort


def test_merge_sort():
    test_arr = [1, 9, 3, 7, 5, 8, 2, 6]
    expected = [1, 2, 3, 5, 6, 7, 8, 9]
    actual = merge_sort(test_arr)
    assert actual == expected


def test_merge_sort_one():
    test_arr = [8]
    expected = [8]
    actual = merge_sort(test_arr)
    assert actual == expected


def test_merge_sort_empty():
    test_arr = []
    expected = []
    actual = merge_sort(test_arr)
    assert actual == expected


def test_merge_sort_duplicates():
    test_arr = [1, 5, 9, 3, 7, 5, 8, 1]
    expected = [1, 1, 3, 5, 5, 7, 8, 9]
    actual = merge_sort(test_arr)
    assert actual == expected
