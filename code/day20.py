import sys
import math
from helperfunc import *


def prepare_input(input_file):
    return [int(line) for line in read_input_lines(input_file)]


def get_wrapped_index(a, s, length):
    # probably far too complicated and possible much simpler, but i went through so many wrong iterations of this,
    # that I don't wanna think about it anymore. It works and that's enough for me
    i = a+s
    if i <= 0 and s != 0:
        index = i % (length-1)
        if index == 0:
            index = length-1
        return index
    if i == length-1:
        return i
    index = i % (length - 1)
    return index


def part1(numbers):
    length = len(numbers)
    numbers = [(n, False) for n in numbers]
    i = 0
    while i < length:
        if not numbers[i][1]:
            elem = (numbers.pop(i)[0], True)
            numbers.insert(get_wrapped_index(i, elem[0], length), elem)
        if numbers[i][1]:
            i += 1
    zero = numbers.index((0, True))
    return sum([numbers[(n+zero) % length][0] for n in [1000, 2000, 3000]])


def part2(numbers_only):
    key = 811589153
    length = len(numbers_only)
    numbers = [(alt_module(n*key, length-1), i) for i, n in enumerate(numbers_only)]
    for k in range(10):
        for i in range(length):
            for j, n in enumerate(numbers):
                if n[1] == i:
                    elem = numbers.pop(j)
                    numbers.insert(get_wrapped_index(j, elem[0], length), elem)
                    break
    index_zero = next(i for i in range(len(numbers_only)) if numbers_only[i] == 0)
    zero = next(i for i in range(len(numbers)) if numbers[i][1] == index_zero)
    return sum([numbers_only[numbers[(n + zero) % length][1]]*key for n in [1000, 2000, 3000]])


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
