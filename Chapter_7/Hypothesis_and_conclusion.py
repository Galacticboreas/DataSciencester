from typing import Tuple
import math

# Пример: бросание монеты

# Представим, что у нас есть монета, которую требуется проверить, уравновешена
# ли она. Для этого делается допущение, что монета имеет некую вероятность р
# выпадения орла, и выдвигается нулеваня гипотеза о том, что монета уравнове-
# шена, т.е. р = 0.5. Проверим ее, сопоставив с альтернативной гипотезой р != 0.5

# В частности, наша проверка будет предусматривать бросание монеты n раз с
# подсчетом количества орлов Х. Каждый бросок монеты - это бурнуллиево испытание,
# где Х - это биномиальная случайная величина binomial(n, p), которую, как мы
# уже убедились в главе 6, можно аппроксимировать с помощью нормального распре-
# деления:

# Аппроксимация биномиальной случайной величины нормальным распределением
def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Возвращает mu и sigma, соответствующие binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# Всякий раз, когда случайная величина подчиняется нормальному распределению,
# мы можем использовать функцию normal_cdf для выявления вероятности, что ее
# реализованное значение лежит в пределах или за пределами определенного
# интервала:

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2
# Нормальная функция CDF (normal_cdf) - это вероятность, что переменная
# лежит ниже порога
normal_probability_below = normal_cdf

# Она лежит выше порога, если она не ниже порога
def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """Вероятность, что N(mu, sigma) выше, чем lo."""
    return 1 - normal_cdf(lo, mu, sigma)

# Она лежит между, если она меньше, чем hi, но не менее, чем lo
def normal_probability_between(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """Веротность, что N(mu, sigma) между lo и hi."""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# Она лежит за пределами, если она лежит между
def normal_probability_outside(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """Вероятность, что N(mu, sigma) не лежит между lo и hi."""
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# Мы также можем сделать обратное - отыскать нехвостовой участок или
# же (симметричный) интервал вокруг среднего значения, на который при-
# ходится определенный уровень правдоподобия. Например, если нам нужно
# отыскать интервал с центром в среднем значении, содержащий 60%-ную
# вероятность, то мы отыскиваем точки отсечения, где верхний и нижний
# "хвосты" содержат по 20 % вероятности каждый (с остатком в 60%):

def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """Находит приблизительное обратное с помощью двоичного поиска"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0                      # normal_cdf(-10) is (very close to) 0
    hi_z  =  10.0                      # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # Consider the midpoint
        mid_p = normal_cdf(mid_z)      # and the cdf's value there
        if mid_p < p:
            low_z = mid_z              # Midpoint too low, search above it
        else:
            hi_z = mid_z               # Midpoint too high, search below it

    return mid_z

# Верхняя граница
def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Возвращает z, для которой P(Z <= z) = вероятность"""
    return inverse_normal_cdf(probability, mu, sigma)

# Нижняя граница
def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Возвращает z, для которой P(Z >= z) = вероятность"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

# Двусторонняя граница
def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """Возвращает симметрические (вокруг среднего) границы,
       которые содержат указанную вероятность
    """
    tail_probability = (1 - probability) / 2

    # Верхняя граница должна иметь хвостовую tail_probability выше ее
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # Нижняя граница должна иметь хвостовую tail_probability ниже ее
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound

# В частности, будем считать, что мы решили сделать n=1000 бросков.
# Если гипотетически об уравновешенности монеты является истинной,
# то Х должна быть приближенно нормально распределена со средним значением,
# равным 500, и стандартным отклонением 15.8:

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print(mu_0, sigma_0)
