import sys
from helperfunc import *


def prepare_input(input_file):
    pairs = [line.split(',') for line in read_input_lines(input_file)]
    ass_list = []
    for i in range(len(pairs)):
        ass_list.append([ass.split('-') for ass in pairs[i]])
    return ass_list


def part1(ass_list):
    counter = 0
    for assignment in ass_list:
        lb = [int(assignment[0][0]), int(assignment[1][0])]
        ub = [int(assignment[0][1]), int(assignment[1][1])]
        if lb[0] == lb[1] or ub[0] == ub[1]:
            counter += 1
        elif lb[0] < lb[1] and ub[0] > ub[1]:
            counter += 1
        elif lb[0] > lb[1] and ub[0] < ub[1]:
            counter += 1
    return counter


def part2(ass_list):
    counter = 0
    for assignment in ass_list:
        lb = [int(assignment[0][0]), int(assignment[1][0])]
        ub = [int(assignment[0][1]), int(assignment[1][1])]
        if lb[0] == lb[1] or ub[0] == ub[1]:
            counter += 1
        elif lb[0] <= ub[0] <= ub[1]:
            counter += 1
        elif lb[1] <= lb[0] <= ub[1]:
            counter += 1
    return counter


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
