import tkinter as tk


class ChatbotWindow(tk.Tk):

    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase padre

        # Configuración de la ventana
        self.title("Chatbot")
        self.configure(bg="#fafafa")
        self.resizable(width=True, height=True)
        self.minsize(800, 600)
        
        # Creación del texto de bienvenida
        texto_bienvenida = tk.Label(
            self, text="¡Bienvenido al Chatbot!", font=("Arial", 20))
        texto_bienvenida.pack(padx=50, pady=50)

        ancho_ventana = 800
        altura_ventana = 600
        x_pos = (self.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y_pos = (self.winfo_screenheight() // 2) - (altura_ventana // 2)
        self.geometry(f"{ancho_ventana}x{altura_ventana}+{x_pos}+{y_pos}")

