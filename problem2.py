__author__ = 'diogomartins'
__doc__ = """Write a function that combines two lists by
            alternatingly taking elements. For example: given the two
            lists [a, b, c] and [1, 2, 3], the function should return
            [a, 1, b, 2, c, 3]."""

def solution1(first: list, second: list) -> list:
    """
    Assumes that both lists, like the given example, have the same size.
    """
    assert len(first) == len(second)

    combined = []
    for i in range(len(first)):
        combined += first[i], second[i]

    return combined

def solution2(first: list, second: list) -> list:
    """
    Supports different list sizes
    """
    l_first = len(first)
    l_second = len(second)
    max_size = max(l_first, l_second)

    combined = []
    for i in range(max_size):
        if i < l_first:
            combined.append(first[i])
        if i < l_second:
            combined.append(second[i])

    return combined


if __name__ == "__main__":
    l1 = ['a', 'b', 'c']
    l2 = [1, 2, 3]

    print(solution1(l1, l2))
    print(solution2(l1, l2))
