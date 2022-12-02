import sys
import re
from helperfunc import *


def prepare_input(input_file):
    with open(input_file, 'r') as input_string:
        lines = re.sub("[AX]", "1", re.sub("[BY]", "2", re.sub("[CZ]", "3", input_string.read()))).splitlines()
        res = [(eval(num) for num in l.split(" ")) for l in lines]
        return res


def part1(input_file):
    points = [(game[1] + 3*((game[1]-game[0]-2) % 3)) for game in prepare_input(input_file)]
    return points


def part2(input_file):
    points = [(3*(game[1]-1) + (((game[0]+game[1]) % 3)+1)) for game in prepare_input(input_file)]
    return points


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/day2.txt'
    if sys.argv[1] == '1':
        print(part1(input_file))
    elif sys.argv[1] == '2':
        print(part2(input_file))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
