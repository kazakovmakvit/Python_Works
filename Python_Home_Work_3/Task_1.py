# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

summ = 0
count_ = 1
list_p = list(input('Введите числа через пробел: ').split(' '))
int_list_p = [int(x) for x in list_p]

while len(int_list_p) > count_:
    summ = int_list_p[count_] + summ
    count_ += 2
print(summ)