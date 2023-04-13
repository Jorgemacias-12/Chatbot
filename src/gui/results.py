import tkinter as tk

from tkinter.font import *


class resultsWindow(tk.Tk):

    window_width = 800
    window_height = 520

    default_font = None
    title_font = None

    def __init__(self, total_points):

        super().__init__()

        self.title(f"")
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
        pass