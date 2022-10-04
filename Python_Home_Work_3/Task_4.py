# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

x = int(input('Введите число для перевода в 2-чную систему: '))
list_x = []

while x > 0:
    x_ost = x % 2
    x //= 2
    if x_ost > 0:
        list_x.append(1)
    else:
        list_x.append(0)
    x = int(x)
list_x.reverse()
print(list_x)