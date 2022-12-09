import copy
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors

from helperfunc import *

# dict of each direction as two-dimensional vector
direction = {'U': (0, 1),
             'R': (1, 0),
             'D': (0, -1),
             'L': (-1, 0)
             }


def prepare_input(input_file):
    """ Turns input lines into set of direction as vector and number. """

    return [(direction[line[0]], int(line.split(' ')[1])) for line in read_input_lines(input_file)]


def get_tail_pos(pos_h, pos_t):
    """ Returns new position of tail given its current position and the position of the head it follows.
    Also returns a bool that tells whether the position was changed. """

    dif = (pos_h[0] - pos_t[0], pos_h[1] - pos_t[1])
    changed = True
    # moving diagonal behind the head if it is too far away on both axis
    if dif[0] >= 2 and dif[1] >= 2:
        pos_t = (pos_h[0] - 1, pos_h[1] - 1)
    elif dif[0] >= 2 and dif[1] <= -2:
        pos_t = (pos_h[0] - 1, pos_h[1] + 1)
    elif dif[0] <= -2 and dif[1] >= 2:
        pos_t = (pos_h[0] + 1, pos_h[1] - 1)
    elif dif[0] <= -2 and dif[1] <= -2:
        pos_t = (pos_h[0] + 1, pos_h[1] + 1)

    # moving right behind the head if it is too far on just one axis
    elif dif[0] >= 2:
        pos_t = (pos_h[0]-1, pos_h[1])
    elif dif[0] <= -2:
        pos_t = (pos_h[0]+1, pos_h[1])
    elif dif[1] >= 2:
        pos_t = (pos_h[0], pos_t[1]+1)
    elif dif[1] <= -2:
        pos_t = (pos_h[0], pos_t[1]-1)
    else:
        # return False if nothing was changed
        changed = False
    return pos_t, changed


def plot_visited(visited, filename):
    """ Plots the result map showing all spaces that were visited. """

    # calculating the smallest element to start the plot at that position
    min_x = min([v[0] for v in visited])
    min_y = min([v[1] for v in visited])
    # getting the size of the plot as the maximum distance (on one axis) between elements
    size = int(max([max([v[0] for v in visited]) - min_x, max([v[1] for v in visited]) - min_y])) + 1
    model = np.zeros((size, size))
    # writing in the visited positions
    for v in visited:
        model[int(v[1] - min_y), int(v[0] - min_x)] = 1

    plt.pcolormesh(model, cmap='Greys')
    plt.axis('Off')
    plt.savefig('../plots/'+filename+'.png')


def get_visited(moves, nr_of_tails):
    """ Returns list of all positions that were visited by the last tile, given the moves and number of tails. """

    # starting positions
    pos_h = (0, 0)
    pos_t = [(0, 0) for n in range(nr_of_tails)]
    # set of all position visited by the tail
    visited = {(0, 0)}
    # loops over every move in the instructions
    for m in moves:
        for n in range(m[1]):
            # moves head to new position
            pos_h = (pos_h[0] + m[0][0], pos_h[1] + m[0][1])
            # moves tails to calculated position
            for t in range(nr_of_tails):
                # first tail moves relative to head
                if t == 0:
                    pos_t[0], changed = get_tail_pos(pos_h, pos_t[0])
                # every other tail moves relative to the one before it
                else:
                    pos_t[t], changed = get_tail_pos(pos_t[t - 1], pos_t[t])
                # saves position of the last tail if it changed
                if t == nr_of_tails - 1 and changed:
                    visited.add(pos_t[t])
    return visited


def part1(moves):
    visited = get_visited(moves, 1)
    plot_visited(visited, 'day9_part1')
    return len(visited)


def part2(moves):
    visited = get_visited(moves, 9)
    plot_visited(visited, 'day9_part2')
    return len(visited)


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
