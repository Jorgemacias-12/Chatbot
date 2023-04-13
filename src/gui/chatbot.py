import tkinter as tk

from src.constants.data import questions
from src.constants.data import options_label_text
from src.constants.data import options_label_selected


class ChatbotWindow(tk.Tk):

    question_counter = 1
    question = ""

    def __init__(self):
        pass