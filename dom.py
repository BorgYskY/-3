import tokens
<<<<<<< Updated upstream
f = open("sample html.html")
def getch():
    return f.read(1)
tokens.get_char = getch
tokens.cur_char = tokens.get_char()
temp = None
tree = tokens.token("document", None, None)
flag = tree

while temp != 'eof':
    temp = tokens.get_token()
    if temp is not None and temp != 'eof':
        if temp.tag != 'end' and temp.tag != 'meta' and temp.tag != 'data':
            flag.add_child(temp)
            flag = temp
        elif temp.tag == 'meta' or temp.tag == 'data':
            flag.add_child(temp)
        elif temp.tag == 'end':
            if flag.tag == temp.val:
                flag.add_child(temp)
                flag = flag.parent 

f.close()
=======
from element import Element

def build_dom(file):
    with open(file, 'r') as f:
        def getch():
            return f.read(1)

        tokens.get_char = getch
        tokens.cur_char = tokens.get_char()

        root = Element('document')
        while True:
            token = tokens.get_token()
            if token == 'eof':
                break
            if token is None or isinstance(token, str):
                continue
            element = parse_element()
            if element:
                root.add_child(element)

    return root

def parse_element():
    token = tokens.get_token()
    if token is None or isinstance(token, str):
        return None
    if token.tag == 'data':
        return Element(None, text=token.val.strip())
    elif token.tag == 'doctype':
        return None
    elif token.tag == 'end':
        return None

    elem = Element(token.tag)
    if token.func:
        elem.attributes[token.func] = token.val

    while True:
        next_token = tokens.get_token()
        if next_token == 'eof':
            break
        if next_token.tag == 'end' and next_token.val == token.tag:
            break
        child_element = parse_element()
        if child_element:
            elem.add_child(child_element)
    
    return elem
>>>>>>> Stashed changes

def print_tree(node, level=0):
    print(node.__str__(level))

print_tree(tree)
