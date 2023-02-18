from connection import get_connection
from read_info import read_students, read_subjects
from connection import exc_log


def add_teacher_or_student(cur, table_name):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    pater_name = input('Введите отчество: ')
    sex = input('Выберите пол (1 - мужской, 2 - женский):')
    while sex not in '1 2'.split():
        sex = input('Выберите пол (1 - мужской, 2 - женский):')
    sex = 'male' if sex == '1' else 'female'
    phone_number = ''
    while not phone_number.isdigit():
        phone_number = input('Введите номер телефона: ')
    cur.execute(f'SELECT COUNT(*) FROM {table_name}')
    id = cur.fetchone()[0] + 1
    try:
        exc_log("INSERT INTO %s VALUES (%d, '%s', '%s', '%s', '%s', '%s');" % (
            table_name, id, first_name, last_name, pater_name, sex, phone_number
        ))
        print('Успешно добавлена новая запись!')
        return id
    except:
        print('Что-то не получилось')

@get_connection
def add_student(cur=None):
    add_teacher_or_student(cur, table_name='students')

@get_connection
def add_teacher(cur=None):
    teacher_id = add_teacher_or_student(cur, table_name='teachers')
    cur.execute("""
                SELECT subject_id, name
                FROM subjects
                WHERE fk_teacher_id IS NULL
                """)
    lessons = cur.fetchall()
    if not lessons:
        print('Добавьте сначала предмет')
        return None
    for i, name in lessons:
        print(f"{i}) {name}")
    subject_id = input('Введи порядковый номер предмета, который преподает учитель: ')
    try:
        exc_log("""
                    UPDATE subjects
                    SET fk_teacher_id = '%s'
                    WHERE subject_id = '%s'
                    """ % (teacher_id, subject_id))
        print('Дело сделано!')
    except:
        print('Что-то пошло не так')


@get_connection
def add_subject(cur=None):
    name = input('Введите название предмета: ')
    
    cur.execute('SELECT COUNT(*) FROM subjects')
    id = cur.fetchone()[0] + 1
    try:
        exc_log("INSERT INTO subjects VALUES (%d, '%s');" % (
            id, name
        ))
        print('Успешно добавлена новая запись!')
    except:
        print('Что-то не получилось')

def get_subject_id(cur):
    read_subjects()
    lesson = ''
    while not lesson.isdigit():
        lesson=input('По какому предмету ставим оценку? ')
    lesson = int(lesson)
    cur.execute("""
                SELECT name
                FROM subjects
                WHERE subject_id=%s
                """ % (lesson))
    try:
        lesson_id = cur.fetchone()[0]
        return lesson_id
    except:
        print('Нет такого предмета!')
        return None

def get_student_id(cur):
    read_students()
    student = ''
    while not student.isdigit():
        student=input('Выберите порядковый номер ученика: ')
    student = int(student)
    cur.execute("""
                SELECT name
                FROM subjects
                WHERE subject_id=%s
                """ % (student))
    try:
        stud_id = cur.fetchone()[0]
        return stud_id
    except:
        print('Нет такого ученика!')
        return None


@get_connection
def add_mark(cur=None):
    cur.execute('SELECT COUNT(*) FROM marks')
    id = cur.fetchone()[0] + 1
    student_id = get_student_id(cur)
    subject_id = get_subject_id(cur)
    mark = ''
    while True: 
        if  mark.isdigit() and mark in '12345':
            break
        mark = input('Введите оценку от 1 до 5: ')
    mark = int(mark)
    try:
        exc_log("INSERT INTO marks VALUES (%d, '%d', '%d', '%d');" % (
            id, mark, student_id, subject_id 
        ))
        print('Успешно добавлена новая запись!')
    except Exception as ex:
        print('Что-то не получилось', ex.args)
    
@get_connection
def show_tabel(cur=None):
    student_id = get_student_id(cur)
    cur.execute("""
                SELECT first_name, last_name, pater_name, sex, phone_number
                FROM students
                WHERE student_id = '%s';
                """ % (student_id))
    student = cur.fetchone()
    cur.execute("""
                SELECT subjects.name , AVG(mark)
                FROM marks
                INNER JOIN students ON fk_student_id = students.student_id
                INNER JOIN subjects ON fk_subject_id = subjects.subject_id 
                WHERE fk_student_id = '%s'
                GROUP BY subjects.name
                ORDER BY subjects.name;
                """ % (student_id))
    avg_mark = cur.fetchall()
    cur.execute("""
                SELECT subjects.name , mark
                FROM marks
                INNER JOIN students ON fk_student_id = students.student_id
                INNER JOIN subjects ON fk_subject_id = subjects.subject_id 
                WHERE fk_student_id = '%s'
                ORDER BY subjects.name;
                """ % (student_id))
    all_marks = cur.fetchall()
    print("Ученик %s %s %s\nПол: %s\nНомер телефона: %s" % (student))
    chosen_lesson = ''
    avg_ind = 0
    for lesson, mark in all_marks:
        if lesson != chosen_lesson:
            print(f"\n\nПредмет:{lesson}.\n\tСредняя оценка: {round(avg_mark[0][1],1)}\n\tОценки:", end=' ')
            avg_ind+=1
            chosen_lesson = lesson
        print(mark, end=' ')
    print('')        

