import psycopg2
from db_create_connect_fill.config import host, user, password, db_name, port

def connToDb ():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    return connection