# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numm_n = int(input('Введите натуральное число n - '))

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac

print(primfacs(numm_n))
