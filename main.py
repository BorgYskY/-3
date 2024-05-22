import dom

try:
    file = input("Введите название файла: ")
    dom.print_tree(dom.dom(file))
except Exception:
    print("Некорректное имя файла")
    pass