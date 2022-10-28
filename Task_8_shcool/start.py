# Данный блок осуществляет авторизацию пользователя в системе \
# и регитсрацию нового пользователя.

import time
from registering_a_new_user import registering_a_new_user as r_new
from check_user_input import chek_use_inpt as check
from logger_action import logger_action as log
from color_out_text import out_green as green
from color_out_text import out_white as white
from color_out_text import out_red as red
from student import user_student_start as student
from teacher_menu import teacher_menu as teacher
from data_file import open_data_user as open_
from data_file import add_record_new_user as record_


def start():
    print('Школа ГБ Приветствует вас!\n')
    path = 'data_users.txt'
    while True:
        print('Выберите действие:\n\
            \n1.Регистрация\n2.Вход\n3.Завершить работу')
        select_ = None
        user_list = None
        select_ = check(1)
        list_data = open_(path)
        if select_:
            if select_ == '1':
                new_user = r_new(list_data)
                if new_user:
                    log(\
                        f'зарегистрировал новый контакт: {new_user[2]} {new_user[3]}    ')
                    list_data = record_(list_data, new_user, path)
                    green('\nПользователь успешно зарегистрирован в системе.')
                    white('')
                else:
                    continue
            elif select_ == '2':
                log_ = check(2, list_data)
                if log_:
                    log(f'пытается зайти под логином: {log_}')
                    user_list = [i for i in list_data if i[0] == log_]
                    if user_list:
                        user_list = user_list[0]
                    else:
                        continue
                else:
                    continue
                password = check(3, user_list)
                if password:
                    log(f'успешно авторизовался в системе под логином: {log_}')
                    print('')
                    if user_list[5] == '0':
                        log('перешел в меню ученика.')
                        user_list = student(list_data, user_list)
                    elif user_list[5] == '1':
                        log('перешел в меню преподавателя.')
                        user_list = teacher(list_data, user_list)
                    else:
                        log('авторизовал неизвестный аккаунт.')
                        print('Неизвестный пользователь.')
                        user_list.clear()
                        continue
                else:
                    continue
            elif select_ == '3':
                log('вышел из программы.')
                return print('Программа завершена')
        else:
            red('От греха подальше ....')
            print('Программа завершится через 3 секунды')
            print('Прощайте. ')
            white('')
            time.sleep(3)
            log('принудительно и по доброй воле вышел из программы.')
            return print('Программа завершена')


start()