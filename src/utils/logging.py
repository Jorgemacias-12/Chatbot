import os 
import logging
import tkinter as tk

from datetime import date

class LoggingTkClass(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        
        appdata_path = os.getenv("APPDATA")

        logger_folder_path = os.path.join(appdata_path, 'com.jamz.orientador-vocacional')

        if not os.path.exists(logger_folder_path):
            os.makedirs(logger_folder_path)

        log_filename = os.path.join(
            logger_folder_path, f"{date.today().strftime('%d-%m-%Y')}.log")
        
        logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s: %(message)s')
        
        self.logger = logging.getLogger(__name__)
