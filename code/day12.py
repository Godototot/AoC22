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
        return ord(char)-ord('a')


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


def find_shortest_distance(heightmap, start, end):
    """ Calculates map with all min distances from given starting point
    and returns the distance between start and end """

    pathmap = np.zeros(heightmap.shape, int)  # map to fill with min distance from start point
    pathmap[start] = 1  # start is set to 1 instead of zero, so the algorithm doesn't jump back to it
    next_nodes = deque()  # stack filled with all nodes that are adjacent to a calculated one, but are not calculated yet
    current_node = start

    while not current_node == end:
        # check if node is at the border
        if current_node[0] > 0:
            up_node = (current_node[0] - 1, current_node[1])
            # check if the node still has to be calculated and if it is possible to move to it from the current node
            if pathmap[up_node] == 0 and heightmap[up_node] <= heightmap[current_node] + 1:
                # write in the distance from start to current node + 1
                pathmap[up_node] = pathmap[current_node] + 1
                next_nodes.appendleft(up_node)
        if current_node[0] < (len(heightmap) - 1):
            down_node = (current_node[0] + 1, current_node[1])
            if pathmap[down_node] == 0 and heightmap[down_node] <= heightmap[current_node] + 1:
                pathmap[down_node] = pathmap[current_node] + 1
                next_nodes.appendleft(down_node)
        if current_node[1] > 0:
            left_node = (current_node[0], current_node[1] - 1)
            if pathmap[left_node] == 0 and heightmap[left_node] <= heightmap[current_node] + 1:
                pathmap[left_node] = pathmap[current_node] + 1
                next_nodes.appendleft(left_node)
        if current_node[1] < (len(heightmap[0]) - 1):
            right_node = (current_node[0], current_node[1] + 1)
            if pathmap[right_node] == 0 and heightmap[right_node] <= heightmap[current_node] + 1:
                pathmap[right_node] = pathmap[current_node] + 1
                next_nodes.appendleft(right_node)
        # if there are no nodes left in 'next_nodes' but there is no other position then can be reached
        # therefore the endpoint cannot be reached from the start and the distance can be represented as infinity
        if len(next_nodes) == 0:
            return math.inf
        else:
            # move to next node in the stack
            current_node = next_nodes.pop()
    # 1 has to be subtracted, since we started with distance 1 for the start position
    return pathmap[end] - 1


def part1(heightmap_data):
    heightmap, start, end = heightmap_data
    return find_shortest_distance(heightmap, start, end)


def part2(heightmap_data):
    heightmap, start, end = heightmap_data
    all_paths = []
    # iterates over all elements of the map and calculates the distance to the end point if the height is 0
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if heightmap[i, j] == 0:
                all_paths.append(find_shortest_distance(heightmap, (i, j), end))
    return min(all_paths)


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
