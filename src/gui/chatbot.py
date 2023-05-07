import tkinter as tk
from src.utils.logging import LoggingTkClass

from tkinter.font import *
from src.gui.results import ResultsWindow
from src.gui.questionPage import QuestionPageWindow
from src.constants.data import welcome_message
from src.utils.logging import log



class ChatbotWindow(LoggingTkClass):

    def __init__(self):
        
        super().__init__(800, 520, "Orientador Vocacional CUCOSTA" )  # Llamada al constructor de la clase padre
        
        self.init_components()

    def init_components(self):

        # Informar al log que la ventana fue invocada
        log(self.logger, "La ventana principal del orientador fue invocada")

        # Añadir imagen
        self.logo = tk.PhotoImage(file="./resources/logo.png")
        Lbl_logo = tk.Label(self, image=self.logo)
        Lbl_logo.grid(row=0, column=0, padx=10, pady=10, sticky="NE")

        # Texto introductorio
        Lbl_introduction = tk.Label(self, text=welcome_message)
        Lbl_introduction.config(foreground='#6209be', font=self.title_font)
        Lbl_introduction.grid(row=1, column=0, columnspan=2,
                              padx=10, pady=10, sticky="N")

        # Botón para invocar el questionario (formulario)
        self.startButtonLogo = tk.PhotoImage(file="./resources/rButton.png")
        Btn_invoke = tk.Button(self, image=self.startButtonLogo, borderwidth=0,
                               highlightthickness=0, command=self.invoke_next_form)
        Btn_invoke.grid(row=3, column=0, columnspan=2,
                        padx=10, pady=10, sticky="S")

    def invoke_next_form(self):
        
        log(self.logger, "Se ha invocado next_form")

        self.destroy()

        # Invocar el formulario que contiene las preguntas
        question_window = QuestionPageWindow()
        question_window.mainloop()
