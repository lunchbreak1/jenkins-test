import pytest

def get_number() :
    return 2

def test_number():
    assert get_number() == 3 # expected result