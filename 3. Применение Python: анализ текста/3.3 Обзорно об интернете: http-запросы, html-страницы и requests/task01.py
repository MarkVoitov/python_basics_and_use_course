# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

# Sample Input 1:
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
# Sample Output 1:
# Yes

# Sample Input 2:
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample1.html
# Sample Output 2:
# No

# Sample Input 3:
# https://stepic.org/media/attachments/lesson/24472/sample1.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
# Sample Output 3:
# Yes




import re
import requests
import sys

url_ab = []
for line in sys.stdin:
    line = line.strip()
    url_ab.append(line)

res = requests.get(url_ab[0])
pattern = r'<a href="(.*)".*'
result = re.findall(pattern, res.text)

res_list = []
for link in result:
    res2 = requests.get(link)
    result2 = re.findall(pattern, res2.text)
    res_list.append(result2)

res_list = [x for l in res_list for x in l]

if url_ab[1] in res_list:
    print('Yes')
else:
    print('No')
