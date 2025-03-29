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

def addIscrizione(matricola, codiceCorso):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """insert into iscrizione (matricola, codins) values (%s, %s)"""
    cursor.execute(query, (matricola, codiceCorso))
    cnx.commit()
    cnx.close()
    return

def getHasIscritto(matricola, codiceCorso):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """ select * from iscrizione where matricola=%s and codins=%s"""
    cursor.execute(query, (matricola, codiceCorso))
    result = cursor.fetchall()
    cnx.close()
    return len(result) > 0

