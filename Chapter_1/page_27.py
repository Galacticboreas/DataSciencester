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

