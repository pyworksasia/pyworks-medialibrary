
import pytest


def is_palindrome(str):
    # Run loop from 0 to len/2 
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", False),
    ("Never odd or even", False),
    ("Do geese see God?", False),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result

