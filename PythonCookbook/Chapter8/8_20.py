import operator
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)

d = getattr(p, 'distance')(0, 0)
print(d)

operator.methodcaller('distance', 0, 0)(p)


points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]

points.sort(key=operator.methodcaller('distance', 0, 0))

print(points)
