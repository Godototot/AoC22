from operator import methodcaller


def read_input_lines(file_name):
    lines = open(file_name, 'r').readlines()
    return list(map(methodcaller('replace', '\n', ''), lines))