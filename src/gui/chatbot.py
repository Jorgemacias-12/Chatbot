import tkinter as tk

from src.constants.data import questions
from src.constants.data import options_label_text
from src.constants.data import options_label_selected


class ChatbotWindow(tk.Tk):

    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase padre

        # Configuración de la ventana
        self.title("Chatbot")
        self.configure(bg="#fafafa")
        self.resizable(width=True, height=True)
        self.minsize(800, 600)

        self.title = tk.Label(self, text="¡Bienvenido!", font=('Arial', 40, 'bold'), foreground='#5600ff')
        self.title.pack(pady=10)

        self.question_label = tk.Label(self, text=f"{self.getQuestion(1)}", font=('Arial', 24, 'normal'))
        self.question_label.pack(pady=30)

        self.questionsContainer = tk.LabelFrame(self, padx=5, pady=5)
        self.questionsContainer.pack()

        for i, label in enumerate(options_label_text):

            self.checkbox_question = tk.Checkbutton(
                self.questionsContainer, text=label, variable=options_label_selected, onvalue='1', offvalue='0')
            self.checkbox_question.grid(row=0, column=i, sticky='w')
            self.bind('<Button-1>', self.on_click)        

        ancho_ventana = 1280
        altura_ventana = 720
        x_pos = (self.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y_pos = (self.winfo_screenheight() // 2) - (altura_ventana // 2)
        self.geometry(f"{ancho_ventana}x{altura_ventana}+{x_pos}+{y_pos}")

    def on_window_open(event):

        print("Si")

        pass

    def show_questions(self):

        for key, value in questions.items():

            self.textarea.insert("1.0", f"{key} {value['pregunta']} \n")

            self.textarea.insert("1.0", "\n")

            for option, points in zip(value["opciones"], value["puntos"]):

                self.textarea.insert("1.0", f"{option} - {points} \n")

        # self.textarea.insert("1.0", questions)

        pass

    def getQuestion(self, index):

        question = None

        question = questions.pop(index)

        question = question["pregunta"]

        return question

    def on_click(self, event):

        for i, selected in enumerate(options_label_selected):
            if i != event.widget.grid_info()['row']:
                selected.set('0')

        pass

    def selectOption(self):

        pass

    def pregunta_anterior(self):
        pass

    def pregunta_siguiente(self):
        pass
