import sys
from helperfunc import *


def prepare_input(input_file):
    return read_input_lines(input_file)


def calculate_value(item_string):
    points = 0
    for char in item_string:
        points += ord(char)-38 if char.isupper() else ord(char)-96
    return points


def find_common_char(bp_list):
    for char in bp_list[0]:
        if len([bp for bp in bp_list if char in bp]) == len(bp_list):
            return char


def part1(backpack_list):
    wrong_items = [find_common_char([backpack[:int(len(backpack)/2)], backpack[int(len(backpack)/2):]]) for backpack in backpack_list]
    return calculate_value(wrong_items)


def part2(backpack_list):
    badges = ""
    for i in range(0, len(backpack_list), 3):
        badges += find_common_char([backpack_list[i], backpack_list[i+1], backpack_list[i+2]])
    return calculate_value(badges)


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
