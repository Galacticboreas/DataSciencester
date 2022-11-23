"""
Функции
"""

from tkinter import W


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

"""
Списки
"""
integer_list = [1, 2, 3]                                 # Список целых чисел
heterogeneous_list = ["строка", 0.1, True]               # Разнородный список
list_of_lists = [integer_list, heterogeneous_list, []]   # Список списков

list_length = len(integer_list)    # Длина списка равна 3
list_sum = sum(integer_list)       # Сумма значений в списке равна 6

x = list(range(10))   # Задаёт список [0, 1, ... , 9]
zero = x[0]     # равно 0, т.е. индекс 1-го элемента равен 0
one = x[1]      # равно 1
nine = x[-1]    # равно 9, по-Python'овски взять последний элемент
eight = x[-2]   # равно 8, по-Python'овски взять предпоследний элемент
x[0] = -1       # Теперь х равен [-1, 1, 2, 3, ..., 9]

first_three = x[:3]     # Первые три равны [-1, 1, 2]
three_to_end = x[3:]    # С третьего до конца равно [3, 4, ..., 9]
one_to_four = x[1:5]    # С первого по четвертый равно [1, 2, 3, 4]
last_three = x[-3:]     # Последне три равны [7, 8, 9]
without_first_and_last = x[1:-1]   # Без первого и последнего
                                   # равно [1, 2, ..., 8]
copy_of_x = x[:]        # Копия списка х равна [-1, 1, 2, ..., 9]

every_third = x[::3]        # [-1, 3, 6, 9] - сдвиг равен 3
five_to_three = x[5:2:-1]   # [5, 4, 3]

1 in [1, 2, 3]     # True
0 in [1, 2, 3]     # False

x = [1, 2, 3]
x.extend([4, 5, 6])   # Теперь х равен [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
y = x + [4, 5, 6]     # y равен [1, 2, 3, 4, 5, 6]; x остался без изменений

x = [1, 2, 3]
x.append(0)        # Теперь х равен [1, 2, 3, 0]
y = x[-1]          # равно 0
z = len(x)         # равно 4

# распаковка списков
x, y = [1, 2]    # Теперь х равен 1, у равен 2

_, y = [1, 2]    # Теперь у равен 2, а первый элемент не нужен

# Кортежи
my_list = [1, 2]     # Задать список
my_tuple = (1, 2)    # Задать кортеж
other_tuple = 3, 4   # Еще один кортеж
my_list[1] = 3       # Теперь список my_list равен [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("Кортеж нельзя модифицировать")

# Функция возвращает сумму и произведение двух параметров
def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)      # равно (5, 6)
s, p = sum_and_product(5, 10)   # равно 15, р равно 50

# Кортежи (и списки) также используют во множественном присваивании:

x, y = 1, 2   # Теперь х равен 1, у равен 2
x, y = y, x   # Обмен значениями переменных по-Python'овски;
              # теперь х равен 2, у равен 1

# Словари

emty_dict = {}                     # Задать соварь по-Python'овски
emty_dict2 = dict()                # Не совсем по-Python'овски
grades = {"Joel": 80, "Tim": 95}   # Литерал словаря (оценки за экзамен)

joels_grade = grades["Joel"]       # равно 80

# При попытке запросить значение, которое в словаре отсутствует, будет выдано
# сообщение об ошибке ключа KeyError:

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("Оценки для Кэйт отсутствуют!")

# Проверить наличие ключа можно при помощи оператора in:

joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False

# Словари имеют метод get, который при поиске отсутствующего ключа вместо
# вызова исключения возвращает значение по умолчанию:

joels_grade = grades.get("Joel", 0)     # равно 80
kates_grade = grades.get("Kate", 0)     # равно 0
one_ones_grade = grades.get("Никто")    # Значение по умолчанию равно None

grades["Tim"] = 99             # Заменяет старое значение
grades["Kate"] = 100           # Добавляет третью запись
num_students = len(grades)     # равно 3

# Словари часто используют в качестве простого способа представить структурные
# данные:

tweet = {
    "user" : "joelgrus",
    "text" : "Наука о данных - потрясающая тема",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()      # Итерируемый объект для ключей
tweet_values = tweet.values()  # Итерируемый объект для значений
tweet_items = tweet.items()    # Итерируемый объект для кортежей
                               # (ключ, значение)

"user" in tweet_keys        # Возвращает True, но не по-Python'овски
"user" in tweet             # Python'вский способ проверки ключа,
                            # используя быстрое in
"joelgrus" in tweet_values  # True (медленно, но единственный способ проверки)

# Словарь defultdict

# Частотности слов
word_counts = {}
document = {}
for word in word_counts:
    word_counts[word] += 1
else:
    word_counts[word] = 1

# Кроме того можно воспользоваться приемом под названием "лучше просить
# прощения, чем разрешения" и перехватывать ошибку при попытке обратиться
# к отсутствующему ключу:
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# Третий подход - использовать метод get, который изящно выходит из
# ситуации с отсутствующими ключами:
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

