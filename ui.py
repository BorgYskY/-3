import tkinter as tk

class app(tk.Tk):
    def __init__(self, text):
        super().__init__()
        self.title("DOM viewer")
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.frame.pack_propagate(True)
        self.label = tk.Label(self.frame, text=text, anchor='w', justify="left")
        self.label.pack(pady=20)

if __name__ == "__main__":
    text = """текст
    из
    нескольких
    строк"""
    window = app(text)
    window.mainloop()
