# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Вхождения строки t в строке s могут пересекаться.

# Sample Input 1:
# abababa
# aba
# Sample Output 1:
# 3

# Sample Input 2:
# abababa
# abc
# Sample Output 2:
# 0

# Sample Input 3:
# abc
# abc
# Sample Output 3:
# 1

# Sample Input 4:
# aaaaa
# a
# Sample Output 4:
# 5




s, t = (input() for _ in range(2))

count = 0
for i in range(len(s)):
    if s.find(t) == 0:
        count += 1
    s = s[1:]
print(count)
