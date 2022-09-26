# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

X = int(input('Введите Х: '))
Y = int(input('Введите Y: '))

if X == 0 or Y == 0:
    print('X ≠ 0 и Y ≠ 0')
else:
    if X < 0 and Y > 0:
        print('1')
    else:
        if X > 0 and Y > 0:
            print('2')
        else:
            if X < 0 and Y < 0:
                print('3')
            else:
                print('4')