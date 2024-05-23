class Element:
    def __init__(self, tag, text=None):
        self.tag = tag
        self.text = text
        self.attributes = {}
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        indent = "  " * level
        if self.tag:
            result = f"{indent}<{self.tag}"
            for attr, val in self.attributes.items():
                result += f' {attr}="{val}"'
            result += ">\n"
        else:
            result = ""

        if self.text:
            result += f"{indent}  {self.text}\n"

        for child in self.children:
            result += child.__str__(level + 1)

        if self.tag:
            result += f"{indent}</{self.tag}>\n"
        
        return result

    def __repr__(self):
        return self.__str__()
