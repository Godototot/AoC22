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


def get_blocker(trees, height, rev=False):
    if not rev:
        for i in range(0, len(trees)):
            if trees[i] >= height:
                return i
        return len(trees)-1
    else:
        for i in range(len(trees)-1, -1, -1):
            if trees[i] >= height:
                return i
        return 0


def part2(forrest):
    max_scenic = 0
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    for i in range(1, forrest.shape[0]-1):
        for j in range(1, forrest.shape[0]-1):
            scenic_score = 1
            remaining_max = j*(forrest.shape[0]-j-1)*i*(forrest.shape[0]-i-1)
            # get left trees
            blocked = get_blocker(forrest[i, 0:j], forrest[i, j], True)
            scenic_score *= j-blocked

            # get right trees
            remaining_max /= j
            if scenic_score * remaining_max > max_scenic:
                counter_1 += 1
                blocked = get_blocker(forrest[i, j+1:], forrest[i, j])
                scenic_score *= blocked+1
                remaining_max = i*(forrest.shape[0]-i-1)

                # get trees above
                if scenic_score * remaining_max > max_scenic:
                    counter_2 += 1
                    blocked = get_blocker(forrest[0:i, j], forrest[i, j], True)
                    scenic_score *= i-blocked
                    remaining_max /= i

                    # get trees below
                    if scenic_score * remaining_max > max_scenic:
                        counter_3 += 1
                        blocked = get_blocker(forrest[i+1:, j], forrest[i, j])
                        scenic_score *= blocked+1
                        max_scenic = max(max_scenic, scenic_score)
    print('All: ', pow(forrest.shape[0]-2, 2))
    print('Calculated second side: ', counter_1)
    print('Calculated third side: ', counter_2)
    print('Calculated all sides: ', counter_3)
    return max_scenic


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
