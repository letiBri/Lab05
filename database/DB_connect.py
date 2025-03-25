import mysql.connector
from mysql.connector import errorcode


def get_connection() -> mysql.connector.connection:
    try:
        cnx = mysql.connector.connect(
            option_files='./database/connector.cnf'
        )
        return cnx

    except BaseException as e:
        print(e)


