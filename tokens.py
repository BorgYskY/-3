cur_char = ''

get_char = None
digits = [x for x in "123456"]
def get_token():
    global cur_char
    if cur_char == -1:
        return('end')
    skip_comment()
    if cur_char == '<':
        c = get_char()
        if c == 'h':
            d = get_char()
            if d == 't':
                return html()
            elif d == 'e':
                return head()
            elif d in digits:
                return header()
        elif c == 'm':
            return meta()
        elif c == 't':
            return title()
        elif c == 'b':
            return body()
        elif c == 'p':
            return paragraph()
        elif c == '/':
            d = get_char()
            if d == 'h':
                e = get_char()
                if e == 'e':
                    return head_end()
                elif e in digits:
                    return header_end()
            elif d == 't':
                return title_end()
            elif d == 'b':
                return body_end()
            elif d == 'p':
                return paragraph_end()
          
def html():
    return('html_start')
def head():
    return('head_start')
def header():
    number = cur_char
    return('h{}_start'.format(number))
def meta():
    return('meta_start')
def title():
    return('title_start')
def body():
    return('body_start')
def paragraph():
    return('par_start')
def head_end():
    return('head_end')
def header_end():  
    number = cur_char
    return('h{}_end'.format(number))
def title_end():
    return('title_end')
def body_end():
    return('body_end')
def paragraph_end():
    return('par_end')
