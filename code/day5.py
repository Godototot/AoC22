import collections
import sys
from helperfunc import *


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    split = lines.index('')
    length = int((len(lines[split-1])+1)/4)
    stacks = []
    for i in range(length):
        stacks.append(collections.deque())
    for i in range(split-2, -1, -1):
        for j in range(int((len(lines[i])+1)/4)):
            value = lines[i][j*4+1]
            if value != ' ':
                stacks[j].append(value)
    moves = []
    for i in range(split+1, len(lines)):
        moves.append([int(elem) for elem in lines[i].split(' ') if elem.isnumeric()])
    return stacks, moves


def part1(input_tuple):
    stacks, moves = input_tuple
    for move in moves:
        for j in range(move[0]):
            stacks[move[2]-1].append(stacks[move[1]-1].pop())
    res = ""
    return res.join(([stack.pop() for stack in stacks]))


def part2(input_tuple):
    stacks, moves = input_tuple
    for move in moves:
        temp = collections.deque()
        for j in range(move[0]):
            temp.append(stacks[move[1] - 1].pop())
        for j in range(move[0]):
            stacks[move[2]-1].append(temp.pop())
    res = ""
    return res.join(([stack.pop() for stack in stacks]))


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
