cur_char = ''

get_char = None

class token:
    def __init__(self, tag, func, val):
        self.tag = tag
        self.func = func
        self.val = val
    
    def __str__(self):
        if self.func == "":
            self.func = None
        if self.val == "":
            self.val = None
        return f"{self.tag}, {self.func}, {self.val}"
    

def get_token():
    global cur_char
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
    elif cur_char == '>':
        cur_char = get_char()
        if cur_char == '':
            return 'eof'
        if cur_char != '\n' and cur_char != '<':
            return data()
        if cur_char == '<':
            return get_token()
        else: 
            skip_whitespace()
            return get_token()
    elif cur_char == '\n':
        skip_whitespace()
        return get_token()

def doctype():
    global cur_char
    dtype = ""
    while cur_char != ' ':
        cur_char = get_char()
    cur_char = get_char()
    while cur_char != '>':
        dtype += cur_char
        cur_char = get_char()
    return token("doctype", None, dtype)

def start_tag():
    global cur_char
    tag, func, val = "", "", ""
    func_state, val_state = False, False
    while True:
        if cur_char == ' ':
            skip_whitespace()
            func_state = True
        if func_state == True and val_state == False:
           if cur_char == '=':
               cur_char = get_char()
               val_state = True
               continue
           func += cur_char
        if cur_char == '>':
            break            
        if val_state == True:
            val += cur_char
        if func_state == False and val_state == False:
            tag += cur_char
        cur_char = get_char()
    return token(tag, func, val)

def end_tag():
    tag = ""
    global cur_char
    cur_char = get_char()
    while cur_char != '>':
        tag += cur_char
        cur_char = get_char()
    return token('end', None, tag)

def data():
    data = ""
    global  cur_char
    while cur_char != '<':
        data += cur_char
        cur_char = get_char()
    return token('data', None, data)

def skip_comment():
    global cur_char
    while cur_char != '>':
        cur_char = get_char()

def skip_whitespace():
    global cur_char
    while True:
        if cur_char == ' ' or cur_char == '\n':
            cur_char = get_char()
        else: break

if __name__ == '__main__':
    print("Test tokens")
    f = open("html2.html")

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