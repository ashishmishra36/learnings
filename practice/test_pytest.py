import pytest

# important : test should be starting with test or ending with test

def test_method_one():
    a, b = 4, 5
    assert a==b, 'test failed: a and b are not equal'


def test_method_two():
    s = 'Ashish'
    assert len(s)==9, 'test failed: length is not as per expectation'
