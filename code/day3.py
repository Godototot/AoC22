import sys
from helperfunc import *


def calculateValue(item_string):
    points = 0
    for char in item_string:
        points += ord(char)-38 if char.isupper() else ord(char)-96
    return points


def part1(input_file):
    backpack_list = read_input_lines(input_file)
    wrong_items = ""
    for backpack in backpack_list:
        first_comp = backpack[:int(len(backpack)/2)]
        second_comp = backpack[int(len(backpack)/2):]
        i = 0
        wrong_items += next((char for char in first_comp if char in second_comp))
    return calculateValue(wrong_items)


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
