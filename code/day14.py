import sys
import numpy as np

from helperfunc import *


def prepare_input(input_file):
    walls = [[(int(l.split(',')[1]), int(l.split(',')[0])) for l in line.split(' -> ')] for line in read_input_lines(input_file)]
    min_x = min(min(wall_part[1] for wall_part in wall) for wall in walls)
    max_x = max(max(wall_part[1] for wall_part in wall) for wall in walls)
    max_y = max(max(wall_part[0] for wall_part in wall) for wall in walls)
    cave_map = set()
    for wall in walls:
        for i in range(1, len(wall)):
            if wall[i-1][0] < wall[i][0]:
                cave_map.update([(j, wall[i][1]) for j in range(wall[i-1][0], wall[i][0]+1)])
            elif wall[i-1][0] > wall[i][0]:
                cave_map.update([(j, wall[i][1]) for j in range(wall[i][0], wall[i-1][0]+1)])
            elif wall[i-1][1] < wall[i][1]:
                cave_map.update([(wall[i][0], j) for j in range(wall[i-1][1], wall[i][1]+1)])
            elif wall[i-1][1] > wall[i][1]:
                cave_map.update([(wall[i][0], j) for j in range(wall[i][1], wall[i-1][1]+1)])
    return cave_map, min_x, max_x, max_y


def part1(cave_map_input):
    cave_map, min_x, max_x, max_y = cave_map_input
    counter = 0
    while True:
        sand = (0, 500)
        still = False
        while not still:
            if sand[0] >= max_y or sand[1] <= min_x or sand[1] >= max_x:
                return counter
            if (sand[0]+1, sand[1]) not in cave_map:
                sand = (sand[0]+1, sand[1])
            elif (sand[0]+1, sand[1]-1) not in cave_map:
                sand = (sand[0]+1, sand[1]-1)
            elif (sand[0]+1, sand[1]+1) not in cave_map:
                sand = (sand[0]+1, sand[1]+1)
            else:
                cave_map.add((sand[0], sand[1]))
                still = True
        counter += 1


def part2(cave_map_input):
    cave_map, min_x, max_x, max_y = cave_map_input
    counter = 0
    while True:
        counter += 1
        sand = (0, 500)
        still = False
        while not still:
            if sand[0]+1 == max_y+2:
                cave_map.add((sand[0], sand[1]))
                still = True
            elif (sand[0] + 1, sand[1]) not in cave_map:
                sand = (sand[0] + 1, sand[1])
            elif (sand[0] + 1, sand[1] - 1) not in cave_map:
                sand = (sand[0] + 1, sand[1] - 1)
            elif (sand[0] + 1, sand[1] + 1) not in cave_map:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                if sand[0] == 0:
                    return counter
                cave_map.add((sand[0], sand[1]))
                still = True


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
