def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()






def input_data():
    data_type = input(' 1 работа с комплексными числами,\n\
                        2 работа с рациональными числами')
                        
    if data_type == '1':

        left_value = input('Введите первое число:')
        right_value =input('Введите второе число 3j:')

        if right_value[-1] != 'j':
            right_value.write('j')
            
        print(right_value)

        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (используйте формат: "5/11"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "5/11"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    return (data_type, left_value, oper, right_value)