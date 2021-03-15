from typedtuples import *

Point1 = TypedTuple.of('Point', {'x': float, 'y': float})

class Point2(TypedTuple):
    x: float
    y: float
    def __add__(self, other):
        return Point2(self.x+other.x, self.y+other.y)

@TypedTuple.apply({'x': int, 'y': int})
class IntPoint:
    def __add__(self, other):
        return IntPoint(self.x+other.x, self.y+other.y)

print(Point1(x=2.5, y=5.3))
print(Point2(1.1, 3.2) + Point2(2.4, 5.5))
print(IntPoint(x=1, y=3) + IntPoint(5, 2))
