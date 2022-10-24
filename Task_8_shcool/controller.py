from telegram import Update
from telegram.ext import ContextTypes
from User_Interface import user_choice
from  process import data_processor
from work_file import *
import telegram_bot_commands as tbc

data = 'Task_8_stud/processing_model.csv'
user_list = data_processor(read_file(data), user_choice())
print(user_list)
tbc.id_command(Update, ContextTypes)

write_file(user_list, mod='a')