import time


def fib_recursion(x):
    """Calculate fibonacci using regular recursion."""
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib_recursion(x-2) + fib_recursion(x-1)


def fib_memo(x: int, cache: list = None):
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
        cache[x - 2] = fib_memo(x - 2, cache)
    if not cache[x - 1]:
        cache[x - 1] = fib_memo(x - 1, cache)
    return cache[x - 2] + cache[x - 1]


if __name__ == '__main__':

    for f in [fib_memo, fib_recursion]:

        start = time.time()
        xx = 37
        fibonacci = f(xx)

        stop = round(time.time()-start, 4)  # seconds with round 4 numbers after float

        print(f'Function: {f.__name__}({xx}) | Execution time is {stop} seconds. | Result is {fibonacci}.')
