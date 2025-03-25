from database.corso_DAO import getCorsi
from database.studente_DAO import getIscritti

class Model:
    def __init__(self):
        pass

    def elencoCorsi(self):
        return getCorsi()

    def cercaIscritti(self, codiceCorso):
        return getIscritti(codiceCorso)
