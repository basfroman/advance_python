import time


def fib_recursion(x):
    """Calculate fibonacci using regular recursion."""
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib_recursion(x - 2) + fib_recursion(x - 1)


def fib_memo_list(x: int, cache: list = None):
    """Calculate fibonacci using recursion with memoization.
    Args:
        x: number for calculation
        cache: list with values where cache[x] = fib_memo(x)

    Return: fib_memo(x, cache) or 0 or 1
    """
    if x == 0:
        return 0
    if x == 1:
        return 1
    if not cache:
        cache = [0] * x
    if not cache[x - 2]:
        cache[x - 2] = fib_memo_list(x - 2, cache)
    if not cache[x - 1]:
        cache[x - 1] = fib_memo_list(x - 1, cache)
    return cache[x - 2] + cache[x - 1]


def fib_memo_dict(x, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}
    if x in cache:
        return cache[x]
    cache[x] = fib_memo_dict(x - 1, cache) + fib_memo_dict(x - 2, cache)
    return cache[x]


class Fibonacci:

    def __init__(self):
        self.cache = [0, 1]
        self.__name__ = 'cls Fibonacci'

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


if __name__ == '__main__':
    fib_class = Fibonacci()

    for f in [fib_memo_list, fib_memo_dict, fib_class, fib_recursion]:
        start = time.time()
        number = 34
        fibonacci = f(number)

        stop = round(time.time() - start, 4)  # seconds with round 4 numbers after float

        print(f'Object: {f.__name__}({number}) | Execution time is {stop} seconds. | Result is {fibonacci}.')
