import sys
from helperfunc import *


def prepare_input(input_file):
    return [(int(line), False) for line in read_input_lines(input_file)]


def get_wrapped_index(i, length):
    if i <= 0:
        while i <= 0:
            i += length-1
    elif i >= (length-1):
        while i >= (length-1):
            i -= length-1
    return i


def part1(numbers):
    length = len(numbers)
    i = 0
    while i < length:
        if not numbers[i][1]:
            elem = (numbers.pop(i)[0], True)
            numbers.insert(get_wrapped_index(i+elem[0], length), elem)
        if numbers[i][1]:
            i += 1
    zero = numbers.index((0, True))
    return sum([numbers[(n+zero) % length][0] for n in [1000, 2000, 3000]])


def part2(numbers):
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
