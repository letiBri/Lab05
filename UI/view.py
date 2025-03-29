import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None
        self.btn_searchIscritti = None
        self.listaCorsi = None
        self.btn_iscrivi = None
        self.btn_searchCorsi = None
        self.btn_searchStudente = None
        self.txt_cognome = None
        self.txt_nome = None
        self.txt_matricola = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)

        # aggiungo la dropdown dei corsi --> menu a tendina
        self.listaCorsi = ft.Dropdown(label="corso", hint_text="Selezionare un corso", width=500, options=[])
        self._controller.fillListaCorsi()

        # bottone che cerca gli iscritti
        self.btn_searchIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_searchIscritti)

        row = ft.Container(self._title, alignment=ft.alignment.center)
        row1 = ft.Row([self.listaCorsi, self.btn_searchIscritti], alignment=ft.MainAxisAlignment.CENTER)

        # textfield per la matricola
        self.txt_matricola = ft.TextField(label="matricola", width=200, hint_text="inserisci la matricola")
        self.txt_nome = ft.TextField(label="nome", width=200, read_only=True)
        self.txt_cognome = ft.TextField(label="cognome", width=200, read_only=True)

        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        #bottoni cliccabili
        self.btn_searchStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_searchStudente)
        self.btn_searchCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_searchCorsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)

        row3 = ft.Row([self.btn_searchStudente, self.btn_searchCorsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row, row1, row2, row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
