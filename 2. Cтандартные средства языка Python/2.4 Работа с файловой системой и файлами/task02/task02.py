# Вам дана в архиве (ссылка https://stepik.org/media/attachments/lesson/24465/main.zip) файловая структура, состоящая из директорий и файлов.

# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 

# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

# Для лучшего понимания формата задачи, ознакомьтесь с примером.
# Пример архива https://stepik.org/media/attachments/lesson/24465/sample.zip
# Пример ответа https://stepik.org/media/attachments/lesson/24465/sample_ans.txt




import os

final_list = []
for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file[-3:] == '.py':
            current_dir = current_dir.replace("\\", "/")
            final_list.append(current_dir)
final_list = sorted(list(set(final_list)))

with open("task02.txt", "w") as w:
    answer = "\n".join(final_list)
    w.write(answer)
