import tkinter as tk
from src.utils.logging import LoggingTkClass

from tkinter.font import *
from tkinter import StringVar
from tkinter import messagebox

from src.gui.results import ResultsWindow
from src.constants.data import questions_colors, questions_size, question_options_size
from src.constants.data import get_options, get_points, get_question
from src.utils.logging import log


class QuestionPageWindow(LoggingTkClass):

    question_index = 1
    unanswered_questions = []
    questionary_total_points = 0

    CANVAS_X_POSITION = 100
    CANVAS_Y_POSITION = 150
    CANVAS_Y_SCALE = 50

    OVAL_X = 5
    OVAL_Y = 5
    OVAL_WIDTH = 25
    OVAL_HEIGHT = 25

    BUTTON_OPTION_FONT = ("Arial", 12, "bold")
    BUTTON_OPTION_X_POSITION = 150
    BUTTON_Y_POSITION = 200
    BUTTON_Y_SCALE = 50
    BUTTON_OPTION_PADDING_X = 20
    BUTTON_OPTION_PADDING_Y = 5

    LBL_QUESTION_COUNTER_FONT = ("Arial", 12, "bold")

    BUTTON_CHANGE_QUESTION_PAD_X = 50
    BUTTON_CHANGE_QUESTION_PAD_Y = 30

    def __init__(self):

        super().__init__(
            title=f"Questionario - pregunta #{self.question_index}")

        # Inicializar variables
        self.question = StringVar()
        self.question_counter = StringVar()
        self.question_options = [StringVar()
                                 for _ in range(question_options_size)]

        # Cargar imagenes

        # Logo de bienvenida
        self.logo = tk.PhotoImage(file="./resources/logo.png").subsample(2)

        # Imagen de fondo para mostrar las respuestas a pregunta actual
        self.panel_image = tk.PhotoImage(file="./resources/panel_bg.png")

        # Cargar iconos para los botones (cambiar de pregunta)
        self.BUTTON_NEXT_BG = tk.PhotoImage(file="./resources/button_next.png")
        self.BUTTON_PREV_BG = tk.PhotoImage(file="./resources/button_prev.png")

        # Inicializar componentes (vista)
        self.init_components()

    def init_components(self):

        log(self.logger,
            f"{type(self).__name__}-init_components ha sido invocado")

        # Asignar valores para inicializar vista
        self.question.set(get_question(self.question_index))
        self.question_counter.set(
            f"\tPregunta {self.question_index}/{questions_size}")
        self.canvas = [tk.Canvas() for _ in range(question_options_size)]

        # Componente label para mostrar el logo
        Lbl_logo = tk.Label(self, image=self.logo)
        Lbl_logo.pack(anchor=tk.NW)

        # Componente para mostrar la pregunta
        Lbl_question = tk.Label(self, textvariable=self.question)
        Lbl_question.config(foreground="#6209be", font=(
            "Arial", 16, "bold"), pady=10)
        Lbl_question.pack()

        # Componente contenedor
        self.panel = tk.Label(self, image=self.panel_image)
        self.panel.pack()

        #  Mostrar las opciones para responder la pregunta
        for index, [option, point] in enumerate(zip(get_options(self.question_index),
                                                    get_points(self.question_index))):

            log(self.logger,
                f"init_components -> crear respuestas indice: {index}")

            # Asignar valor de respuesta
            self.question_options[index].set(option)

            # Inicializar canvas
            self.canvas[index] = tk.Canvas(self, width=30, height=30)
            self.canvas[index].place(
                x=self.CANVAS_X_POSITION, y=self.CANVAS_Y_POSITION + index * self.CANVAS_Y_SCALE)

            # Crear indicadores graficos
            self.canvas[index].create_oval(
                self.OVAL_X, self.OVAL_Y, self.OVAL_WIDTH, self.OVAL_HEIGHT, fill=questions_colors[index])

            # Crear boton que contiene la respuesta a mostrar
            Btn_choice_option = tk.Button(
                self, textvariable=self.question_options[index], borderwidth=0, highlightthickness=0, activebackground=questions_colors[index])
            Btn_choice_option.config(
                bg=questions_colors[index], fg="white", font=self.BUTTON_OPTION_FONT, padx=self.BUTTON_OPTION_PADDING_X, cursor="hand2")
            Btn_choice_option.config(pady=self.BUTTON_OPTION_PADDING_Y)

            # Añadir evento choice
            Btn_choice_option.config(
                command=lambda option=option, point=point: self.handle_choice_option(option, point))

            Btn_choice_option.place(x=self.BUTTON_OPTION_X_POSITION,
                                    y=self.BUTTON_OPTION_X_POSITION + index * self.BUTTON_Y_SCALE)

        # Cuenta actual de preguntas (wtf thegrefg reference)
        Lbl_question_counter = tk.Label(
            self, textvariable=self.question_counter)
        Lbl_question_counter.config(
            foreground="#6209be", font=self.LBL_QUESTION_COUNTER_FONT)
        Lbl_question_counter.pack(anchor=tk.SW)

        # Botones de dirección para cambiar entre preguntas
        Btn_next_question = tk.Button(
            self, image=self.BUTTON_NEXT_BG, borderwidth=0, highlightthickness=0, cursor="hand2")
        Btn_next_question.config(command=self.next_question, anchor="center",
                                 padx=self.BUTTON_CHANGE_QUESTION_PAD_X, pady=self.BUTTON_CHANGE_QUESTION_PAD_Y)
        Btn_next_question.pack(side="right")

        Btn_prev_question = tk.Button(
            self, image=self.BUTTON_PREV_BG, borderwidth=0, highlightthickness=0, cursor="hand2")
        Btn_prev_question.config(command=self.prev_question, anchor="center",
                                 padx=self.BUTTON_CHANGE_QUESTION_PAD_X, pady=self.BUTTON_CHANGE_QUESTION_PAD_Y)
        Btn_prev_question.pack(side="left")

    def handle_choice_option(self, option, point):
        
        if len(self.unanswered_questions) >= 1:

            messagebox.showwarning("¡Aviso!", f"Hay {len(self.unanswered_questions) + 1} preguntas por contestar, para continuar contestelas!")
            return
        
        if self.question_index >= questions_size:
            
            log(self.logger, f"Puntos totales: {self.questionary_total_points}")

            self.destroy()
            results_window = ResultsWindow(self.total_points)
            results_window.mainloop()
            return

        if self.question_index <= questions_size:
            
            log(self.logger, f"handle_choice_option invocado con valores: {option}-{point}")

            self.question_index += 1
            self.questionary_total_points += point
            self.update_view()

    def update_view(self):

        log(self.logger, "update_view invocado")

        # Actualizar título
        self.title(f"Questionario - pregunta #{self.question_index}")

        # Pregunta
        self.question.set(get_question(self.question_index))

        # Opciones de la pregunta
        for index, [option, point] in enumerate(zip(get_options(self.question_index), get_points(self.question_index))):

            self.question_options[index].set(option)

            Btn_choice_option = tk.Button(
                self, textvariable=self.question_options[index], borderwidth=0, highlightthickness=0, activebackground=questions_colors[index])
            Btn_choice_option.config(
                bg=questions_colors[index], fg="white", font=self.BUTTON_OPTION_FONT, padx=self.BUTTON_OPTION_PADDING_X, cursor="hand2")
            Btn_choice_option.config(pady=self.BUTTON_OPTION_PADDING_Y)

            # Añadir evento choice
            Btn_choice_option.config(
                command=lambda option=option, point=point: self.handle_choice_option(option, point))

            Btn_choice_option.place(x=self.BUTTON_OPTION_X_POSITION,
                                    y=self.BUTTON_OPTION_X_POSITION + index * self.BUTTON_Y_SCALE)

    def next_question(self):

        if self.question_index < questions_size:

            # Modificar el "contador" de preguntas sin responder
            self.unanswered_questions.append(True)
            self.question_index += 1
            self.update_view()

            log(self.logger, f"next_question invocado")

    def prev_question(self):

        if self.question_index > 1:

            # Eliminar una posición del "contador" de preguntas sin resolver
            self.unanswered_questions.pop()
            self.question_index -= 1
            self.update_view()

            log(self.logger, f"prev_question invocado")
