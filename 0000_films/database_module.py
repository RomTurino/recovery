import random
from connection import get_connection, exc_log


@get_connection
def init_db(con=None):
    exc_log(con, """
                CREATE TABLE IF NOT EXISTS films
                (
                    film_id int PRIMARY KEY,
                    title varchar(256) NOT NULL,
                    image text NOT NULL,
                    description text
                ) 
                """)


@get_connection
def add_film(con=None,
             title='',
             image='',
             description=''):
    con.execute("SELECT COUNT(*) FROM films")
    film_id = int(con.fetchone()[0]) + 1
    con.execute(f"SELECT * FROM films WHERE title='%{title}%'")
    is_film_there = con.fetchone()
    if not is_film_there:
        return None
    con.execute("""
                INSERT INTO films VALUES
                (%d, '%s', '%s', '%s')
                """ % (film_id, title, image, description))
    return True
    
@get_connection
def delete_film(con=None,
                title=''):
    try:
        con.execute(f"DELETE FROM films WHERE title='%{title}%'")
        return True
    except:
        return False
    
@get_connection
def get_film(con=None):
    con.execute("""
                SELECT title, image, description
                FROM films
                """)
    films = con.fetchall()
    if not films:
        return False
    title, image, description = random.choice(films)
    return title, image, description 