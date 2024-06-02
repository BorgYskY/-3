import tkinter as tk
from tkinter import filedialog, messagebox
from element import Element
import dom

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Интернет-браузер")
        self.geometry("1500x700")
        self.create_menu()
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Загрузить файл", command=self.load_file)
        menubar.add_cascade(label="Файл", menu=filemenu)
        self.config(menu=menubar)

    def clear_canvas(self):
        self.canvas.delete("all")

    def load_file(self):
        filename = filedialog.askopenfilename(title="Выберите файл HTML", filetypes=[("HTML файлы", "*.html")])
        if filename:
            try:
                self.clear_canvas()
                root_element = dom.dom(filename)
                self.display_dom_tree(root_element)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

    def display_dom_tree(self, element, y=20):
        if element.tag == 'title':
            self.title(element.children[0].text)
        if element.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            for child in element.children:
                if child.tag == 'data' and child.text:
                    font_size = {
                        'h1': 32,
                        'h2': 24,
                        'h3': 18,
                        'h4': 16,
                        'h5': 13,
                        'h6': 11}[element.tag]
                    self.canvas.create_text(10, y, anchor='nw', text=child.text, font=('Times New Roman', font_size, 'bold'))
                    y += font_size + 10
        elif element.tag == 'p':
            for child in element.children:
                if child.tag == 'data' and child.text:
                    self.canvas.create_text(10, y, anchor='nw', text=child.text, font=('Times New Roman', 12))
                    y += 20

        for child in element.children:
            y = self.display_dom_tree(child, y)
        
        return y

if __name__ == "__main__":
    app = app()
    app.mainloop()
