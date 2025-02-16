import math

def solve_quadratic(a, b, c):
    """Возвращает корни уравнения ax^2 + bx + c = 0 в порядке возрастания."""
    if a == 0:
        if b == 0:
            return None if c != 0 else "infinite solutions"
        return (-c / b,)

    D = b**2 - 4*a*c  # дискриминант

    if D < 0:
        return None  # нет корней
    elif D == 0:
        return (-b / (2*a),)  # один корень
    else:
        root1 = (-b - math.sqrt(D)) / (2*a)
        root2 = (-b + math.sqrt(D)) / (2*a)
        return tuple(sorted([root1, root2]))  # два корня

#print(solve_quadratic(0, 2, -4))  # (2.0,)
#print(solve_quadratic(0, 0, 5))   # None
#print(solve_quadratic(0, 0, 0))   # "infinite solutions"
