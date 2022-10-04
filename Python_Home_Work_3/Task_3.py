# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from asyncio.windows_events import NULL


list_v_num = input('Введите список вещественных чисел через пробел "Пример 5.120 6.2 1 4": ').split()

float_list_v_num = []
max = NULL
min = 99999999999999999999999999999999999999999999999999999       #я не могу понять как сделать иначе )))) САМАЯ СЛОЖНАЯ ДЛЯ МЕНЯ ЗАДАЧА БЫЛА )))
diff = NULL



for x in list_v_num:
    for j in x:
        if j != '.':
            continue
        else: 
            temp = x
            temp_int = temp.split('.')
            fraction = int(temp_int[1])

            if fraction > max:
                max = fraction

            if fraction < min:
                min = fraction
            
    diff: float = max - min

print(f'0.{diff}') # Хитро правда ?)

