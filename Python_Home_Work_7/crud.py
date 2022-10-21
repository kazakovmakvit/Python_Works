import csv
import os.path



db_file_name = ''
db = []

def init_data_base(file_name='db.csv'):
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()

    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
    else:
        open(db_file_name, 'w', newline='', encoding='utf-8').close()
    

def create(name='', surname='', number='', email=''):
    global db
    global db_file_name
    if(name == ''):
        print("Имя не указано, Запись не произведена!")
        return
    if(surname == ''):
        print("Фамилия не указано, Запись не произведена!")
        return
    if(number == ''):
        print("Телефон не указано, Запись не произведена!")
        return
    if(email == ''):
        print("Элетронная почта не указано, Запись не произведена!")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            return

    new_row = [name.title(), surname.title(), number, email.lower()]
    db.append(new_row)

    with open(db_file_name, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)

def retrive(name='', surname='', number='', email=''):
    global db
    global db_file_name
    result = []
    for row in db:
        if(name != '' and row[0] != name.title()):
            continue
        if(surname != '' and row[1] != surname.title()):
            continue
        if(number != '' and row[2] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result

