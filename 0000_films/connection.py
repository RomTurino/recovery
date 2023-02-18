import psycopg2

database = {
    'database': 'film_generator',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5432    
}



def get_connection(func):
    def wrapper(*args, **kwargs):
        with psycopg2.connect(**database) as conn:
            with conn.cursor() as cur:
                return func(cur, *args, **kwargs)
    return wrapper

def exc_log(con, string):
    con.execute(string)
    with open('insertion.sql', 'a', encoding='utf-8') as file:
        file.write(string)