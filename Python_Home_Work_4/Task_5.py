# аны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import random


with open('Python_Home_Work_4/poly_1.txt', 'w', encoding='utf-8') as file:
    file.write(f'{int(random()* 100)}*x^2 + {int(random()* 100)}*x^5')

with open('Python_Home_Work_4/poly_2.txt', 'w', encoding='utf-8') as file:
    file.write(f'{int(random()* 100)}*x^4 + {int(random()* 100)}*x^6')

with open('Python_Home_Work_4/poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('Python_Home_Work_4/poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('Python_Home_Work_4/sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')