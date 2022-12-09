import sys
from helperfunc import *


def prepare_input(input_file):
    return [[direction[line[0]], int(line.split(' ')[1])] for line in read_input_lines(input_file)]


direction = {'U': (0, 1),
             'R': (1, 0),
             'D': (0, -1),
             'L': (-1, 0)
             }


def part1(moves):
    pos_h = (0, 0)
    pos_t = (0, 0)
    visited = {(0, 0)}
    for m in moves:
        for n in range(m[1]):
            pos_h = (pos_h[0]+m[0][0], pos_h[1]+m[0][1])
            dif = (pos_h[0]-pos_t[0], pos_h[1]-pos_t[1])
            if abs(pos_h[0]-pos_t[0]) >= 2:
                pos_t = (pos_t[0]+(pos_h[0]-pos_t[0])/2, pos_h[1])
                visited.add(pos_t)
            elif abs(pos_h[1]-pos_t[1]) >= 2:
                pos_t = (pos_h[0], pos_t[1]+(pos_h[1]-pos_t[1])/2)
                visited.add(pos_t)
    return len(visited)


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
