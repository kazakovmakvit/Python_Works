"""4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции вводятся пользователем с клавиатуры. 5 2 8"""

n = int(input('Введите число "N" '))
list_ = []
n_comp = []
composition = 1
count_ = 1

def my_range_n(start: int, stop: int, inc: int = 1):
    while (start < stop and inc > 0):
        yield start
        start += inc

for i in my_range_n(-n, n + 1):
    list_.append(i)
    for i in range(len(list_)):
        list_[i] = int(list_[i])

print(list_)

n_comp = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, n_comp))
print(num_list)

for i in my_range_n(0, len(num_list)):
    box = num_list[i]
    composition = list_[box-1] * composition
print(composition)