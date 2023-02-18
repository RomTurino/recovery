from connection import get_connection


def say_nothing():
    print('Упс! Пока пусто!')
    

@get_connection
def read_students(con=None):
    con.execute('SELECT * FROM students')
    students = con.fetchall()
    if not students:
        say_nothing()
        return None
    headers = '№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона'
    print(headers)
    for student in students:
        print(*student, sep='\t')
    
@get_connection
def read_subjects(con=None):
    con.execute("""
                SELECT "name", last_name, first_name, pater_name
                FROM subjects
                INNER JOIN teachers ON fk_teacher_id = teachers.teacher_id;
                """)
    subjects = con.fetchall()
    if not subjects:
        say_nothing()
        return None

    for subject in subjects:
        name = subject.pop(0)
        fio = " ".join(subject) if subject[0] else "отсутствует"
        print("Название предмета %s Преподаватель: %s" % (name, fio))


@get_connection
def read_female(con=None):
    con.execute("SELECT * FROM students WHERE sex='female'")
    students = con.fetchall()
    if not students:
        say_nothing()
        return None
    headers = '№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона'
    print(headers)
    for student in students:
        print(*student, sep='\t')        

@get_connection
def read_males(con=None):
    con.execute("SELECT * FROM students WHERE sex='male'")
    students = con.fetchall()
    if not students:
        say_nothing()
        return None
    headers = '№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона'
    print(headers)
    for student in students:
        print(*student, sep='\t')




      
if __name__ == '__main__':
    read_subjects()