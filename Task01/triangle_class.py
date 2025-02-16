class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass

class Triangle:
    def __init__(self, a, b, c):
        if any(side <= 0 for side in [a, b, c]) or (a + b <= c or a + c <= b or b + c <= a):
            raise IncorrectTriangleSides("Некорректные стороны треугольника")

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c
