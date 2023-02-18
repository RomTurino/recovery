from connection import get_connection


@get_connection
def create_table_students(cur=None):
    cur.execute('''
                CREATE TABLE IF NOT EXISTS students 
                (
                    student_id int PRIMARY KEY,
                    first_name varchar(64) NOT NULL,
                    last_name varchar(64) NOT NULL,
                    pater_name varchar(64) NOT NULL,
                    sex varchar(6),
                    phone_number varchar(12) NOT NULL
                )
                ''')


@get_connection
def create_subjects(cur=None):
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS subjects 
                (
                    subject_id int PRIMARY KEY,
                    name varchar(128) NOT NULL,
                    fk_teacher int REFERENCES teachers(teacher_id)
                )
        '''
    )


@get_connection
def create_marks(cur=None):
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS marks 
                (
                    mark_id int PRIMARY KEY,
                    mark int CHECK(mark IN (1,2,3,4,5)) NOT NULL,
                    fk_student_id int REFERENCES students(student_id) ON DELETE CASCADE,
                    fk_subject_id int REFERENCES subjects(subject_id) ON DELETE CASCADE
                )
        '''
    )


@get_connection
def create_teachers(cur=None):
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS teachers 
                (
                    teacher_id int PRIMARY KEY,
                    first_name varchar(64) NOT NULL,
                    last_name varchar(64) NOT NULL,
                    pater_name varchar(64) NOT NULL,
                    sex varchar(6),
                    phone_number varchar(12) NOT NULL
                )
        '''
    )




@get_connection
def drop_databases(con=None):
    con.execute('DROP table IF EXISTS teachers')
    con.execute('DROP table IF EXISTS marks')
    con.execute('DROP table IF EXISTS students')
    con.execute('DROP table IF EXISTS subjects')


def database_init():
    drop_databases()
    create_table_students()
    create_subjects()
    create_marks()
    create_teachers()