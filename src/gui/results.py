import tkinter as tk
import random

from src.utils.logging import LoggingTkClass

from tkinter.font import *
from src.constants.data import questions_colors
from src.constants.data import carrers


class ResultsWindow(LoggingTkClass):

    window_width = 800
    window_height = 520

    default_font = None
    title_font = None

    panel_image = None

    def __init__(self, total_points):

        super().__init__()

        self.title(f"Resultados")
        self.resizable(False, False)
        x_pos = (self.winfo_screenwidth() // 2) - (self.window_width // 2)
        y_pos = (self.winfo_screenheight() // 2) - (self.window_height // 2)

        # Guardar puntos totales
        self.total_points = total_points

        # Definir fuentes por defecto
        self.default_font = Font(family='Arial', size=12, weight='normal')
        self.title_font = Font(family='Arial', size=20, weight='bold')
        self.counter_font = Font(family='Arial', size=12, weight='bold')

        self.init_components()

        self.geometry(
            f"{self.window_width}x{self.window_height}+{x_pos}+{y_pos}")
        
        self.logger.info(f"{__name__} ha sido invocado!")

    def calculate_carrer(self):
    
        """
            Intentar mejorar el algoritmo de calculo, para tener encuenta lo siguiente

                * La opción elegida en algunas preguntas es crucial para recomendar una
                 carrrera, por lo que, necesitaremos una forma de almacenar aquellas opcion
                 es de las preguntas clave para empezar a implementar un filtro especial
        """

        carrers_to_suggest = []

        for carrer, requriement in carrers.items():

            if "min" in requriement and "max" in requriement:

                carrers_to_suggest.append(carrer)

            if "min" in requriement and self.total_points >= requriement["min"]:

                carrers_to_suggest.append(carrer)
            
            if "max" in requriement and self.total_points <= requriement["max"]:

                carrers_to_suggest.append(carrer)
        
        self.logger.info(f"Se ha calculado la carrera exitosamente")

        return random.choice(carrers_to_suggest)

    def init_components(self):

        # Calcular carrera a sugerir en base a puntuaje total
        suggested_carrer = self.calculate_carrer()

        # print(suggested_carrer)

        # Label de explicación
        Lbl_response = tk.Label(
            self, text="¡La carrera recomendada para tí es:")
        Lbl_response.config(foreground='#6209be', font=self.counter_font)
        Lbl_response.pack(pady=10)

        self.panel_image = tk.PhotoImage(file="./resources/panel_bg.png")

        panel = tk.Label(self, image=self.panel_image)
        panel.pack()

        Lbl_suggestion = tk.Label(self, text=f"¡{suggested_carrer}!")
        Lbl_suggestion.config(
            foreground=questions_colors[0], font=self.title_font)
        
        Lbl_suggestion.place(relx=.5, rely=.3, anchor="center")

        Btn_start = tk.Button(self, text="Ir al inicio", bg="#ef476f", fg="white", cursor="hand2", font=("Arial", 16, "bold"))
        Btn_start.config(command=self.go_to_main_screen)
        Btn_start.pack(pady=30, side="bottom")

    def go_to_main_screen(self):
        
        from src.gui.chatbot import ChatbotWindow

        self.destroy()

        chatbot_window = ChatbotWindow()
        chatbot_window.mainloop()

        self.logger.info("Se ha regresado al menú principal")