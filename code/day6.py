import sys
from helperfunc import *


def prepare_input(input_file):
    return open(input_file, 'r').readline()


def find_package(signal, p_len):
    marker_lb = 0
    for marker_ub in range(len(signal)):
        index = signal.find(signal[marker_ub], marker_lb, marker_ub)
        if index != -1:
            marker_lb = index+1
        elif marker_ub+1 - marker_lb >= p_len:
            return marker_ub+1
    return -1


def part1(signal):
    return find_package(signal, 4)


def part2(signal):
    return find_package(signal, 14)


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
