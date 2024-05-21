import tokens
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

def print_tree(node, level=0):
    indent = "  " * level
    print(f"{indent}{node}")
    for child in node.children:
        print_tree(child, level + 1)

print_tree(tree)
