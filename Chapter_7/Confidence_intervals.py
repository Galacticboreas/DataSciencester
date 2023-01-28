# Доверительные интервалы

# Мы проверяли гиротезы о значении вероятности орлов р, т.е. параметре
# неизвестного распределения "орлов". В этом случае используют третий
# подход - строят доверительный интервал вокруг наблюдаемого значения
# параметра.

# Например, мы можем оценить вероятность неуравновешенной монеты, обра-
# тившись к среднему значению бернуллиевых величин, соответствующих
# каждому броску монеты - 1(орел) и 0 (решка). Если мы наблюдаем 525
# орлов из 1000 бросков, то мы оцениваем, что р равно 0.525.

# Насколько можно быть уверенным в этой оценке? Дело в том, что если
# бы имелось точное значение р, то согласно центральной предельной 
# теореме среднее этих бернуллиевых величин должно быть приближенно 
# нормальным со средним р и стандартным отклонением:

import math, random
from typing import Tuple, List



def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

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

# math.sqrt(p * (1 - p) / 100)

# Здесь мы не знаем р, и поэтому вместо него мы используем оценку:

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158

# Это не совсем оправданно, и тем не менее все равно поступают именно
# так. Используя нормальную аппроксимацию, мы делаем вывод, что с
# "уверенностью на 95%" следующий ниже интервал содержит истинный 
# параметр р:

normal_two_sided_bounds(0.95, mu, sigma)     # [0.4940, 0.5560]

# Это утверждение касается интервала, а не р. Следует понимать его
# как утверждение, что если бы пришлось повторять эксперимент много
# раз, то в 95% случаев "истинный" параметр (который каждый раз одинаков)
# будет лежать в пределах наблюдаемого доверительного интервала (который
# каждый раз может быть разным).

# В частности, мы не делаем заключения о том, что монета не уравновешена,
# поскольку 0.5 попадает в пределы доверительного интервала.

# И напротив, если бы выпало 540 орлов, то мы имели бы:

p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158

normal_two_sided_bounds(0.95, mu, sigma)    # [0.5091, 0.5709]

# Здесь "уравновешенная монета" не лежит в доверительном интервале.
# (Гипотеза об уравновешенной монете не проходит проверки, которую,
# как ожидалось, она должна проходить в 95% случаев, если бы она
# была истинной.)

# Взлом р-значения

# Процедура, которая отклоняет нелувую гиротезу только в 5% случаев -
# по определению, - в 5% случаев будет отклонять нулевую гиротезу 
# ошибочно:

def run_experiment() -> List[bool]:
    """Подбрасывает уравновешенную монету 1000 раз,
       Истина = орлы, Ложь = решки"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment: List[bool]) -> bool:
    """Использование 5%-ных уровней значимости"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]

num_rajections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])

assert num_rajections == 46
