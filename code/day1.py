import sys
from helperfunc import *


def get_sorted_elves(input_file):
    elves = []
    calories = read_input_lines(input_file)
    add_up = 0
    for cal in calories:
        if cal == '':
            elves.append(add_up)
            add_up = 0
        else:
            add_up += int(cal)
    elves.sort()
    return elves


def part1(input_file):
    return get_sorted_elves(input_file)[-1]


def part2(input_file):
    elves = get_sorted_elves(input_file)
    out = str(elves[-1])+' + '+str(elves[-2])+' + '+str(elves[-3])+' = '+str(sum(elves[-3:]))
    return out


def main() -> None:
    input_file = ''
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(input_file))
    elif sys.argv[1] == '2':
        print(part2(input_file))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
