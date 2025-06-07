'''
Author: sunjie
Date: 2025-03-12 22:57:51
LastEditors: sunj
LastEditTime: 2025-03-12 23:11:08
FilePath: /sunjPy/wDemos/clock.py
'''
import time


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {res}')
        return res
    return clocked


class clock_class:
    def __init__(selft):
        pass

    def __call__(self, func):
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            res = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_str = ', '.join(repr(arg) for arg in args)
            print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {res}')
            return res
        return clocked
