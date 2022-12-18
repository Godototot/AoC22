import sys
import numpy as np
from helperfunc import *


def prepare_input(input_file):
    lines = (line.split(',') for line in read_input_lines(input_file))
    return {(int(pixel[0]), int(pixel[1]), int(pixel[2])) for pixel in lines}


sides = ((1, 0, 0), (-1, 0, 0),
         (0, 1, 0), (0, -1, 0),
         (0, 0, 1), (0, 0, -1))


def add_sets(a, b):
    return a[0]+b[0], a[1]+b[1], a[2]+b[2]


def part1(pixel_list):
    surface = 0
    for pixel in pixel_list:
        surface += sum(1 for s in sides if add_sets(pixel, s) not in pixel_list)
    return surface


def part2(input_data):
    return ''


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
