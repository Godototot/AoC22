import sys
import numpy as np
from helperfunc import *


def prepare_input(input_file):
    lines = (line.split(',') for line in read_input_lines(input_file))
    return {(int(pixel[0]), int(pixel[1]), int(pixel[2])) for pixel in lines}


sides = {(1, 0, 0), (-1, 0, 0),
         (0, 1, 0), (0, -1, 0),
         (0, 0, 1), (0, 0, -1)}


def get_surface(pixel_list):
    surface = 0
    for pixel in pixel_list:
        surface += sum(1 for s in sides if add_tuple(pixel, s) not in pixel_list)
    return surface


def part1(pixel_list):
    return get_surface(pixel_list)


def get_negative(cube_size, pixel_list):
    negative = set()
    for x in range(cube_size[0]):
        for y in range(cube_size[1]):
            for z in range(cube_size[2]):
                pixel = (x, y, z)
                if pixel not in pixel_list:
                    negative.add(pixel)
    return negative


def get_poisoned_walls(cube_size):
    poisoned = set()
    for y in range(cube_size[1]):
        for z in range(cube_size[2]):
            poisoned.add((-1, y, z))
            poisoned.add((cube_size[0]+1, y, z))

    for x in range(cube_size[1]):
        for z in range(cube_size[2]):
            poisoned.add((x, -1, z))
            poisoned.add((x, cube_size[1]+1, z))

    for x in range(cube_size[1]):
        for y in range(cube_size[2]):
            poisoned.add((x, y, -1))
            poisoned.add((x, y, cube_size[2]+1))

    return poisoned


def part2(pixel_list):
    max_x = max(pixel[0] for pixel in pixel_list)+1
    max_y = max(pixel[1] for pixel in pixel_list)+1
    max_z = max(pixel[2] for pixel in pixel_list)+1
    air = get_negative((max_x, max_y, max_z), pixel_list)
    poisoned = get_poisoned_walls((max_x, max_y, max_z))
    while not len(poisoned) == 0:
        new_poisoned = set()
        new_air = set()
        for pixel in air:
            for s in sides:
                if add_tuple(pixel, s) in poisoned:
                    new_poisoned.add(pixel)
                    break
            else:
                new_air.add(pixel)
        poisoned = new_poisoned
        air = new_air
    return get_surface(pixel_list)-get_surface(air)


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
