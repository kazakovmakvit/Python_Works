# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
numm_p = list(input('Введите числа через пробел ').split(' '))

int_numm_p = [int(x) for x in numm_p]
len_int_numm_p = len(int_numm_p)
list_pr = []
count_ = 0

while len_int_numm_p / 2 > count_:
    list_pr.append(int_numm_p[count_] * int_numm_p[(len_int_numm_p - 1) - count_])
    count_ += 1
print(list_pr)