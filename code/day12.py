import sys
import numpy as np
import math
from collections import deque
from helperfunc import *


def parse_char_as_int(char):
    """ Returns the numbers 1-25 for each lowercase letter given (with exceptions for 'S' and 'E') """

    if char == 'S':
        return 0
    elif char == 'E':
        return 25
    else:
        return ord(char) - ord('a')


def prepare_input(input_file):
    """ Returns a tuple consisting of a heightmap filled with integers and the coordinates of the start and endpoint"""

    lines = read_input_lines(input_file)
    start = None
    end = None
    # check each line for 'S' or 'E' to save as start and end coordinates
    for i in range(len(lines)):
        if not start:
            s = lines[i].find('S')
            if not s == -1:
                start = (i, s)
        if not end:
            e = lines[i].find('E')
            if not e == -1:
                end = (i, e)
    heightmap = np.array([[parse_char_as_int(char) for char in l] for l in lines])
    return heightmap, start, end


def find_shortest_distance(heightmap, start, end, reverse=False):
    """ Calculates map with all min distances from given starting point
        and returns the distance between start and end.
        If reversed it gives distance between start and first node that has value 0 """

    pathmap = np.zeros(heightmap.shape, int)  # map to fill with min distance from start point
    pathmap[start] = 1  # start is set to 1 instead of zero, so the algorithm doesn't jump back to it
    next_nodes = deque()  # stack filled with all nodes that are adjacent to a calculated one, but are not calculated yet
    current_node = start
    # if reversed is false, it stops at the and, otherwise it stops if the current node is 'a'
    while not ((not reverse and current_node == end) or
               (reverse and heightmap[current_node] == 0)):
        # calculate all neighbours
        all_neighbours = [(current_node[0] - 1, current_node[1]),
                          (current_node[0] + 1, current_node[1]),
                          (current_node[0], current_node[1] + 1),
                          (current_node[0], current_node[1] - 1)]
        for neighbour in all_neighbours:
            # checks if neighbour is out of scope
            if 0 <= neighbour[0] < len(heightmap) and 0 <= neighbour[1] < len(heightmap[0]):
                # checks if node was already calculated
                if pathmap[neighbour] == 0:
                    # check if the node can be reached by current node (or reversed)
                    if (not reverse and heightmap[neighbour] <= heightmap[current_node] + 1) or \
                            (reverse and heightmap[neighbour] + 1 >= heightmap[current_node]):
                        # write in the distance from start to current node + 1
                        pathmap[neighbour] = pathmap[current_node] + 1
                        next_nodes.appendleft(neighbour)
        # # if there are no nodes left in 'next_nodes' but there is no other position then can be reached
        # therefore the endpoint cannot be reached from the start and the distance can be represented as infinity
        if len(next_nodes) == 0:
            return math.inf
        else:
            # move to next node in the stack
            current_node = next_nodes.pop()
    # 1 has to be subtracted, since we started with distance 1 for the start position
    return pathmap[current_node] - 1


def part1(heightmap_data):
    heightmap, start, end = heightmap_data
    return find_shortest_distance(heightmap, start, end)


def part2(heightmap_data):
    # this part can be calculated in one go by starting at the end, reversing the pathfinder and stop if height is a
    heightmap, start, end = heightmap_data
    return find_shortest_distance(heightmap, end, start, True)


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/' + sys.argv[0][:-3] + '.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
