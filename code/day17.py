import sys
from helperfunc import *


def prepare_input(input_file):
    jet_pattern = []
    for char in open(input_file, 'r').readline():
        if char == '>':
            jet_pattern.append(1)
        elif char == '<':
            jet_pattern.append(-1)
    return jet_pattern


shapes = ({(0, 0), (1, 0), (2, 0), (3, 0)},
          {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
          {(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)},
          {(0, 0), (0, 1), (0, 2), (0, 3)},
          {(0, 0), (1, 0), (0, 1), (1, 1)})


def part1(jet_pattern):
    walls = {(i, 0) for i in range(7)}
    highest = 0
    jet_counter = 0
    for i in range(2022):
        static = False
        falling_rock = list(part for part in shapes[i % 5])
        for p in range(len(falling_rock)):
            falling_rock[p] = (falling_rock[p][0] + 2, falling_rock[p][1] + 4 + highest)
        while not static:
            jet = jet_pattern[jet_counter % len(jet_pattern)]
            jet_counter += 1
            new_position_side = [(part[0]+jet, part[1]) for part in falling_rock]
            for part in new_position_side:
                if 0 > part[0] or part[0] > 6 or part in walls:
                    break
            else:
                falling_rock = new_position_side
            new_position_down = [(part[0], part[1]-1) for part in falling_rock]
            for part in new_position_down:
                if part in walls:
                    walls.update(falling_rock)
                    highest = max(highest, max(falling_rock, key=lambda x: x[1])[1])
                    static = True
                    break
            else:
                falling_rock = new_position_down
    return highest


def part2(jet_pattern):

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
