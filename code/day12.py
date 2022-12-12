import sys
import numpy as np
from collections import deque
from helperfunc import *


def parse_char_as_int(char):
    if char == 'S':
        return 0
    elif char == 'E':
        return 25
    else:
        return ord(char)-ord('a')


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    start = None
    end = None
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


def part1(heightmap_data):
    heightmap, start, end = heightmap_data
    pathmap = np.zeros(heightmap.shape, int)
    pathmap[start] = 1
    next_nodes = deque()
    current_node = start
    while not current_node == end:
        if current_node[0] > 0:
            u_node = (current_node[0]-1, current_node[1])
            if pathmap[u_node] == 0 and heightmap[u_node] <= heightmap[current_node]+1:
                pathmap[u_node] = pathmap[current_node]+1
                next_nodes.appendleft(u_node)
        if current_node[0] < (len(heightmap)-1):
            d_node = (current_node[0]+1, current_node[1])
            if pathmap[d_node] == 0 and heightmap[d_node] <= heightmap[current_node]+1:
                pathmap[d_node] = pathmap[current_node]+1
                next_nodes.appendleft(d_node)
        if current_node[1] > 0:
            l_node = (current_node[0], current_node[1]-1)
            if pathmap[l_node] == 0 and heightmap[l_node] <= heightmap[current_node]+1:
                pathmap[l_node] = pathmap[current_node]+1
                next_nodes.appendleft(l_node)
        if current_node[1] < (len(heightmap[0])-1):
            r_node = (current_node[0], current_node[1]+1)
            if pathmap[r_node] == 0 and heightmap[r_node] <= heightmap[current_node]+1:
                pathmap[r_node] = pathmap[current_node]+1
                next_nodes.appendleft(r_node)
        if len(next_nodes) == 0:
            raise Exception("The device is broken, there is no way to E.")
        else:
            current_node = next_nodes.pop()
    return pathmap[end]-1


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
