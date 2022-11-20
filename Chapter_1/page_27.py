from operator import truediv
from collections import Counter


users = [
    {"id": 0, "name": "Herro"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]
friendships_f = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9),]

# Инициализировать словарь пустым списком для идентификатора
# каждого пользователя
friendships = {user["id"]: [] for user in users}
# {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

# И перебрать все дружеские пары, заполняя их:
for i, j in friendships_f:
    friendships[i].append(j) # Добавить j как друга для i
    friendships[j].append(i) # Добавить i как друга для j
# {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [4, 6, 7], 6: [5, 8], 
# 7: [5, 8], 8: [6, 7, 9], 9: [8]}

# число друзей
def number_of_friends(user):
    """Сколько друзей есть у пользователя user?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
total_connections = sum(number_of_friends(user) for user in users)
# Суммарное число связей 24

num_users = len(users) # Длина списка пользователей
avg_connections = total_connections / num_users # 24 / 10 = 2.4

# Создать список в формате (id пользователя, число друзей)
num_friends_by_id = [(user["id"], number_of_friends(user))
                    for user in users]

# Отсортировать список по полю num_friends в убывающем порядке
num_friends_by_id.sort(
        key=lambda id_and_friends: id_and_friends[1],
        reverse=True)

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]   #   По каждому моему другу
        for foaf_id in friendships[friend_id]   #   отыскать его друзей,
        if foaf_id != user_id                   #   которые не являются мной
        and foaf_id not in friendships[user_id] #   и не являются моими друзьями
    )

print(friends_of_friends(users[3]))             # Counter({0: 2, 5: 1})

# Интересы пользователей
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
