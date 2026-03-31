"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_single_element():
    assert max_subarray_sum([1]) == 1                      # Test for single element

def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10           # Test for all positive numbers

def test_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1      # Test for all negative numbers

def test_mixed_numbers():
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7  # Test for mixed numbers

def test_all_same():
    assert max_subarray_sum([2, 2, 2, 2]) == 8            # Test for all same positive numbers
    assert max_subarray_sum([-2, -2, -2, -2]) == -2      # Test for all same negative numbers

def test_empty_list():
    with pytest.raises(IndexError):                        # Test if raises specified error
        max_subarray_sum([])                                # Line of code to be tested

def test_correct_datatype():
    with pytest.raises(TypeError):
        max_subarray_sum("string")
        max_subarray_sum(["string", "string"])

if __name__ == "__main__":
    pytest.main()