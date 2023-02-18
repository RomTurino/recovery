import psycopg2

database = {
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5432    
}



def get_connection(func):
    def wrapper():
        with psycopg2.connect(**database) as conn:
            with conn.cursor() as cur:
                func(cur)
    return wrapper

def exc_log(con, string):
    con.execute(string)
    with open('insertion.sql', 'a', encoding='utf-8') as file:
        file.write(string)