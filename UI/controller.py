import flet as ft

from model import corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillListaCorsi(self):
        lista = self._model.elencoCorsi()
        for i in lista:
            self._view.listaCorsi.options.append(ft.dropdown.Option(key=i.codins, text=str(i)))

    def handle_searchIscritti(self, e):
        corsoScelto = self._view.listaCorsi.value
        if corsoScelto is None:
            self._view.txt_result.controls.append(ft.Text("Attenzione: non hai scelto un corso"))
            self._view.update_page()
            return
        codiceCorso = corsoScelto.codins
        listaStudenti = self._model.cercaIscritti(codiceCorso)
        for studente in listaStudenti:
            self._view.txt_result.controls.append(ft.Text(str(studente)))
        self._view.update_page()
        return

