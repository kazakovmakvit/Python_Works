a = int(input("Введите число a: "))
d = 2
mylist = []
while a != 1:
    if a % d:
        d += 1
    else:
        mylist.append(d)
        a /= d
print("Его делители:")
print(mylist)



k = 2
numbs = []
a = int(input('Введите число : '))
while a != 1:
    if a % k == 0:
        numbs.append(k)
        a //= k
    else:
        k += 1
print(numbs)
