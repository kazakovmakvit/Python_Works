from os.path import exists
from Table_Header import creating
from Save_option import writing_scv
from Save_option import writing_txt


path = 'Python_Home_Work_7/Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()