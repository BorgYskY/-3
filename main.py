import dom
import argparse
import ui
from tkinter import messagebox

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('filename', type = str)
filename = arg_parser.parse_args().filename

try:
    app = ui.app(dom.dom(filename))
    app.mainloop()
except Exception as e:
    messagebox.showerror("Ошибка", e)
    pass