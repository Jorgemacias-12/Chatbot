import os 
import logging
import platform
import subprocess
import tkinter as tk
from tkinter.font import *

from datetime import date

class LoggingTkClass(tk.Tk):
    


    def __init__(self, window_width=800, window_height=520, title="Frame", resizable_x=False, resizable_y=False):
        
        super().__init__()
        
        self.title(title)

        self.resizable(resizable_x, resizable_y)
        self.minsize(window_width, window_height)

        # Use fonts
        self.default_font = Font(family="Arial", size=12, weight="normal")
        self.title_font = Font(family="Arial", size=14, weight="bold")

        # Calculate Frame position
        window_x_pos = (self.winfo_screenwidth() // 2) - (window_width // 2)
        window_y_pos = (self.winfo_screenheight() // 2) - (window_height // 2)

        self.geometry(f"{window_width}x{window_height}+{window_x_pos}+{window_y_pos}")

        #  Debug setup
        appdata_path = os.getenv("APPDATA")

        logger_folder_path = os.path.join(appdata_path, 'com.jamz.orientador-vocacional')

        if not os.path.exists(logger_folder_path):
            os.makedirs(logger_folder_path)

        log_filename = os.path.join(
            logger_folder_path, f"{date.today().strftime('%d-%m-%Y')}.log")
        
        logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s: %(message)s')
        
        self.logger = logging.getLogger(__name__)

        self.initial_log()

    def initial_log(self):

        username = os.getlogin()
        processor_name = subprocess.check_output(
            ["wmic", "cpu", "get", "name"]).decode().strip().split("\n")[1]
        architecture = platform.architecture()[0]
        os_version = platform.version()
        operating_system = platform.system()


        # Imprimir información del sistema en un formato ordenado 
        # Solo si la clase es ChatbotWindow
        if type(self).__name__ == "ChatbotWindow":
            self.logger.info("\n")
            self.logger.info("+{:-^60}+".format(""))
            self.logger.info("|{:^60}|".format("Organizador Vocacional CUCOSTA inicializado"))
            self.logger.info("+{:-^60}+".format(""))
            self.logger.info("|{:^60}|".format("Información del sistema"))
            self.logger.info("+{:-^60}+".format(""))
            self.logger.info("| {:<20} | {:<35} |".format("Nombre de usuario", username))
            self.logger.info("| {:<20} | {:<35} |".format("Procesador", processor_name))
            self.logger.info("| {:<20} | {:<35} |".format("Arquitectura", architecture))
            self.logger.info("| {:<20} | {:<35} |".format("Versión del SO", os_version))
            self.logger.info("| {:<20} | {:<35} |".format(
        "Sistema Operativo", operating_system))
            self.logger.info("+{:-^60}+".format(""))   
        
        # Imprimir que frame fue inicializado
        log(self.logger, f"Inicializar frame: {type(self).__name__}")

def log(logger, message):

    logger.info("+{:-^{width}}+".format("", width=len(message) + 25))
    logger.info("| {:<20} | {:{width}} |".format("Mensaje", message, width=len(message)))
    logger.info("+{:-^{width}}+".format("", width=len(message) + 25))
