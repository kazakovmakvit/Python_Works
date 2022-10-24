# Указать командам исполняющие методы.

from telegram.ext import ApplicationBuilder, CommandHandler
from telegram_bot_commands import *
from User_Interface import user_choice
from process import data_processor
from work_file import read_file

app = ApplicationBuilder().token("5459035295:AAEW1z7_Dd7BWOma0w6oZZVh-R0-g6ncnx0").build()

app.add_handler(CommandHandler("f1", help_command))          # Показать список команд

app.add_handler(CommandHandler("1", id_command))             # 1 - вывод ID
app.add_handler(CommandHandler("2", fio_command))            # 2 - вывод ФИО
app.add_handler(CommandHandler("3", birthday_command))       # 3 - вывод ДР
app.add_handler(CommandHandler("4", progress_command))       # 4 - вывод успеваемости
app.add_handler(CommandHandler("5", sex_command))            # 5 - вывод пола
app.add_handler(CommandHandler("6", all_data_command))       # 6 - вывод всех данных
app.add_handler(CommandHandler("0", exit_command))           # 0 - выход

print('server start')

app.run_polling()


