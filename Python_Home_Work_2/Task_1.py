#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите вещественное число через точку: ')

num_int = num.split('.')
remainder = int(num_int[0]) # целая часть
numbers = int(num_int[1])   # дробная
sum = 0

while remainder != 0:
    sum = sum + (remainder % 10)
    remainder //= 10

while numbers != 0:
    sum = sum + (numbers % 10)
    numbers //= 10
    
print(f'Сумма цифр числа: {num}, равна: {sum}')
