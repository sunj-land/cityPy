'''
Author: sunjie
Date: 2025-03-06 23:39:26
LastEditors: sunj
LastEditTime: 2025-03-11 23:15:50
FilePath: /sunjPy/wDemos/dict.py
'''
import timeit
import sys
import array
from collections import UserDict


class Nu:
    def __init__(self, num=0):
        self.num = num

    def __abs__(self):
        return abs(self.num)


n1 = Nu(-123)


# 使用 list


dial = [(2, "aa"), (10, "bb"), (3, "cc")]
a = {
    val: key for key, val in dial if key > 3
}


def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 1, **names}:
            return names
        case {"type": "book", "api": 2, "authors": names}:
            return [names]
        case {"type": "book"}:
            return [11]
        case _:
            raise ValueError("Invalid record!")


# print(get_creators({
#     "type": "book",
#     "api": 1,
#     "aaa": "aaa"
# }))

a = {'a': "aaa"}
print(a.get("b"))


class StrKeyDict0(UserDict):
    def __missing__(self, key):
        print("missing", key)
        if isinstance(key, str):
            raise KeyError("missing")
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            print("missing", key)
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


sd1 = StrKeyDict0({"2": "two", "4": "four"})
l1 = sd1.values()
print(l1)
sd1["ccc"] = "cccc"
print(l1)
