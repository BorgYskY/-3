import tokens
from element import Element

def dom(file):
    f = open(file)
    def getch():
        return f.read(1)
    tokens.get_char = getch
    tokens.cur_char = tokens.get_char()
    root = parse_element()
    return root

def parse_element(parent=None):
    token = tokens.get_token()
    if token is None:
        return None
    if token == 'eof':
        return None
    if token.tag == 'end':
        return None
    if token.func:
        elem = Element(token.tag)
    else:
        elem = Element(token.tag, token.val)
    if token.func and token.val:
        elem.attributes[token.func] = token.val
    
    if token.tag != 'data' and token.tag != 'meta':
        while True:
            child = parse_element()
            if child is None:
                break
            elem.add_child(child)   
    return elem
   
def print_element(element, indent=0):
    attributes_str = ""
    for attr, value in element.attributes.items():
        attributes_str += f" {attr}=\"{value}\""
    result = '  ' * indent + f"<{element.tag}{attributes_str}>{element.text if element.text else ''}\n"
    for child in element.children:
        result += print_element(child, indent + 1)
    return result


if __name__ == "__main__":
    print(print_element(dom("html1.html")))