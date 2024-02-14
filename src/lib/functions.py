from functools import reduce
from itertools import takewhile

reduce_while = lambda condition, func, iterable: reduce(func, takewhile(condition, iterable))
