import sys
from helperfunc import *


def get_points(input_file, Points_dict):
    points_sum = 0
    rounds = read_input_lines(input_file)
    for r in rounds:
        points_sum += Points_dict.get(r)
    return points_sum


def part1(input_file):
    Points = {'A X': 4, 'A Y': 8, 'A Z': 3,
              'B X': 1, 'B Y': 5, 'B Z': 9,
              'C X': 7, 'C Y': 2, 'C Z': 6}
    return get_points(input_file, Points)


def part2(input_file):
    Points = {'A X': 3, 'A Y': 4, 'A Z': 8,
              'B X': 1, 'B Y': 5, 'B Z': 9,
              'C X': 2, 'C Y': 6, 'C Z': 7}
    return get_points(input_file, Points)


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
