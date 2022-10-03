from random import randint


n = 6 #int(input("введите кол-во элеементов списка: "))
a = [] * n

for i in range(0, n + 1 ):
    a.append(randint(0, n).split(','))
print(a)
..split(',')
