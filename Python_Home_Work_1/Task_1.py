# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

dayWeek = int(input('Введите день недели: '))

if dayWeek > 7:
    print('Ошибка, в неделе всего 7 дней! Повторите еще раз')
else:
    if dayWeek == 6 or dayWeek == 7:
        print('Чешим пузо и смотрим телик')
    else:
        print('Опять работа')