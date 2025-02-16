class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass

def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по его сторонам.
    """
    if any(side <= 0 for side in [a, b, c]) or (a + b <= c or a + c <= b or b + c <= a):
        raise IncorrectTriangleSides("Некорректные стороны треугольника")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"

#print(get_triangle_type(2, 2, 3))