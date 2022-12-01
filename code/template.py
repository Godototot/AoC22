import sys
from helperfunc import *


def part1(input_file):
    return ''


def part2(input_file):
    return ''


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(input_file))
    elif sys.argv[1] == '2':
        print(part2(input_file))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
