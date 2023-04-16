import tkinter as tk

from tkinter.font import *
from tkinter import *

from src.gui.results import ResultsWindow
from src.constants.data import questions
from src.constants.data import questions_size
from src.constants.data import questions_colors
from src.constants.data import button_fg, button_bg, button_font


class QuestionPageWindow(tk.Tk):

    window_width = 800
    window_height = 520
    default_font = None
    title_font = None
    
    option_indicator_row_start = 150

    panel_image = None

    question_index = 1
    question_counter = None

    question = None

    question_options = [None] * 4

    total_points = 0

    responses = [False] * 19

    internal_counter = 0

    canvas = [None] * 4

    def __init__(self):

        super().__init__()

        self.title(f"Questionario - pregunta {self.question_index}")

        self.resizable(False, False)
        x_pos = (self.winfo_screenwidth() // 2) - (self.window_width // 2)
        y_pos = (self.winfo_screenheight() // 2) - (self.window_height // 2)

        # Definir fuentes por defecto
        self.default_font = Font(family='Arial', size=12, weight='normal')
        self.title_font = Font(family='Arial', size=14, weight='bold')
        self.counter_font = Font(family='Arial', size=12, weight='bold')

        self.init_components()

        self.geometry(
            f"{self.window_width}x{self.window_height}+{x_pos}+{y_pos}")

    def init_components(self):

        # Área para cargar valores por defecto
        self.question = StringVar()
        self.question.set(self.get_question(self.question_index))

        self.question_counter = StringVar()
        self.question_counter.set(
            f"\tPregunta {self.question_index}/{questions_size}")

        self.question_options = [StringVar() for _ in range(4)]
        self.canvas = [tk.Canvas() for _ in range(4)]


        # Logo
        self.logo = tk.PhotoImage(file="./resources/logo.png").subsample(2)
        Lbl_logo = tk.Label(self, image=self.logo)
        Lbl_logo.pack(anchor=tk.NW)

        # Pregunta
        Lbl_question = tk.Label(
            self, textvariable=self.question)
        Lbl_question.config(foreground="#6209be", font=("Arial", 16, "bold"), pady=10)
        Lbl_question.pack()

        # Contenedor para las opciones
        self.panel_image = tk.PhotoImage(file="./resources/panel_bg.png")
        self.panel = tk.Label(self, image=self.panel_image)
        self.panel.pack()

        # Mostrar las opciones para la pregunta
        for index, (option, point) in enumerate(zip(self.get_options(self.question_index), self.get_points(self.question_index))):

            # modificar el valor de las opciones disponibles
            self.question_options[index].set(option)

            # Usar canvas para emular un checkbox
            self.canvas[index] = tk.Canvas(self, width=30, height=30)
            self.canvas[index].place(x=100, y=self.option_indicator_row_start + index * 50)

            self.canvas[index].create_oval(
                5, 5, 25, 25, fill=questions_colors[index])

            # Inicializar variable para actualizar valor en update
            Lbl_option = tk.Label(
                self, textvariable=self.question_options[index])
            Lbl_option.config(
                bg=questions_colors[index], fg="white", font=self.counter_font, padx=20, cursor="hand2")
            Lbl_option.bind("<Button-1>", lambda event, points=point: self.choice(points))
            Lbl_option.place(x=150, y=self.option_indicator_row_start + index * 50)

        # Contador de preguntas (wtf thegrefg reference)
        Lbl_questionCounter = tk.Label(
            self, textvariable=self.question_counter)
            
        Lbl_questionCounter.config(
            foreground="#6209be", font=self.counter_font)
        Lbl_questionCounter.pack(anchor=tk.SW)
        
        # Botones para cambiar entre preguntas
        Btn_next = tk.Button(self, text=">", fg=button_fg,
                             bg=button_bg, font=button_font)
        Btn_next.config(command=self.next_question,
                        anchor="center", padx=50, pady=30)
        Btn_next.pack(side="right")

        Btn_prev = tk.Button(self, text="<", fg=button_fg,
                             bg=button_bg, font=button_font)
        Btn_prev.config(command=self.prev_question, padx=50, pady=30)
        Btn_prev.pack(side="left")

    def choice(self, point):
    
        if self.question_index >= questions_size:
            
            self.destroy()

            results_window = ResultsWindow(self.total_points)
            results_window.mainloop()

            return

        
        if self.question_index <= questions_size:
            
            self.total_points += point
            self.question_index +=  1
            self.update_view()

    def update_view(self):

        # Titulo del formulario
        self.title(f"Questionario - pregunta {self.question_index}")

        # Pregunta actual
        self.question.set(self.get_question(self.question_index))

        # Opciones de la pregunta (repuestas)
        for index, option in enumerate(self.get_options(self.question_index)):

            # Respuestas
            self.question_options[index].set(option)

            # Ovalos correspondiente a la respuesta
            self.canvas[index] = tk.Canvas(self, width=30, height=30)
            self.canvas[index].create_oval(
                5, 5, 25, 25, fill=questions_colors[index])
            self.canvas[index].place(x=100, y=self.option_indicator_row_start + index * 50)

        # Contador de la pregunta
        self.question_counter.set(
            f"\tPregunta {self.question_index}/{questions_size}")

    def next_question(self):

        if self.question_index < questions_size:
            self.question_index += 1
            self.update_view()

    def prev_question(self):

        if self.question_index > 1:
            self.question_index -= 1
            self.update_view()

    def get_question(self, index):

        return questions.get(index)["pregunta"]

    def get_options(self, index):

        return questions.get(index)["opciones"]

    def get_points(self, index):

        return questions.get(index)["puntos"]