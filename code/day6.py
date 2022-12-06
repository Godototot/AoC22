import sys
from helperfunc import *


def prepare_input(input_file):
    return open(input_file, 'r').readline()


def find_package(signal, p_len):
    marker = ''
    for i in range(len(signal)):
        index = marker.find(signal[i])
        if index == -1:
            marker += signal[i]
            if len(marker) == p_len:
                return i + 1
        else:
            marker = marker[index + 1:] + signal[i]
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
