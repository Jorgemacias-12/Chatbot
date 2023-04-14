import tkinter as tk

from tkinter.font import *
from src.gui.results import ResultsWindow
from src.gui.questionPage import QuestionPageWindow
from src.constants.data import questions_size, welcome_message




class ChatbotWindow(tk.Tk):

    window_width = 800
    window_height = 520

    default_font = None
    title_font = None

    logo = None
    startButtonLogo = None

    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase padre

        # Configuración de la ventana
        self.title("Orientador Vocacional CUCOSTA")
        self.resizable(width=False, height=False)
        self.minsize(800, 520)
        # self.geometry(self.window_width, self.window_height)

        x_pos = (self.winfo_screenwidth() // 2) - (self.window_width // 2)
        y_pos = (self.winfo_screenheight() // 2) - (self.window_height // 2)

        # Definir fuentes por defecto
        self.default_font = Font(family='Arial', size=14, weight='normal')
        self.title_font = Font(family='Arial', size=14, weight='bold')

        self.init_components()

        self.geometry(
            f"{self.window_width}x{self.window_height}+{x_pos}+{y_pos}")

    def init_components(self):

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

        self.destroy()
        
        # Invocar el formulario que contiene las preguntas
        question_window = QuestionPageWindow()
        question_window.mainloop()
        points = question_window.get_curent_points()

        results_window = ResultsWindow(points)
        results_window.mainloop()