

from array import array
import math
import inspect


class Vector2d:
    typecode = 'd'

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        print("__repr__ ")
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        print(inspect.currentframe().f_code.co_name)

        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        print("__abs__ ")
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '===({},{})'.format(*components)

    def __hash__(self):
        return hash((self.x, self.y))

    # @classMethod
    # def frombytes(cls, octets):
    #     typecode = chr(octets[0])
    #     memv = memoryview(octets[1:]).cast(typecode)
    #     return cls(*memv)


v1 = Vector2d(1, 2)
# print(repr(v1))
# print(str(v1))


v1.ff = "fff"
