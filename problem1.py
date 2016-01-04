from random import randint

__author__ = 'diogomartins'
__doc__ = """Write three functions that compute the sum
            of the numbers in a given list using a for-loop, a
            while-loop, and recursion."""

def for_loop(a_list: list) -> int:
    l_sum = 0
    for i in a_list:
        l_sum += i
    return l_sum

def while_loop(a_list: list) -> int:
    l_size = len(a_list)
    l_sum = 0
    i = 0

    while i < l_size:
        l_sum += a_list[i]
        i += 1

    return l_sum

def recursion(a_list: list) -> int:
    if not a_list:  # 'pythonic' len == 0
        return 0

    return a_list[0] + recursion(a_list[1:])


if __name__ == "__main__":
    l = [randint(1, 100) for i in range(5)]
    sum_of_numbers = sum(l)                     # built-in sum. Always correct.

    assert for_loop(l) == sum_of_numbers
    assert while_loop(l) == sum_of_numbers
    assert recursion(l) == sum_of_numbers
