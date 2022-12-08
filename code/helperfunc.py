from operator import methodcaller


def read_input_lines(file_name):
    """takes file and returns strings for each line, removing the 'new line'"""
    lines = open(file_name, 'r').readlines()
    return list(map(methodcaller('replace', '\n', ''), lines))
