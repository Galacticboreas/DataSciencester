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

from collections import defaultdict

word_count = defaultdict(int)       # int() возвращает 0
for word in document:
    word_count[word] += 1

# Кроме того, использование словарей defaultdict имеет практическую
# пользу во время работы со списками, словарями и даже со собственными
# функциями:

dd_list = defaultdict(list)        # list() возвращает пустой список
dd_list[2].append(1)               # Теперь dd_list содержит {2: [1]}

dd_dict = defaultdict(dict)        # dict() возвращает пустой словарь dict
dd_dict["Джоел"]["город"] = "Сиэтл"  # { "Джоэл" : { "город" : "Сиэтл"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                  # Теперь dd_pair содержит {2: [0,1]}

# Эти возможности понадобятся, когда словари будут использоваться для "сбора"
# результатов по некоторому ключу и когда необходимо избежать повторяющихся
# проверок на присутствие ключа в словаре

# Счетчики

# Словарь-счетчик Couner трансформирует последовательность значений в объект,
# похожий на словарь defaultdict(int), где ключам поставлены в соответствие
# количества появлений. Он в основном будет применяться при создании гисто-
# грамм:

from collections import Counter

c = Counter([0, 1, 2, 0])     # В результате с равно { 0 : 2, 1 : 1, 2 : 1 }

# Лучший вариант подсчета количества появлений слов
word_counts = Counter(document)

# Словарь Counter располагает методом most_common, который нередко бывает
# полезен:

# Напечатать 10 наиболее встречаемых слов и их количество появлений
for word, count in word_counts.most_common(10):
    print(word, count)
