from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, sides: float):
        self.sides = sides

    def calArea(self):
        return self.sides * self.sides


circ = Circle(10.2)
sq = Square(5)

print(circ.calArea())
print(sq.calArea())
