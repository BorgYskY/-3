import tokens
f = open("sample html.html")
def getch():
    tokens.cur_char
    return f.read(1)

tokens.get_char = getch
tokens.cur_char = tokens.get_char()
temp = None
tree = tokens.token("document", None, None)
flag = tokens.get_token()
# tokens.get_token()
tree.add_child(flag)
while temp != 'eof':
    temp = tokens.get_token()
    if temp != None and temp != 'eof':
        if flag.tag != 'end' and flag.tag != 'meta' and flag.tag != 'data':
            flag.add_child(temp)
            flag = temp
        else: 
            flag = flag.parent
            flag.add_child(temp)
f.close()

#ворует что ни попадя, начиная с головы

# class Node:
#     def __init__(self, ):
#         self.children = []
#         self.variables = []
#         self.name = ""
#     def append(self, obj):
#         self.children.append(obj)

