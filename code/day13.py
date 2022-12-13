import sys
from functools import cmp_to_key
from helperfunc import *


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    pairs = [[eval(lines[i]), eval(lines[i+1])] for i in range(0, len(lines), 3)]
    return pairs


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return 1
        elif right > left:
            return -1
        else:
            return 0
    else:
        if not isinstance(left, list):
            left = [left]
        if not isinstance(right, list):
            right = [right]
        for i in range(len(right)):
            if i >= len(left):
                return -1
            comp = compare(left[i], right[i])
            if comp == 1:
                return 1
            elif comp == -1:
                return -1
        else:
            if len(left) > len(right):
                return 1
            else:
                return 0


def part1(pair_list):
    right_order = []
    for n, pair in enumerate(pair_list):
        comp = compare(pair[0], pair[1])
        if comp == -1:
            right_order.append(n+1)
    return sum(right_order)


def part2(pair_list):
    packets = []
    for pair in pair_list:
        packets.extend(pair)
    deviders = [[2], [6]]
    packets.extend(deviders)
    packets.sort(key=cmp_to_key(compare))
    return (packets.index(deviders[0])+1)*(packets.index(deviders[1])+1)


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
