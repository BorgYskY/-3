import tokens
from element import Element
import html

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
        text = html.unescape(token.val)
        elem = Element(token.tag, text)
    if token.func and token.val:
        elem.attributes[token.func] = token.val
    
    if token.tag != 'data' and token.tag != 'meta':
        while True:
            child = parse_element()
            if child is None:
                break
            elem.add_child(child)   
    return elem
   