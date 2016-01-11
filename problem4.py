__author__ = 'diogomartins'
__doc__ = """Write a function that given a list of non
             negative integers, arranges them such that they form the
             largest possible number. For example, given
             [50, 2, 1, 9], the largest formed number is 95021."""

class CustomCompare:
    def __init__(self, item: int):
        self.item = str(item)

    def __lt__(self, other):
        return self.item + other.item < other.item + self.item

    def __gt__(self, other):
        return self.item + other.item > other.item + self.item

def biggest_possible_number(a_list: list) -> int:
    sorted_list = sorted(a_list, key=CustomCompare, reverse=True)

    return int(''.join(sorted_list))


if __name__ == "__main__":
    l = [50, 2, 1, 9]
    print(biggest_possible_number(l))
