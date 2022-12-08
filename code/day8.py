import sys
import numpy as np
from helperfunc import *


def prepare_input(input_file):
    # turns string input into two-dimensional numpy-array with integers
    forrest = np.array([[int(t) for t in line] for line in read_input_lines(input_file)])
    return forrest


def get_coverage(forrest):
    """ Returns a two-dimensional numpy array of 0 and 1,
     corresponding to the visibility of the tree at that position. """

    visibility = np.zeros(forrest.shape, dtype=int)

    # Marks all outer trees as visible.
    visibility[0] = 1
    visibility[-1] = 1
    visibility[:, 0] = 1
    visibility[:, -1] = 1

    last_elem = forrest.shape[0] - 1

    for i in range(1, last_elem):
        for j in range(1, last_elem):
            # Checks if there is at least one side where the highest tree is smaller than the current tree.
            if min(np.max(forrest[i, 0:j]), np.max(forrest[i, j + 1:]), np.max(forrest[0:i, j]),
                   np.max(forrest[i + 1:, j])) < forrest[i, j]:
                visibility[i, j] = 1
    return visibility


def part1(forrest):
    return get_coverage(forrest).sum()


def get_blocker(trees, height, rev=False):
    """ Returns the index of first (if rev=False) or last (if rev=True) tree that has at least the given height. """

    if not rev:
        for i in range(0, len(trees)):
            if trees[i] >= height:
                return i
        # returns last tree if no tree meets condition
        return len(trees)-1
    else:
        for i in range(len(trees)-1, -1, -1):
            if trees[i] >= height:
                return i
        # returns first tree if no tree meets condition
        return 0


def part2(forrest):

    max_scenic = 0

    # counters show how many iterations calculate each of the directions
    # here to visualize how cutting the iteration of improves the efficiency
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0

    for i in range(1, forrest.shape[0]-1):
        for j in range(1, forrest.shape[0]-1):

            scenic_score = 1

            # the maximum value the remaining directions can have if all trees would be visible
            remaining_max = j*(forrest.shape[0]-j-1)*i*(forrest.shape[0]-i-1)

            # get visible trees to the left
            scenic_score *= j - get_blocker(forrest[i, 0:j], forrest[i, j], True)

            # get visible trees to the right
            remaining_max /= j
            # Checks if this tree could get a higher scenic_score than the current max,
            # if all other sides would have max value.
            # Otherwise, it can't be the solution and the remaining sides don't have to be calculated.
            if scenic_score * remaining_max > max_scenic:
                counter_2 += 1
                scenic_score *= get_blocker(forrest[i, j+1:], forrest[i, j]) + 1

                # get visible trees above
                remaining_max = i * (forrest.shape[0] - i - 1)
                if scenic_score * remaining_max > max_scenic:
                    counter_3 += 1
                    scenic_score *= i - get_blocker(forrest[0:i, j], forrest[i, j], True)

                    # get visible trees below
                    remaining_max /= i
                    if scenic_score * remaining_max > max_scenic:
                        counter_4 += 1
                        blocked = get_blocker(forrest[i+1:, j], forrest[i, j])
                        scenic_score *= blocked+1

                        # change max_scenic if this scenic_score is higher
                        max_scenic = max(max_scenic, scenic_score)

    print('All: ', pow(forrest.shape[0]-2, 2))
    print('Calculated second side: ', counter_2)
    print('Calculated third side: ', counter_3)
    print('Calculated all sides: ', counter_4)
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
