class Element:
    def __init__(self, tag, text=None):
        self.tag = tag
        self.text = text
        self.attributes = {}
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    