import sys
import numpy as np
from helperfunc import *


def prepare_input(input_file):
    forrest = np.array([[int(t) for t in line] for line in read_input_lines(input_file)])
    return forrest


def get_coverage(forrest):
    visibility = np.zeros(forrest.shape, dtype=int)
    visibility[0] = 1
    visibility[-1] = 1
    visibility[:, 0] = 1
    visibility[:, -1] = 1
    inner_len = forrest.shape[0] - 1
    for i in range(1, inner_len):
        for j in range(1, inner_len):
            if min(np.max(forrest[i, 0:j]), np.max(forrest[i, j + 1:]), np.max(forrest[0:i, j]),
                   np.max(forrest[i + 1:, j])) < forrest[i, j]:
                visibility[i, j] = 1
    return visibility


def part1(forrest):
    return get_coverage(forrest).sum()


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
