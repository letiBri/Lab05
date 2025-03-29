import flet as ft

from model import corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillListaCorsi(self):
        lista = self._model.elencoCorsi()
        for i in lista:
            self._view.listaCorsi.options.append(ft.dropdown.Option(key=i.codins, text=str(i))) #dovrei salvare l'oggetto Corso

    def handle_searchIscritti(self, e):
        codiceCorso = self._view.listaCorsi.value
        if codiceCorso is None:
            self._view.create_alert("Attenzione: non hai scelto un corso!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: non hai scelto un corso", color="red"))
            self._view.update_page()
            return
        listaStudenti = self._model.cercaIscritti(codiceCorso)
        lunghezzaLista = len(listaStudenti)
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {lunghezzaLista} iscritti al corso:"))
        for studente in listaStudenti:
            self._view.txt_result.controls.append(ft.Text(str(studente)))
        self._view.txt_result.controls.append(ft.Text("-------------------------------------------------"))
        self._view.update_page()
        return

    def handle_searchStudente(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Attenzione: non hai inserito una matricola!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: non hai inserito una matricola", color="red"))
            self._view.update_page()
            return
        nome, cognome = self._model.cercaStudente(matricola)
        if nome == "":
            self._view.create_alert("Attenzione: la matricola non esiste!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: la matricola non esiste", color="red"))
            self._view.update_page()
            return
        self._view.txt_nome.value = nome
        self._view.txt_cognome.value = cognome
        self._view.update_page()
        return

    def handle_searchCorsi(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Attenzione: non hai inserito una matricola!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: non hai inserito una matricola", color="red"))
            self._view.update_page()
            return
        nome, cognome = self._model.cercaStudente(matricola)
        if nome == "":
            self._view.create_alert("Attenzione: la matricola non esiste!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: la matricola non esiste", color="red"))
            self._view.update_page()
            return
        self._view.txt_nome.value = nome
        self._view.txt_cognome.value = cognome
        listaCorsi = self._model.cercaCorsi(matricola)
        lunghezzaLista = len(listaCorsi)
        self._view.txt_result.controls.append(ft.Text(f"Risultano {lunghezzaLista} corsi:"))
        for corso in listaCorsi:
            self._view.txt_result.controls.append(ft.Text(str(corso)))
        self._view.txt_result.controls.append(ft.Text("-------------------------------------------------"))
        self._view.update_page()
        return

    def handle_iscrivi(self, e):
        codiceCorso = self._view.listaCorsi.value
        if codiceCorso is None:
            self._view.create_alert("Attenzione: non hai scelto un corso!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: non hai scelto un corso", color="red"))
            self._view.update_page()
            return
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Attenzione: non hai inserito una matricola!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: non hai inserito una matricola", color="red"))
            self._view.update_page()
            return
        nome, cognome = self._model.cercaStudente(matricola)
        if nome == "":
            self._view.create_alert("Attenzione: la matricola non esiste!")
            #self._view.txt_result.controls.append(ft.Text("Attenzione: la matricola non esiste", color="red"))
            self._view.update_page()
            return
        self._view.txt_nome.value = nome
        self._view.txt_cognome.value = cognome
        if self._model.hasIscritto(matricola, codiceCorso):
            self._view.create_alert(f"Attenzione: lo studente {matricola} è gia iscritto al corso {codiceCorso}!")
            #self._view.txt_result.controls.append(ft.Text(f"Attenzione: lo studente {matricola} è già iscritto al corso {codiceCorso}", color="red"))
            self._view.update_page()
            return
        self._model.aggiungiIscrizione(matricola, codiceCorso)
        self._view.txt_result.controls.append(ft.Text(f"Lo studente {matricola} è stato aggiunto correttamente al corso {codiceCorso}", color="green"))
        self._view.update_page()
        return

