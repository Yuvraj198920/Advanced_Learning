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

class Square(GraphicShape):
    def __init__(self, sides: float):
        self.sides = sides


graphicShape = GraphicShape()
circ = Circle(10.2)
sq = Square(5)

print(graphicShape)
print(circ.calArea())
print(sq.calArea())