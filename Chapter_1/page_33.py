from collections import defaultdict


# Зарплаты и стаж
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Зарплата в зависимости от стажа.
# Ключи - это годы, значения - списки зарплат для каждого стажа
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Средняя зарплата в зависимости от стажа.
# Ключи - это годы, каждое значение - средняя зарплата по этому стажу
average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print(average_salary_by_tenure)

# Целесообразнее разбить продолжительности стажа на группы:

# Стажная группа
def tenure_bucket(tenure):
    if tenure < 2:
        return "менее двух"
    elif tenure < 5:
        return "между двумя и пятью"
    else:
        return "более пяти"

# Зарплата в зависимости от стажной группы.
# Ключи - это стажные группы, значения - списки зарплат в этой группе.
# Словарь содержит списки зарплат, соответствующие каждой стажной группе
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Средняя зарплата по группе.
# Ключи - это стажные группы, значения - средняя зарплата по этой группе
average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print(average_salary_by_bucket)
