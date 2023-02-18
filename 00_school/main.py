from init import database_init
from create_operations import *
from read_info import *

while True:
    menu = '''
        1 - инициализировать все таблицы
        2 - добавить ученика
        3 - добавить предмет
        4 - добавить оценку
        5 - показать всех учеников
        6 - показать только мальчиков
        7 - показать только девочек
        8 - показать табель успеваемости ученика
        9 - добавить преподавателя
        0 - выйти
    '''
    item = input(f'Добро пожаловать в электронный дневник! Выберите один из пунктов:\n{menu}')
    if item == '1':
        database_init()
        print('Созданы все таблицы!')
    elif item == '2':
        add_student()
    elif item == '3':
        add_subject()
    elif item == '4':
        add_mark()
    elif item == '5':
        read_students()
    elif item == '6':
        read_males()
    elif item == '7':
        read_female()
    elif item == '8':
        show_tabel()
    elif item == '9':
        add_teacher()
    elif item == '0':
        print('Всего доброго!')
        exit()
        
    input('Нажмите Enter, чтобы продолжить')
        
        


