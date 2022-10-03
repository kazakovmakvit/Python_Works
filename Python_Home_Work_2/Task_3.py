#3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.  - Для n = 6: 14.07
n = int(input('Введите число n '))
list_ =[]
summ_: float = 0

def range_n (start: int, stop: int, inc: int = 1):
    while start < stop and inc > 0:
        yield start
        start += inc

for i in range_n(1, n + 1):
    list_.append((1 + (1 / i)) ** i)    

for const in range_n(1, len(list_)):
    summ_ = list_[const] + summ_
print(round(summ_, 2))