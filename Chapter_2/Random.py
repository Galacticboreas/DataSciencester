# -------------
# Случайность |
# -------------

# По мере изучения науки о данных перед нами часто
# возникает необходимость генерировать случайные
# числа. Для этого предназначен модуль random:
import random
random.seed(10)     # Этим обеспечивается, что
                    # всякий раз мы получаем
                    # одинаковые результаты

# Четыре равномерные случайные величины
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)  
# 0.5714025946899135   # Функция random.random() производит числа
# 0.4288890546751146   # равномерно в интервале между 0 и 1
# 0.5780913011344704   # Указанная функция будет применяться
# 0.20609823213950174  # наиболее часто.

# Модуль random на самом деле генерирует псевдослучайные (т.е.
# детерминированные) числа на основе внутреннего состояния.
# Когда требуется получать воспроизводимые результаты, внутреннее
# состояние можно задавать при помощи посева начального значения
# для генератора псевдослучайных чисел random.seed:
random.seed(10)          # Задать начальное число для генератора
                         # случайных чисел равным 10
print(random.random())   # Получаем 0.5714025946899135
random.seed(10)          # Переустановим начальное значение, задав 10
print(random.random())   # Снова получаем 0.5714025946899135

# Иногда будет применяться метод random.randrange, который принимает
# один или два аргумента и возвращает элемент, выбранный случайно
# из соответствующего интервала range:

random.randrange(10)     # Случайно выбрать из range(10) = [0, 1, ..., 9]
random.randrange(3, 6)   # Случайно выбрать из range(3, 6) = [3, 4, 5]

# Есть еще ряд методов, которые пригодятся. Метод random.shuffle,
# например, перетасовывает элементы в списке в случайном порядке:

up_to_ten = range(10)     # Задать последовательность из 10 элементов
random.shuffle(up_to_ten)
print(up_to_ten)
# [2, 5, 1, 9, 7, 3, 8, 6, 4, 0] (фактически результаты могут отличаться)

# Если вам нужно случайно выбрать один элемент из списка, то можно
# воспользоваться методом random.choice:

# Мой лучший друг
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])  # У меня "Bob"
