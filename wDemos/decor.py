import time
from clock import clock, clock_class
from functools import lru_cache


@lru_cache(maxsize=128)
@clock_class()
def fb(n):
    return 1 if n < 2 else fb(n-2) + fb(n-1)


if __name__ == "__main__":
    print(fb(11))
