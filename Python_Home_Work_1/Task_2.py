"""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """

#{Не уверен что верно!}


xyz = ["X", "Y", "Z"]
a = []
for i in range(3):
    a.append(input(f"Введите значение {xyz[i]}: "))

left = not (xyz[0] or xyz[1] or xyz[2])
right = not xyz[0] and not xyz[1] and not xyz[2]
result = left == right


if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")