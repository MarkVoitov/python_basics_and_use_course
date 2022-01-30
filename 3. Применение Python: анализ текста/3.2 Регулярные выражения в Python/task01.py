# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так

# import sys

# for line in sys.stdin:
#     line = line.rstrip()
#     # process line

# Sample Input:
# catcat
# cat and cat
# catac
# cat
# ccaatt

# Sample Output:
# catcat
# cat and cat




import sys

cat_list = []
for line in sys.stdin:
    line = line.rstrip()
    cat_list.append(line)

for i in cat_list:
    if i.count("cat") >= 2:
        print(i)
