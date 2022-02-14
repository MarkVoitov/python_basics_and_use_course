# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

# Одним из атрибутов преступления является его тип – Primary Type.

# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

# Файл с данными:
# Crimes.csv




import csv
from collections import Counter

with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    types_counter = []
    for row in reader:
        if row["Date"][6:10] == "2015":
            types_counter.append(row["Primary Type"])
            
print(Counter(types_counter).most_common(1)[0][0])
