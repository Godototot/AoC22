import sys
from helperfunc import *
from collections import deque


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    operations = deque()
    for l in reversed(lines):
        sp = l.split(' ')
        if sp[0] == 'addx':
            operations.append((2, int(sp[1])))
        elif sp[0] == 'noop':
            operations.append((1, 0))
    return operations


def part1(operations):
    clock = 1
    signal_sum = 0
    x = 1
    current_op = 0
    timer = 0
    while len(operations) > 0:
        if timer == 0:
            x += current_op
            timer, current_op = operations.pop()
        if clock % 40 == 20:
            signal_sum += clock*x
        timer -= 1
        clock += 1
    return signal_sum


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
