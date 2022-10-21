import crud as cr


print('\nВас приветствует телефонная книга')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        
        print('1. Добавить новую запись.')
        print('2. Показать все записи.')
        print('3. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            email = input('Введите электронную почту: ')
            cr.create(name, surname, number, email)

        elif n == 2:
            print(cr.retrive())

        elif n == 3:
            print('Спасибо за работу!')
            break

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)