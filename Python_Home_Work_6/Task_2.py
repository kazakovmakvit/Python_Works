# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n")

find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i] ###### list comprehension
print(f'Результат: {" ".join(lst)}')