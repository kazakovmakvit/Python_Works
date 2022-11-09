from telebot import types
import telebot.types
from telebot import TeleBot
import cmath
import datetime

bot = TeleBot('5459035295:AAEW1z7_Dd7BWOma0w6oZZVh-R0-g6ncnx0')

value = ""
old_value = ""

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton("j", callback_data="j"),
                telebot.types.InlineKeyboardButton("C", callback_data="C"),
                telebot.types.InlineKeyboardButton("<=", callback_data="<="),
                telebot.types.InlineKeyboardButton("/", callback_data="/") )

keyboard.row(   telebot.types.InlineKeyboardButton("7", callback_data="7"),
                telebot.types.InlineKeyboardButton("8", callback_data="8"),
                telebot.types.InlineKeyboardButton("9", callback_data="9"),
                telebot.types.InlineKeyboardButton("*", callback_data="*") )

keyboard.row(   telebot.types.InlineKeyboardButton("4", callback_data="4"),
                telebot.types.InlineKeyboardButton("5", callback_data="5"),
                telebot.types.InlineKeyboardButton("6", callback_data="6"),
                telebot.types.InlineKeyboardButton("-", callback_data="-") )

keyboard.row(   telebot.types.InlineKeyboardButton("1", callback_data="1"),
                telebot.types.InlineKeyboardButton("2", callback_data="2"),
                telebot.types.InlineKeyboardButton("3", callback_data="3"),
                telebot.types.InlineKeyboardButton("+", callback_data="+") )

keyboard.row(   telebot.types.InlineKeyboardButton("", callback_data="no"),
                telebot.types.InlineKeyboardButton("0", callback_data="0"),
                telebot.types.InlineKeyboardButton(",", callback_data="."),
                telebot.types.InlineKeyboardButton("=", callback_data="=") )


def logger_action(action: str):
    today = datetime.datetime.today()
    with open('Task_kalk\log.txt', 'a', encoding='utf-8') as data:
        data.write(\
            f'{today.strftime("%Y-%m-%d-(%H) %H:%M")} Пользователь {action} \n')


@bot.message_handler(commands=['help'])
def help_answer(message: types.Message):
    logger_action('посмотрел справку.')
    bot.send_message(message.from_user.id, text='Калькулятор работает в автономном режиме, бот в закрытом Бета-тесте\n\
                                                 Возможны сбои, сообщите если такое случится\n\
                                                 Для решения  комплексного числа используется кнопка "J"')


@bot.message_handler(commands=['start', 'calculater'])
def getMessage(msg):
    global value
    if value == '':
        bot.send_message(msg.from_user.id, 'Калькулятор в вашем распоряжении', reply_markup=keyboard)
    else:
        bot.send_message(msg.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data


    logger_action(f'Запись данных пользователя: {data} .')
    if data == 'no':
        pass
    elif data == 'j':
        if value[-1] != 'j':
            value += data
    elif data == 'C':
        value = ''
        logger_action(f'Чистка поля {value}')
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
            logger_action(f'Удаление значение {value}')
    elif data == '=':
        try:
            if value.count('j'):
                logger_action('Пример комплексного числа.')
            logger_action(f'Ввод примера: {value}')
            value = str( eval(value) )
            logger_action(f'Ответ: {value} .')
        except Exception:
            value = 'Ошибка'
            logger_action(f'Ошибка')

    else:
        value += data

    if ( value != old_value and value != '') or ( '0' != old_value and value == '' ):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value
    
    if value == 'Ошибка':  
        logger_action('Ошибка ввода')
        value = ''

bot.polling(non_stop=False, interval=0)


