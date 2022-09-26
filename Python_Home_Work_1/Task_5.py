import math


x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
r = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(f'расстояние между точек = {r}')