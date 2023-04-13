import tkinter as tk

from tkinter.font import *

from src.constants.data import questions
from src.constants.data import questions_size
from src.constants.data import questions_colors

class QuestionPageWindow(tk.Tk):

    window_width = 800
    window_height = 520

    default_font = None
    title_font = None

    panel_image = None
    
    counter = 0

    def __init__(self, question_index):

        super().__init__()

        self.question_index = question_index

        self.title(f"Pregunta {question_index}")
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

    def get_question(self, index):

        question = None
        question = questions.get(index)
        question = question["pregunta"]

        return question

    def get_options(self, index):

        options = None
        options = questions.get(index)
        options = options["opciones"]

        return options
    
    def get_points(self, index):

        points = None
        points = questions.get(index)
        points = points["puntos"]

        return points

    def choice(self, point):

        self.counter += point
        
        self.destroy()

    def init_components(self):

        # Logo
        self.logo = tk.PhotoImage(file="./resources/logo.png").subsample(2)
        Lbl_logo = tk.Label(self, image=self.logo)
        Lbl_logo.pack(anchor=tk.NW)

        # Pregunta
        Lbl_question = tk.Label(
            self, text=self.get_question(self.question_index))
        Lbl_question.config(foreground="#6209be", font=self.default_font)
        Lbl_question.pack()

        self.panel_image = tk.PhotoImage(file="./resources/panel_bg.png")

        panel = tk.Label(self, image=self.panel_image)
        panel.pack()

        # Contador de preguntas (wtf thegrefg reference)
        Lbl_questionCounter = tk.Label(
            self, text=f"\tPregunta {self.question_index}/{questions_size}")
        Lbl_questionCounter.config(
            foreground="#6209be", font=self.counter_font)
        Lbl_questionCounter.pack(anchor=tk.SW)

        # Obtener los puntos 
        # points = self.get_points(self.question_index)

        # Mostrar las opciones para responder a la pregunta
        for index, (option, point) in enumerate(zip(self.get_options(self.question_index), self.get_points(self.question_index))):

            canvas = tk.Canvas(panel, width=30, height=30)
            canvas.place(x=100, y=80 + index * 50)

            canvas.create_oval(5, 5, 25, 25, fill=questions_colors[index])

            Btn_option = tk.Button(panel, text=option)
            Btn_option.config(bg=questions_colors[index], fg="white", font=self.counter_font, padx=20)
            Btn_option.config(command= lambda points = point: self.choice(points))
            Btn_option.place(x=150, y=80 + index * 50)
        
    def get_current_points(self):
        return self.counter