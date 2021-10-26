import pytest

def get_number() :
    return 3

def test_number():
    assert get_number() == 3 # expected result
