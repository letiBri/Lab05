# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


def getIscritti(codiceCorso):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """select studente.matricola, studente.cognome, studente.nome, studente.CDS
                from studente, iscrizione
                where codins =%s and studente.matricola = iscrizione.matricola"""
    cursor.execute(query, (codiceCorso, ))
    result = []
    for row in cursor:
        result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
    cnx.close()
    return result

def getStudente(matricola): #restituisce nome, cognome dello studente che cerchiamo attraverso la matricola
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query= """ select nome, cognome from studente where matricola=%s"""
    cursor.execute(query, (matricola, ))
    nome = ""
    cognome = ""
    for row in cursor:
        nome = row["nome"]
        cognome = row["cognome"]
    cnx.close()
    return nome, cognome

def getCorsiStudente(matricola):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """select corso.codins, crediti, nome, pd
                from corso, iscrizione 
                where iscrizione.matricola=%s and iscrizione.codins=corso.codins"""
    cursor.execute(query, (matricola, ))
    result = []
    for row in cursor:
        corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
        result.append(corso)
    cnx.close()
    return result
