# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


def getCorsi():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT * FROM corso"""
    cursor.execute(query)
    result = []
    for row in cursor:
        corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
        result.append(corso)
    cnx.close()
    return result



