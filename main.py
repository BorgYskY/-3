import dom
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('filename', type = str)
filename = arg_parser.parse_args().filename

try:
    file = filename
    dom.print_tree(dom.build_dom(file))
except Exception:
    print("Некорректное имя файла")
    pass