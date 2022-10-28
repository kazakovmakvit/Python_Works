# Данный блок проверяет любой ввод пользователя на стадии шагов авторизации \
# и регистрации нового пользователя.

import re
from logger_action import logger_action as log
from color_out_text import out_red as red
from color_out_text import out_white as white
from color_out_text import out_yellow as yellow
from color_out_text import out_green as green


def check_chars_fullname(x):
    reg = re.search(r'^\D{2,20} \D{2,20} \w{2,20}$', x)
    return True if reg else False

def check_new_login(x):
    reg = re.search(r'^\w{2,20}$', x)
    return True if reg else False

def check_name_object(x):
    match = re.search(r'^\D{5,20}$', x)
    return True if match else False

def check_input_date(x):
    math = re.search(r'^\d\d.\d\d.\d{4}$', x)
    return True if math else False

def cheats_date (x):
    math = re.sub(r'\d\d.\d\d.\d{4}', f'{x[:2]}.09.2022', x)
    return math

def check_groupe_in_data(groupe, data):
    list_group_user = [i for i in data if i[7] == groupe]
    return True if list_group_user else False

def check_groupe_in_marks(groupe, data):
    list_group_user = [i for i in data if i[1] == groupe]
    return True if list_group_user else False

def chek_use_inpt(flag, user = None):
    count_ = 5
    login = None
    action = None
    while True:
        if flag == 1 and count_ > 0:
            input_ = input('\nвыберете пункт меню: ').strip()
            action = 'пункт меню'
        elif flag == 2 and count_ > 0:
            input_ = input('\nВведите ваш login: ').strip()
            action = 'логинн'
        elif flag == 3 and count_ > 0:
            input_ = input('\nВведите ваш пароль: ').strip()
            action = 'пароль'
        elif flag == 4 and count_ > 0:
            input_ = input('\nВведите ваше полное имя(ФИО) через пробел\n: ').strip()
            action = 'именя нового пользователя'
        elif flag == 5 and count_ > 0:
            input_ = input('\nВведите login (MIN-2 MAX-20): ').strip()
            action = 'логин нового пользователя'
        elif flag == 6 and count_ > 0:
            input_ = input('\nСтудент или учитель: ').strip().lower()
            action = 'принядлежность нового пользователя'
        elif flag == 7 and count_ > 0:
            input_ = input('\nВыберите свою группу:\n1.ГБ-Разработчик группа \n2.ГБ-Аналитик \n3.ГБ-Тестеровщик \nваш выбор: ').strip().lower()
            action = 'выбора группы'
        elif flag == 8 and count_ >0:
            input_ = input('\n Напишите название вашего предмета: ').strip().lower()
            action = 'названия предмета'
        else:
            log(f'Превысили допустимое количество попыток ввода {action} .')
            red('\nвы превысили количество попыток.\n')
            white('')
            return False
        try:
            if flag == 1:
                if input_ == '1' or input_ == '2' or input_ == '3':
                    return input_
                else:
                    raise ValueError
            elif flag == 2:
                if 0 < len(input_) < 10:
                    login = list(filter(lambda x: x[0] == input_, user))
                    if login:
                        return input_
                    else:
                        ValueError
                else:
                    raise ValueError
            elif flag == 3:
                if input_ == user[1]:
                    green(f'\nАвторизация выполнена. \
                        \nЗдравствуйте:, {user[2]} {user [3]} {user [4]} !')
                    white('')
                    return input_
                else:
                    raise ValueError
            elif flag == 4:
                if check_chars_fullname(input_):
                    return input_.strip().split()
                else:
                    raise ValueError
            elif flag == 5:
                if check_new_login(input_):
                    key_log = list(filter(lambda x: x[0] == input_, user))
                    if not key_log:
                        return input_
                    else:
                        raise NameError
                else:
                    raise ValueError
            elif flag == 6:
                if input_ == 'студент' or input_ == 'ученик':
                    return '0'
                elif input_ == 'учитель' or input_ == 'преподаватель':
                    return '1'
                else:
                    raise ValueError
            elif flag == 7:
                if input_ == '1' or input_ == '3-я' or input_ == '3-я группа' or input_ == '3':
                    return '3'
                elif input_ == '2' or input_ == '2-я' or input_ == '2-я группа' or input_ == '2':
                    return '2'
                elif input_ == '3' or input_ == '1-я' or input_ == '1-я группа' or input_ == '1':
                    return '1'
                else:
                    raise ValueError
            elif flag == 8:
                if check_name_object(input_):
                    return input_
                else:
                    raise NameError
        except ValueError:
            if flag == 1 and count_ == 5:
                red('\nНет такого пункта. Повторите ввод.\n')
                yellow('\nОшибка ввода, попробуйте еще раз\n')
            elif flag == 1:
                yellow('введите число соответстветствующее пункту меню.')
            elif flag == 2:
                yellow('\nТакого логина в базе нет.')
            elif flag == 3:
                yellow('\nВы ввели неверный пароль.')
            elif flag == 4:
                yellow('\nВы ввели неверный формат.')
            elif flag == 5:
                yellow('\nВы ввели неверный формат.')
            elif flag == 6:
                yellow('\nВы ввели неизвестное слово.')
            elif flag == 7:
                yellow('\nВыберите вашу группу из списка.')
            count_ -= 1
            if count_ > 0:
                print(f'Осталось {count_} попыток.')
                white('')
            continue
        except NameError:
            if flag == 5:
                yellow('\nлогин уже занят, придумайте другой.')
            elif flag == 8:
                yellow('\nэто не похоже на название предмета.')
            count_ -= 1
            if count_ > 0:
                print(f'Осталось {count_} попыток.')
                white('')
            continue