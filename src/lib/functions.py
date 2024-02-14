from functools import reduce
from itertools import takewhile


def reduce_while(condition, func, iterable, initial):
    """
    reducer that takes an early exit condition
    e.g. reduce_while(lambda acc, next: acc + next >= 20, lambda x, y: x + y, numbers, 0)
    """
    return reduce(func, takewhile(condition, iterable), initial)
