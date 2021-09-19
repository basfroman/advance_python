import time


def fib_recursion(x):
    """Calculate fibonacci using regular recursion."""
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib_recursion(x-2) + fib_recursion(x-1)


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


if __name__ == '__main__':

    for f in [fib_recursion, fib_memo_list, fib_memo_dict]:

        start = time.time()
        xx = 35
        fibonacci = f(xx)

        stop = round(time.time()-start, 4)  # seconds with round 4 numbers after float

        print(f'Function: {f.__name__}({xx}) | Execution time is {stop} seconds. | Result is {fibonacci}.')
