"""2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

num_ = int(input("Введите число: "))
count_ = 1
list_ = []

def my_range(start: int, stop: int, inc: int = 1):
    while (start < stop and inc > 0):
        yield start     # Ключевое слово yield возврат с сохранением состояния переменной
        start += inc

for i in my_range(1, num_):
    count_ *= i
    list_.append(count_)
print(list_)


# долго думал, как сделать
# получился вот такой костыль) но вроде работает )