from typing import Callable, List

Vector = List[float]

def dot(v: Vector, w: Vector) -> float:
    """Вычисляет v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "векторы должны быть одинаковой длины"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    """Вычисляет сумму возведенных в квадрат элементов в v"""
    return dot(v, v)

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h
# при стремлении h к нулю

# Для многих функций достаточно легко выполнить точное вычисление
# производных. Например, функция возведения в степень square:

def square(x: float) -> float:
    return x * x

# имеет производную:
def derivative(x: float) -> float:
    return 2 * x

xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]


