from typing import Dict
from functools import lru_cache
from typing import Generator


def fibonacci(n: int) -> int:
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n: int) -> int:
    if n < 2:
        return n

    return fibonacci2(n - 1) + fibonacci2(n - 2)


memo: Dict[int, int] = {0: 0, 1: 1}  # base case


def fibonacci3(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci3(n - 1) + fibonacci3(n - 2)  # memoization
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci4(n: int) -> int:  # same as fibonacci2()
    if n < 2:  # base case
        return n
    return fibonacci4(n - 2) + fibonacci4(n - 1)  # recursive case


# keep it simple
def fibonacci5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next
        return next


# generating fibonacci numbers with a generator
def fibonacci6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generator step


if __name__ == "__main__":
    for i in fibonacci6(50):
        print(i)
