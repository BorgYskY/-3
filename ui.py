import tkinter as tk
from element import Element

class app(tk.Tk):
    def __init__(self, element):
        super().__init__()
        self.geometry("1500x700")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.display_dom(element)

    def display_dom(self, element, y=20):
        if element.tag == 'title':
            self.title(element.children[0].text)
        if element.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
            for child in element.children:
                if child.tag == 'data' and child.text:
                    self.canvas.create_text(10, y, anchor='nw', text=child.text)
                    y += 20
        
        for child in element.children:
            y = self.display_dom(child, y)
        
        return y


if __name__ == "__main__":
    from element import Element
    root = Element('html')
    body = Element('body')
    root.add_child(body)
    body.add_child(Element('h1', 'This is an H1 tag'))
    body.add_child(Element('p', 'This is a paragraph tag'))
    body.add_child(Element('p', 'This is another paragraph tag'))
    app = app(root)
    app.mainloop()