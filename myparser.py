def parser(path):
    f = open(path)
    keywords = []
    kword = ""
    flag = False
    for line in f:
        for x in line:
            if x == '<':
                kword += x
                flag = True
                continue
            if x == '>':
                kword += x
                keywords.append(kword)
                kword = ""
                flag = False
            if flag == True:
                kword += x
    return keywords