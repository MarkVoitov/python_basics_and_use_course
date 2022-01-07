# Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя.
# Например, число 2 является простым, так как делится только на 1 и 2.
# Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел.
# Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4.
# Также простым не является число 1, так как оно имеет ровно один делитель – 1.

# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

# Пример использования:

# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]




def primes():
    a = 2
    while True:
        count = 0
        for i in range(a):
            if a % (i + 1) == 0:
                count += 1
        if count == 2:
            yield a
        a += 1
