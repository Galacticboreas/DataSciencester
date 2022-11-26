# -----------
# Множества |
# -----------

s = set()     # Задать пустое множество
s.add(1)      # Теперь s равно { 1 }
s.add(2)      # Теперь s равно { 1, 2 }
s.add(2)      # s как и прежде равно { 1, 2 }
x = len(s)    # равно 2
y = 2 in s    # равно True
z = 3 in s    # равно False

# Множество будут использоваться по двум причинам. Во первых, операция
# in на множествах очень быстрая. Если необходимо проверить большую
# совокупность элементов на принадлежность некоторой последовательности,
# то множество set подходит для этого лучше, чем список:

# Список стоп-слов
hundreds_of_other_words = ["big", "smoll", "easy"]
stopword_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopword_list      # False, но проверяется каждый элемент

# Множество стоп-слов
stopwords_set = set(stopword_list)
"zip" in stopwords_set      # Очень быстрая проверка

# Вторая причина - получение уникальных элементов в наборе данных:
item_list = [1, 2, 3, 1, 2, 3]       # Список
num_items = len(item_list)           # Равно 6
item_set = set(item_list)            # Множество {1, 2, 3}
num_distinct_items = len(item_set)   # равно 3
distinct_item_list = list(item_set)  # Список [1, 2, 3]

# Множества будут применяться намного реже словарей и списков

# ------------------
# Поток управления |
# ------------------

# Как и в большенстве других языков программирования, действия
# можно выполнять по условию, применяя инструкцию if:

if 1 > 2:
    message = "если 1 была бы больше 2 ..."
elif 1 > 3:
    message = "elif означает 'else if'"
else:
    message = "когда все предыдущие условия не выполняются, используется else"

# Кроме того, можно воспользоваться однострочной трехместной инструкцией
# if-then-else, которая будет иногда применяться в дальнейшем:

parity = "четное" if x % 2 == 0 else "нечетное"

# В Python имеется цикл while:

x = 0
while x < 10:
    print(x, "меньше 10")
    x += 1

# Однако чаще будет использоваться цикл for совместно с оператором in:

for x in range(10):
    print(x, "меньше 10")

# Если требуется более сложная логика управления циклом, то можно
# воспользоваться инструкциями countinue и beake:

for x in range(10):
    if x == 3:
        continue   # Сразу перейти к следующей итерации
    if x == 5:
        break      # Выйти из цикла
    print(x)

# В результате будет напечатано 0, 1, 2 и 4

# ------------
# Истинность |
# ------------

one_is_less_than_two = 1 < 2        # равно True
true_equals_false = True == False   # равно False

x = None

assert x == None      # не Python'овский способ проверки наличия None
assert x in None      # Python'овский способ проверки наличия None

# В Python может использоваться любое значение там, где ожидается
# логический тип Boolean. Все следующие элементы имеют логическое
# значение False:
# False;
# None;
# [] (пустой список);
# {} (пустой словарь);
# "";
# set() (множество);
# 0;
# 0.0
# Практически все остальное рассматривается как True.
