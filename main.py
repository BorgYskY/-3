import myparser
file = "sample html.html"
f = open(file)

print(myparser.parser(file))