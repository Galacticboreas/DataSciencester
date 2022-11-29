# ----------------------------------
# Итерируемые объекты и генераторы |
# ----------------------------------

# Один из способов создания генераторов заключается в
# использовании функций и инструкций yield:

from tkinter import N


def generate_range(n):
    i = 0
    while i < n:
        yield i     # Каждый вызов инструкции yield
        i += 1      # производит значение генератора

# Приведенный ниже цикл будет потреблять предоставляемые
# инструкцией yield значения по одному за раз до тех пор,
# пока элементы не закончатся:

for i in generate_range(10):
    print(f"i: {i}")

# На самом деле функция _range сама является "ленивой",
# поэтому делать это нет смысла.

# С помощью генератора можно создать бесконечную последовательность:
# Натуральные числа:
def natural_numbers():
    """Возвращает 1, 2, 3 ..."""
    n = 1
    while True:
        yield n
        n += 1
# хотя, наверное, не стоит перебирать такую последовательность
# без применения какой-нибудь логики выхода из цикла.

# Второй способ создания генераторов - использовать операции
# включения с инструкцией for, обернутые в круглые скобки:

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# При таком включении генератор не выполняет никакой работы до
# тех пор, пока вы не выполните его обход (с использованием
# инструкции for или next). Его можно применить для наращивания
# изощренных конвейеров по обработке данных:

# Ни одно из этих вычислений *не делеает ничего*
# до тех пор, пока мы не выполним обход

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

# Нередко, когда мы перебираем список или генератор, нам нужны не
# только значения, но и их индексы. Для этого общего случая Python
# предоставляет фуекцию enumerate, которая превращает значения в пары
# (индекс, значение):
names = ["Alice", "Bob", "Charlie", "Debbie"]

# Не по Python'овски
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# Тоже не по-Python'овски
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# По Python'овски
for i, name in enumerate(names):
    print(f"name {i} is {name}")
# Мы будем использовать эту функцию очень много.
