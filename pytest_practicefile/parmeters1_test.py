"""Parameterizing pytest functions"""
import pytest

@pytest.mark.parametrize("input1, input2, expected", [
    (1, 2, 3),    # Test case 1
    (2, 3, 6),    # Test case 2
    (3, 5, 8)     # Test case 3
])
def test_addition(input1, input2, expected):
    assert input1 + input2 == expected

# Parametrize with multiple parameters of different types and values
@pytest.mark.parametrize("username, password, expected_result", [
    ("user1", "pass1", True),    # Valid credentials
    ("user2", "wrong_pass", False),  # Invalid password
    ("", "pass3", False),       # Empty username
])
def test_login(username, password, expected_result):
    # Simulate a login function
    result = (username == "user1" and password == "pass1")
    assert result == expected_result

