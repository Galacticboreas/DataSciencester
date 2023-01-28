import math

from typing import Tuple

# P-значения

# Альтернативный подход к приведенной выше проверке предусматривает
# применение р-значения. Вместо выбора границ на основе некоторой
# точки отсечения вероятности вычисляется вероятность (при условии
# , что Н0 является истинной) получения как минимум такого же 
# предельного значения, как и то, которое фактически наблюдалось.

# Для нашей двусторонней проверки, является ли монета уравновешенной,
# мы вычисляем:

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

normal_probability_below = normal_cdf

def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """Вероятность, что N(mu, sigma) выше, чем lo."""
    return 1 - normal_cdf(lo, mu, sigma)

# Двустороннее р-значение
def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    Насколько правдоподобно увидеть значение, как минимум, такое же
    предельное, что и х (в любом направлении), если наши значения
    поступают из N(mu, sigma)?
    """
    if x >= mu:
        # x больше, чем среднее, поэтому хвост везде больше, чем х
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x меньше, чем среднее, поэтому хвост везде меньше, чем х
        return 2 * normal_probability_below(x, mu, sigma)

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Возвращает mu и sigma, соответствующие binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
                                           # mu_0 = 500.0 
                                           # sigma_0 = 15.811388300841896

# Если бы мы увидели 530 орлов, то мы бы вычислили:
two_sided_p_value(529.5, mu_0, sigma_0)    # 0.06207721579598835

# Фактически р-значение - это вероятность ошибки при отклонении нелувой
# гипотезы (ошибки 1-го рода)

# Одним из способов убедиться, что этот результат является разумной
# оценкой, - провести симуляцию:

import random

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

# р-значение было 0.062 => ~62 предельных значения из 1000
assert 59 < extreme_value_count < 65, f"{extreme_value_count}"

# Поскольку р-значение превышает заданный 5%-ный уровень значимости,
# то нулевая гипотеза не отклоняется. И напротив, при выпадении 532
# орлов р-значение будет равно:

two_sided_p_value(531.5, mu_0, sigma_0)   # 0.046345287837786575

# что меньше 5%-ного уровня значимости, и, следовательно, нулевая
# гипотеза будет отклонена. Это в точности такая же проверка, что
# и прежде. Разница лишь в подходе к статистикам.

# Верхнее и нижнее р-значене можно получить аналогичным образом:

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

# и, следовательно, нулевая гипотеза не будет отклонена. При выпадении
# 527 орлов вычисление будет:

upper_p_value(526.5, mu_0, sigma_0)   # 0.04686839508859242

# и нулевая гиротеза будет отклонена.

# Следует удостоверится, что ваши данные являются приближенно нормально
# распределенными, и только после этого можно применять функцию normal_
# probability_above для вычисления р-значений. Анналы плохой науки о 
# данных полны примеров людей, считающих, что шанс наступления некоего
# наблюдаемого события случайным образом равен одному на миллион, когда
# на самом деле они имеют в виду "шанс с учетом того, что данные являются
# нормально распределенными", что достаточно бессмысленно, если данные
# такими не являются.
# 
# Существуют разнообразные проверки на нормальность, но если просто 
# вывести данные на график, то это будет шагом в правильном направлении.