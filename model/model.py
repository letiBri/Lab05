from database.corso_DAO import getCorsi, addIscrizione, getHasIscritto
from database.studente_DAO import getIscritti, getStudente, getCorsiStudente

class Model:
    def __init__(self):
        pass

    def elencoCorsi(self):
        return getCorsi()

    def cercaIscritti(self, codiceCorso):
        return getIscritti(codiceCorso)

    def cercaStudente(self, matricola):
        return getStudente(matricola)

    def cercaCorsi(self, matricola):
        return getCorsiStudente(matricola)

    def aggiungiIscrizione(self, matricola, codiceCorso):
        return addIscrizione(matricola, codiceCorso)

    def hasIscritto(self, matricola, codiceCorso):
        return getHasIscritto(matricola, codiceCorso)
