cur_char = ''

get_char = None

class token:
    def __init__(self, tag, func, val):
        self.tag = tag
        self.func = func
        self.val = val
        self.children = []
        self.parent = None
    
    def __str__(self):
        if self.func == "":
            self.func = None
        if self.val == "":
            self.val = None
        return f"{self.tag}, {self.func}, {self.val}"
    
    def add_child(self, token):
        self.children.append(token)
        token.parent = self

def get_token():
    global cur_char
    while cur_char == ' ' or cur_char == '\n':
        cur_char = get_char()
    
    if cur_char == '<':
        cur_char = get_char()
        if cur_char == '/':
            return end_tag()
        elif cur_char == '!':
            cur_char = get_char()
            if cur_char == '-':
                skip_comment()
                return get_token()
            else:
                return doctype()
        else:
            return start_tag()
<<<<<<< Updated upstream
    elif cur_char == '>':
        cur_char = get_char()
        if cur_char == '':
            return 'eof'
        if cur_char != '\n':
            return data()
        else: 
            skip_whitespace()
    elif cur_char == '\n':
        skip_whitespace()
=======
    elif cur_char != '':
        return data()
    else:
        return 'eof'
>>>>>>> Stashed changes

def doctype():
    global cur_char
    dtype = ""
    while cur_char != ' ':
        cur_char = get_char()
    while cur_char != '>':
        dtype += cur_char
        cur_char = get_char()
    cur_char = get_char()  # move past '>'
    return token("doctype", None, dtype.strip())

def start_tag():
    global cur_char
    tag, func, val = "", "", ""
    func_state, val_state = False, False
    while cur_char != '>':
        if cur_char == ' ' and not func_state:
            func_state = True
            cur_char = get_char()
            continue
        if func_state and not val_state:
            if cur_char == '=':
                cur_char = get_char()  # move past '='
                val_state = True
                continue
            if cur_char == ' ':
                cur_char = get_char()
                continue
            func += cur_char
        elif val_state:
            if cur_char == ' ':
                cur_char = get_char()
                continue
            if cur_char == '"':
                cur_char = get_char()
                while cur_char != '"':
                    val += cur_char
                    cur_char = get_char()
                cur_char = get_char()  # move past closing '"'
            else:
                val += cur_char
        else:
            tag += cur_char
        cur_char = get_char()
    
    cur_char = get_char()  # move past '>'
    return token(tag.strip(), func.strip(), val.strip())

def end_tag():
    global cur_char
    tag = ""
    while cur_char != '>':
        tag += cur_char
        cur_char = get_char()
    cur_char = get_char()  # move past '>'
    return token('end', None, tag.strip())

def data():
    global cur_char
    data = ""
    while cur_char != '<':
        data += cur_char
        cur_char = get_char()
    return token('data', None, data.strip())

def skip_comment():
    global cur_char
    while True:
        cur_char = get_char()
        if cur_char == '>':
            break

if __name__ == '__main__':
    print("Test tokens")
    f = open("sample html.html")

    def getch():
        global cur_char
        return f.read(1)
    temp = None
    get_char = getch
    cur_char = get_char()
    while temp != 'eof':
        temp = get_token()
        if temp != None:
            print(temp)
    f.close()
