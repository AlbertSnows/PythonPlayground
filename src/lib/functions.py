from functools import reduce
from itertools import takewhile

def attempt(action, failure):
    try:
        return action()
    except Exception:
        return failure

def reduce_while(condition, reducer, iterable, initial):
    """
    reducer that takes an early exit condition
    e.g. reduce_while(lambda acc, next: acc + next >= 20, lambda x, y: x + y, numbers, 0)
    """
    accumulator = initial
    for item in iterable:
        if condition(accumulator, item):
            accumulator = reducer(accumulator, item)
        else:
            break
    return accumulator
