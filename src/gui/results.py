import tkinter as tk

from tkinter.font import *

from src.constants.data import questions_colors
from src.constants.data import carrers


class ResultsWindow(tk.Tk):

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
        self.title_font = Font(family='Arial', size=24, weight='bold')
        self.counter_font = Font(family='Arial', size=12, weight='bold')

        self.init_components()

        self.geometry(
            f"{self.window_width}x{self.window_height}+{x_pos}+{y_pos}")

    def calculate_carrer(self):
        
        valid_carrers = []
        min_diff = float("inf")
        suggested_carrer = None

        for carrer, score in carrers.items():

            if "min" in score and self.total_points >= score["min"]:

                if "max" in score and self.total_points <= score["max"] or "max" not in score:

                    valid_carrers.append(carrer)

                    print(f"{carrer} added to valid careers")

        if not valid_carrers: 
            return "Ninguna carrera coincide con la canitdad de puntos obtenida"
        

        if len(valid_carrers) == 1:
            return valid_carrers[0]

        for carrer in valid_carrers:

            score = carrers[carrer]

            diff = abs(self.total_points - score["min"])

            print(f"{carrer} difference: {diff}")

            if diff < min_diff:
                
                suggested_carrer = carrer
                min_diff = diff

        
        if suggested_carrer is None:
            return "No hay carrera existente para tí"

        return suggested_carrer

    def init_components(self):

        print("Si")

        # Calcular carrera a sugerir en base a puntuaje total
        suggested_carrer = self.calculate_carrer()

        # Label de explicación
        Lbl_response = tk.Label(
            self, text="¡La carrera recomendada para tí es:")
        Lbl_response.config(foreground='#6209be', font=self.counter_font)
        Lbl_response.pack()

        self.panel_image = tk.PhotoImage(file="./resources/panel_bg.png")

        panel = tk.Label(self, image=self.panel_image)
        panel.pack()

        Lbl_suggestion = tk.Label(self, text=f"¡{suggested_carrer}!")
        Lbl_suggestion.config(
            foreground=questions_colors[0], font=self.title_font)
        Lbl_suggestion.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
