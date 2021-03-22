from task2 import count_valid_passwords
from task2 import parse_policy
from task2 import validate_password_by_policy
import pytest

def test_count_valid_passwords():
    num = count_valid_passwords("day2/example_input.txt")
    assert num == 2

@pytest.mark.parametrize("test_input,expected", [
    pytest.param("1-3 a: abcde", True, id="valid password"), 
    pytest.param("1-3 b: cdefg", False, id="not valid password")])
def test_validate_password_by_policy_success(test_input, expected):
    valid = validate_password_by_policy(test_input)
    assert valid == expected

def test_parse_policy():
    arity, char = parse_policy("1-3 b")

    assert arity == {"min": 1, "max": 3}
    assert char == "b"
