"""
Функции
"""

def double(x):
    """
    Когда требуется, здесь размещают
    многострочный документирующий комментарий docstring,
    который поясняет, что именно функция вычисляет.
    Например, указанная функция умножает входящие значения на 2
    """
    return x * 2

# Применение функции f к единице
def apply_to_one(f):
    """Вызываем функцию f с единицей в качестве аргумента"""
    return f(1)

my_double = double                  # Ссыдка на ранее определенную функцию
x = apply_to_one(my_double)         # равно 2

y = apply_to_one(lambda x: x + 4)   # равно 5

def full_name(first="некто", last="как-то там"):
    return first + " " + last

full_name("Джоэл", "Грас")
full_name("Джоэл")
full_name(last="Грас")

"""
Исключения
"""
try:
    print(0 / 0)
except ZeroDivisionError:
    print("Нельзя делить на ноль")
