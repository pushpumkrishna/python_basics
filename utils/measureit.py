import time
from functools import wraps


def measure_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # measure execution time for method
        s = time.time()
        res = func(*args, **kwargs)
        print("{} -> took {} seconds".format(func.__name__, time.time() - s))
        return res

    return wrapper
