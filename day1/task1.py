def find_two_numbers_that_sum_up_to(numbers, sum):
    for number in numbers:
        r = sum - number
        if r in numbers:
            return True, r, number
    return False, 0, 0

def find_three_numbers_that_sum_up_to(numbers, sum):
    while numbers:
        number = numbers.pop()
        r = sum - number
        found, val1, val2 = find_two_numbers_that_sum_up_to(numbers, r)
        if found:
            return True, number, val1, val2
    return False, 0, 0, 0
