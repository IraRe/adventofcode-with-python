from task1 import find_two_numbers_that_sum_up_to
from task1 import find_three_numbers_that_sum_up_to

input_numbers = [ 1721, 979, 366, 299, 675, 1456 ]

def test_find_two_numbers_that_sum_up_to():
    found, first, second = find_two_numbers_that_sum_up_to(input_numbers, 2020)
    assert found
    assert first * second == 514579

def test_find_three_numbers_that_sum_up_to():
    found, first, second, third = find_three_numbers_that_sum_up_to(input_numbers, 2020)
    assert found
    assert first * second * third == 241861950
