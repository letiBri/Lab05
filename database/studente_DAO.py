# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
def getIscritti(codiceCorso):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT matricola FROM iscrizione WHERE codins=codiceCorso"""
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row["matricola"])
    cnx.close()
    return result

