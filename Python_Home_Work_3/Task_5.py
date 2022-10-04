# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

len_fibonachi = int(input('Введите число'))
list_fibonachi = [0, 1]

for x in range(len_fibonachi - 1):
    list_fibonachi.append(list_fibonachi[-2] - list_fibonachi[-1])

list_fibonachi.reverse()

for x in range(len_fibonachi):
    list_fibonachi.append(list_fibonachi[-1] + list_fibonachi[-2])

print(list_fibonachi)