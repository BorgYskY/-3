file = "test.txt"
f = open(file)
for line in f:
    for x in line:
        if x != '\u000a':
            print(x)
        
