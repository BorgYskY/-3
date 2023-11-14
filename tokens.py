cur_char = ''

get_char = None
#digits = [x for x in "123456"]
def get_token():
    global cur_char
    if cur_char == '<':
        cur_char = get_char()
        if cur_char == '/':
            return end_tag()
        elif cur_char == '!': 
            skip_comment()
        else: return start_tag()
    elif cur_char == '>': return data()

def start_tag():
    tag = ""
    while cur_char != '>':
        tag += cur_char
        cur_char = get_char()
    return('start', tag)

def end_tag():
    tag = ""
    while cur_char != '>':
        cur_char = get_char()
        tag += cur_char
    return('end', tag)

def data():
    data = ""
    while cur_char != '<':
        cur_char = get_char()
        data += cur_char
    return('data', data)

def skip_comment():
    while cur_char != '>':
        cur_char = get_char()
    cur_char = get_char()