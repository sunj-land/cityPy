import typing
from collections import namedtuple
# Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)

print(issubclass(Coordinate, tuple))

m = Coordinate(55.11, 22.33)

print(m)


City = namedtuple("City", "name country", defaults=["sj", "china"])

tokyo = City()

print(tokyo)


l1 = (1, 2)
print(id(l1))
l1 += (1, 2)
print(id(l1))


def getParm(parm=[]):
    return


print(type(None))
